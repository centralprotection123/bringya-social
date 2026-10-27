# BringYa daily post design rules

Every post is designed from scratch at run time: HTML/CSS → `render.py` → 1080×1350 JPEG.
The owner's bar: **unique, creative, professional, audience-gaining.** Posts built as "headline + checklist + button" were rejected as not creative enough. The four files in `examples/` are the approved level; beat them, don't copy them.

## 1. Start from an idea, not a layout
Build each post around **one real-life moment or object** the audience recognises in a second. The joke, story or object is the hero; the brand supports it.

Formats to rotate (pick one not used in the last 14 posts; see `posts/log.json`):
- Group chat / text thread (family, roommates, coworkers, shop owner and customer)
- Parcel label, receipt, sticky note, to-do list, delivery slip, ticket
- Shop door sign, chalkboard menu, storefront window, price tag
- Phone notification stack or lock screen
- "POV:" scene, mini comic (3–4 panels), before/after split
- Myth vs fact, this-or-that poll, quiz card, "rate this excuse"
- Map/route art (the route drawing a shape or a word)
- Annotated real app screen with sticky-note callouts
- Calendar / clock moment (Friday-evening errands, Monday office runs)
- Big-type poster with one bold claim and generous space
- Seasonal or local moment (snowy day, long weekend, back to school, gift seasons), using no unverified claims

Customer ideas: forgotten items, gifts and surprises, groceries and essentials, dinner from a local spot, sending to family, students, weekend errands, tracking and PIN peace of mind, upfront fare, referral $5/$5, "one app".
Business ideas: flip from pickup-only to delivery, no van or drivers needed, pack → tap Ready → rider, card checkout and bank payouts, pause your shop, spreadsheet import, office documents same day, client tracking link, photo proof + PIN, restaurants, cafés, boutiques, florists, convenience stores.

## 2. Visual craft
- Brand colours only: blue #154CFE, lime #DDFB33, navy #0B1B4D, light #F4F7FF, white. Rotate which one leads; never the same lead colour two posts in a row.
- Brand font Inter (and Inter Display) for headings and body. Courier 10 Pitch / DejaVu Sans Mono only for "object" text (labels, receipts). Fonts must be installed locally; no web fonts.
- Spend boldness in one place. Generous space; no clutter. Readable on a phone: body text ≥ 28px, headline 56–120px.
- Avoid template tells: no ALL-CAPS eyebrow label above every headline, no "→" glued to every CTA, no headline with one word recoloured, no stack of identical rounded cards, no 01/02/03 unless it really is a sequence.
- Logo: always the real file `brand/bringya-logo.png` (icon only: `brand/bringya-icon.png`, e.g. for app icons in notifications), never redrawn, recoloured or stretched. On blue or navy backgrounds put it on a white rounded badge.
- Include `bringya.ca` (customers) or `bringya.ca/business` (business) somewhere small.
- Make it feel human and specific: names, times, everyday details ("12 minutes later", "the lunch on the counter").

## 3. Real app screens (`brand/screens/`)
Use them often, always inside a phone mockup. See `brand/screens/README.md`.
- Frame shape follows the screenshot: `.phone{width:Wpx;height:auto}` and `.phone img{width:100%;height:auto}`.
- Never a fixed frame height, never `object-fit:cover`. The whole screen must show.
- `customer-shops.png` shows a real partner (Appetizer Hut): only show its top half (search + categories) until the owner confirms the partner agreed.

## 4. QA before posting (mandatory)
- Mark mockups/objects `data-qa="mock"` and every text block `data-qa="text"`.
- `python3 render.py post.html post.jpg` must print `QA passed`. If it fails, fix the HTML and re-render.
- Then look at the JPEG yourself. Fix anything awkward: empty dead zones, cramped text, arrows pointing at the wrong thing, low contrast, text near the edge (keep ≥ 56px margins).

## 5. Facts (never break)
- Only state facts from the playbook's BUSINESS NOTES. No invented prices, discounts, delivery times, hours, stats, rider pay, commission, fees or offers.
- "$9.99" only as "From $9.99*" with "*Extra distance and service charges may apply." in the image or caption.
- No late-night/midnight claims until the playbook says hours are confirmed. No "free delivery" claims. No coupon codes.
- No competitor names. No prescriptions. BringYa doesn't carry passengers.
- Any people in chats/scenes are fictional first names; never show real customer data.
