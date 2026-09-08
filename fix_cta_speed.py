# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Replace speed
content = content.replace('p.y -= p.v * 0.02;', 'p.y -= p.v * 0.01;')

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
