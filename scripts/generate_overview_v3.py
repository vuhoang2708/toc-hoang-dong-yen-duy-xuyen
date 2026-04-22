import os
import asyncio
import requests
import time
import edge_tts
from playwright.async_api import async_playwright
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, vfx
from PIL import Image
import numpy as np

# Setup paths
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets", "videos")
TEMP_DIR = os.path.join(WORKSPACE_DIR, "temp_video")

os.makedirs(ASSETS_DIR, exist_ok=True)
# os.makedirs(TEMP_DIR, exist_ok=True)
# Không xóa file cũ để tận dụng các audio đã tải thành công

FPT_API_KEY = "a7eutHcRA60XMdj746z0viJVt0KK2gR6"
FPT_VOICE = "giahuy" # Giọng Nam Đà Nẵng
FPT_SPEED = "-1"     # Giảm tốc độ đọc cho trang nghiêm (-1 là chậm vừa)

# Lời thoại và kịch bản cảnh quay (Segments)
segments = [
    {
        "id": "01_hero_a",
        "text": "Kính thưa Hội đồng gia tộc và toàn thể bà con. Nhân Lễ tế xuân đầu năm mới hai nghìn không trăm hai mươi sáu.",
        "page": "index.html",
        "selector": ".hero-v2",
        "voice": FPT_VOICE
    },
    {
        "id": "01_hero_b",
        "text": "Nhóm thực hiện đã nỗ lực để xây dựng cổng thông tin điện tử, là một trong những viên gạch đầu tiên cho ngôi nhà của Tộc ta.",
        "page": "index.html",
        "selector": "section#about", # Phân đoạn Cội nguồn
        "voice": FPT_VOICE
    },
    {
        "id": "01_hero_c",
        "text": "Đây là khởi đầu của hành trình kết nối cội nguồn thiêng liêng, hướng tới tương lai bền vững.",
        "page": "index.html",
        "selector": "section#values", # Phân đoạn Giá trị cốt lõi
        "voice": FPT_VOICE
    },
    {
        "id": "02_genealogy",
        "text": "Ngoài những nội dung cơ bản về giá trị cốt lõi và Lịch sử, trang web cũng đã triển khai được Cây Phả Hệ - Linh hồn của cổng thông tin với sơ đồ tương tác trực quan, giúp thế hệ trẻ dễ dàng tra cứu dòng dõi và tự hào về tổ tiên ngàn đời của mình.",
        "page": "index.html",
        "selector": "section#tree-map",
        "voice": FPT_VOICE
    },
    {
        "id": "03_contribution",
        "text": "Mục thông tin gia phả là cầu nối quan trọng. Chúng tôi thiết tha kêu gọi bà con cùng chung tay cập nhật, bổ sung thông tin để bộ rễ của dòng họ ngày càng sum suê và chính xác hơn.",
        "page": "index.html",
        "selector": ".letter-parchment", # Chụp phân đoạn Thư Ngỏ
        "voice": FPT_VOICE
    },
    {
        "id": "04_map",
        "text": "Nhà Thờ Tộc tại Đông Yên hiện nay cũng đã được định vị trên bản đồ thế giới. Dù ở bất cứ đâu, những người con Tộc Hoàng cũng có thể tìm được lối về quê nhà.",
        "page": "index.html",
        "selector": "h2:has-text('Vị Trí Nhà Thờ Tộc')", # Selector chuẩn dựa trên tiêu đề
        "voice": FPT_VOICE
    },
    {
        "id": "05_admin",
        "text": "Hệ thống quản trị thông minh giúp Ban biên tập hoàn toàn chủ động cập nhật tin tức, đảm bảo ngôi nhà số luôn sống động và đầy ắp những câu chuyện dòng tộc mới.",
        "page": "genealogy/index.html",
        "selector": "body", # Trang Admin chụp toàn cảnh
        "voice": FPT_VOICE
    },
    {
        "id": "06_social",
        "text": "Trang web phiên bản này mới chỉ là điểm khởi đầu. Kính mong bà con cùng tham gia nhóm Facebook, Zalo để kết nối tình thân và cập nhật thông tin dòng tộc nhanh nhất.",
        "page": "index.html",
        "selector": "section:has(h3:has-text('Group Facebook'))", # Chụp phần Facebook/Zalo
        "voice": FPT_VOICE
    },
    {
        "id": "07_final",
        "text": "Tộc Hoàng Đông Yên. Phúc ấm tổ tiên lưu hậu thế, Đức dày con cháu hiển tiền nhân. Hướng về nguồn cội, kết nối tương lai.",
        "page": "index.html",
        "selector": "footer", # Chụp Footer chứa câu đối
        "voice": FPT_VOICE
    },
    {
        "id": "08_qr",
        "text": "Kính mời bà con cùng quét mã trên màn hình để tham gia các nhóm cộng đồng của Tộc ta.",
        "page": "qr_page.html",
        "selector": "body",
        "voice": FPT_VOICE
    }
]

