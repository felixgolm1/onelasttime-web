import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("let _mobR = window.matchMedia('(max-width: 768px)').matches ? -90 : 0; let rz1=-90+(90*rp1)+_mobR", "let rz1=-90+(90*rp1)")
content = content.replace("let rz2=-90+(90*rp2)+_mobR", "let rz2=-90+(90*rp2)")
content = content.replace("let rz3=-90+(90*rp3)+_mobR", "let rz3=-90+(90*rp3)")
content = content.replace("let rz4=-90+(90*rp4)+_mobR", "let rz4=-90+(90*rp4)")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted HTML scattered cards rotation")
