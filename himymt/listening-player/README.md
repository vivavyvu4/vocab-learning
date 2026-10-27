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
