# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()
idx = html.find('una y otra vez')
if idx != -1:
    print(html[idx-1500:idx])
