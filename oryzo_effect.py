import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"// 5\. Texto derecha:.*?\n\s*scrollTl\.to\('#subheadline', \{ x: 50, '--sub-blur': '0px', '--sub-alpha': 0, duration: 0\.08, ease: 'power2\.inOut' \}, 0\);\n\s*scrollTl\.to\('#subheadline p', \{ autoAlpha: 0, duration: 0\.08, ease: 'power2\.inOut' \}, 0\);"

new_js = """// 5. Texto derecha: se recorta hacia arriba (Oryzo effect)
      scrollTl.to('#subheadline', { '--sub-blur': '0px', '--sub-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);
      scrollTl.to('.sub-oh-inner', { y: '-150%', duration: 0.05, ease: 'power2.in', stagger: { each: 0.005, from: 'start' } }, 0);"""

content = re.sub(pattern, new_js, content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
