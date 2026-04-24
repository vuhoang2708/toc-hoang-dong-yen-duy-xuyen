/**
 * Google Apps Script for Đông Yên Clan Portal
 * Supports: Event Registration & Genealogy Updates
 */

const ADMIN_EMAILS = ["vuhoang2708@gmail.com", "hoangconghien@gmail.com"];
const SPREADSHEET_ID = "1Wa34sit-DkzrCq1U68JMlvMX1L11FES4VnFsO1Pxlts"; // Thay ID thực tế của Tộc Hoàng

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    
    // Phân luồng các loại Payload (Biên tập | Gia Phả | Đăng ký)
    if (data.section) {
      return handleEditorUpdate(ss, data);
    } else if (data.type === 'GENEALOGY_UPDATE') {
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
 * Handle Editor Updates
 */
function handleEditorUpdate(ss, data) {
  const SHEET_NAME = "Biên Tập";
  const sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(["Timestamp", "Phần (Section)", "Nội dung cũ", "Nội dung mới"]);
    sheet.getRange(1, 1, 1, 4).setBackground("#e3f2fd").setFontWeight("bold");
    sheet.setColumnWidth(2, 150);
    sheet.setColumnWidth(3, 400);
    sheet.setColumnWidth(4, 400);
  }
  
  sheet.appendRow([
    new Date(),
    data.section || "",
    data.old_content || "",
    data.new_content || ""
  ]);
  
  // Gửi Email thông báo thay đổi (Optional - tuỳ chọn thêm sau nếu cần)
  sendEditorNotification(data);
  
  return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
    .setMimeType(ContentService.MimeType.JSON);
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

function sendEditorNotification(data) {
  const subject = `[BIÊN TẬP] Cập nhật mục: ${data.section}`;
  const htmlBody = `
    <h3>Có sự thay đổi nội dung ở Bảng Biên Tập:</h3>
    <ul>
      <li><b>Phần:</b> ${data.section}</li>
      <li><b>Nội dung MỚI:</b><br /> ${data.new_content}</li>
      <hr>
      <li><b>Nội dung CŨ:</b><br /> ${data.old_content}</li>
    </ul>
    <p><i>Trang dữ liệu: Sheet "Biên Tập".</i></p>
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
