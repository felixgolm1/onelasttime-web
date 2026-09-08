# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Step 2 title
old_anim1 = "scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.015, stagger: 0.001, ease: 'none' }, t + 0.01);"
new_anim1 = "scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.01, stagger: 0.0004, ease: 'none' }, t + 0.01);"
content = content.replace(old_anim1, new_anim1)

# Step 3 title
old_anim2 = "scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.015, stagger: 0.001, ease: 'none' }, t + 0.01);"
new_anim2 = "scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.01, stagger: 0.0004, ease: 'none' }, t + 0.01);"
content = content.replace(old_anim2, new_anim2)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
