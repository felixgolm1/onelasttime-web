# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_block = '''} else {
               if (bottomCta.classList.contains('smoke-out')) {
                   bottomCta.classList.remove('smoke-out');
                   gsap.to(bottomCta, {
                       xPercent: -50, x: 0,
                       y: 0,
                       scaleX: 1, scaleY: 1,
                       skewX: 0, rotation: 0,
                       opacity: 1,
                       filter: 'blur(0px)',
                       duration: 0.35,
                       ease: 'power2.out',
                       overwrite: true
                   });
                   bottomCta.style.pointerEvents = 'auto';
               } else if (!bottomCta.style.opacity || bottomCta.style.opacity === '0') {
                   bottomCta.style.opacity = '1';
                   bottomCta.style.pointerEvents = 'auto';
               }
           }'''

if bad_block in html:
    html = html.replace("bottomCta.style.pointerEvents = 'auto';\n            }\n        } else {\n               if (bottomCta.classList.contains('smoke-out')) {", "bottomCta.style.pointerEvents = 'auto';\n            }\n        }\n/* dangling fixed */\nif (false) {")
    html = html.replace(bad_block, "")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)
