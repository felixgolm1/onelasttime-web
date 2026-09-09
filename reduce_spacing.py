import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Desktop
content = content.replace('margin: 0.5rem 0 0.5rem;', 'margin: 0.4rem 0 0.4rem;')
# Mobile
content = content.replace('margin: 0.8rem 0 !important;', 'margin: 0.65rem 0 !important;')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
