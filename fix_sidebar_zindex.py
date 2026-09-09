import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #mobile-sidebar
content = re.sub(r'(#mobile-sidebar\s*\{[^}]*?)z-index:\s*99999999;', r'\1z-index: 10000015;', content)

# 2. Update #sidebar-overlay
content = re.sub(r'(#sidebar-overlay\s*\{[^}]*?)z-index:\s*99999998;', r'\1z-index: 10000014;', content)

# 3. Update #mobile-menu-pill inline style
content = content.replace('id="mobile-menu-pill" style="display: none; position: fixed; z-index: 10000010;', 'id="mobile-menu-pill" style="display: none; position: fixed; z-index: 10000016;')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
