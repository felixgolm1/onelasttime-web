import re
with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace maxProg
content = content.replace('const maxProg = 62.55;', 'const maxProg = 63.05;')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
