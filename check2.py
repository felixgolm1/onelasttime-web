# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()
idx = html.find('Preparado en tu mesa')
if idx != -1:
    print(html[idx-3000:idx-1000])
