# BringYa app screenshots for social posts

Use inside a phone mockup (rounded frame, slight tilt or shadow). Never stretch or recolour.

| File | Shows | Use for |
|---|---|---|
| customer-home.png | Customer home: Send a Package, Grow your sales online, BringYa shop | One-app, parcels, shops, "sell on BringYa" business posts |
| customer-fare.png | Fare step: route map, upfront estimated fare, coupon field | Upfront pricing / "see your fare" posts. Do not quote this fare as a typical price; prices are "From $9.99*" |
| customer-shops.png | Shops near you: Pharmacy, Grocery, Convenience, a featured partner shop | Shop-local posts. It shows a real partner (Appetizer Hut) — only use it once the owner confirms that partner is OK with being featured; otherwise crop to the top half (search + categories) |

Not included on purpose:
- Rider home screen: shows a real rider's photo, name and earnings (rider pay is not to be advertised).
- Rider active-delivery screen: shows a test route with a wrong distance (10,544 km), which would look like a bug.

## Mockup rule (always)
- The phone frame takes its shape from the screenshot: fixed width, `height:auto`, image `width:100%;height:auto`.
- Never give the frame a fixed height and never use `object-fit:cover` — the full screen must always be visible.
- Mark the frame `data-qa="mock"` and every text block `data-qa="text"`; `render.py` fails the design if a screenshot is cropped or stretched, or if text overlaps the phone, other text or the canvas edge.
