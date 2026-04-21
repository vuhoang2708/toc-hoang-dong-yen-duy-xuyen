import base64
import os

brain_dir = r'C:\Users\vu.hoang\.gemini\antigravity\brain\eb9b703f-4fcc-488f-9663-77d04d395a58'
output_dir = 'editor'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_file = os.path.join(output_dir, 'index.html')

imgs = {
    'HERO': 'hero_section_1776679509005.png',
    'ABOUT': 'about_section_1776679520136.png',
    'VALUES': 'values_section_1776679529910.png',
    'LETTER_SIGN': 'genealogy_letter_2_1776679650126.png',
    'INFO': 'info_card_section_1776679659928.png',
    'EVENT': 'event_section_1776679671260.png'
}

b64_data = {}
for k, v in imgs.items():
    with open(os.path.join(brain_dir, v), 'rb') as f:
        b64_data[k] = base64.b64encode(f.read()).decode('utf-8')

template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bảng Biên Tập Nội Dung - Tộc Hoàng Đông Yên</title>
    <style>
        :root { --primary: #8b0000; --gold: #fbc02d; --bg: #f4f7f6; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 1500px; margin: 0 auto; padding: 20px; background: var(--bg); }
        h1 { text-align: center; color: var(--primary); padding: 20px 0; margin-bottom: 20px; border-bottom: 4px var(--primary) double; position: relative; }
        .instruction { background: #fffde7; border-left: 5px solid var(--gold); padding: 20px; margin-bottom: 30px; border-radius: 4px; font-size: 1.1rem; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        
        /* Floating Toolbar */
        .toolbar { position: sticky; top: 10px; z-index: 1000; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); padding: 15px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border: 1px solid #ddd; }
        .status-badge { font-size: 0.9rem; color: #666; font-weight: bold; }
        .btn { padding: 12px 25px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 1rem; transition: all 0.3s; }
        .btn-submit { background: #2e7d32; color: white; }
        .btn-submit:hover { background: #1b5e20; transform: scale(1.05); }
        .btn-submit:disabled { background: #ccc; cursor: not-allowed; }

        table { width: 100%; border-collapse: collapse; background: #fff; margin-bottom: 100px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); table-layout: fixed; }
        th, td { border: 1px solid #ddd; padding: 20px; text-align: left; vertical-align: top; word-wrap: break-word; }
        th { background-color: var(--primary); color: white; text-transform: uppercase; font-size: 0.9rem; }
        .section-name { background: #333; color: #fff; font-weight: bold; font-size: 1.2rem; padding: 10px 20px; }
        .screen-img { width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px; display: block; filter: grayscale(20%); transition: filter 0.3s; }
        .screen-img:hover { filter: grayscale(0%); }
        
        .current-content { background: #f9f9f9; padding: 15px; border: 1px solid #eee; white-space: pre-wrap; font-size: 1.05rem; color: #000; line-height: 1.8; }
        .edit-box { min-height: 250px; width: 100%; border: 2px solid var(--primary); padding: 15px; background: #fff; font-size: 1.1rem; font-weight: 500; color: #d32f2f; box-sizing: border-box; border-radius: 4px; outline: none; }
        .edit-box:focus { background: #fff8f8; box-shadow: 0 0 10px rgba(139,0,0,0.1); }
        
        .signed-notice { color: #555; font-style: italic; text-align: center; padding: 60px; background: #f5f5f5; border: 2px dashed #bbb; font-size: 1.2rem; }
        .verbatim-label { display: block; font-weight: bold; color: var(--primary); margin-bottom: 10px; text-decoration: underline; font-size: 0.9rem; opacity: 0.8; }

        /* Toast notifications */
        #toast { visibility: hidden; min-width: 250px; margin-left: -125px; background-color: #333; color: #fff; text-align: center; border-radius: 5px; padding: 16px; position: fixed; z-index: 2000; left: 50%; bottom: 30px; font-size: 17px; }
        #toast.show { visibility: visible; -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s; animation: fadein 0.5s, fadeout 0.5s 2.5s; }
        @-webkit-keyframes fadein { from {bottom: 0; opacity: 0;} to {bottom: 30px; opacity: 1;} }
        @keyframes fadein { from {bottom: 0; opacity: 0;} to {bottom: 30px; opacity: 1;} }
        @-webkit-keyframes fadeout { from {bottom: 30px; opacity: 1;} to {bottom: 0; opacity: 0;} }
        @keyframes fadeout { from {bottom: 30px; opacity: 1;} to {bottom: 0; opacity: 0;} }
    </style>
</head>
<body>
    <h1>📋 HỆ THỐNG BIÊN TẬP NỘI DUNG TỘC HOÀNG</h1>
    
    <div class="toolbar">
        <div class="status-badge" id="save-status">Dữ liệu: Chưa có thay đổi</div>
        <div>
            <button class="btn btn-submit" id="submit-btn" onclick="submitToGoogleSheets()">🚀 GỬI BAN BIÊN TẬP (LƯU LÊN CLOUD)</button>
        </div>
    </div>

    <div class="instruction">
        <b>Dành cho Ban biên tập:</b><br>
        1. Các bác vui lòng gõ nội dung mới vào ô màu trắng bên phải.<br>
        2. <b>Hệ thống tự động lưu:</b> Các bác yên tâm gõ, dữ liệu sẽ tự động lưu vào máy tính/điện thoại, dù đóng trang cũng không mất.<br>
        3. <b>Gửi duyệt:</b> Sau khi sửa xong, các bác vui lòng bấm nút màu xanh <b>"GỬI BAN BIÊN TẬP"</b> ở phía trên để cháu (Hoàng Vũ) nhận được nội dung.
    </div>

    <table>
        <thead>
            <tr>
                <th width="35%">ẢNH CHỤP GIAO DIỆN</th>
                <th width="35%">NỘI DUNG HIỆN TẠI</th>
                <th width="30%">NỘI DUNG MỚI (CÁC BÁC NHẬP TẠI ĐÂY)</th>
            </tr>
        </thead>
        <tbody>
            <!-- 1. HERO -->
            <tr><td colspan="3" class="section-name">1. PHẦN ĐẦU TRANG (HERO)</td></tr>
            <tr>
                <td><img src="data:image/png;base64,__HERO__" class="screen-img"></td>
                <td class="current-content" id="orig_hero">
<span class="verbatim-label">[Tiêu đề tổ chức]:</span>HỘI ĐỒNG GIA TỘC

<span class="verbatim-label">[Tên dòng tộc]:</span>TỘC HOÀNG/HUỲNH ĐÔNG YÊN

<span class="verbatim-label">[Địa danh]:</span>Thôn Đông Yên, Xã Duy Xuyên, Thành phố Đà Nẵng (nguyên là Thôn Đông Yên, Xã Duy Trinh, Huyện Duy Xuyên, Tỉnh Quảng Nam)

<span class="verbatim-label">[Câu đối]:</span>"Cây có gốc mới nở nhành xanh ngọn, Nước có nguồn mới bể rộng sông sâu"
                </td>
                <td><div class="edit-box" id="edit_hero" contenteditable="true" oninput="autoSave(this)"></div></td>
            </tr>

            <!-- 2. ABOUT -->
            <tr><td colspan="3" class="section-name">2. GIỚI THIỆU CỘI NGUỒN (ABOUT)</td></tr>
            <tr>
                <td><img src="data:image/png;base64,__ABOUT__" class="screen-img"></td>
                <td class="current-content" id="orig_about">
Tộc Hoàng Đông Yên có khởi nguồn từ vùng đất Duy Xuyên, Quảng Nam - nơi địa linh nhân kiệt với truyền thống hiếu học và lòng yêu quê hương nồng nàn.

Qua bao thế hệ, con cháu họ Hoàng đã không ngừng nỗ lực, đóng góp công sức xây dựng quê hương, gìn giữ nếp gia phong và bản sắc của tổ tiên để lại.

Nhà thờ Tộc không chỉ là nơi thờ tự linh thiêng mà còn là biểu tượng của sự đoàn kết, nơi hội tụ của những tâm hồn luôn hướng về cội nguồn.
                </td>
                <td><div class="edit-box" id="edit_about" contenteditable="true" oninput="autoSave(this)"></div></td>
            </tr>

            <!-- 3. VALUES -->
            <tr><td colspan="3" class="section-name">3. GIÁ TRỊ CỐT LÕI (VALUES)</td></tr>
            <tr>
                <td><img src="data:image/png;base64,__VALUES__" class="screen-img"></td>
                <td class="current-content" id="orig_values">
1. Uống Nước Nhớ Nguồn: Gìn giữ truyền thống thờ cúng tổ tiên, hiếu kính với cha mẹ và tiền nhân.

2. Đoàn Kết Tương Trợ: Kết nối con cháu trong và ngoài nước, cùng nhau sẻ chia và hỗ trợ trong cuộc sống.

3. Khuyến Học Khuyến Tài: Động viên tinh thần hiếu học của thế hệ trẻ, vinh danh những tấm gương thành đạt.
                </td>
                <td><div class="edit-box" id="edit_values" contenteditable="true" oninput="autoSave(this)"></div></td>
            </tr>

            <!-- 4. LETTER (READ ONLY) -->
            <tr><td colspan="3" class="section-name">4. THƯ NGỎ TRƯỞNG TỘC (KHÔNG THAY PHẦN NÀY)</td></tr>
            <tr>
                <td><img src="data:image/png;base64,__LETTER_SIGN__" class="screen-img"></td>
                <td colspan="2" class="signed-notice">
                    <b>THÔNG BÁO:</b> Nội dung thư ngỏ đã được ký và đóng dấu chính thức bởi Trưởng tộc HOÀNG NGỌC THỊNH (Đời thứ 11).
                </td>
            </tr>

            <!-- 5. INFO REQUIREMENTS -->
            <tr><td colspan="3" class="section-name">5. THÔNG TIN CUNG CẤP & LIÊN HỆ</td></tr>
            <tr>
                <td><img src="data:image/png;base64,__INFO__" class="screen-img"></td>
                <td class="current-content" id="orig_info">
<span class="verbatim-label">[Tiêu đề phần]:</span>Cập Nhật Thông Tin Gia Phả

<span class="verbatim-label">[Lời dẫn]:</span>Để hoàn thiện dữ liệu Phả hệ kỹ thuật số và chuẩn bị cho Đại lễ Tế Xuân 2026, Hội đồng Gia tộc kính mong Quý bà con cung cấp thông tin chi tiết về các thành viên trong gia đình.

<span class="verbatim-label">[Nội dung cung cấp]:</span>
- Thông tin cá nhân (Ngày sinh Dương/Âm, Quê quán, Nơi cư trú).
- Thông tin gia đình (Họ tên Cha, Ông nội, Vợ/Chồng, Con cái).
- Đối với người đã quá cố: Cung cấp thêm ngày mất, nơi an táng.
- Các ông bà các đời trước: Cung cấp thông tin chính xác để hiệu chỉnh.

<span class="verbatim-label">[Liên hệ]:</span>Ông Hoàng Công Hiên (Thư ký Tộc) - 0946.000.777
                </td>
                <td><div class="edit-box" id="edit_info" contenteditable="true" oninput="autoSave(this)"></div></td>
            </tr>

            <!-- 6. EVENT -->
            <tr><td colspan="3" class="section-name">6. THÔNG TIN ĐẠI LỄ TẾ XUÂN 2026</td></tr>
            <tr>
                <td><img src="data:image/png;base64,__EVENT__" class="screen-img"></td>
                <td class="current-content" id="orig_event">
Kính Mời Tham Dự Lễ Tế Xuân 2026

Ngày: 26.04.2026 (Tức 10/3 Âm Lịch)
Giờ: 08:00 Sáng - Bắt đầu hành lễ
Địa điểm: Duy Xuyên, Quảng Nam
                </td>
                <td><div class="edit-box" id="edit_event" contenteditable="true" oninput="autoSave(this)"></div></td>
            </tr>
        </tbody>
    </table>

    <div id="toast"></div>

    <script>
        const GOOGLE_APP_URL = "https://script.google.com/macros/s/AKfycby3QJAZN7y_aB1NvmwB4bHsqpGYYfoHBCLXlP8fNtfqiEfz5QPxa1t6XyoLOGj8GzaU/exec";

        // Load saved content on startup
        window.onload = function() {
            const boxes = document.querySelectorAll('.edit-box');
            boxes.forEach(box => {
                const saved = localStorage.getItem(box.id);
                if (saved) box.innerText = saved;
            });
            updateStatus("Sẵn sàng biên tập");
        }

        function autoSave(el) {
            localStorage.setItem(el.id, el.innerText);
            updateStatus("Đã lưu tự động lúc " + new Date().toLocaleTimeString());
        }

        function updateStatus(msg) {
            document.getElementById('save-status').innerText = msg;
        }

        function showToast(msg) {
            const t = document.getElementById("toast");
            t.innerText = msg;
            t.className = "show";
            setTimeout(() => { t.className = t.className.replace("show", ""); }, 3000);
        }

        async function submitToGoogleSheets() {
            const btn = document.getElementById('submit-btn');
            const editBoxes = document.querySelectorAll('.edit-box');
            let hasChanges = false;
            
            btn.disabled = true;
            btn.innerText = "⌛ ĐANG GỬI DỮ LIỆU...";

            try {
                for (let box of editBoxes) {
                    const newContent = box.innerText.trim();
                    if (!newContent) continue;

                    const sectionId = box.id.replace('edit_', '');
                    const origContent = document.getElementById('orig_' + sectionId).innerText;

                    const data = {
                        section: sectionId.toUpperCase(),
                        old_content: origContent,
                        new_content: newContent
                    };

                    await fetch(GOOGLE_APP_URL, {
                        method: 'POST',
                        mode: 'no-cors', // Apps Script requires no-cors for simple Web Apps
                        cache: 'no-cache',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                    hasChanges = true;
                }

                if (hasChanges) {
                    showToast("✅ Đã gửi dữ liệu thành công lên Google Sheet!");
                    updateStatus("Đã đồng bộ lên Cloud lúc " + new Date().toLocaleTimeString());
                } else {
                    showToast("⚠️ Bác chưa nhập nội dung mới nào để gửi.");
                }
            } catch (error) {
                console.error(error);
                showToast("❌ Lỗi khi gửi dữ liệu. Các bác vui lòng liên hệ Hoàng Vũ.");
            } finally {
                btn.disabled = false;
                btn.innerText = "🚀 GỬI BAN BIÊN TẬP (LƯU LÊN CLOUD)";
            }
        }

        window.onbeforeunload = function() {
            return "Bác có chắc chắn muốn rời khỏi trang không? Hãy đảm bảo đã bấm 'GỬI' để lưu dữ liệu.";
        };
    </script>
</body>
</html>
"""

for k, v in b64_data.items():
    template = template.replace(f"__{k}__", v)

template = template.replace("\\n", "<br>")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(template)
