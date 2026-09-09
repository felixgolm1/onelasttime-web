import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('translateX(-15px)', 'translateX(-22px)')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
