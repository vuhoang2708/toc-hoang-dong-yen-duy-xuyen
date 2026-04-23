# 🛠️ TÀI LIỆU HƯỚNG DẪN KỸ THUẬT (TECHNICAL SPECIFICATION)
**Dự án: Cổng thông tin Tộc Hoàng Đông Yên**

👉 **Mục đích:** Hướng dẫn kỹ thuật về cấu trúc mã nguồn, quy trình triển khai (Deployment) và vận hành các script tự động hóa.

---

## 1. CẤU TRÚC HỆ THỐNG (STACK)
*   **Frontend:** HTML5, Vanilla CSS3 (Glassmorphism UI), Javascript (ES6+).
*   **Backend (Serverless):** Google Apps Script (Webhook) kết nối Google Sheets CRM.
*   **Infrastructure:** GitHub (Source Control), Vercel (Auto-deployment).
*   **Media Production:** Python 3.12 (Edge-TTS, MoviePy) để tạo video giới thiệu tự động.

---

## 2. QUY TRÌNH TRIỂN KHAI (DEPLOYMENT)

### 📡 Kết nối GitHub & Vercel
*   **Repository:** `https://github.com/vuhoang2708/toc-hoang-dong-yen-duy-xuyen`
*   **Luồng làm việc:** 
    1.  Mọi thay đổi commit lên nhánh `main` sẽ kích hoạt Webhook của Vercel.
    2.  Vercel tự động build và cập nhật bản mới nhất lên link [Live](https://toc-hoang-dong-yen-duy-xuyen.vercel.app/).
*   **Môi trường Local:** Chạy `python -m http.server 8000` để kiểm thử giao diện trước khi push.

---

## 3. CẤU TRÚC THƯ MỤC (DIRECTORY STRUCTURE)
```text
/
├── index.html          # Trang chủ chính thức
├── admin.html          # Trung tâm quản trị (Admin Portal)
├── editor/             # Trình biên tập nội dung 3 cột (Verbatim Editor)
├── login.html          # Trang đăng nhập bảo mật
├── genealogy/          # Trang Bổ sung thành viên gia phả
├── genealogy-tree/     # Cây phả hệ tương tác (Interactive Tree)
├── register/           # Trang đăng ký Lễ Tế Xuân (Auto-switch logic)
├── assets/             # Hình ảnh, CSS, Javascript dùng chung
├── scripts/            # Bộ công cụ Python sản xuất Video Overview
└── google_apps_script.js # Mã nguồn Webhook chạy trên Google Cloud
```

---

## 4. CÔNG CỤ SẢN XUẤT VIDEO AI (SCRIPTS)
Bộ công cụ nằm trong thư mục `scripts/` cho phép tạo video giới thiệu portal tự động:
1.  **Cài đặt:** `pip install edge-tts moviepy opencv-python pillow`
2.  **Sử dụng:**
    *   Chạy `python scripts/generate_overview_v3.py`: Lấy screenshot website và lồng tiếng AI.
    *   Chạy `scripts/assemble_video_v3.py`: Xuất video MP4 hoàn chỉnh.

---

## 5. LOGIC TỰ ĐỘNG HÓA (AUTOMATION)
Website tích hợp logic kiểm tra thời gian thực tại `index.html` và `register/index.html`:
```javascript
const EVENT_DATE = new Date('2026-04-26T12:00:00');
if (new Date() > EVENT_DATE) {
    // Tự động ẩn Form và chuyển sang giao diện "Ký ức"
}
```

---
**[Liên hệ Kỹ thuật]**
Mọi thắc mắc về source code vui lòng liên hệ đội ngũ Antigravity.
*(Cập nhật: 22/04/2026)*
