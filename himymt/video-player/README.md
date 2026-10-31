# HIMYM Video & Subtitle Player

A small, dependency-free browser player for watching local *How I Met Your Mother* Season 1 videos with external SRT subtitles.

## Open

Open `index.html` in Chrome or Edge. No installation or server is required.

## Load videos

1. Click **Add videos**.
2. Select one episode or all episodes from your local Season 1 video folder.
3. The playlist is sorted by filename. Choose any episode to play it.

Videos are opened locally in your browser. They are not uploaded to GitHub or any external service.

## Load subtitles

You can use any of these combinations:

- English only: select files in **English SRT**.
- English + Vietnamese: select matching files in **English SRT** and **Vietnamese SRT**.
- One bilingual file: select `.en-vn.srt` files in **Bilingual SRT** instead.

You can select multiple subtitle files at once. The player matches each subtitle to its episode by reading either `1x01` or `S01E01` from the filenames. This allows names such as:

- `How I Met Your Mother - 1x01 - Pilot.en.srt`
- `How I Met Your Mother - 1x01 - Pilot.en-vn.srt`
- `How.I.Met.Your.Mother.S01E01.720p.mp4`

For a single subtitle file without an episode number, that file is used as the fallback for every selected video. If you have several subtitle files, include the episode number in each filename for reliable matching.

## Controls

- Native video controls: play, pause, volume, fullscreen and seeking.
- Subtitle toggles: show/hide English and Vietnamese independently.
- Subtitle font size and vertical position.
- Sync offset in milliseconds. Positive values delay subtitles; negative values move them earlier.
- Playback speed and 5-second skip buttons.
- Keyboard: `Space` toggles play/pause; `←` and `→` seek 5 seconds.

## Notes

- This player does not depend on the existing TTS-based `listening-player`; both tools are kept separate.
- Subtitle files are read locally in the browser. Nothing is uploaded.
- MP4 (H.264/AAC) has the broadest browser support. AVI is accepted by the file picker, but the browser may not decode its container/codecs. If an AVI file does not play, convert it to MP4 (H.264/AAC). The subtitle files do not need to be changed.

### Convert AVI files on macOS with FFmpeg

Install FFmpeg once with Homebrew:

```bash
brew install ffmpeg
```

In Terminal, go to the folder containing the AVI files and run:

```bash
mkdir -p mp4
for f in ./*.avi; do
  [ -e "$f" ] || continue
  name="${f##*/}"
  name="${name%.*}"
  ffmpeg -i "$f" -map 0:v:0 -map '0:a?' -c:v libx264 -crf 20 -preset fast -c:a aac -b:a 192k -movflags +faststart "mp4/${name}.mp4"
done
```

This creates MP4 copies inside an `mp4` subfolder and leaves the original AVI files untouched. Then load those MP4 files in this player with the same SRT files.
- Bilingual SRT splitting uses Vietnamese diacritics and italic tags to distinguish Vietnamese lines from English lines. If a subtitle file has unusual formatting, load its English and Vietnamese tracks separately for the most reliable result.
