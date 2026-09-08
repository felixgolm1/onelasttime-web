# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

target = "const rightChars = splitFltChars('.flt-in-up'); // texto derecho:   slide desde abajo"
replacement = "const rightChars = splitFltChars('.flt-in-up'); // texto derecho:   slide desde abajo\n      const glassWhoTitle = splitFltChars('#glass-who h3');\n      const glassObjTitle = splitFltChars('#glass-objectives h3');"

content = content.replace(target, replacement)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
