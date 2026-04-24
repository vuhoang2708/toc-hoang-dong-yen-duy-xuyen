# Kế Hoạch Cập Nhật & Tích Hợp Dữ Liệu Bảng Biên Tập Tộc Hoàng Đông Yên

Bản kế hoạch (Implementation Plan) vạch ra các bước cần thiết để kết nối và khôi phục luồng dữ liệu từ bảng biên tập (`editor/index.html`) để tự động đồng bộ dự liệu vào nền tảng Google Sheets.

> [!IMPORTANT]
> **Auditor Review (Dành cho rà soát/Codex):**
> Vấn đề cốt lõi (Root Cause) không nằm ở trình duyệt mà do mã nguồn Google Apps Script (Backend) đang thiếu hàm nhận thông tin. Yêu cầu bắt buộc phải triển khai (Deploy) lại đoạn mã Apps Script thì cơ chế tiếp nhận từ Editor mới hoạt động thành công.

## 1. Phạm Vi Các Tệp Bị Ảnh Hưởng (Proposed Changes)

--------------------------------------------------------------------------------
### Tầng Backend (Google Apps Script)
*Xử lý logic tiếp nhận dữ liệu qua API*

#### [MODIFY] [google_apps_script.js](file:///c:/Users/vu.hoang/.gemini/antigravity/scratch/gio-to-toc-hoang2026/google_apps_script.js)
- Cập nhật ID `SPREADSHEET_ID`: Đổi chuỗi mặc định sang `1Wa34sit-DkzrCq1U68JMlvMX1L11FES4VnFsO1Pxlts`.
- Sửa đổi hàm gốc `doPost(e)`: Bổ sung luồng kiểm tra `if (data.section)` để nhận diện yêu cầu gửi từ Bảng biên tập.
- Viết mới hàm `handleEditorUpdate(ss, data)`: Khởi tạo/Tìm Sheet tên `"Biên Tập"` và Ghi các cột: `Thời gian`, `Phần nội dung`, `Nội dung cũ`, `Nội dung mới`. Phản hồi trạng thái (status: "success").

--------------------------------------------------------------------------------
### Tầng Frontend (HTML/JS)
*Xử lý logic hiển thị và cập nhật liên kết Endpoint API.*

#### [MODIFY] Báo cáo thao tác thủ công (Manual Configuration Handover):
- Sau khi cập nhật file `google_apps_script.js`, Agent sẽ bàn giao mã để User copy mã nguồn, cấu hình trên Google App Script (Tạo bản triển khai/New Deployment).
- Sau khi lấy được `URL Endpoint` mới sinh từ bản triển khai, thay đè vào hằng số `GOOGLE_APP_URL` trong khối script của `editor/index.html`.

## 2. Quy Trình Vận Hành Thử Nghiệm (Verification Plan)

### Automated Test/Kiểm toán tự động
- Chạy Regex / Grep để quét lại file `google_apps_script.js` rà soát 100% không còn thẻ gán comment Placeholder (TODO, v.v.).
- Rà soát sự hiện diện của `handleEditorUpdate`.

### Thực tế (Manual Verification & Handover)
1. Tiến hành sửa code logic file `.js`.
2. Yêu cầu triển khai.
3. Test bấm GỬI.
