# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

banner = '''<body>
<div style="position: fixed; top: 0; left: 0; width: 100vw; background: red; color: white; display: flex; justify-content: center; align-items: center; padding: 20px; z-index: 999999; font-size: 30px; font-weight: bold; pointer-events: none;">
  VERSION ACTUALIZADA - RECARGA FUNCIONO OK
</div>'''

# 1. Remove banner
text = text.replace(banner, '<body>')

# 2. Fix the GSAP null error: replace 'sc-title' target with 'sc-title-wrap'
# We have a line: const scTitle   = document.getElementById('sc-title');
text = text.replace("document.getElementById('sc-title')", "document.getElementById('sc-title-wrap')")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed script target and removed banner!')
