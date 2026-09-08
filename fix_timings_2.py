# -*- coding: utf-8 -*-
import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_step2 = '''          if (i === 1) {
            scrollTl.to('#glass-who', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.01, stagger: 0.00042, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-who .glass-mask-line', { yPercent: 0, duration: 0.02427, stagger: 0, ease: 'power2.out' }, t + 0.01);
            scrollTl.to('#glass-who .glass-bullet', { opacity: 1, duration: 0.012, stagger: 0, ease: 'power2.out' }, t + 0.022);
          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.02427, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01, stagger: -0.00042, ease: 'none' }, t);
            scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.02427, stagger: 0, ease: 'power2.out' }, t);
            scrollTl.to('#glass-who .glass-bullet', { opacity: 0, duration: 0.012, stagger: 0, ease: 'power2.out' }, t);
          }'''

new_step2 = '''          if (i === 1) {
            scrollTl.to('#glass-who', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.01, stagger: 0.00069, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-who .glass-mask-line', { yPercent: 0, duration: 0.0335, stagger: 0, ease: 'power2.out' }, t + 0.01);
            scrollTl.to('#glass-who .glass-bullet', { opacity: 1, duration: 0.015, stagger: 0, ease: 'power2.out' }, t + 0.0285);
          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.0335, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01, stagger: -0.00069, ease: 'none' }, t);
            scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.0335, stagger: 0, ease: 'power2.out' }, t);
            scrollTl.to('#glass-who .glass-bullet', { opacity: 0, duration: 0.015, stagger: 0, ease: 'power2.out' }, t);
          }'''

content = content.replace(old_step2, new_step2)

old_step3 = '''          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.01, stagger: 0.00064, ease: 'none' }, t + 0.01);
            scrollTl.to(glassObjFinalText, { opacity: 1, duration: 0.01, stagger: -0.000175, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 0, duration: 0.02345, stagger: 0, ease: 'power2.out' }, t + 0.01);
            scrollTl.to('#glass-objectives .glass-bullet', { opacity: 1, duration: 0.0117, stagger: 0, ease: 'power2.out' }, t + 0.0217);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: 0.02345, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01, stagger: -0.00064, ease: 'none' }, t);
            scrollTl.to(glassObjFinalText, { opacity: 0, duration: 0.01, stagger: 0.000175, ease: 'none' }, t);
            scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 110, duration: 0.02345, stagger: 0, ease: 'power2.out' }, t);
            scrollTl.to('#glass-objectives .glass-bullet', { opacity: 0, duration: 0.0117, stagger: 0, ease: 'power2.out' }, t);
          }'''

new_step3 = '''          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.01, stagger: 0.00108, ease: 'none' }, t + 0.01);
            scrollTl.to(glassObjFinalText, { opacity: 1, duration: 0.01, stagger: -0.00029, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 0, duration: 0.0327, stagger: 0, ease: 'power2.out' }, t + 0.01);
            scrollTl.to('#glass-objectives .glass-bullet', { opacity: 1, duration: 0.015, stagger: 0, ease: 'power2.out' }, t + 0.0277);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: 0.0327, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01, stagger: -0.00108, ease: 'none' }, t);
            scrollTl.to(glassObjFinalText, { opacity: 0, duration: 0.01, stagger: 0.00029, ease: 'none' }, t);
            scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 110, duration: 0.0327, stagger: 0, ease: 'power2.out' }, t);
            scrollTl.to('#glass-objectives .glass-bullet', { opacity: 0, duration: 0.015, stagger: 0, ease: 'power2.out' }, t);
          }'''

content = content.replace(old_step3, new_step3)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
