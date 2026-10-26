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


def to_ipa(line: str) -> str:
    """Return a readable, approximate General American IPA transcription."""
    result = subprocess.run(
        ["espeak", "-q", "-v", "en-us", "--ipa=3", line],
        check=True,
        capture_output=True,
        text=True,
    )
    # eSpeak may include line breaks or unusual spacing in its output.
    ipa = " ".join(result.stdout.split()).strip()
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
