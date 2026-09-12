# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Match from the comment down to the next comment
pattern = re.compile(r"// Controlar la visibilidad del CTA inferior[\s\S]*?// Animaci.n de los paneles de rese.a")

replacement = """// Controlar la visibilidad del CTA inferior
        const bottomCta = document.getElementById('cta-bottom-container');
        if (bottomCta) {
            bottomCta.classList.remove('smoke-out');
            if (prog >= 38.45) {
                let pOffset = prog - 38.45;
                let yMove = pOffset * 100; 
                
                gsap.set(bottomCta, {
                    xPercent: -50, x: 0,
                    y: -yMove + 'vh',
                    opacity: 1,
                    scaleX: 1, scaleY: 1, skewX: 0, rotation: 0, filter: 'blur(0px)',
                    overwrite: true
                });
                bottomCta.style.pointerEvents = 'auto';
            } else {
                gsap.set(bottomCta, {
                    xPercent: -50, x: 0,
                    y: 0,
                    opacity: 1,
                    scaleX: 1, scaleY: 1, skewX: 0, rotation: 0, filter: 'blur(0px)',
                    overwrite: true
                });
                bottomCta.style.pointerEvents = 'auto';
            }
        }

        // Animación de los paneles de reseña"""

html = pattern.sub(replacement, html)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)
