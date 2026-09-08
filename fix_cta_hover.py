# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Remove background hover trigger
target_hover = '''          document.addEventListener('mouseover', (e) => {
              const cta = e.target.closest('a[href*="reservar-mi-cena.html"], button[onclick*="reservar-mi-cena.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
              if (cta) window._ctaHoverActive = true;
          });
          document.addEventListener('mouseout', (e) => {
              const cta = e.target.closest('a[href*="reservar-mi-cena.html"], button[onclick*="reservar-mi-cena.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
              if (cta) {
                  if (e.relatedTarget && cta.contains(e.relatedTarget)) return;
                  window._ctaHoverActive = false;
              }
          });'''

content = content.replace(target_hover, '')

# 2. Inject CTA canvas script at the end of body
cta_script = '''
  <script>
    // Efecto de lucecitas exclusivas dentro del CTA
    document.addEventListener("DOMContentLoaded", () => {
      const ctaCanvas = document.createElement('canvas');
      ctaCanvas.style.position = 'absolute';
      ctaCanvas.style.top = '0';
      ctaCanvas.style.left = '0';
      ctaCanvas.style.width = '100%';
      ctaCanvas.style.height = '100%';
      ctaCanvas.style.pointerEvents = 'none';
      ctaCanvas.style.zIndex = '0'; // Detras del texto
      ctaCanvas.style.opacity = '0';
      ctaCanvas.style.transition = 'opacity 0.4s ease';
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
      
      let ctaAnimId;
      function drawCtaParticles() {
          cCtx.clearRect(0,0, ctaCanvas.width, ctaCanvas.height);
          cCtx.fillStyle = '#ccff00';
          ctaParticles.forEach(p => {
              p.y -= p.v * 0.01;
              p.a += 0.05;
              if (p.y < 0) p.y = 1;
              cCtx.globalAlpha = (Math.sin(p.a) * 0.5 + 0.5) * 0.9;
              cCtx.beginPath();
              cCtx.arc(p.x * ctaCanvas.width, p.y * ctaCanvas.height, p.s, 0, Math.PI*2);
              cCtx.fill();
          });
          ctaAnimId = requestAnimationFrame(drawCtaParticles);
      }
      
      document.querySelectorAll('.btn-blue').forEach(btn => {
          btn.style.overflow = 'hidden'; // Contener el canvas
          btn.addEventListener('mouseenter', () => {
              btn.appendChild(ctaCanvas);
              ctaCanvas.width = btn.offsetWidth;
              ctaCanvas.height = btn.offsetHeight;
              ctaCanvas.style.opacity = '1';
              if (!ctaAnimId) drawCtaParticles();
          });
          btn.addEventListener('mouseleave', () => {
              ctaCanvas.style.opacity = '0';
              setTimeout(() => {
                 if (ctaCanvas.style.opacity === '0' && ctaCanvas.parentNode) {
                     ctaCanvas.parentNode.removeChild(ctaCanvas);
                     cancelAnimationFrame(ctaAnimId);
                     ctaAnimId = null;
                 }
              }, 400);
          });
      });
    });
  </script>
'''

content = content.replace('</body>', cta_script + '\n</body>')

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
