import os
import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to add #vip-overlay { height: 100dvh !important; } inside our media query
    if '#vip-overlay { height: 100dvh !important; }' not in content:
        content = content.replace(
            '@media screen and (max-width: 768px) {',
            '@media screen and (max-width: 768px) {\n  /* Modern mobile viewport fix */\n  #vip-overlay { height: 100dvh !important; }\n'
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file}")
    else:
        print(f"Already patched {file}")
