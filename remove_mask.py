import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove overflow:hidden from the spans
old_html = """  <div id="subheadline">
    <span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="sub-oh-inner" style="display:block; margin:0;">¿Otra cena más con tu</p></span>
    <span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="sub-oh-inner" style="display:block; margin:0;">pareja u otra cita? Nah,</p></span>
    <span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="sub-oh-inner" style="display:block; margin:0;">hagámosla inolvidable</p></span>
  </div>"""

new_html = """  <div id="subheadline">
    <span style="display:block; padding-bottom:4px;"><p class="sub-oh-inner" style="display:block; margin:0;">¿Otra cena más con tu</p></span>
    <span style="display:block; padding-bottom:4px;"><p class="sub-oh-inner" style="display:block; margin:0;">pareja u otra cita? Nah,</p></span>
    <span style="display:block; padding-bottom:4px;"><p class="sub-oh-inner" style="display:block; margin:0;">hagámosla inolvidable</p></span>
  </div>"""

if old_html in content:
    content = content.replace(old_html, new_html)
    print("Replaced HTML")
else:
    print("Failed to find HTML")

# 2. Add autoAlpha: 0 to the GSAP tween
old_js = "scrollTl.to('.sub-oh-inner', { y: '-150%', duration: 0.05, ease: 'power2.in', stagger: { each: 0.005, from: 'start' } }, 0);"
new_js = "scrollTl.to('.sub-oh-inner', { y: '-150%', autoAlpha: 0, duration: 0.05, ease: 'power2.in', stagger: { each: 0.005, from: 'start' } }, 0);"

if old_js in content:
    content = content.replace(old_js, new_js)
    print("Replaced JS")
else:
    print("Failed to find JS")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
