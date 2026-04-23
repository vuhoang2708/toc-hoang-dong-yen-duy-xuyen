# ============================================================
#  LAUNCHER - Video Overview V3 (Tộc Hoàng Portal)
#  Sử dụng Python Portable để đảm bảo đủ thư viện
# ============================================================

$PYTHON  = "C:\Users\vu.hoang\.gemini\antigravity\scratch\tools\python\python.exe"
$SCRIPT  = "$PSScriptRoot\generate_overview_v3.py"

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  VIDEO OVERVIEW V3 - TOC HOANG DONG YEN  " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[STEP 1] Kiem tra thu vien Python Portable..." -ForegroundColor Yellow

# Cài playwright nếu chưa có
& $PYTHON -m playwright install chromium 2>&1 | Out-Null

Write-Host "[STEP 2] Bat dau tao video..." -ForegroundColor Yellow
Write-Host ""

# Chạy script với unbuffered output để thấy tiến trình thực tế
& $PYTHON -u $SCRIPT

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  HOAN TAT! Kiem tra thu muc: assets/videos/" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
