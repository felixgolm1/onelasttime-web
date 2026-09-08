# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

target = r"        \}, true\); // use capture phase\s*\}"

restore_hover = '''        }, true); // use capture phase

        document.addEventListener('mouseover', (e) => {
            const cta = e.target.closest('a[href*="reservar-mi-cena.html"], button[onclick*="reservar-mi-cena.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
            if (cta) window._ctaHoverActive = true;
        });
        document.addEventListener('mouseout', (e) => {
            const cta = e.target.closest('a[href*="reservar-mi-cena.html"], button[onclick*="reservar-mi-cena.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
            if (cta) {
                if (e.relatedTarget && cta.contains(e.relatedTarget)) return;
                window._ctaHoverActive = false;
            }
        });
    }'''

content = re.sub(target, restore_hover, content, count=1)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
