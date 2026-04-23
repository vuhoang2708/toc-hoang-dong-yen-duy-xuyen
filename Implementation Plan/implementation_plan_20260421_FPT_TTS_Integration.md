# Kế hoạch thực thi (Implementation Plan)

**Task:** Tích hợp API FPT.AI để sử dụng giọng đọc **Gia Huy (Nam - Đà Nẵng)** cho Video Overview V3.
**Ngày:** 2026-04-21

## 1. Giải pháp kỹ thuật
Thay thế thư viện `edge-tts` (giọng cũ) bằng phương thức gọi API của FPT.AI.

*   **Thông tin API:**
    *   **API Key:** `a7eutHcRA60XMdj746z0viJVt0KK2gR6` (Đã được User cung cấp).
    *   **Giọng đọc:** `giahuy` (Nam miền Trung - Đà Nẵng).
    *   **Cơ chế:** Gửi yêu cầu -> Nhận URL file MP3 -> Chờ file xử lý xong -> Tải về máy.
*   **Thư viện cập nhật:** Sử dụng thư viện `requests` (đã có sẵn trong môi trường Python) để gọi API.

## 2. Các file bị ảnh hưởng
*   **`scripts/generate_overview_v3.py`**:
    *   Xóa logic `import edge_tts`.
    *   Thêm hàm `fpt_ai_tts` để đẩy văn bản lên FPT.
    *   Cập nhật danh sách `segments` để đổi giá trị "voice" thành `giahuy`.

## 3. Rủi ro tiềm ẩn
*   **FPT API Rate Limit:** Nếu gọi liên tục quá nhanh có thể bị từ chối (sẽ thêm `time.sleep` để tránh lỗi).
*   **Thời gian chờ:** FPT.AI xử lý file MP3 mất khoảng vài giây, script cần có vòng lặp kiểm tra (polling) cho đến khi file sẵn sàng.

## 4. Auditor Review
*   Đảm bảo không lộ API Key trong các log công khai (sẽ lưu key vào biến nội bộ trong script).
*   Kiểm tra tính toàn vẹn của file MP3 sau khi tải về trước khi ghép vào video.

---

**VÀO VÒNG LẶP CHỜ PHÊ DUYỆT (Rule 1.2):**
Tôi đã sẵn sàng cập nhật script để video có giọng **Gia Huy (Đà Nẵng)**. Vui lòng phản hồi **"Approve"** hoặc **"Đồng ý"** để tôi thực hiện thay đổi mã nguồn!
