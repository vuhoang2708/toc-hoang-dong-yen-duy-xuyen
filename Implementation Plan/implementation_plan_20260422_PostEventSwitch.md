# Implementation Plan - 20260422 - Post-Event Auto-Switch for Registration Page

## Task Description
Implement a logic in `register/index.html` that automatically hides the registration form and displays an "Event Recap & Gallery" section after the event date (April 26, 2026).

## Technical Solution (Giải pháp kỹ thuật)
1. **HTML Structure (index.html & register/index.html)**:
   - Wrap registration-specific sections/buttons in `<div class="pre-event-only">`.
   - Add `<div class="post-event-only" style="display: none;">` for the Event Recap content.
2. **Javascript Logic**:
   - Add a shared script (or common function) that compares `new Date()` with `2026-04-26T12:00:00`.
   - Toggle visibility of `.pre-event-only` and `.post-event-only` elements.
3. **Design**:
   - Home Page: Change "Đăng ký dự lễ" section to a featured "Hành trình Lễ Tế Xuân 2026" with photos.
   - Register Page: Full transformation to an Event Gallery.

## Affected Files (Các file bị ảnh hưởng)
- `index.html`
- `register/index.html`
- `assets/js/tracking.js` (Optional: to handle logic globally)

## Potential Risks (Rủi ro tiềm ẩn)
- Client-side date can be manipulated by user system clock, but for a clan website, this is acceptable.

## Auditor Review
- Codex to verify the event date constant matches the UI text (26/04/2026).
