# Implementation Plan - Video Overview V3 (2026-04-21)

**Task**: Xây dựng video tổng quan giới thiệu website (Video Overview V3) sử dụng kịch bản âm thanh Neural AI và hiệu ứng hình ảnh Zoom-Out.

## 1. Giải pháp kỹ thuật (Technical Solution)
- **Công cụ (Tooling)**: 
  - `Python 3.12` (môi trường portable).
  - `playwright`: Tự động chụp ảnh màn hình các vùng giao diện (viewport) chính.
  - `edge-tts`: Tạo giọng đọc AI tiếng Việt tự nhiên (Neural Voice `vi-VN-HoaiMyNeural`).
  - `moviepy`: Lắp ráp video, xử lý hiệu ứng hình ảnh và âm thanh.
- **Quy trình thực thi**:
  1. Dùng Playwright truy cập trang Live (hoặc local) để chụp chính giữa các vùng: Hero, Phả Hệ, Kêu gọi đóng góp, Bản đồ, và trang Quản trị (Admin).
  2. Synthesize (Tổng hợp) các đoạn âm thanh từ kịch bản bằng Edge-TTS.
  3. Dùng MoviePy để tạo các ImageClip có độ dài khớp với từng đoạn âm thanh.
  4. Áp dụng hiệu ứng **Zoom-Out**: Scale khung hình từ 1.2x giảm dần về 1.0x trong suốt thời lượng của clip.
  5. Ghép nối (Concatenate) các clip lại với nhau, sử dụng kỹ thuật **Cross-fade** 0.5s giữa các scene.

## 2. File bị ảnh hưởng (Affected Files)
- Tạo mới: `scripts/generate_overview_v3.py` (Script Python tự động hóa).
- Đầu ra: `assets/videos/overview_v3.mp4`

## 3. Rủi ro tiềm ẩn (Risks)
- **Chụp ảnh màn hình (Screenshot)**: Playwright có thể cần chờ nội dung (như font chữ, bản đồ) tải xong để chụp không bị lỗi. Sẽ áp dụng độ trễ (delay) nhỏ và định vị `locator` chính xác.
- **MoviePy & RAM**: Cần render video ở độ phân giải hợp lý (VD: 1280x720) để tránh tràn RAM và tối ưu thời gian tạo video.

## 4. Auditor Review & Verification
- Soát lỗi: Agent sẽ kiểm tra script Python xem có cài đầy đủ thư viện yêu cầu (edge-tts, moviepy, playwright) hay không.
- Nghiệm thu: Sau khi tạo video, sẽ gọi trình phát video hoặc đảm bảo tệp MP4 được xuất thành công ở thư mục đích.
