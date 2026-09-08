# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

target = '<li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con tu pareja de hace 10 a&ntilde;os?</li>'
new_bullet = '<li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con tu marido/mujer con quien ya has compartido 40 a&ntilde;os y 2 hijos?</li>\n        ' + target

content = content.replace(target, new_bullet)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
