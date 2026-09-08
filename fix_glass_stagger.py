# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# We need to change the duration and stagger of the li elements
# Currently: duration: 0.025, stagger: 0.0025
# We change it to: duration: 0.01, stagger: 0.006 (total time 0.01 + 8*0.006 = 0.058)

old_who = "scrollTl.to('#glass-who li', { y: 0, opacity: 1, duration: 0.025, stagger: 0.0025, ease: 'power2.out' }, t + 0.01);"
new_who = "scrollTl.to('#glass-who li', { y: 0, opacity: 1, duration: 0.015, stagger: 0.004, ease: 'power2.out' }, t + 0.01);"
content = content.replace(old_who, new_who)

old_obj = "scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 0, opacity: 1, duration: 0.025, stagger: 0.0025, ease: 'power2.out' }, t + 0.01);"
new_obj = "scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 0, opacity: 1, duration: 0.015, stagger: 0.004, ease: 'power2.out' }, t + 0.01);"
content = content.replace(old_obj, new_obj)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
