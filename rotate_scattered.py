import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add _mobR definition right before the scattered cards loop logic starts.
# We can find `let localP = mapRange(pProg, 0, 1, 0, 10);` and inject there, or just directly in the rz1 lines.

content = content.replace(
    "let rz1=-90+(90*rp1)",
    "let _mobR = window.matchMedia('(max-width: 768px)').matches ? -90 : 0; let rz1=-90+(90*rp1)+_mobR"
)

content = content.replace("let rz2=-90+(90*rp2)", "let rz2=-90+(90*rp2)+_mobR")
content = content.replace("let rz3=-90+(90*rp3)", "let rz3=-90+(90*rp3)+_mobR")
content = content.replace("let rz4=-90+(90*rp4)", "let rz4=-90+(90*rp4)+_mobR")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done rotating scattered cards on mobile.")
