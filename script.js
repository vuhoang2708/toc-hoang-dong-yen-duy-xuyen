const topics = [
  {
    num: 1,
    name: "Thoả thuận Văn hoá",
    en: "Culture Pact",
    desc: "Thảo luận và thiết lập các hành vi, thái độ chung được thống nhất giữa các thành viên để tạo ra môi trường học tập và làm việc an toàn, cởi mở. Chọn 3 hành vi từ 11 đề xuất — chỉ giữ 3 để dễ nhớ và ai cũng thực hiện được."
  },
  {
    num: 2,
    name: "Giá trị Cốt lõi",
    en: "Core Values (ME & WE)",
    desc: "Khám phá 7 cấp độ nhận thức và giá trị cốt lõi cá nhân (ME), từ đó đối chiếu và thống nhất với các giá trị chung của tập thể (WE) thông qua những hành vi cụ thể. Giá trị thật sự = La bàn dẫn lối + Thời gian thực sự dành cho nó."
  },
  {
    num: 3,
    name: "La bàn và Đồng hồ",
    en: "Compass & Clock",
    desc: "Đánh giá sự đồng nhất giữa những gì chúng ta coi trọng, dẫn lối cuộc sống (La bàn) và các hành động thực tế chúng ta đang dành thời gian thực hiện hàng ngày (Đồng hồ). Nơi hai yếu tố khớp nhau = giá trị thực sự (actual values)."
  },
  {
    num: 4,
    name: "Ba cấp độ Hạnh phúc",
    en: "Levels of Happiness",
    desc: "Pleasure (thú vui) → Passion (đam mê) → Higher Purpose (mục đích cao cả). Hạnh phúc bền lâu đến từ Higher Purpose — việc gắn kết hành động với điều gì đó lớn hơn chính bản thân. Aristotle: 'Hạnh phúc là mục đích tồn tại của chúng ta và hạnh phúc phụ thuộc vào chính chúng ta.'"
  },
  {
    num: 5,
    name: "Khoa học Hạnh phúc & 3 Đòn bẩy",
    en: "Science of Happiness & 3 Levers",
    desc: "Thuyết Tự quyết (Self-Determination Theory): Cảm giác Tiến bộ · Cảm giác Tự chủ · Cảm giác Kết nối. Ba cảm giác này chuyển hóa thành 5 thói quen hạnh phúc. Kết nối = với chính mình + với người xung quanh + với thiên nhiên."
  },
  {
    num: 6,
    name: "Thói quen Tỉnh thức",
    en: "Mindfulness",
    desc: "Rèn luyện sự tập trung chú ý vào khoảnh khắc hiện tại mà không phán xét. Đây là trạng thái nền tảng và cốt lõi nhất để có thể thực hành các thói quen hạnh phúc còn lại. 98% dân số không thể đa nhiệm hiệu quả — tỉnh thức giúp chúng ta tập trung."
  },
  {
    num: 7,
    name: "Thói quen Biết ơn",
    en: "Gratitude",
    desc: "Học cách nhận thức và trân trọng không chỉ những điều tốt đẹp, mà còn biết ơn nghịch cảnh, những điều tốt đẹp sẽ đến trong tương lai và biết ơn chính bản thân mình. Biết ơn trực tiếp kích hoạt Cảm giác Tiến bộ."
  },
  {
    num: 8,
    name: "Thói quen Lạc quan",
    en: "Optimism (ABCDE Tool)",
    desc: "Rèn luyện não bộ nhìn nhận sự việc theo hướng tích cực. Công cụ ABCDE: A-Adversity (nghịch cảnh) → B-Belief (niềm tin phát sinh) → C-Consequence (hậu quả) → D-Dispute (phản biện lại) → E-Effect & Action (kết quả mới). Biến cạm bẫy thành cơ hội."
  },
  {
    num: 9,
    name: "Thói quen Phiêu",
    en: "Flow",
    desc: "Trạng thái đắm chìm hoàn toàn và không bị phân tâm vào công việc hiện tại. Để đạt Phiêu cần: (1) Nhiệm vụ đầy thách thức, (2) Kỹ năng đủ để chinh phục, (3) Nhận phản hồi ngay lập tức, (4) Hiện diện và không bị phân tâm. Tìm 'microflow' trong những việc nhỏ hằng ngày."
  },
  {
    num: 10,
    name: "Thói quen Vị nhân",
    en: "Altruism",
    desc: "Khuyến khích sự cống hiến vì lợi ích chung và giúp đỡ người khác từ tận đáy lòng. Học cách trở thành 'người cho đi thông minh' (smart giver) — kết hợp giữa lòng tốt và trí tuệ, tránh trở thành 'người hy sinh' tiêu cực. Fit-forward: nhận và trao tiếp."
  }
];

// Render topics
const list = document.getElementById('topicsList');
topics.forEach(t => {
  const item = document.createElement('div');
  item.className = 'topic-item';
  item.innerHTML = `
    <div class="topic-header">
      <div class="topic-num">${t.num}</div>
      <div style="flex:1">
        <div class="topic-name">${t.name}</div>
        <div class="topic-en">${t.en}</div>
      </div>
      <div class="topic-chevron">▾</div>
    </div>
    <div class="topic-body">${t.desc}</div>
  `;
  item.querySelector('.topic-header').addEventListener('click', () => {
    const isOpen = item.classList.contains('open');
    // close all
    document.querySelectorAll('.topic-item.open').forEach(el => el.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  });
  list.appendChild(item);
});
