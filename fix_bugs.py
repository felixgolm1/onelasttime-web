import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update JS loop logic
old_js = """
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

new_js = """
      // 1. Translación fluida de la sección (hasta el centro de la pantalla)
      var tSlide = clamp01((p - 26.6) / 2.0); // 26.6 to 28.6
      var slideY = (1 - ease(tSlide)) * 130; // Nunca baja de 0 para no romper el fondo
      oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
      oryzoSec.style.pointerEvents = tSlide > 0.5 ? 'auto' : 'none';

      // Sincronizamos el fondo morado 
      window._scrollUpVh = 130 - slideY;

      // Fase de salida (la cámara "baja", los textos suben, la caja se queda en medio)
      var tExit = ease(clamp01((p - 28.6) / 1.0));  // 28.6 to 29.6
      var contentY = -(tExit * 100); // 0 a -100vh
      
      if (oryzoTxtL) oryzoTxtL.style.transform = 'translateY(' + contentY + 'vh)';
      if (oryzoTxtR) oryzoTxtR.style.transform = 'translateY(' + contentY + 'vh)';
      if (conectaTxt) conectaTxt.style.transform = 'translate(-50%, calc(-50% + ' + contentY + 'vh))';

      // 2. Baraja - animacion de apertura
      var deckClone = document.getElementById('oryzo-deck-clone');
      if (deckClone) {
         var volume = deckClone.querySelector('.box-3d-volume');
         if (volume) {
           volume.style.setProperty('transition', 'none', 'important');
           // Gira un poco más hacia la izquierda para revelar la frase mientras se abre
           // y se queda quieta en el centro de la pantalla (translateY = 0)
           var rotY = -25 - (tExit * 15); // de -25deg a -40deg
           volume.style.setProperty('transform', 'rotateX(0deg) rotateY(' + rotY + 'deg) rotateZ(0deg)', 'important');
         }
         
         // La tapa principal
         var topFlap = deckClone.querySelector('.box-flap');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            // Empieza a abrirse durante tSlide
            topFlap.style.transform = 'rotateX(' + (110 * ease(tSlide)) + 'deg)';
         }
         // Solapas pequeñas de polvo (se abren hacia los lados)
         var dustLeft = deckClone.querySelector('.dust-flap.left');
         var dustRight = deckClone.querySelector('.dust-flap.right');
         if (dustLeft) {
            dustLeft.style.transition = 'none';
            dustLeft.style.transform = 'rotateY(' + (-80 * ease(tSlide)) + 'deg)';
         }
         if (dustRight) {
            dustRight.style.transition = 'none';
            dustRight.style.transform = 'rotateY(' + (80 * ease(tSlide)) + 'deg)';
         }
      }
"""

if old_js.strip() in content:
    content = content.replace(old_js.strip(), new_js.strip())
else:
    print("Could not find old JS block!")

# Fix the endContainer transform in the testimonials JS
content = content.replace("endContainer.style.opacity = (p > 28.6) ? 1 : 0;", "endContainer.style.opacity = (p > 28.6) ? 1 : 0;\n          endContainer.style.transform = 'translateY(' + contentY + 'vh)';")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Bugs fixed.')
