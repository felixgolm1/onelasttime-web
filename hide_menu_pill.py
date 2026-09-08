import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add opacity: 0 to mobile-menu-pill CSS
old_css = """  #mobile-menu-pill {
    -webkit-tap-highlight-color: transparent;
    display: flex !important;
    align-items: center;
    justify-content: center;"""

new_css = """  #mobile-menu-pill {
    -webkit-tap-highlight-color: transparent;
    display: flex !important;
    align-items: center;
    justify-content: center;
    opacity: 0;"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Could not find CSS to replace")

# Add to GSAP array
old_gsap = "gsap.to(['#nav-logo', '#nav-menu', '#cta-top-container', '#cta-bottom-container', '.scroll-indicator', '#headline', '#subheadline']"
new_gsap = "gsap.to(['#nav-logo', '#nav-menu', '#mobile-menu-pill', '#cta-top-container', '#cta-bottom-container', '.scroll-indicator', '#headline', '#subheadline']"

if old_gsap in content:
    content = content.replace(old_gsap, new_gsap)
else:
    print("Could not find GSAP array to replace")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
