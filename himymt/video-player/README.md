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

## Word lookup and playback

When you tap an English subtitle word, the player pauses the video if it was playing. Close the word card (or press Escape) to resume from the same position. If the video was already paused before opening the card, closing the card keeps it paused. Selecting another episode closes the card without resuming the previous episode.

## Loading and progress indicators

- **Adding videos:** the playlist progress bar counts how many local file references have been added to the playlist. It does not upload or copy the video file.
- **Preparing playback:** the player shows when the browser is reading video metadata and preparing the first frame.
- **Buffering / seeking:** when playback needs more data, the second bar estimates how much of the video's duration is currently buffered by the browser. This is time coverage, not an upload percentage; a local file may become playable before the entire video is buffered.

The browser uses `URL.createObjectURL(file)` to read the selected file locally. Large videos are not sent to GitHub Pages.

## Controls

- Native video controls: play, pause, volume, fullscreen and seeking.
- Subtitle toggles: show/hide English and Vietnamese independently.
- Subtitle font size and vertical position.
- Sync offset in milliseconds. Positive values delay subtitles; negative values move them earlier.
- Playback speed and 5-second skip buttons.
- Keyboard: `Space` toggles play/pause; `←` and `→` seek 5 seconds.

## Load a video from Google Drive

The playlist also accepts a Google Drive **file share link**:

1. In Google Drive, open the video's **Share** settings and set **General access → Anyone with the link → Viewer**. Make sure downloading is allowed.
2. Copy the file link, for example `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`.
3. In the player, paste the link into **Load from Google Drive**.
4. Enter a display filename containing the episode number, such as `HIMYM - 1x01 - Pilot.mp4`. This name is used to match the SRT file.
5. Click **Add Google Drive video**.

This first version uses a direct Drive download URL for public shared files. It is a best-effort browser streaming method, not the authenticated Drive API. Google Drive may block direct streaming, show a download confirmation page, throttle a file, or reject range requests depending on the file and browser. If the video does not start, download it from Drive to your device and use **Add videos** instead. The SRT overlay and click-to-lookup controls work only when the video is playing in this player.

Private files are not supported by this link field. To choose private Drive files securely, the player needs a Google Cloud project, the Google Picker API, and user OAuth authorization. Do not paste OAuth access tokens or API secrets into this public page.

## Click an English word to learn it

Tap/click any English word in the subtitle to open its word card. The card can show:

- Vietnamese meaning from Google Translate.
- IPA and English definitions from Free Dictionary API.
- A dictionary audio sample when available. If the audio URL is hosted on `ssl.gstatic.com`, the card identifies it as Google Dictionary audio.
- A browser text-to-speech fallback when the dictionary does not provide an audio file.

Google does not provide a supported public Google Dictionary API for querying IPA. Therefore IPA comes from Free Dictionary API; the player uses Google-hosted dictionary audio when that source is included in the API response. Google Translate's web endpoint is also undocumented and may be rate-limited or changed by Google.

Only the selected word is sent to the translation and dictionary services. Local video and SRT files remain in the browser and are not uploaded. Word lookups are cached in memory while the page is open.

## Use on a phone (iPhone / Android)

The layout is responsive and the player reads video and subtitle files directly from the phone. First publish the folder with GitHub Pages:

1. Open the repository **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**, then click **Save**.
4. After GitHub finishes publishing, open this address in Safari or Chrome:

   `https://vivavyvu4.github.io/vocab-learning/himymt/video-player/`

The repository is public, so the published website and repository files are publicly accessible. Your personal video files stay on your phone and are not uploaded by this player.

### On the phone

1. Keep the MP4 video(s) and SRT file(s) in the Files app (iPhone) or Downloads / File Manager (Android). On iPhone, download the video from iCloud Drive or save it to Files first.
2. Open the player URL above.
3. Tap **Add videos** and select an episode (or multiple episodes if your phone's file picker allows it).
4. Pick the matching English SRT and, optionally, the Vietnamese SRT. You can also use the bilingual SRT input.
5. Turn the phone sideways for a larger player; use the video controls for full screen.

For phone browsers, use MP4 with H.264 video and AAC audio. AVI/MKV files are not reliably supported by mobile browsers; convert them to MP4 before copying them to the phone. If selecting a whole season at once is awkward, load one episode and its subtitle files at a time.

You can use the browser's **Add to Home Screen** / **Install** option as a shortcut to the player.

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
