with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Buscar el bloque desde if (magazineScene) { hasta tracksToAnimate.forEach
match = re.search(r'if \(magazineScene\) \{\s*magazineScene\.style\.opacity = 1;[\s\S]*?tracksToAnimate\.forEach', text)

new_logic = """if (magazineScene) {
           magazineScene.style.opacity = 1;
           const uiFade = typeof prog !== 'undefined' ? (prog < 15.0 ? 1 : Math.max(0, 1 - (prog - 15.0) / 1.5)) : 1;
           const expandP = 1 - uiFade;
           const easeP = expandP * expandP * (3 - 2 * expandP); // 0 to 1
           
           const magUIs = magazineScene.querySelectorAll('.mag-ui');
           magUIs.forEach(el => el.style.opacity = uiFade);
           
           // Pop out of the layout and expand to full screen
           const baseW = window.innerWidth > 768 ? 466 : window.innerWidth * 0.9;
           const baseH = window.innerWidth > 768 ? 626 : window.innerWidth * 1.3;
           const targetW = window.innerWidth;
           const targetH = window.innerHeight;
           
           if (easeP > 0.01) {
              magazineScene.style.position = 'fixed';
              magazineScene.style.left = '50vw';
              magazineScene.style.top = '50vh';
              magazineScene.style.transform = 'translate(-50%, -50%)';
              magazineScene.style.zIndex = '10000';
           } else {
              // Reseteamos a su estado original en la tira del carrusel
              magazineScene.style.position = 'relative';
              magazineScene.style.left = 'auto';
              magazineScene.style.top = 'auto';
              magazineScene.style.transform = 'none';
              magazineScene.style.zIndex = '2';
           }
           magazineScene.style.width = `${baseW + (targetW - baseW) * easeP}px`;
           magazineScene.style.height = `${baseH + (targetH - baseH) * easeP}px`;

           const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              magContent.style.borderColor = `rgba(249, 204, 16, ${uiFade})`;
              magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;
              magContent.style.backgroundColor = `rgba(6, 2, 15, ${uiFade})`;
              
              // Ajustamos la imagen para que se mantenga encuadrada durante la expansion
              const bgSize = 250 - (150 * easeP);
              const bgPos = 15 + (35 * easeP); // de 15% a 50% (centrado)
              magContent.style.backgroundSize = `${bgSize}%`;
              magContent.style.backgroundPosition = `center ${bgPos}%`;
           }
           
           const magSvg = document.getElementById('magazine-border-svg');
           if (magSvg) magSvg.style.opacity = uiFade;

           const tracksToAnimate = magazineScene.querySelectorAll('.carousel-track-small, .carousel-track-large');
           tracksToAnimate.forEach"""

if match:
    text = text.replace(match.group(0), new_logic)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Expansion applied!")
else:
    print("Match not found")
