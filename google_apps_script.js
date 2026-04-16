/**
 * Google Apps Script for Đông Yên Clan Event Registration
 * Target: Save to Sheet and Email BTC
 */

const ADMIN_EMAILS = ["vuhoang2708@gmail.com", "hoangconghien@gmail.com"];
const SPREADSHEET_ID = "YOUR_SPREADSHEET_ID_HERE"; // Thay bằng ID của Google Sheet của bạn
const SHEET_NAME = "Registration";

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME) || 
                  SpreadsheetApp.openById(SPREADSHEET_ID).insertSheet(SHEET_NAME);
    
    // Header nếu sheet mới
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["Timestamp", "Họ tên", "Số điện thoại", "Email", "Số người dự", "Đi chung xe", "Session ID", "Source"]);
    }
    
    const timestamp = new Date();
    sheet.appendRow([
      timestamp,
      data.fullName || "",
      data.phone || "",
      data.email || "",
      data.numAttendees || "1",
      data.shuttle_bus || "No",
      data.sessionId || "",
      data.source || ""
    ]);
    
    // Gửi email cho BTC
    sendNotificationEmail(data);
    
    return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function sendNotificationEmail(data) {
  const subject = `[ĐĂNG KÝ MỚI] Lễ tế xuân Tộc Hoàng - ${data.fullName}`;
  const htmlBody = `
    <h3>Thông tin đăng ký mới:</h3>
    <ul>
      <li><b>Họ tên:</b> ${data.fullName}</li>
      <li><b>Số điện thoại:</b> ${data.phone}</li>
      <li><b>Email:</b> ${data.email || "Không có"}</li>
      <li><b>Số người dự:</b> ${data.numAttendees || "1"}</li>
      <li><b>Đi chung xe 16 chỗ từ Đà Nẵng:</b> ${data.shuttle_bus === 'Yes' ? 'Có' : 'Không'}</li>
    </ul>
    <p><i>Dữ liệu đã được lưu vào Google Sheet.</i></p>
  `;
  
  ADMIN_EMAILS.forEach(email => {
    MailApp.sendEmail({
      to: email,
      subject: subject,
      htmlBody: htmlBody
    });
  });
}
