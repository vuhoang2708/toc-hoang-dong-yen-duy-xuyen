# Implementation Plan - Spacing & Typography Optimization (2026-04-21)

**Task**: Improve vertical rhythm and refine the "Thư Ngỏ" (Letter) layout.

## 1. Technical Solution
- **Global Spacing**: Increase `.section-padding` in `style-v2.css` to provide more breathing room between sections.
- **Letter Header**: Reduce margins on the top text blocks in `#genealogy` (Thư Ngỏ header).
- **Letter Footer**: Reduce the padding/margin after the final paragraph and before the signature.
- **Signature Alignment**: Use a flex column with `align-items: center` for the signature block to center the name under the title.

## 2. Affected Files
- `index.html`
- `assets/css/style-v2.css`

## 3. Potential Risks
- **Mobile View**: Extreme padding might push content too far on small screens. I will use responsive units if needed.
- **Line Height**: Over-compacting the letter header might make it look crowded. I will balance it.

## 4. Execution Steps
1. **CSS Update**: 
   - Add `.section-padding { padding: 6rem 0; }` (currently might be less).
   - Ensure sections have a clear separator look.
2. **HTML Letter Refinement**:
   - Locate the header of the letter and remove extra `<p>` or `margin` in inline styles.
   - Adjust the signature block: wrap "TM. HOÀNG TỘC" and the name in a div and center them.
3. **Verification**: 
   - Check the visually restored blocks.

## 5. Auditor Review
- Plan created by Antigravity.
- Awaiting User approval to execute.
