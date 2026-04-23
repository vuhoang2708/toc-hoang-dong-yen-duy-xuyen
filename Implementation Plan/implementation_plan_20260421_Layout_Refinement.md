# Implementation Plan - Layout Refinement (2026-04-21)

**Task**: Remove duplicate content and reorder sections in `index.html`.

## 1. Technical Solution
We will reorder the DOM elements in `index.html`. 
- The `#location` section (currently near the bottom) will be moved above the `#community` section.
- The orphan duplicate Facebook info block (lines 241-257) will be deleted.

## 2. Affected Files
- `index.html`

## 3. Potential Risks
- **HTML Syntax Errors**: Improperly closing or nesting tags during cut/paste. I will carefully identify section boundaries.
- **Visual Gaps**: Moving sections might affect the alternating background patterns. I will check the `style` attributes.

## 4. Execution Steps
1. **Read**: Load `index.html` content.
2. **Move Section**: 
   - Locate `<!-- CLAN COMMUNITY -->` to `</section>` (Lines 179-215).
   - Locate `<!-- CLAN LOCATION (GOOGLE MAPS) -->` to `</section>` (Lines 259-278).
   - Move the Location section before the Community section.
3. **Clean Duplicates**: 
   - Locate and delete the orphan block (Lines 241-257).
4. **Consistency Check**: 
   - Ensure `id="event"` (Lines 218-240) is not affected.
5. **Update**: Save `index.html`.
6. **Audit**: Run `grep` search for `_files` or duplicate text.

## 5. Auditor Review
- Plan created by Antigravity.
- Awaiting User approval to execute.
