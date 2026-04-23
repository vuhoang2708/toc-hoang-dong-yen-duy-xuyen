# Implementation Plan - 20260423 - Update Documentation with Restored Links

## Task Description
Update `TOC_HOANG_HANDOVER.md` and `TOC_HOANG_TECHNICAL.md` to include information and links about the restored Editorial Dashboard (Content Editor).

## Technical Solution (Giải pháp kỹ thuật)
1. **Editorial Guide (`TOC_HOANG_HANDOVER.md`)**:
   - Add "Trung tâm Biên tập Nội dung" link: `https://toc-hoang-dong-yen-duy-xuyen.vercel.app/editor/`.
   - Update instructions for content review using the 3-column dashboard.
2. **Technical Guide (`TOC_HOANG_TECHNICAL.md`)**:
   - Add `editor/` directory to the structure map.
   - Mention the persistence logic in the editor (LogToSheet via GAS).
3. **Admin Portal (`admin.html`)**:
   - Ensure the link is absolute in documentation but relative in the UI.

## Affected Files (Các file bị ảnh hưởng)
- `TOC_HOANG_HANDOVER.md`
- `TOC_HOANG_TECHNICAL.md`

## Potential Risks (Rủi ro tiềm ẩn)
- None.

## Auditor Review
- Codex to verify all links match the restored structure.
