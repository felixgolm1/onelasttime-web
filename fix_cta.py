import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

bad_js1 = "scrollTl.to('#heroCta', { autoAlpha: 0, scale: 0.95, transformOrigin: '50% 50%', duration: 0.06, ease: 'power2.inOut' }, 0.84);"
good_js1 = "if (!window._cIsMobile) scrollTl.to('#heroCta', { autoAlpha: 0, scale: 0.95, transformOrigin: '50% 50%', duration: 0.06, ease: 'power2.inOut' }, 0.84);"

bad_js2 = "scrollTl.to('#heroCta', { autoAlpha: 1, scale: 1, transformOrigin: '50% 50%', duration: 0.20, ease: 'power2.out' }, t2 + 0.075);"
good_js2 = "if (!window._cIsMobile) scrollTl.to('#heroCta', { autoAlpha: 1, scale: 1, transformOrigin: '50% 50%', duration: 0.20, ease: 'power2.out' }, t2 + 0.075);"

content = content.replace(bad_js1, good_js1)
content = content.replace(bad_js2, good_js2)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