async def generate_audio():
    print(f"--- GENERATING AUDIO (FPT.AI TTS - Voice: {FPT_VOICE}) ---")
    
    for seg in segments:
        audio_path = os.path.join(TEMP_DIR, f"{seg['id']}.mp3")
        
        # Nếu file đã tồn tại và hợp lệ (>10KB), bỏ qua để tiết kiệm quota
        if os.path.exists(audio_path) and os.path.getsize(audio_path) > 10000:
            print(f"[{seg['id']}] Audio already exists. Skipping.")
            continue
            
        print(f"[{seg['id']}] Processing TTS...")
        
        text_clean = seg['text'].replace("\n", " ").strip()
        
        success_segment = False
        for attempt in range(2): # Thử lại tối đa 2 lần nếu polling thất bại
            try:
                # Cấu trúc lại theo tài liệu: Tham số nằm ở Headers, Text nằm ở Body
                headers = {
                    "api_key": FPT_API_KEY,
                    "voice": FPT_VOICE,
                    "speed": FPT_SPEED,
                    "Cache-Control": "no-cache"
                }
                
                # Gửi text dạng raw data (utf-8)
                response = requests.post(
                    "https://api.fpt.ai/hmi/tts/v5", 
                    data=text_clean.encode('utf-8'), 
                    headers=headers,
                    timeout=20
                )
                res_json = response.json()
                
                if res_json.get("error") != 0:
                    print(f"[{seg['id']}] FPT Error: {res_json.get('message')}")
                    break # Lỗi API thì không retry
                    
                async_url = res_json.get("async")
                print(f"[{seg['id']}] Waiting for result (Attempt {attempt+1})...")
                print(f"[{seg['id']}] Async URL: {async_url}")
                
                # Polling để chờ file sẵn sàng
                max_retries = 30 # Tổng cộng khoảng 2-3 phút
                success_poll = False
                for i in range(max_retries):
                    time.sleep(3)
                    try:
                        # Polling link MP3 trực tiếp (không dùng headers key ở đây)
                        check_res = requests.get(async_url, timeout=5)
                        if check_res.status_code == 200:
                            # Kiểm tra xem có đúng là file MP3 hay lỗi JSON
                            if b"error" in check_res.content[:50] and b"message" in check_res.content:
                                print(f"[{seg['id']}] FPT returned error JSON in poll.")
                                break
                            
                            with open(audio_path, 'wb') as f:
                                f.write(check_res.content)
                            print(f"[{seg['id']}] Downloaded successfully ({len(check_res.content)} bytes).")
                            success_poll = True
                            success_segment = True
                            break
                        else:
                            # Log trạng thái 404 hoặc khác để theo dõi
                            if i % 5 == 0: # Cứ 5 lần poll log 1 lần để đỡ rác log
                                print(f"[{seg['id']}] Polling status: {check_res.status_code} (Retry {i}/{max_retries})")
                                
                    except Exception as poll_e:
                        print(f"[{seg['id']}] Polling error: {poll_e}")
                
                if success_poll:
                    break # Thoát vòng lặp retry segment
                else:
                    print(f"[{seg['id']}] Polling timeout on attempt {attempt+1}. Retrying request...")
                    
            except Exception as e:
                print(f"[{seg['id']}] Connection error on attempt {attempt+1}: {e}")
                time.sleep(2)
        
        if not success_segment:
            print(f"[{seg['id']}] FPT.AI failed. Falling back to EDGE-TTS (HoaiMy)...")
            try:
                # Fallback sang Edge-TTS giọng Hoài My (Nam bộ)
                fallback_voice = "vi-VN-HoaiMyNeural"
                communicate = edge_tts.Communicate(text_clean, fallback_voice)
                await communicate.save(audio_path)
                print(f"[{seg['id']}] Saved using Edge-TTS fallback.")
                success_segment = True
            except Exception as e_fallback:
                print(f"[{seg['id']}] Fallback also failed: {e_fallback}")
            
    print("=> Audio generation complete.")

