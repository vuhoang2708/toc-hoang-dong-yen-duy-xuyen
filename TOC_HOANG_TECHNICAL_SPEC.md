# 🛠️ TÀI LIỆU MÔ TẢ KỸ THUẬT CHUYÊN SÂU (DEEP TECH SPEC)
## 🏯 DỰ ÁN: CỔNG THÔNG TIN SỐ TỘC HOÀNG ĐÔNG YÊN (2026)

---

## 1. TỔNG QUAN KIẾN TRÚC (ARCHITECTURE OVERVIEW)
Dự án được xây dựng theo mô hình **Serverless Hybrid Architecture**, kết hợp giữa nền tảng Hosting tĩnh (Vercel) và Hệ quản trị dữ liệu dựa trên đám mây (Google Workspace).

*   **Frontend**: Cấu trúc Single Page Application (SPA) giả lập bằng Vanilla JS & CSS Grid/Flexbox. Đạt hiệu năng tối ưu (Google Lighthouse > 95 pts).
*   **Backend & API**: Hoạt động hoàn toàn qua **Google Apps Script (GAS)** dưới dạng Webhook POST Request.
*   **Database (CRM)**: Sử dụng **Google Sheets** làm cơ sở dữ liệu thời gian thực, cho phép quản lý phi kỹ thuật dễ dàng.
*   **Media Automation**: Sử dụng Python Integration để xử lý Media và tạo video marketing tự động.

---

## 2. CHI TIẾT CÁC THÀNH PHẦN (COMPONENT DETAILS)

### 2.1. Hệ thống Frontend (Glassmorphism Design System)
*   **Giao diện**: Áp dụng phong cách **Glassmorphism** (kính mờ) với hiệu ứng `backdrop-filter: blur(20px)`.
*   **Layout**: Thiết kế Responsive tuyệt đối, tối ưu hóa cho màn hình điện thoại (Mobile-First) để bà con dễ dàng truy cập.
*   **Animation**: Sử dụng CSS Transitions và Intersection Observer API để kích hoạt hiệu ứng khi người dùng cuộn trang.

### 2.2. Hệ thống Admin & Biên tập (CMS)
Thay vì sử dụng các CMS nặng nề như WordPress, dự án phát triển 2 Module quản trị tinh gọn:
1.  **Admin Portal (`admin.html`)**: Trung tâm điều khiển chính, chứa các shortcut đến CRM, công cụ tạo video và hệ thống quản trị Webhook.
2.  **Verbatim Editor (`editor/index.html`)**: Trình biên tập đối soát 3 cột chuyên dụng. 
    *   **Logic**: Fetch dữ liệu từ Client -> Cho phép edit -> POST ngược lại Webhook để lưu vào Cloud.
    *   **Persistence**: Tích hợp `localStorage` để tự động lưu bản nháp ngay cả khi mất mạng hoặc đóng trình duyệt đột ngột.

### 2.3. Backend Logic (Google Apps Script)
File `google_apps_script.js` xử lý toàn bộ logic nghiệp vụ:
*   **`doPost(e)`**: Entry point tiếp nhận mọi yêu cầu.
*   **`logToSheet(data)`**: Trình xử lý thông minh tự động nhận diện dữ liệu thuộc nhóm "Gia Phả", "Đăng Ký" hay "Biên Tập" để đổ vào đúng trang tính.
*   **Email Automation**: Tích hợp `GmailApp` để gửi thông báo tức thì cho người quản lý khi có người đăng ký mới.

---

## 3. CƠ SỞ DỮ LIỆU & QUẢN LÝ TÀI NGUYÊN (DATABASE & STORAGE)

*   **Google Sheets Structure**:
    *   `Sheet1 (Registration)`: Lưu trữ danh sách đăng ký tham dự lễ.
    *   `Sheet2 (Gia Phả)`: Lưu trữ thông tin bổ sung phả hệ.
    *   `Sheet3 (Content_Updates)`: Lưu trữ các bản nháp chỉnh sửa nội dung website.
*   **Media Assets**: Toàn bộ hình ảnh được tối ưu hóa chuẩn `.webp` để đảm bảo tốc độ load trang dưới 2 giây.

---

## 4. TỰ ĐỘNG HÓA & TRUYỀN THÔNG (AUTOMATION)

### 4.1. Video Generation Script (`scripts/`)
Sử dụng bộ công cụ Python để tạo video giới thiệu website chuyên nghiệp:
*   **Voice**: Tích hợp `edge-tts` (Neural AI Voice) với giọng đọc tiếng Việt (`vi-VN-HoaiNinhNeural`).
*   **Visual**: Sử dụng `OpenCV` và `MoviePy` để thực hiện các hiệu ứng Zoom-in/Zoom-out và chèn QR Code động vào cuối video.

### 4.2. Timeline Switcher Logic
Tích hợp logic tự động ẩn các form đăng ký và chuyển sang chế độ "Ký Ức" sau ngày tổ chức Lễ Tế Xuân (26/04/2026) thông qua xử lý Date object trong Javascript.

---

## 5. QUY TRÌNH TRIỂN KHAI (CI/CD PIPELINE)

1.  **Local Development**: Edit mã nguồn trên máy local.
2.  **Version Control**: Commit lên GitHub (`branch: main`).
3.  **Automatic Build**: Vercel lắng nghe Webhook từ GitHub và tự động triển khai bản mới nhất lên Production trong vòng 60 giây.
4.  **Backend Sync**: Cập nhật Script ID trong file `google_apps_script.js` nếu cấu hình Webhook thay đổi.

---

## 6. DANH MỤC FILE CORE (CORE FILE MAP)
*   `index.html`: Cổng vào chính.
*   `admin.html`: Bảng điều khiển quản trị.
*   `editor/index.html`: Trình biên tập nội dung.
*   `google_apps_script.js`: Logic xử lý serverless.
*   `assets/css/style-v2.css`: Toàn bộ linh hồn của thiết kế.
*   `scripts/generate_overview_v3.py`: Mã nguồn tự động hóa video.

---
*Tài liệu được soạn thảo bởi Antigravity AI - Phiên bản Tộc Hoàng Đông Yên Chính thức (23/04/2026).*
