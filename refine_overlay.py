import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("transition: opacity 0.4s ease;", "transition: opacity 0.5s ease;")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
