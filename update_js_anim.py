# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Buscamos el bloque de magazineScene logic
match = re.search(r'if \(magazineScene\) \{\s*magazineScene\.style\.opacity = 1;[\s\S]*?tracksToAnimate\.forEach', text)

if match:
    new_logic = """if (magazineScene) {
           magazineScene.style.opacity = 1;
           const uiFade = typeof prog !== 'undefined' ? (prog < 15.0 ? 1 : Math.max(0, 1 - (prog - 15.0) / 1.5)) : 1;
           const expandP = 1 - uiFade;
           const easeP = expandP * expandP * (3 - 2 * expandP); // 0 to 1
           
           const baseW = window.innerWidth > 768 ? 466 : window.innerWidth * 0.9;
           const baseH = window.innerWidth > 768 ? 626 : window.innerWidth * 1.3;

           // 1. Letras de RISE se van hacia arriba escalonadamente
           const riseLetters = magazineScene.querySelectorAll('.rise-l, .rise-dot');
           riseLetters.forEach((el, index) => {
               const delay = index * 0.15;
               const letterP = Math.max(0, Math.min(1, (expandP - delay) / (1 - delay)));
               const letterEase = letterP * letterP;
               el.style.transform = `translateY(-${letterEase * 100}px)`;
               el.style.opacity = 1 - letterEase;
           });
           
           // 2. Otras letras y cajas de texto
           const magUIs = magazineScene.querySelectorAll('.mag-ui');
           magUIs.forEach(el => {
               // Evitamos ocultar el h1 y su contenedor directamente, lo controlamos por letra
               if (!el.querySelector('h1')) {
                   el.style.opacity = uiFade;
                   el.style.transform = `scale(${1 + expandP * 0.05})`;
               }
           });

           const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              
              // 3. Expansión a pantalla completa
              if (easeP > 0) {
                  magazineScene.style.position = 'fixed';
                  magazineScene.style.left = '50vw';
                  magazineScene.style.top = '50vh';
                  magazineScene.style.transform = 'translate(-50%, -50%)';
                  magazineScene.style.zIndex = '10000';
              } else {
                  magazineScene.style.position = 'absolute';
                  magazineScene.style.left = '0';
                  magazineScene.style.top = '0';
                  magazineScene.style.transform = 'none';
                  magazineScene.style.zIndex = '2';
              }

              const targetW = window.innerWidth;
              const targetH = window.innerHeight;
              magazineScene.style.width = `${baseW + (targetW - baseW) * easeP}px`;
              magazineScene.style.height = `${baseH + (targetH - baseH) * easeP}px`;

              magContent.style.borderColor = `rgba(249, 204, 16, ${uiFade})`;
              magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;
              magContent.style.backgroundColor = `rgba(6, 2, 15, ${uiFade})`;
              
              // Zoom effect: La chica pasa a cubrir la pantalla
              const bgSize = 250 - (150 * easeP);
              const bgPos = 15 + (35 * easeP);
              magContent.style.backgroundSize = `${bgSize}%`;
              magContent.style.backgroundPosition = `center ${bgPos}%`;
           }

           const tracksToAnimate = magazineScene.querySelectorAll('.carousel-track-small, .carousel-track-large');
           tracksToAnimate.forEach"""

    updated_text = text.replace(match.group(0), new_logic)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("JS Animation Updated!")
else:
    print("Could not find JS block to replace.")
