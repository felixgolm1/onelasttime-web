import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML
html_old = '''    <div class="oryzo-review-panel" id="review-panel-1">
      <div class="review-text-col">
        <div class="review-quote">"Es increíble cómo una simple carta puede generar <span class="review-highlight">conversaciones tan profundas</span> y auténticas. Lo recomiendo 100%."</div>
        <div class="review-author">SARA M.<br>APASIONADA DEL BAILE</div>
      </div>
      <div class="review-img-col">
        <!-- Temporary placeholder logic using SVG data URI -->
        <img src="assets/img/mock-sara.jpg" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMjIyIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZpbGw9IiM2NjYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+Rm90byBkZSBTYXJhPC90ZXh0Pjwvc3ZnPg=='" alt="Review 1">
      </div>
    </div>'''

html_new = '''    <div class="oryzo-review-panel" id="review-panel-1">
      <div class="osr-top-line">
        <div style="display:flex; align-items:center;">
          <div>RESEÑA DESTACADA</div>
          <div class="osr-stars">★★★★★</div>
        </div>
        <div>ORYZO - EXPERIENCIA CINEMÁTICA</div>
      </div>
      <div class="osr-body">
        <div class="review-text-col">
          <div class="osr-stars-small">5 ESTRELLAS</div>
          <div class="review-quote">
            <span class="review-quote-bg">"Es increíble cómo una simple carta puede generar conversaciones tan profundas y auténticas. Lo recomiendo 100%."</span>
            <span class="review-quote-fg">"Es increíble cómo una simple carta puede generar <span class="review-highlight">conversaciones tan profundas</span> y auténticas. Lo recomiendo 100%."</span>
          </div>
          <div class="review-author">ELSA M.<br>APASIONADA DEL BAILE</div>
        </div>
        <div class="review-img-col">
          <img src="assets/img/elsa.png" alt="Review 1">
        </div>
      </div>
    </div>'''

if html_old in content:
    content = content.replace(html_old, html_new)
else:
    print("WARNING: html_old not found!")

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
    content = content.replace('</style>', css_new + '\n  </style>', 1)

# 3. Update JS
js_old = '''      const rev1 = document.getElementById('review-panel-1');
      if (rev1) {
        if (prog > 3.0 && prog < 4.6) {
          if (prog <= 3.4) {
            // Fade in al acercarse
            let pIn = mapRange(prog, 3.0, 3.4, 0, 1);
            rev1.style.opacity = pIn;
            rev1.style.transform = `translateY(0)`; // Aseguramos que esté quieto
          } else if (prog <= 4.2) {
            // Visible durante el Hang Time y el primer 10% de alejamiento
            rev1.style.opacity = '1';
            rev1.style.transform = `translateY(0)`;
          } else {
            // Fade out al alejarse
            let pOut = mapRange(prog, 4.2, 4.6, 0, 1);
            rev1.style.opacity = 1 - pOut;
            rev1.style.transform = `translateY(0)`;
          }
        } else {
          rev1.style.opacity = '0';
        }
      }'''

js_new = '''      // Animación de los paneles de reseña (AHORA ORYZO SLIDE UP)
      const rev1 = document.getElementById('review-panel-1');
      if (rev1) {
        if (prog > 3.0 && prog < 4.6) {
          let pRev = mapRange(prog, 3.0, 4.6, 0, 1);
          
          // 1. Desplazamiento desde abajo hacia arriba
          let yVal = mapRange(prog, 3.0, 4.6, window.innerHeight, -window.innerHeight);
          rev1.style.transform = `translateY(${yVal}px)`;
          
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
             textP = Math.max(0, Math.min(100, textP));
             quoteFg.style.clipPath = `inset(0% 0% 0% ${textP}%)`;
          }

          // 4. Imagen se agranda 30% y se ilumina
          const img = rev1.querySelector('.review-img-col img');
          if (img) {
             let imgP = mapRange(pRev, 0.1, 0.6, 0, 1);
             imgP = Math.max(0, Math.min(1, imgP));
             let scale = 1.0 + (0.3 * imgP);
             let brightness = 0.3 + (0.7 * imgP);
             img.style.transform = `scale(${scale})`;
             img.style.filter = `brightness(${brightness})`;
          }
        } else {
          rev1.style.opacity = '0';
        }
      }'''

if js_old in content:
    content = content.replace(js_old, js_new)
else:
    print("WARNING: js_old not found!")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Safely injected everything without regex.")
