# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Update gsap.set
old_set = "gsap.set('#glass-who li', { opacity: 0, y: 30 });\n      gsap.set('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { opacity: 0, y: 30 });"
new_set = "gsap.set('#glass-who .glass-mask-inner, #glass-objectives .glass-mask-inner', { yPercent: 110 });"
content = content.replace(old_set, new_set)

# 2. Update Step 1 animation
old_anim_who = "scrollTl.to('#glass-who li', { y: 0, opacity: 1, duration: 0.01, stagger: 0.005, ease: 'power2.out' }, t + 0.01);"
new_anim_who = "scrollTl.to('#glass-who .glass-mask-inner', { yPercent: 0, duration: 0.02, stagger: 0, ease: 'power2.out' }, t + 0.01);"
content = content.replace(old_anim_who, new_anim_who)

old_anim_who_out = "scrollTl.to('#glass-who li', { y: 30, opacity: 0, duration: 0.01 }, t);"
new_anim_who_out = "scrollTl.to('#glass-who .glass-mask-inner', { yPercent: 110, duration: 0.01 }, t);"
content = content.replace(old_anim_who_out, new_anim_who_out)

# 3. Update Step 2 animation
old_anim_obj = "scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 0, opacity: 1, duration: 0.01, stagger: 0.005, ease: 'power2.out' }, t + 0.01);"
new_anim_obj = "scrollTl.to('#glass-objectives .glass-mask-inner', { yPercent: 0, duration: 0.02, stagger: 0, ease: 'power2.out' }, t + 0.01);"
content = content.replace(old_anim_obj, new_anim_obj)

old_anim_obj_out = "scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 30, opacity: 0, duration: 0.01 }, t);"
new_anim_obj_out = "scrollTl.to('#glass-objectives .glass-mask-inner', { yPercent: 110, duration: 0.01 }, t);"
content = content.replace(old_anim_obj_out, new_anim_obj_out)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
