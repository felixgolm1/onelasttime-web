import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('bottom: calc(3% + 3.3rem) !important;', 'bottom: calc(3% + 2.2rem) !important;')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
