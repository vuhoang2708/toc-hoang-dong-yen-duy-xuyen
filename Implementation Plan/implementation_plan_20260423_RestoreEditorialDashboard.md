# Implementation Plan - 20260423 - Restore Editorial Internal Dashboard

## Task Description
Restore the 3-column Editorial Dashboard (found in commit `5641af9a`) that allows the Clan's Editorial Board to review existing content and submit changes to Google Sheets.

## Technical Solution (Giải pháp kỹ thuật)
1. **Restore Folder**: Recreate the `editor/` directory.
2. **Recover File**: Extract `editor/index.html` from commit `5641af9a`.
3. **Integration**: 
   - Add a direct link from the new `admin.html` to `editor/index.html` (labelled as "Trung tâm Biên tập Nội dung").
   - Ensure `tracking.js` is updated if needed to support the `logToSheet` call for editorial submission.
4. **Validation**: Check that the 3-column layout correctly displays the reference sections (Hero, History, Values) and the "Save" button is functional.

## Affected Files (Các file bị ảnh hưởng)
- `editor/index.html` (RESTORED)
- `admin.html` (Link added)

## Potential Risks (Rủi ro tiềm ẩn)
- The Google Sheets ID might have changed if the user created a new sheet. I will check `google_apps_script.js` to ensure consistency.

## Auditor Review
- Codex to verify the restored file contains the exact same logic for verbatim content review.
