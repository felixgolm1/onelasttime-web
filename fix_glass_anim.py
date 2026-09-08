# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_glass_anim = '''// Animacion de la caja glass-objectives en el Paso 3
          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
          }'''

new_glass_anim = '''// Animacion de la caja glass-who en el Paso 2
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

# Since exactly matching whitespace is hard, let's use regex
regex = r'// Animacion de la caja glass-objectives en el Paso 3\s*if \(i === 2\) \{\s*scrollTl\.to\(\'#glass-objectives\', \{ autoAlpha: 1, duration: PAN, ease: \'power1\.inOut\' \}, t\);\s*\} else \{\s*scrollTl\.to\(\'#glass-objectives\', \{ autoAlpha: 0, duration: PAN, ease: \'power1\.inOut\' \}, t\);\s*\}'

content = re.sub(regex, new_glass_anim, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
