import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("var validCodes = ['PASS007'];", "var validCodes = ['PASS007', 'ESENCIAL'];")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
