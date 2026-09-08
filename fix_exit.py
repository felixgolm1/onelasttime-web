# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Step 2 exit
old_exit_2 = '''          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.01 }, t);
            scrollTl.to('#glass-who .glass-bullet', { opacity: 0, duration: 0.01 }, t);
          }'''

new_exit_2 = '''          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01, stagger: -0.0004, ease: 'none' }, t);
            scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.02, stagger: 0, ease: 'power2.out' }, t);
            scrollTl.to('#glass-who .glass-bullet', { opacity: 0, duration: 0.01, stagger: 0, ease: 'power2.out' }, t);
          }'''
content = content.replace(old_exit_2, new_exit_2)


# Step 3 exit
old_exit_3 = '''          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to(glassObjFinalText, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 110, duration: 0.01 }, t);
            scrollTl.to('#glass-objectives .glass-bullet', { opacity: 0, duration: 0.01 }, t);
          }'''

new_exit_3 = '''          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01, stagger: -0.0004, ease: 'none' }, t);
            scrollTl.to(glassObjFinalText, { opacity: 0, duration: 0.01, stagger: 0.00015, ease: 'none' }, t);
            scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 110, duration: 0.02, stagger: 0, ease: 'power2.out' }, t);
            scrollTl.to('#glass-objectives .glass-bullet', { opacity: 0, duration: 0.01, stagger: 0, ease: 'power2.out' }, t);
          }'''
content = content.replace(old_exit_3, new_exit_3)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
