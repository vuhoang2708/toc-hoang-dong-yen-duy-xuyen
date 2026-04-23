# Implementation Plan - 20260422 - Fix Genealogy Tree Link Naming

## Task Description
Rename the confusing `/map/` directory to `/genealogy-tree/` to accurately reflect its content (Interactive Genealogy Diagram) and update all internal links.

## Technical Solution (Giải pháp kỹ thuật)
1. **Directory Rename**: Rename `C:\Users\vu.hoang\.gemini\antigravity\scratch\gio-to-toc-hoang2026\map` to `C:\Users\vu.hoang\.gemini\antigravity\scratch\gio-to-toc-hoang2026\genealogy-tree`.
2. **Update Links in `index.html`**:
   - Change `https://toc-hoang-dong-yen-duy-xuyen.vercel.app/map/` to `https://toc-hoang-dong-yen-duy-xuyen.vercel.app/genealogy-tree/`.
3. **Audit Other Files**: Check if `scripts/generate_overview_v3.py` or other files use the old `/map/` path and update them.
4. **Verification**: Confirm navigation works as expected.

## Affected Files (Các file bị ảnh hưởng)
- `index.html`
- `genealogy-tree/index.html` (renamed from `map/index.html`)
- `scripts/generate_overview_v3.py`

## Potential Risks (Rủi ro tiềm ẩn)
- Broken links if any file is missed.

## Auditor Review
- Codex to verify that the "Vị Trí Nhà Thờ" (Google Maps) section is NOT accidentally renamed or pointed to the new folder.
