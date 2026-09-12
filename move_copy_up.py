# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'(<h2 id="oxitocina-title" style="[^>]*?top:)\s*67%;')
replacement = r'\163%;'

html = pattern.sub(replacement, html)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)
