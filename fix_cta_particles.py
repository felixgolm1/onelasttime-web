# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Replace size
content = content.replace('s: Math.random() * 1.5 + 0.5,', 's: Math.random() * 3 + 1,')

# Replace speed
content = content.replace('p.y -= p.v * 0.01;', 'p.y -= p.v * 0.02;')

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
