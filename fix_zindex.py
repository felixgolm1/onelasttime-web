# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'(#cta-bottom-container\s*\{\s*position:\s*fixed;\s*bottom:\s*3\.7rem;)')
replacement = r'\1 z-index: 10000020 !important;'

html = pattern.sub(replacement, html)

pattern2 = re.compile(r'(#cta-bottom-container\s*\{\s*bottom:\s*3%\s*!important;\s*padding:\s*0\s*0\.4rem\s*!important;)')
replacement2 = r'\1 z-index: 10000020 !important;'
html = pattern2.sub(replacement2, html)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)
