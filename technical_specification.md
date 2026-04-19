# 🏗️ TÀI LIỆU KỸ THUẬT (TECHNICAL SPECIFICATION) — Tộc Hoàng Đông Yên Portal
*Dự án: Hệ thống Quản lý Đăng ký Lễ tế xuân & Cập nhật Gia phả Tộc Hoàng*

---

## 🛠️ Tổng quan Giải pháp (Overview)
Website được thiết kế như một cổng thông tin tập trung dành cho bà con Tộc Hoàng Đông Yên, phục vụ hai mục đích chính:
1.  **Đăng ký tham dự Lễ tế xuân hằng năm.**
2.  **Thu thập và số hóa dữ liệu Gia phả** (Cập nhật thông tin từ đời thứ 10 trở về sau).

## 🧩 Kiến trúc Hệ thống (Architecture)
*   **Frontend:** HTML5, CSS3 (Vanilla), JavaScript. Sử dụng phong cách thiết kế **Glassmorphism** với tông màu Đỏ - Vàng (Truyền thống & Trang trọng).
*   **Backend:** Google Apps Script (GAS) đóng vai trò Webhook API xử lý các yêu cầu POST.
*   **Cơ sở dữ liệu:** Google Sheets (Lưu trữ tập trung đa phương thức).
*   **Deployment:** Vercel (CI/CD từ GitHub).

---

## 📊 Cấu trúc Dữ liệu & Luồng xử lý (Data Flow)

### 1. Webhook Web App (GAS)
*   **URL:** `https://script.google.com/macros/s/AKfycbxDtkXPMrcU4vtKwV6ZTIZ0PpQiZ1hiuUCo_QbG8MfLnhCPoXYXgg-f6lhdjt6Mb16Uvw/exec`
*   **Logic xử lý đa biến:** Script tự động nhận diện `type` dữ liệu gửi về để điều hướng vào đúng Sheet:
    *   `type: 'CLAN_MEMBER_CONFIRM'` -> Lưu vào Sheet **"Registration"**.
    *   `type: 'GENEALOGY_UPDATE'` -> Lưu vào Sheet **"Gia Phả"**.

### 2. Schema Dữ liệu (Mapping)

#### A. Sheet: Registration (Đăng ký Lễ)
| Cột | Dữ liệu | Mô tả |
|:---|:---|:---|
| A | Timestamp | Thời gian đăng ký |
| B | Họ tên | Tên bà con đăng ký |
| C | Số điện thoại | SĐT liên lạc |
| D | Email | Email (Tùy chọn) |
| E | Số người dự | Số thành viên đi cùng |
| F | Đi chung xe | Đăng ký xe 16 chỗ từ Đà Nẵng |
| G | Session ID | Định danh phiên làm việc |

#### B. Sheet: Gia Phả (Cập nhật thông tin)
| Cột | Dữ liệu | Mô tả |
|:---|:---|:---|
| A | Timestamp | Thời gian gửi |
| B | Người cung cấp | Họ tên người gửi thông tin |
| C | Đời thứ | Vị trí thế hệ trong Tộc |
| D | Họ tên cha | Dữ liệu đối chiếu cây phả hệ |
| E | Thông tin gia đình | Vợ/Chồng, Con cái, Dâu/Rể |
| F | Người quá cố | Ngày mất, nơi an táng |

---

## 🎨 Chuẩn mực Thương hiệu & UI (Visual Standards)
*   **Tên Tộc thống nhất:** `TỘC HOÀNG ĐÔNG YÊN - DUY XUYÊN - QUẢNG NAM (ĐÀ NẴNG)`
*   **Màu chủ đạo:**
    *   Deep Red: `#b91c1c` (Nền chính)
    *   Gold: `#D4AF37` (Tiêu đề & Divider)
*   **Typography:** Ưu tiên Font Serif (Times New Roman/Roboto) cho các văn bản trang trọng (Thư ngỏ).

---

## 🚀 Quy trình Triển khai (Deployment)
1.  **GitHub:** Toàn bộ mã nguồn được lưu trữ tại `https://github.com/vuhoang2708/gio-to-toc-hoang2026.git`.
2.  **Vercel:** Tự động Build & Deploy mỗi khi có lệnh `git push` lên nhánh `main`.
3.  **GAS:** Khi cập nhật code backend, bắt buộc **Deploy -> Manage Deployments -> New Version** để giữ nguyên ID Webhook.

---

## 📅 Lịch sử Thay đổi (Change Log)
| Phiên bản | Ngày | Nội dung | Chi tiết |
| :--- | :--- | :--- | :--- |
| **v2.0** | 13/04 | Clan Migration | Chuyển đổi từ dự án DH sang Tộc Hoàng. |
| **v2.5** | 16/04 | Hero UI Fix | Chuyển tên Tộc sang In hoa, dịch chuyển vị trí lộ bức hoành phi. |
| **v3.0** | 16/04 | Genealogy System | Tích hợp Form Gia phả và hệ thống lưu trữ đa Sheet. |

---
*Cập nhật bởi Antigravity v3.0 (Tộc Hoàng Edition) - 19/04/2026*
