CETL – San Germán Campus Website (English)

Name:
- Center for Excellence in Teaching and Learning (CETL)

Contents:
- index.html  (main page)
- img/ucan-logo.png  (header logo)
- img/eduardo.jpg    (team photo placeholder)
- img/tarjeta.jpg    (original uploaded image)

How to open:
1) Extract the ZIP.
2) Open index.html in your browser.

How to update the team:
- In index.html, locate the TEAM constant inside <script>.
- Replace the 5 placeholders with real staff data.
- Add photos to /img and update the "photo" field.

Notes:
- The form is a demo (client-side validation only). Connect it to your backend/ticketing system to submit requests.
- Resource links are samples (#). Replace them with real URLs.


Update:
- Added CETL logo to img/cetl-logo.png and applied it to the header and hero.
- Added favicon using the same logo.


Update:
- Added rotating banners below the main menu (auto-rotate every 10 seconds) with Pause/Prev/Next controls.
- Service Request submissions open the user's email client and send to: ucan_ppoha@intersg.edu
- Primary theme colors updated to the institutional palette (Inter green/yellow/gold).


Fix:
- Service Request now generates a ready-to-send email and provides 3 delivery options:
  Outlook Web (recommended), Gmail, or Mail app (mailto), plus a Copy button.
- Target recipient: ucan_ppoha@intersg.edu


Fix:
- Banner controls now overlay on top of the banners (z-index) and are clickable.
- Banner overlay no longer blocks clicks on controls (pointer-events fix) while keeping CTA clickable.
