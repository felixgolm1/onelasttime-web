import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update #sidebar-overlay
content = re.sub(r'(#sidebar-overlay\s*\{[^}]*z-index:\s*)10000014', r'\g<1>10000090', content)

# Update #mobile-sidebar
content = re.sub(r'(#mobile-sidebar\s*\{[^}]*z-index:\s*)10000015', r'\g<1>10000091', content)

# Update #mobile-menu-pill inline style
content = re.sub(r'(id="mobile-menu-pill"[^>]*z-index:\s*)10000016', r'\g<1>10000092', content)

# Update nav-menu
content = re.sub(r'(#nav-menu\s*\{[^}]*z-index:\s*)10000010', r'\g<1>10000095', content)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
