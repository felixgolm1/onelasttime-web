import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .oh-inner:not(.headline-sub)
old_oh_inner = "scrollTl.to('.oh-inner:not(.headline-sub)', { y: '150%', duration: 0.04, ease: 'power2.in', stagger: { each: 0.005, from: 'end' } }, 0);"
new_oh_inner = "scrollTl.to('.oh-inner:not(.headline-sub)', { y: '150%', duration: 0.039, ease: 'power2.in', stagger: { each: 0.003, from: 'end' } }, 0);"
content = content.replace(old_oh_inner, new_oh_inner)

# 2. Update .headline-sub
old_headline_sub = "scrollTl.to('.headline-sub', { y: '150%', duration: 0.08, ease: 'power2.inOut' }, 0);"
new_headline_sub = "scrollTl.to('.headline-sub', { y: '150%', duration: 0.045, ease: 'power2.inOut' }, 0);"
content = content.replace(old_headline_sub, new_headline_sub)

# 3. Update .headline-divider
old_headline_divider = "scrollTl.to('.headline-divider', { clipPath: 'inset(0% 100% 0% 0%)', duration: 0.06, ease: 'power3.in' }, 0);"
new_headline_divider = "scrollTl.to('.headline-divider', { clipPath: 'inset(0% 100% 0% 0%)', duration: 0.045, ease: 'power3.in' }, 0);"
content = content.replace(old_headline_divider, new_headline_divider)

# 4. Update #blur-bg-head
old_blur_bg_head = "scrollTl.to('#blur-bg-head', { opacity: 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
new_blur_bg_head = "scrollTl.to('#blur-bg-head', { opacity: 0, duration: 0.045, ease: 'power2.inOut' }, 0);"
content = content.replace(old_blur_bg_head, new_blur_bg_head)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
