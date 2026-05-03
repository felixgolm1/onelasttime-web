import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update JS
js_new = '''
      // Animación de los paneles de reseña (Solo Fade In/Out -> AHORA ORYZO SLIDE UP)
      const rev1 = document.getElementById('review-panel-1');
      if (rev1) {
        if (prog > 3.0 && prog < 4.6) {
          let pRev = mapRange(prog, 3.0, 4.6, 0, 1);
          
          // 1. Desplazamiento desde abajo hacia arriba
          let yVal = mapRange(prog, 3.0, 4.6, window.innerHeight, -window.innerHeight);
          rev1.style.transform = 	ranslateY(px);
          
          // 2. Fade in temprano y fade out antes de llegar al menú
          if (pRev < 0.15) {
             rev1.style.opacity = mapRange(pRev, 0, 0.15, 0, 1);
          } else if (pRev > 0.85) {
             rev1.style.opacity = mapRange(pRev, 0.85, 1.0, 1, 0);
          } else {
             rev1.style.opacity = 1;
          }

          // 3. Texto iluminado de derecha a izquierda
          const quoteFg = rev1.querySelector('.review-quote-fg');
          if (quoteFg) {
             let textP = mapRange(pRev, 0.2, 0.5, 100, 0); // inset right de 100 a 0
             // clamped
             textP = Math.max(0, Math.min(100, textP));
             quoteFg.style.clipPath = inset(0% 0% 0% %);
          }

          // 4. Imagen se agranda 30% y se ilumina
          const img = rev1.querySelector('.review-img-col img');
          if (img) {
             let imgP = mapRange(pRev, 0.1, 0.6, 0, 1);
             imgP = Math.max(0, Math.min(1, imgP));
             let scale = 1.0 + (0.3 * imgP);
             let brightness = 0.3 + (0.7 * imgP);
             img.style.transform = scale();
             img.style.filter = rightness();
          }
        } else {
          rev1.style.opacity = '0';
        }
      }
'''

# Use regex to find and replace the block between "const rev1" and "const rev2"
import re
pattern = r"const rev1 = document\.getElementById\('review-panel-1'\);.*?const rev2 = document\.getElementById\('review-panel-2'\);"
match = re.search(pattern, content, re.DOTALL)
if match:
    # replace but keep const rev2
    content = content[:match.start()] + js_new + "\n      const rev2 = document.getElementById('review-panel-2');" + content[match.end():]
else:
    print("JS block not found")

# 2. Update CSS
css_new = '''
    /* ── ORYZO STYLE CSS ── */
    .osr-top-line {
      display: flex; justify-content: space-between; align-items: center;
      width: 100%; border-top: 1px dashed rgba(255,255,255,0.2);
      padding: 1.5rem 0; font-size: 0.75rem; font-weight: 600;
      letter-spacing: 0.05em; color: rgba(255,255,255,0.8);
      position: absolute; top: 10%; left: 10%; right: 10%; width: 80%;
    }
    .osr-stars { margin-left: 1rem; color: #ffffff; }
    .osr-body {
      display: flex; width: 100%; gap: 5vw; align-items: center;
      padding-top: 5rem;
    }
    .osr-stars-small { font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-bottom: 1.5rem; letter-spacing: 0.1em; }
    .review-quote { position: relative; }
    .review-quote-bg { color: rgba(255,255,255,0.15); }
    .review-quote-fg { position: absolute; top: 0; left: 0; width: 100%; color: #ffffff; clip-path: inset(0% 0% 0% 100%); }
    .review-highlight { color: #cc4400; }
'''
if '/* ── ORYZO STYLE CSS ── */' not in content:
    content = content.replace('</style>', css_new + '\n</style>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected fixes")
