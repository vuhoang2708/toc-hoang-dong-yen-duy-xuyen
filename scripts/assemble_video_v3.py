import os
import sys
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image
import numpy as np

WORKSPACE_DIR = r'C:\Users\vu.hoang\.gemini\antigravity\scratch\gio-to-toc-hoang2026'
ASSETS_DIR = os.path.join(WORKSPACE_DIR, 'assets', 'videos')
TEMP_DIR = os.path.join(WORKSPACE_DIR, 'temp_video')
os.makedirs(ASSETS_DIR, exist_ok=True)

SEGMENTS = ['01_hero', '02_genealogy', '03_contribution', '04_map', '05_admin', '06_conclusion']

def zoom_out_effect(clip, zoom_start=1.15, zoom_end=1.0):
    def get_frame(gf, t):
        frame = gf(t)
        im = Image.fromarray(frame)
        w, h = im.size
        dur = max(clip.duration, 0.1)
        scale = zoom_start - (zoom_start - zoom_end) * (t / dur)
        new_w, new_h = int(w * scale), int(h * scale)
        resample = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS
        resized = im.resize((new_w, new_h), resample)
        left = (new_w - w) / 2
        top = (new_h - h) / 2
        cropped = resized.crop((left, top, left + w, top + h))
        return np.array(cropped)
    return clip.transform(get_frame)

def main():
    print("--- VIDEO ASSEMBLY STAGE ---")
    clips = []
    
    for seg_id in SEGMENTS:
        img_path = os.path.join(TEMP_DIR, f"{seg_id}.png")
        audio_path = os.path.join(TEMP_DIR, f"{seg_id}.mp3")
        
        if not os.path.exists(img_path) or not os.path.exists(audio_path):
            print(f"SKIP {seg_id}: missing file")
            continue
        
        if os.path.getsize(audio_path) < 5000:
            print(f"SKIP {seg_id}: audio empty/corrupted ({os.path.getsize(audio_path)} bytes)")
            continue
        
        print(f"Processing [{seg_id}]...")
        audioclip = AudioFileClip(audio_path)
        imgclip = ImageClip(img_path).with_duration(audioclip.duration)
        imgclip = zoom_out_effect(imgclip)
        imgclip = imgclip.with_audio(audioclip)
        clips.append(imgclip)
    
    print(f"\nTotal valid clips: {len(clips)}")
    
    if not clips:
        print("ERROR: Khong co clip nao hop le!")
        sys.exit(1)
    
    final = concatenate_videoclips(clips, padding=-0.5, method='compose')
    out_path = os.path.join(ASSETS_DIR, 'overview_v3.mp4')
    
    print(f"Rendering to: {out_path}")
    final.write_videofile(
        out_path,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        threads=4,
        preset='ultrafast'
    )
    print(f"\n==> HOAN THANH! Video da xuat tai: {out_path}")

if __name__ == '__main__':
    main()
