# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

banner = '''<body>
<div style="position: fixed; top: 0; left: 0; width: 100vw; background: red; color: white; display: flex; justify-content: center; align-items: center; padding: 20px; z-index: 999999; font-size: 30px; font-weight: bold; pointer-events: none;">
  VERSION ACTUALIZADA - RECARGA FUNCIONO OK
</div>'''

if 'VERSION ACTUALIZADA' not in text:
    text = text.replace('<body>', banner)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Banner added!')
else:
    print('Banner already exists')
