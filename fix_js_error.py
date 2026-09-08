# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Remove the gsap.set calls from the wrong place
wrong_set_calls = '''      gsap.set(glassWhoTitle, { opacity: 0 });
      gsap.set(glassObjTitle, { opacity: 0 });
      gsap.set('#glass-who li', { opacity: 0, y: 30 });
      gsap.set('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { opacity: 0, y: 30 });'''

content = content.replace(wrong_set_calls + '\n', '')
content = content.replace(wrong_set_calls, '')

# 2. Add them after the variable definitions
target = "const glassObjTitle = splitFltChars('#glass-objectives h3');"
replacement = "const glassObjTitle = splitFltChars('#glass-objectives h3');\n      gsap.set(glassWhoTitle, { opacity: 0 });\n      gsap.set(glassObjTitle, { opacity: 0 });\n      gsap.set('#glass-who li', { opacity: 0, y: 30 });\n      gsap.set('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { opacity: 0, y: 30 });"

content = content.replace(target, replacement)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
