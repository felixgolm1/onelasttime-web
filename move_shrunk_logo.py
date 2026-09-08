import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_js = "scrollTl.to('#nav-logo', { scale: window.matchMedia('(max-width: 768px)').matches ? 0.6 : 0.5, top: window.matchMedia('(max-width: 768px)').matches ? '1%' : '1.5rem', transformOrigin: 'top left', ease: 'power1.inOut', duration: 0.08 }, 0);"

new_js = "scrollTl.to('#nav-logo', { scale: window.matchMedia('(max-width: 768px)').matches ? 0.6 : 0.5, top: window.matchMedia('(max-width: 768px)').matches ? '2.5%' : '1.5rem', left: window.matchMedia('(max-width: 768px)').matches ? '5%' : '2rem', transformOrigin: 'top left', ease: 'power1.inOut', duration: 0.08 }, 0);"

if old_js in content:
    content = content.replace(old_js, new_js)
    print("Replaced successfully.")
else:
    print("Could not find the exact string.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