async def take_screenshots():
    print("\n--- CAPTURING SCREENSHOTS (PLAYWRIGHT) ---")
    # Dùng URL Live vì Vercel render nhanh và chuẩn asset
    LIVE_URL = "https://toc-hoang-dong-yen-duy-xuyen.vercel.app"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        for seg in segments:
            screenshot_path = os.path.join(TEMP_DIR, f"{seg['id']}.png")
            
            print(f"[{seg['id']}] Accessing {seg['page']}...")
            url = f"{LIVE_URL}/{seg['page']}" if seg['page'] != "index.html" else LIVE_URL
            
            try:
                await page.goto(url, wait_until="load", timeout=60000)
            except Exception as e:
                print(f"Warning: navigation timeout on {url}. Proceeding anyway.")
                
            await asyncio.sleep(2) # Chờ map và animation load xong
            
            try:
                if seg['selector'] and await page.locator(seg['selector']).count() > 0:
                    element = page.locator(seg['selector']).first
                    # Nếu là map, lấy node cha để thấy khung hình đẹp hơn
                    if "Vị Trí Nhà Thờ Tộc" in seg['selector']:
                        element = page.locator("section:has(h2:has-text('Vị Trí Nhà Thờ Tộc'))").first
                    
                    await element.scroll_into_view_if_needed()
                    await asyncio.sleep(3) # Chờ bản đồ/iframe tải hoàn tất
                    await element.screenshot(path=screenshot_path)
                    print(f"[{seg['id']}] Captured element.")
                else:
                    print(f"[{seg['id']}] Selector not found or is body. Taking viewport screenshot.")
                    await page.screenshot(path=screenshot_path)
            except Exception as e:
                print(f"Error scrolling: {e}")
                await page.screenshot(path=screenshot_path)
            
            print(f"[{seg['id']}] Captured.")
            
        await browser.close()
    print("=> Screenshot capture complete.")

def zoom_out_effect(clip, zoom_start=1.2, zoom_end=1.0):
    """
    Áp dụng hiệu ứng Zoom-out từ tỷ lệ zoom_start về zoom_end
    """
    def get_frame(t):
        frame = clip.get_frame(t)
        im = Image.fromarray(frame)
        w, h = im.size
        # Đảm bảo duration không bằng 0
        dur = max(clip.duration, 0.1)
        scale = zoom_start - (zoom_start - zoom_end) * (t / dur)
        
        new_w, new_h = int(w * scale), int(h * scale)
        
        # Resize
        if hasattr(Image, 'Resampling'):
            resample_filter = Image.Resampling.LANCZOS
        else:
            resample_filter = Image.LANCZOS
            
        resized = im.resize((new_w, new_h), resample_filter)
        
        # Crop center
        left = (new_w - w) / 2
        top = (new_h - h) / 2
        right = left + w
        bottom = top + h
        
        cropped = resized.crop((left, top, right, bottom))
        return np.array(cropped)
        
    return clip.transform(lambda gf, t: get_frame(t))

