# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

content = content.replace("duration: 0.015, stagger: 0.004", "duration: 0.01, stagger: 0.005")

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
