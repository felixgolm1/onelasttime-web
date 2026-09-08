import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "transform: translateZ(0);",
    "transform: translate3d(0,0,0) rotate(0.001deg);"
)
content = content.replace(
    "-webkit-transform: translateZ(0);",
    "-webkit-transform: translate3d(0,0,0) rotate(0.001deg);"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
