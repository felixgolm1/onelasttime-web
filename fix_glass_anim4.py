# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_split = '''      function splitFltChars(selector) {
        const chars = [];
        document.querySelectorAll(selector).forEach(span => {
          const text = span.textContent;
          span.textContent = '';
          [...text].forEach(ch => {
            const el = document.createElement('span');
            el.className = 'flt-ch';
            el.style.display = 'inline-block';
            el.textContent = ch === ' ' ? '\\u00a0' : ch;
            span.appendChild(el);
            chars.push(el);
          });
        });
        return chars;
      }
      const leftChars = splitFltChars('#flip-left-text .flt-in');
      const rightChars = splitFltChars('#flip-right-text .flt-in-up');'''

new_split = '''      function splitFltChars(selector) {
        const chars = [];
        document.querySelectorAll(selector).forEach(span => {
          const text = span.textContent;
          span.textContent = '';
          [...text].forEach(ch => {
            const el = document.createElement('span');
            el.className = 'flt-ch';
            el.style.display = 'inline-block';
            el.textContent = ch === ' ' ? '\\u00a0' : ch;
            span.appendChild(el);
            chars.push(el);
          });
        });
        return chars;
      }
      const leftChars = splitFltChars('#flip-left-text .flt-in');
      const rightChars = splitFltChars('#flip-right-text .flt-in-up');
      
      const glassWhoTitle = splitFltChars('#glass-who h3');
      const glassObjTitle = splitFltChars('#glass-objectives h3');'''

content = content.replace(old_split, new_split)

# Set initial states
init_states = '''      gsap.set('#glass-who', { opacity: 0, autoAlpha: 0 });
      gsap.set('#glass-objectives', { opacity: 0, autoAlpha: 0 });
      gsap.set(glassWhoTitle, { opacity: 0 });
      gsap.set(glassObjTitle, { opacity: 0 });
      gsap.set('#glass-who li', { opacity: 0, y: 30 });
      gsap.set('#glass-objectives p, #glass-objectives li, #glass-objectives hr', { opacity: 0, y: 30 });'''

content = content.replace("      gsap.set('#glass-who', { opacity: 0, autoAlpha: 0 });\n      gsap.set('#glass-objectives', { opacity: 0, autoAlpha: 0 });", init_states)


# Modify the timeline animations
old_glass_anim = '''// Animacion de la caja glass-who en el Paso 2
          if (i === 1) {
            scrollTl.to('#glass-who', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
          }

          // Animacion de la caja glass-objectives en el Paso 3
          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
          }'''

new_glass_anim = '''// Animacion de la caja glass-who en el Paso 2
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

content = content.replace(old_glass_anim, new_glass_anim)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
