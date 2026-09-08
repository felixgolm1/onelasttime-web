import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_divider = "scrollTl.to('.headline-divider', { clipPath: 'inset(0% 100% 0% 0%)', duration: 0.045, ease: 'power3.in' }, 0);"
new_divider = "scrollTl.to('.headline-divider', { clipPath: 'inset(0% 100% 0% 0%)', duration: 0.028, ease: 'power2.inOut' }, 0);"
content = content.replace(old_divider, new_divider)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
