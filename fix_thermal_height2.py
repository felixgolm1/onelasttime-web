import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'#thermal-overlay\s*\{\s*height:\s*95vh\s*!important;\s*\}', '', content)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
