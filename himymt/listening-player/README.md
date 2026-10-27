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

Phiên bản này dùng giọng đọc tổng hợp (TTS) có sẵn trên máy/trình duyệt, **không phải âm thanh gốc của diễn viên trong HIMYM**. Chưa cần video hoặc audio file để sử dụng. Chất lượng giọng và các lựa chọn English (US) tùy thuộc hệ điều hành và browser. Player hiển thị tổng số voice mà browser cung cấp, số voice tiếng Anh, danh sách đầy đủ theo ngôn ngữ và nút nghe thử từng voice. Nhấn **Refresh voice list** nếu danh sách chưa tải xong.

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
- Inline `[PAUSE: 400]` adds a pause in milliseconds. `[EMPH: ...]` không còn được dùng để tách lời nói vì khiến câu bị ngắt quãng; nếu gặp marker cũ, player giữ từ đó liền mạch trong câu.

The player detects every distinct `[SPEAKER: ...]` label in the loaded SRT and creates a voice selector for each one. It attempts to assign distinct English voices by inferred character gender; voice gender is not exposed consistently by browsers, so this is a best-effort name-based heuristic. Users can change any assignment afterward. Mood changes are approximations using browser TTS rate and pitch, not the actors' original performances. Inline `[EMPH: ...]` markers were removed because splitting a sentence into separate TTS utterances made the speech sound choppy; the parser also strips such wrappers from older SRT files without splitting the sentence.

**Speaker labels are a first-pass annotation, not a verified script transcript.** Most dialogue cues across EP1 now have a first-pass speaker label; 67 uncertain or mixed-speaker cues remain `UNKNOWN` rather than being confidently assigned to the wrong character. The original English SRT and IPA SRT remain unchanged. If the annotated file cannot load, the player falls back to the original English SRT.


## Xem và bổ sung voice trên máy

- Trong player, xem dòng **N voices total · M English**, bấm **Show every voice available to this browser** để xem tên, ngôn ngữ và nghe thử từng giọng.
- Danh sách này là những voice mà browser hiện tại thật sự cung cấp; trang web không thể tự cài thêm voice hệ thống.
- Trên Windows 10/11, mở **Settings → Time & language → Speech** để xem các voice đã cài và tìm tùy chọn thêm voice. Tùy phiên bản Windows, mục cài ngôn ngữ/voice có thể nằm trong **Time & language → Language & region**. Sau khi cài, đóng/mở lại trình duyệt hoặc nhấn **Refresh voice list**.
- Có thể thử mở player bằng Microsoft Edge nếu Chrome không hiện những voice có sẵn trên Windows. Voice cloud/online và voice local có thể khác nhau tùy trình duyệt, hệ điều hành và kết nối mạng.
- Nếu danh sách không có giọng English nào, player vẫn hiển thị tổng số voice mà browser báo; hãy kiểm tra lại cài đặt speech/voice của hệ điều hành.
- `TED` và `FUTURE_TED` có selector riêng, nên có thể chọn hai giọng nam khác nhau: ví dụ giọng tự nhiên, chậm rãi hơn cho Future Ted và giọng hội thoại hơn cho Ted. Mức độ tự nhiên tùy các voice thực tế có trên máy.


## Floating mini-player (always on top)

Trong bản player web, nhấn **▣ Floating mini-player** để mở một cửa sổ Picture-in-Picture riêng. Cửa sổ nhỏ hiển thị câu tiếng Anh, IPA, nhân vật, tiến độ và nút câu trước/phát-tạm dừng/dừng/câu sau. Cửa sổ được thiết kế để nằm nổi trên các ứng dụng khác, vì vậy có thể vừa làm việc vừa nhìn phụ đề và nghe TTS.

- Cần mở trang bằng HTTPS (GitHub Pages/raw hosting) và dùng phiên bản Chrome hoặc Edge mới có hỗ trợ Document Picture-in-Picture. Hỗ trợ tùy browser; nút sẽ báo nếu tính năng không có.
- Cửa sổ nổi lấy nội dung từ player chính; tiếp tục dùng voice, tốc độ, SRT/IPA và cài đặt trong trang chính. Không đóng tab/player chính khi đang dùng cửa sổ nổi.
- Đây là cửa sổ nổi của trình duyệt, không phải ứng dụng Windows độc lập. Nếu cần bản desktop cài đặt riêng về sau, có thể đóng gói player thành app Electron/Tauri.
