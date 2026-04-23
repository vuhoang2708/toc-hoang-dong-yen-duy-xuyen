/**
 * Google Apps Script for Đông Yên Clan Portal
 * Supports: Event Registration & Genealogy Updates
 */

const ADMIN_EMAILS = ["vuhoang2708@gmail.com", "hoangconghien@gmail.com"];
const SPREADSHEET_ID = "YOUR_SPREADSHEET_ID_HERE"; // Replace with your actual Sheet ID

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    
    if (data.type === 'GENEALOGY_UPDATE') {
      return handleGenealogy(ss, data);
    } else {
      return handleRegistration(ss, data);
    }
      
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Handle Genealogy Form Submissions
 */
function handleGenealogy(ss, data) {
  const SHEET_NAME = "Gia Phả";
  const sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  
  if (sheet.getLastRow() === 0) {
    sheet.appendRow([
      "Timestamp", "Người cung cấp", "Đời thứ", "Con thứ", "Ngày sinh", 
      "Quê quán", "Nơi cư trú", "Họ tên cha", "Họ tên ông nội", 
      "Số điện thoại", "Thông tin gia đình", "Thông tin người quá cố", "Source"
    ]);
    sheet.getRange(1, 1, 1, 13).setBackground("#dcfce7").setFontWeight("bold");
  }
  
  sheet.appendRow([
    new Date(),
    data.providerName || "",
    data.generation || "",
    data.childOrder || "",
    data.dob || "",
    data.hometown || "",
    data.residence || "",
    data.fatherName || "",
    data.gfName || "",
    data.phone || "",
    data.familyInfo || "",
    data.deceasedInfo || "",
    data.source || ""
  ]);
  
  sendGenealogyNotification(data);
  return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Handle Event Registrations
 */
function handleRegistration(ss, data) {
  const SHEET_NAME = "Registration";
  const sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(["Timestamp", "Họ tên", "Số điện thoại", "Email", "Số người dự", "Đi chung xe", "Session ID", "Source"]);
    sheet.getRange(1, 1, 1, 8).setBackground("#fee2e2").setFontWeight("bold");
  }
  
  sheet.appendRow([
    new Date(),
    data.fullName || "",
    data.phone || "",
    data.email || "",
    data.numAttendees || "1",
    data.shuttle_bus || "No",
    data.sessionId || "",
    data.source || ""
  ]);
  
  sendRegistrationNotification(data);
  return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
    .setMimeType(ContentService.MimeType.JSON);
}

function sendRegistrationNotification(data) {
  const subject = `[ĐĂNG KÝ MỚI] Lễ tế xuân Tộc Hoàng - ${data.fullName}`;
  const htmlBody = `
    <h3>Thông tin đăng ký mới:</h3>
    <ul>
      <li><b>Họ tên:</b> ${data.fullName}</li>
      <li><b>Số điện thoại:</b> ${data.phone}</li>
      <li><b>Số người dự:</b> ${data.numAttendees || "1"}</li>
      <li><b>Đi chung xe:</b> ${data.shuttle_bus === 'Yes' ? 'Có' : 'Không'}</li>
    </ul>
  `;
  sendEmail(subject, htmlBody);
}

function sendGenealogyNotification(data) {
  const subject = `[CẬP NHẬT GIA PHẢ] Từ: ${data.providerName} (Cha: ${data.fatherName})`;
  const htmlBody = `
    <h3>Thông tin bổ sung gia phả mới:</h3>
    <ul>
      <li><b>Người cung cấp:</b> ${data.providerName}</li>
      <li><b>Đời thứ:</b> ${data.generation}</li>
      <li><b>Họ tên cha:</b> ${data.fatherName}</li>
      <li><b>Số điện thoại:</b> ${data.phone}</li>
    </ul>
    <p><i>Xem chi tiết tại Sheet "Gia Phả".</i></p>
  `;
  sendEmail(subject, htmlBody);
}

function sendEmail(subject, htmlBody) {
  ADMIN_EMAILS.forEach(email => {
    try {
      MailApp.sendEmail({ to: email, subject: subject, htmlBody: htmlBody });
    } catch (e) { console.error("Email error: " + e); }
  });
}
