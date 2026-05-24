import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update maxProg
content = content.replace('const maxProg = 30.6;', 'const maxProg = 36.0;')

# 2. Update JS loop logic
old_js = """
      // 1. Translación fluida pegada al fondo morado extendido
      var tSlide = clamp01((p - 26.6) / 2.0); // Scroll largo
      var slideY = (1 - ease(tSlide)) * 130; // de 130vh a 0vh (inicia 30vh mas abajo)
      oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
      oryzoSec.style.pointerEvents = tSlide > 0.5 ? 'auto' : 'none';

      // Sincronizamos el fondo morado para que suba EXACTAMENTE igual que la sección verde
      window._scrollUpVh = 130 - slideY; // Va de 0 a 130

      // 2. Baraja - orientacion identica a la primera seccion
      var deckClone = document.getElementById('oryzo-deck-clone');
      if (deckClone) {
         var volume = deckClone.querySelector('.box-3d-volume');
         if (volume) {
           volume.style.setProperty('transition', 'none', 'important');
           volume.style.setProperty('transform', 'rotateX(0deg) rotateY(-25deg) rotateZ(0deg)', 'important');
         }
      }
"""

new_js = """
      // 1. Translación fluida pegada al fondo morado extendido
      var tSlide = clamp01((p - 26.6) / 2.0); // 26.6 to 28.6
      var tExit = clamp01((p - 28.6) / 1.0);  // 28.6 to 29.6 -> Camara baja, seccion sube
      var slideY = (1 - ease(tSlide)) * 130 - (ease(tExit) * 100); 
      oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
      oryzoSec.style.pointerEvents = tSlide > 0.5 ? 'auto' : 'none';

      // Sincronizamos el fondo morado para que suba EXACTAMENTE igual que la sección verde
      window._scrollUpVh = 130 - slideY;

      // 2. Baraja - orientacion identica a la primera seccion y animacion de apertura
      var deckClone = document.getElementById('oryzo-deck-clone');
      if (deckClone) {
         var volume = deckClone.querySelector('.box-3d-volume');
         if (volume) {
           volume.style.setProperty('transition', 'none', 'important');
           // Cae hacia abajo ligeramente con el tExit
           volume.style.setProperty('transform', 'rotateX(0deg) rotateY(-25deg) rotateZ(0deg) translateY(' + (tExit * 30) + 'vh)', 'important');
         }
         var topFlap = deckClone.querySelector('.box-3d-top');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            // Empieza a abrirse cuando aparece
            topFlap.style.transform = 'rotateX(' + (110 * ease(tSlide)) + 'deg)';
         }
      }
"""

content = content.replace(old_js.strip(), new_js.strip())

# 3. Add testimonials JS
end_reviews_js = """
      // 4. Testimonios Finales
      var endRev1 = document.getElementById('end-review-panel-1');
      var endRev2 = document.getElementById('end-review-panel-2');
      var endRev3 = document.getElementById('end-review-panel-3');
      var endRev4 = document.getElementById('end-review-panel-4');
      var endContainer = document.getElementById('end-reviews-container');

      if (endContainer) {
          endContainer.style.opacity = (p > 28.6) ? 1 : 0;
          
          if (endRev1) {
              var f1 = ease(clamp01((p - 29.6) / 0.3)) * (1 - ease(clamp01((p - 30.8) / 0.2)));
              endRev1.style.opacity = f1;
              endRev1.style.transform = 'translateY(' + ((1 - f1) * 20) + 'px)';
          }
          if (endRev2) {
              var f2 = ease(clamp01((p - 31.0) / 0.3)) * (1 - ease(clamp01((p - 32.4) / 0.2)));
              endRev2.style.opacity = f2;
              endRev2.style.transform = 'translateY(' + ((1 - f2) * 20) + 'px)';
          }
          if (endRev3) {
              var f3 = ease(clamp01((p - 32.6) / 0.3)) * (1 - ease(clamp01((p - 34.0) / 0.2)));
              endRev3.style.opacity = f3;
              endRev3.style.transform = 'translateY(' + ((1 - f3) * 20) + 'px)';
          }
          if (endRev4) {
              var f4 = ease(clamp01((p - 34.2) / 0.3)) * (1 - ease(clamp01((p - 35.8) / 0.2)));
              endRev4.style.opacity = f4;
              endRev4.style.transform = 'translateY(' + ((1 - f4) * 20) + 'px)';
          }
      }
"""

js_insert_point = "if (textGradR) {"
js_insert_index = content.find(js_insert_point)
js_insert_end = content.find("}", js_insert_index) + 1
js_insert_end = content.find("}", js_insert_end) + 1 # Need to skip the inner block

# Let's use string replace for safety
target_block = """
      if (textGradR) {
        var charsR = textGradR.querySelectorAll('.oryzo-char-right');
        if (charsR.length > 0) {
           var targetIdxR = txtPR * (charsR.length + blurLen) - blurLen;
           for (var j = 0; j < charsR.length; j++) {
              var opR = 1 - (j - targetIdxR) / blurLen;
              charsR[j].style.opacity = Math.max(0, Math.min(1, opR));
           }
        }
      }
"""

content = content.replace(target_block, target_block + end_reviews_js)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Update JS done.')
