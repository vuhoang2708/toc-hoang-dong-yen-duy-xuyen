const topics = [
  {
    num: 1,
    name: "Khoa học hạnh phúc",
    en: "Science of Happiness",
    desc: "Nền tảng của khóa học dựa trên các nghiên cứu về tâm lý học tích cực và các yếu tố tạo nên hạnh phúc thực sự và bền vững trong công việc cũng như cuộc sống."
  },
  {
    num: 2,
    name: "3 đòn bẩy hạnh phúc",
    en: "3 Levers of Happiness",
    desc: "Khám phá Thuyết Tự quyết với 3 đòn bẩy: Cảm giác Tiến bộ (Progress), Cảm giác Tự chủ (Control) và Cảm giác Kết nối (Connection)."
  },
  {
    num: 3,
    name: "Mục đích cao cả",
    en: "Higher Purpose",
    desc: "Hiểu về ba cấp độ hạnh phúc: Thú vui, Đam mê và Mục đích cao cả. Hạnh phúc lâu dài nhất đến từ việc tìm thấy và cống hiến cho mục đích lớn lao (Higher Purpose)."
  },
  {
    num: 4,
    name: "Giá trị bản thân",
    en: "Core Values",
    desc: "Nhận diện những giá trị cốt lõi của bản thân (ME) và cách để mang những giá trị đó vào môi trường làm việc tập thể (WE)."
  },
  {
    num: 5,
    name: "Thực tế so với Tuyên ngôn",
    en: "Actual vs Declared Values",
    desc: "Đánh giá lại sự khác biệt giữa những giá trị chúng ta tuyên bố với cách chúng ta đang thực sự hành động và tư duy mỗi ngày."
  },
  {
    num: 6,
    name: "La bàn + Tài nguyên (Thời gian và Tiền bạc)",
    en: "Compass & Resources",
    desc: "Sự đồng bộ giữa kim chỉ nam (La bàn) với việc chúng ta phân bổ hai tài nguyên quý giá nhất: Thời gian và Tiền bạc. Giá trị thật sự nằm ở nơi ta dành thời gian."
  },
  {
    num: 7,
    name: "Thói quen hạnh phúc: Biết ơn và Lạc quan, Vị Nhân, Tỉnh thức và Phiêu",
    en: "Happiness Habits",
    desc: "Bộ 5 thói quen cụ thể giúp kích hoạt 3 đòn bẩy hạnh phúc trong não bộ: Biết ơn (nhận ra giá trị), Lạc quan (vượt nghịch cảnh), Vị nhân (cống hiến), Tỉnh thức (tập trung hiện tại) và Phiêu (đắm chìm năng suất cao)."
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
