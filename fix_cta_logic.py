# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Restore the background hover logic
restore_hover = '''        document.addEventListener('mouseover', (e) => {
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

content = content.replace('    }\n\n    \n\n\n\n  </script>', restore_hover + '\n\n    \n\n\n\n  </script>')

# 2. Modify the CTA script to be ALWAYS active
old_cta_script_regex = r'<script>\s*// Efecto de lucecitas exclusivas dentro del CTA.*?</script>'

new_cta_script = '''<script>
    // Efecto de lucecitas exclusivas SIEMPRE activas dentro de los CTAs
    document.addEventListener("DOMContentLoaded", () => {
      document.querySelectorAll('.btn-blue').forEach(btn => {
          btn.style.overflow = 'hidden';
          btn.style.position = 'relative';

          const ctaCanvas = document.createElement('canvas');
          ctaCanvas.style.position = 'absolute';
          ctaCanvas.style.top = '0';
          ctaCanvas.style.left = '0';
          ctaCanvas.style.width = '100%';
          ctaCanvas.style.height = '100%';
          ctaCanvas.style.pointerEvents = 'none';
          ctaCanvas.style.zIndex = '0'; // Detras del texto
          ctaCanvas.style.opacity = '1';
          btn.appendChild(ctaCanvas);
          
          const cCtx = ctaCanvas.getContext('2d');
          
          let ctaParticles = [];
          for(let i=0; i<40; i++){
            ctaParticles.push({
              x: Math.random(),
              y: Math.random(),
              s: Math.random() * 1.5 + 0.5,
              a: Math.random() * Math.PI * 2,
              v: (Math.random() * 0.5 + 0.2)
            });
          }
          
          function drawCtaParticles() {
              ctaCanvas.width = btn.offsetWidth;
              ctaCanvas.height = btn.offsetHeight;
              cCtx.clearRect(0,0, ctaCanvas.width, ctaCanvas.height);
              cCtx.fillStyle = '#ccff00';
              ctaParticles.forEach(p => {
                  p.y -= p.v * 0.01;
                  p.a += 0.05;
                  if (p.y < 0) p.y = 1;
                  cCtx.globalAlpha = (Math.sin(p.a) * 0.5 + 0.5) * 0.7;
                  cCtx.beginPath();
                  cCtx.arc(p.x * ctaCanvas.width, p.y * ctaCanvas.height, p.s, 0, Math.PI*2);
                  cCtx.fill();
              });
              requestAnimationFrame(drawCtaParticles);
          }
          drawCtaParticles();
      });
    });
  </script>'''

content = re.sub(old_cta_script_regex, new_cta_script, content, flags=re.DOTALL)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
