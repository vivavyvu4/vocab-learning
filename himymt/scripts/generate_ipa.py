from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SUBTITLE_ROOT = ROOT / "himymt"


def read_subtitles(path: Path) -> str:
    raw = path.read_bytes()
    # Prefer UTF-8, then fall back to common legacy subtitle encodings.
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeError(f"Could not decode subtitle file: {path}")


def normalize_ipa(ipa: str) -> str:
    """Make eSpeak IPA easier to read while retaining its approximate US pronunciation."""
    # Remove invisible joiners that eSpeak can emit between IPA symbols.
    ipa = re.sub(r"[\u200b-\u200f\ufeff]", "", ipa)
    # Use a familiar Latin r for the American English approximant /ɹ/.
    ipa = ipa.replace("ɹ", "r")

    # eSpeak places stress immediately before the vowel nucleus. Move the
    # marker left over the preceding consonant cluster so it appears at the
    # beginning of the stressed syllable (e.g. mˈʌðɚ -> ˈmʌðɚ).
    vowels = set("i y ɨ ʉ ɯ u ɪ ʏ ʊ e ø ɘ ɵ ɤ o ə ɛ œ ɜ ɞ ʌ ɔ æ ɐ a ɶ ɑ ɒ".split())
    for marker in ("ˈ", "ˌ"):
        start = 0
        while True:
            pos = ipa.find(marker, start)
            if pos < 0:
                break
            cluster_start = pos
            while cluster_start > 0:
                char = ipa[cluster_start - 1]
                if char.isspace() or char in vowels or char in "ˈˌ/.,!?;:()[]":
                    break
                cluster_start -= 1
            if cluster_start < pos:
                ipa = ipa[:cluster_start] + marker + ipa[cluster_start:pos] + ipa[pos + 1:]
                start = cluster_start + len(marker) + (pos - cluster_start)
            else:
                start = pos + 1
    return " ".join(ipa.split()).strip()


def to_ipa(line: str) -> str:
    """Return readable, approximate General American IPA transcription."""
    result = subprocess.run(
        ["espeak", "-q", "-v", "en-us", "--ipa=3", line],
        check=True,
        capture_output=True,
        text=True,
    )
    ipa = normalize_ipa(result.stdout)
    if not ipa:
        return ""
    return f"/{ipa}/"


def generate_file(source: Path) -> Path:
    output = source.with_name(source.name.replace(".en.srt", ".ipa.en.srt"))
    source_text = read_subtitles(source)
    blocks = re.split(r"\n\s*\n", source_text.strip())
    output_blocks = []

    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3 or not lines[0].strip().isdigit() or "-->" not in lines[1]:
            output_blocks.append(block)
            continue

        cue = lines[:2]
        subtitle_lines = lines[2:]
        annotated = []
        for line in subtitle_lines:
            if not line.strip():
                continue

            # Keep standalone markup/URLs unchanged.
            if line.lstrip().startswith("<") or re.fullmatch(r"https?://\S+", line.strip()):
                annotated.append(line)
                continue

            # Preserve any inline subtitle markup in the displayed English line,
            # while omitting tags from the text sent to eSpeak.
            clean = re.sub(r"<[^>]+>", "", line).strip()
            annotated.append(line)
            if clean:
                ipa = to_ipa(clean)
                if ipa:
                    annotated.append(ipa)

        output_blocks.append("\n".join(cue + annotated))

    output.write_text("\n\n".join(output_blocks) + "\n", encoding="utf-8")
    print(f"Wrote {output} ({len(output_blocks)} subtitle cues)")
    return output


def main() -> None:
    sources = sorted(
        path for path in SUBTITLE_ROOT.rglob("*.en.srt")
        if not path.name.endswith(".ipa.en.srt")
    )
    if not sources:
        print("No source .en.srt subtitle files found.")
        return

    for source in sources:
        generate_file(source)


if __name__ == "__main__":
    main()
