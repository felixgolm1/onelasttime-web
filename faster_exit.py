import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make bottom copy exit 30% faster
old_blur = "scrollTl.to('#blur-bg-sub', { opacity: 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
new_blur = "scrollTl.to('#blur-bg-sub', { opacity: 0, duration: 0.045, ease: 'power2.inOut' }, 0);"
content = content.replace(old_blur, new_blur)

old_text = "scrollTl.to('.sub-oh-inner', { y: '-150%', autoAlpha: 0, duration: 0.05, ease: 'power2.in', stagger: { each: 0.005, from: 'start' } }, 0);"
new_text = "scrollTl.to('.sub-oh-inner', { y: '-150%', autoAlpha: 0, duration: 0.035, ease: 'power2.in', stagger: { each: 0.003, from: 'start' } }, 0);"
content = content.replace(old_text, new_text)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
