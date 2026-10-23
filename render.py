#!/usr/bin/env python3
"""Render an HTML design to a 1080x1350 JPEG and run layout QA.

Usage: python3 render.py design.html out.jpg

QA (exit code 1 if anything fails, so the design must be fixed before posting):
- Every <img> inside a phone mockup is shown whole: its displayed aspect ratio
  matches the screenshot's real aspect ratio (no cropping or stretching).
- Nothing marked data-qa="text" overlaps anything marked data-qa="mock".
- Nothing marked data-qa="text" or data-qa="mock" runs off the 1080x1350 canvas.
- No text element overflows its own box (text cut off).

Phone mockup rule (use always):
  <div class="phone" data-qa="mock"><img src="brand/screens/NAME.png"></div>
  .phone{width:<W>px;height:auto;padding:16px;border-radius:64px;background:#0B1B4D}
  .phone img{width:100%;height:auto;border-radius:48px;display:block}
  Never set a fixed height on .phone and never use object-fit:cover on the screenshot.
"""
import sys, pathlib, json
from playwright.sync_api import sync_playwright

QA_JS = r"""
() => {
  const W = 1080, H = 1350, out = [];
  const box = el => el.getBoundingClientRect();
  const texts = [...document.querySelectorAll('[data-qa="text"]')];
  const mocks = [...document.querySelectorAll('[data-qa="mock"]')];
  const hit = (a, b) => a.left < b.right - 2 && a.right > b.left + 2 && a.top < b.bottom - 2 && a.bottom > b.top + 2;
  for (const m of mocks) {
    for (const img of m.querySelectorAll('img')) {
      const real = img.naturalWidth / img.naturalHeight, shown = img.offsetWidth / img.offsetHeight;
      if (!img.naturalWidth) out.push(`screenshot not loaded: ${img.getAttribute('src')}`);
      else if (Math.abs(real - shown) / real > 0.01) out.push(`screenshot cropped/stretched: ${img.getAttribute('src')} (real ${real.toFixed(3)} vs shown ${shown.toFixed(3)})`);
      const fit = getComputedStyle(img).objectFit;
      if (fit === 'cover') out.push(`object-fit:cover on screenshot ${img.getAttribute('src')}`);
    }
  }
  for (const el of [...texts, ...mocks]) {
    const r = box(el);
    if (r.left < -1 || r.top < -1 || r.right > W + 1 || r.bottom > H + 1)
      out.push(`off canvas: <${el.tagName.toLowerCase()} class="${el.className}"> "${el.textContent.trim().slice(0,40)}"`);
  }
  for (const t of texts) {
    if (t.scrollWidth > t.clientWidth + 2 || t.scrollHeight > t.clientHeight + 2)
      if (getComputedStyle(t).overflow !== 'visible') out.push(`text cut off: "${t.textContent.trim().slice(0,40)}"`);
    for (const m of mocks) if (hit(box(t), box(m)))
      out.push(`text overlaps mockup: "${t.textContent.trim().slice(0,40)}"`);
  }
  for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++)
    if (!texts[i].contains(texts[j]) && !texts[j].contains(texts[i]) && hit(box(texts[i]), box(texts[j])))
      out.push(`text overlaps text: "${texts[i].textContent.trim().slice(0,25)}" / "${texts[j].textContent.trim().slice(0,25)}"`);
  return out;
}
"""

src = pathlib.Path(sys.argv[1]).resolve()
out = sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.goto(src.as_uri())
    pg.wait_for_load_state("networkidle")
    pg.wait_for_timeout(300)
    problems = pg.evaluate(QA_JS)
    pg.screenshot(path=out, type="jpeg", quality=92, clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
    b.close()
print("wrote", out)
if problems:
    print("QA FAILED:"); [print(" -", x) for x in problems]; sys.exit(1)
print("QA passed")
