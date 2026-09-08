import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_span = '<span style="position:relative; z-index:2; text-align:center; padding-right:20px;">TRANSFORMAR MI CENA</span>'
new_span = '<span style="position:relative; z-index:2; text-align:center; padding-right:20px; transform: translateX(-15px); display: inline-block;">TRANSFORMAR MI CENA</span>'

content = content.replace(old_span, new_span)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
