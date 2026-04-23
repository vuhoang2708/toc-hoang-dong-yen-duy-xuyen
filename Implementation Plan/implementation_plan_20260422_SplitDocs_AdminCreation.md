# Implementation Plan - 20260422 - Documentation Splitting & Admin Creation

## Task Description
1. Create a dedicated Admin page for the Clan Portal.
2. Split documentation into Editorial (Ban Biên Tập) and Technical (Kỹ Thuật) versions.
3. Update all official links in the documentation.

## Technical Solution (Giải pháp kỹ thuật)
1. **Admin Portal**:
   - Create `admin.html` (renamed and themed from `lms_dashboard.html`).
   - Clean up DH contents, focus on:
     - Overview of registrations.
     - Genealogy update queue.
     - Quick links to Google Sheets.
     - Video generation summary.
   - Update `login.html` to redirect to `admin.html`.
2. **Editorial Documentation (`TOC_HOANG_HANDOVER.md`)**:
   - Focus on Content Management.
   - Add "Bổ sung gia phả" link: `https://toc-hoang-dong-yen-duy-xuyen.vercel.app/genealogy/`.
   - Add "Admin Center" link: `https://toc-hoang-dong-yen-duy-xuyen.vercel.app/login.html` (with credentials doc).
   - Social links: Facebook/Zalo.
3. **Technical Documentation (`TOC_HOANG_TECHNICAL.md`)**:
   - GitHub Repository & Workflow.
   - Vercel Configuration.
   - Local Workspace setup.
   - Python Video Scripts usage.
   - Automation logic (Post-event switch).
4. **Cleanup**:
   - Consolidate `technical_specification.md` and `github_structure_guide.md` into `TOC_HOANG_TECHNICAL.md`.
   - Delete the old/redundant guide files.

## Affected Files (Các file bị ảnh hưởng)
- `admin.html` (NEW)
- `login.html` (Updated redirect)
- `TOC_HOANG_HANDOVER.md` (Split/Updated)
- `TOC_HOANG_TECHNICAL.md` (NEW/Consolidated)

## Potential Risks (Rủi ro tiềm ẩn)
- None. Enhancing documentation clarity.

## Auditor Review
- Codex to verify the new naming convention and link correctness.
