# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_block = '''// Animacion de la caja glass-who en el Paso 2
          if (i === 1) {
            scrollTl.to('#glass-who', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.03, stagger: 0.002, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-who li', { y: 0, opacity: 1, duration: 0.04, stagger: 0.006, ease: 'power2.out' }, t + 0.02);
          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to('#glass-who li', { y: 30, opacity: 0, duration: 0.01 }, t);
          }

          // Animacion de la caja glass-objectives en el Paso 3
          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.03, stagger: 0.002, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 0, opacity: 1, duration: 0.04, stagger: 0.006, ease: 'power2.out' }, t + 0.02);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 30, opacity: 0, duration: 0.01 }, t);
          }'''

new_block = '''// Animacion de la caja glass-who en el Paso 2
          if (i === 1) {
            scrollTl.to('#glass-who', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.015, stagger: 0.001, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-who li', { y: 0, opacity: 1, duration: 0.025, stagger: 0.0025, ease: 'power2.out' }, t + 0.01);
          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to('#glass-who li', { y: 30, opacity: 0, duration: 0.01 }, t);
          }

          // Animacion de la caja glass-objectives en el Paso 3
          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.015, stagger: 0.001, ease: 'none' }, t + 0.01);
            scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 0, opacity: 1, duration: 0.025, stagger: 0.0025, ease: 'power2.out' }, t + 0.01);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: 0.02, ease: 'none' }, t);
            scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01 }, t);
            scrollTl.to('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { y: 30, opacity: 0, duration: 0.01 }, t);
          }'''

content = content.replace(old_block, new_block)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
