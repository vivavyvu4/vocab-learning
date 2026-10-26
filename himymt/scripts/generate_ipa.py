from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "himymt/s01/How I Met Your Mother - 1x01 - Pilot.en.srt"
OUTPUT = ROOT / "himymt/s01/How I Met Your Mother - 1x01 - Pilot.ipa.en.srt"

def to_ipa(line: str) -> str:
    # eSpeak provides a broad General American-style IPA approximation.
    result = subprocess.run(
        ["espeak", "-q", "--ipa=3", line],
        check=True, capture_output=True, text=True
    )
    return result.stdout.strip()

source = SOURCE.read_text(encoding="utf-8-sig")
blocks = re.split(r"\n\s*\n", source.strip())
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
        # Keep subtitle markup/credits as-is; add IPA beneath spoken subtitle text.
        if line.lstrip().startswith("<") or re.fullmatch(r"https?://\S+", line.strip()):
            annotated.append(line)
            continue
        clean = re.sub(r"<[^>]+>", "", line).strip()
        annotated.append(line)
        if clean:
            ipa = to_ipa(clean)
            if ipa:
                annotated.append(ipa)
    output_blocks.append("\n".join(cue + annotated))

OUTPUT.write_text("\n\n".join(output_blocks) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT} ({len(output_blocks)} subtitle cues)")