def zoom_in_effect(clip, zoom_start=1.0, zoom_end=1.2):
    """
    Áp dụng hiệu ứng Zoom-in từ tỷ lệ zoom_start lên zoom_end
    """
    def get_frame(t):
        frame = clip.get_frame(t)
        im = Image.fromarray(frame)
        w, h = im.size
        dur = max(clip.duration, 0.1)
        scale = zoom_start + (zoom_end - zoom_start) * (t / dur)
        
        new_w, new_h = int(w * scale), int(h * scale)
        
        if hasattr(Image, 'Resampling'):
            resample_filter = Image.Resampling.LANCZOS
        else:
            resample_filter = Image.LANCZOS
            
        resized = im.resize((new_w, new_h), resample_filter)
        
        left = (new_w - w) / 2
        top = (new_h - h) / 2
        right = left + w
        bottom = top + h
        
        cropped = resized.crop((left, top, right, bottom))
        return np.array(cropped)
        
    return clip.transform(lambda gf, t: get_frame(t))

def create_video():
    print("\n--- ASSEMBLING VIDEO (MOVIEPY) ---")
    clips = []
    
    for i, seg in enumerate(segments):
        img_path = os.path.join(TEMP_DIR, f"{seg['id']}.png")
        audio_path = os.path.join(TEMP_DIR, f"{seg['id']}.mp3")
        
        if not os.path.exists(img_path) or not os.path.exists(audio_path):
            print(f"Missing assets for {seg['id']}. Skipping.")
            continue

        # Bỏ qua file audio rỗng hoặc hỏng (< 5KB)
        if os.path.getsize(audio_path) < 5000:
            print(f"[{seg['id']}] Audio file empty or corrupted. Skipping this segment.")
            continue
            
        print(f"[{seg['id']}] Processing clip...")
        
        # Tải audio
        audioclip = AudioFileClip(audio_path)
        
        # Tải image và set độ dài theo audio + margin nghỉ
        if seg['id'] == '08_qr':
            duration = audioclip.duration + 4.0 # Cho bà con 4 giây để quét mã sau khi dứt lời
        elif seg['id'] == '07_final':
            duration = audioclip.duration + 1.5
        else:
            duration = audioclip.duration + 1.0
            
        imgclip = ImageClip(img_path).with_duration(duration)
        
        # Áp dụng Zoom effect: 
        # - Đoạn QR không zoom để dễ quét.
        # - Đoạn cuối Zoom-In, các đoạn khác Zoom-Out.
        if seg['id'] == '08_qr':
            pass # No zoom
        elif seg['id'] == '07_final':
            imgclip = zoom_in_effect(imgclip, zoom_start=1.0, zoom_end=1.2)
        else:
            imgclip = zoom_out_effect(imgclip, zoom_start=1.15, zoom_end=1.0)
        
        # Gắn audio vào image
        imgclip = imgclip.with_audio(audioclip)
        
        # Xử lý Cross-fade
        from moviepy.video.fx.CrossFadeIn import CrossFadeIn
        if i > 0:
            imgclip = imgclip.with_effects([CrossFadeIn(0.5)])
            
        clips.append(imgclip)
        
    if not clips:
        print("No clips generated!")
        return

    print("Concatenating clips...")
    # Nối các clip, bỏ padding âm để các đoạn nghỉ không bị đè lên nhau
    final_video = concatenate_videoclips(clips, method="compose")
    
    output_path = os.path.join(ASSETS_DIR, "overview_v3.mp4")
    print(f"Rendering final video to {output_path}...")
    
    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        threads=4,
        preset="ultrafast"
    )
    print("=> Video creation complete!")
    print(f"Final output: {output_path}")

async def main():
    os.makedirs(os.path.join(WORKSPACE_DIR, "scripts"), exist_ok=True)
    await generate_audio()
    await take_screenshots()
    create_video()

if __name__ == "__main__":
    asyncio.run(main())
