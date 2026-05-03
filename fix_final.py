import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. REMOVE DUPLICATE CODE
idx1 = content.find('(function startIntroAnim() {')
idx2 = content.find('(function startIntroAnim() {', idx1 + 10)
if idx2 != -1:
    # Find the closing </script> after idx2
    end_script = content.find('</script>', idx2)
    if end_script != -1:
        content = content[:idx2] + content[end_script:]

# 2. INJECT NEW REVIEW PANEL HTML
html_new = '''
    <div class="oryzo-review-panel" id="review-panel-1">
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
    </div>
'''
html_pattern = r'<div class="oryzo-review-panel" id="review-panel-1">.*?</div>\s*</div>\s*<div class="oryzo-review-panel" id="review-panel-2">'
content = re.sub(html_pattern, html_new + '\n    <div class="oryzo-review-panel" id="review-panel-2">', content, flags=re.DOTALL)


# 3. INJECT NEW JAVASCRIPT
js_new = '''
      // Animación de los paneles de reseña (AHORA ORYZO SLIDE UP)
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
      }
'''
js_pattern = r"const rev1 = document\.getElementById\('review-panel-1'\);.*?const rev2 = document\.getElementById\('review-panel-2'\);"
content = re.sub(js_pattern, js_new + "\n      const rev2 = document.getElementById('review-panel-2');", content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
