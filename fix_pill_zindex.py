import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('z-index: 1000000000;', 'z-index: 10000010;')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
