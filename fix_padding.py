import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'padding:\s*24px\s*20px\s*!important;',
    'padding: 24px 20px 12px 20px !important;',
    content
)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
