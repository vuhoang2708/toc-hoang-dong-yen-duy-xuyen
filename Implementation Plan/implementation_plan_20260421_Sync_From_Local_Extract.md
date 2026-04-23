# Implementation Plan - Sync from Local Browser Extraction (2026-04-21)

**Task**: Synchronize the project code with the version saved by the user from an unrefreshed browser tab.
**Source Path**: `G:\My Drive\download\restore page toc hoang`

## 1. Technical Solution
The user has saved the "perfect" version of the site locally before refreshing. We will read this content and update the workspace. We need to handle the path differences introduced by the "Save Page, Complete" mechanism (which creates a `_files` folder).

## 2. Affected Files
- `index.html`: Will be updated with the content from the saved HTML file.
- `assets/css/style-v2.css`: Will be updated with the content from the saved CSS file.

## 3. Potential Risks
- **Path Mismatch**: The saved HTML might have paths like `Tộc Hoàng..._files/style-v2.css`. These must be changed back to `assets/css/style-v2.css`.
- **Duplicate Metadata**: Browser-saved HTML sometimes adds metadata at the top (like `<meta charset="utf-8">` duplicates or saved-from comments).

## 4. Execution Steps
1. **Read HTML**: Get full content of the saved HTML file.
2. **Read CSS**: Get full content of `style-v2.css` from the `_files` folder.
3. **Clean HTML**: Use string replacement to fix paths:
   - Change `*_files/style-v2.css` -> `assets/css/style-v2.css`
   - Ensure all assets (images/scripts) point to the project's internal `assets/` folder.
4. **Write Files**: Overwrite local workspace files.
5. **Verification**: 
   - `git diff` to see exactly what changed.
   - User verification of the live site after deployment.

## 5. Auditor Review
- Plan created by Antigravity.
- Awaiting User approval to execute.
