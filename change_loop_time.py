import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('4000); // 4s loop', '3500); // 3.5s loop')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
