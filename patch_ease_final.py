import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("rotationZ: 0, duration: 0.35, ease: 'power2.out' },", "rotationZ: 0, duration: 0.35, ease: 'none' },")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replace OK")
