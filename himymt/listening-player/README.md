# HIMYM Subtitle Listening Player — EP1

Trình luyện nghe tiếng Anh theo **Episode Mode** cho *How I Met Your Mother* Season 1, Episode 1 — **Pilot**.

## Tính năng

- Đọc lần lượt các câu trong file SRT bằng giọng English Text-to-Speech của trình duyệt.
- Tự chuyển sang câu kế tiếp, hiển thị câu tiếng Anh và IPA tương ứng.
- Chọn giọng đọc, tốc độ 0.75× / 0.9× / 1× / 1.1× và khoảng nghỉ giữa câu.
- Ẩn/hiện phụ đề tiếng Anh và IPA độc lập.
- Tạm dừng/tiếp tục, dừng, phát lại câu hiện tại, nhảy câu trước/sau và lặp cả tập.
- Tải SRT và IPA từ repo khi có thể; có lựa chọn nạp file thủ công nếu trình duyệt chặn việc tải tự động.

## Mở player

Mở `index.html` trong thư mục này bằng trình duyệt hiện đại như Chrome hoặc Edge. Player sẽ thử tải các file từ `himymt/s01/` qua `raw.githubusercontent.com`.

Nếu trình duyệt không tải tự động được:
1. Chọn `How I Met Your Mother - 1x01 - Pilot.en.srt` ở ô **English SRT**.
2. Chọn `How I Met Your Mother - 1x01 - Pilot.ipa.en.srt` ở ô **IPA SRT**.
3. Nhấn **Play episode** và cho phép âm thanh của trình duyệt nếu được hỏi.

## Lưu ý về âm thanh

Phiên bản này dùng giọng đọc tổng hợp (TTS) có sẵn trên máy/trình duyệt, **không phải âm thanh gốc của diễn viên trong HIMYM**. Chưa cần video hoặc audio file để sử dụng. Chất lượng giọng và các lựa chọn English (US) tùy thuộc hệ điều hành và browser.

Nội dung phụ đề và IPA không được nhúng lại vào player; player tải các file đã có trong repo. IPA được ghép theo timestamp của từng cue. File IPA hiện tại là phiên âm tự động nên có thể có chỗ chưa chính xác hoàn toàn.

## Phím tắt

- `Space`: Play / Pause
- `←`: câu trước
- `→`: câu tiếp theo

## Đường dẫn dữ liệu EP1

- `../s01/How I Met Your Mother - 1x01 - Pilot.en.srt`
- `../s01/How I Met Your Mother - 1x01 - Pilot.ipa.en.srt`


## Speaker + expressive TTS (EP1)

The player now prefers the annotated file:

- `himymt/s01/How I Met Your Mother - 1x01 - Pilot.speakers.srt`

It keeps the original cue timestamps and uses small metadata tags such as:

```srt
[SPEAKER: FUTURE_TED] [MOOD: STORYTELLING]
Kids, I'm gonna tell you an [EMPH: incredible] story ;
```

Supported tags:

- `[SPEAKER: TED]`, `[SPEAKER: BARNEY]`, `[SPEAKER: ROBIN]`, `[SPEAKER: MARSHALL]`, `[SPEAKER: LILY]`, `[SPEAKER: FUTURE_TED]` and other labels.
- `[MOOD: STORYTELLING]`, `[MOOD: EXCITED]`, `[MOOD: QUESTION]`, `[MOOD: THOUGHTFUL]`, `[MOOD: WHISPER]`, `[MOOD: SARCASTIC]`.
- Inline `[EMPH: word]` raises pitch slightly and slows the emphasized word.
- Inline `[PAUSE: 400]` adds a pause in milliseconds.

In the player, choose a separate browser voice for each supported character. A blank character selection uses the default English voice. Mood changes are approximations using browser TTS rate and pitch, not the actors' original performances.

**Speaker labels are a first-pass annotation, not a verified script transcript.** Most dialogue cues across EP1 now have a first-pass speaker label; 67 uncertain or mixed-speaker cues remain `UNKNOWN` rather than being confidently assigned to the wrong character. The original English SRT and IPA SRT remain unchanged. If the annotated file cannot load, the player falls back to the original English SRT.
