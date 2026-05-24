import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to inject the extraction logic for the clone inside the p > 26.0 block.
# Let's find the place inside the JS:
# "// 2. Baraja - animacion de apertura"
# "var deckClone = document.getElementById('oryzo-deck-clone');"

# First, we need to add the card extraction mapping based on `p`.
new_js = """
      // 2. Baraja - animacion de apertura
      var deckClone = document.getElementById('oryzo-deck-clone');
      if (deckClone) {
         var volume = deckClone.querySelector('.box-3d-volume');
         if (volume) {
           volume.style.setProperty('transition', 'none', 'important');
           var rotY = -25 - (tExit * 15); 
           volume.style.setProperty('transform', 'rotateX(0deg) rotateY(' + rotY + 'deg) rotateZ(0deg)', 'important');
         }
         
         var topFlap = deckClone.querySelector('.box-flap');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            topFlap.style.transform = 'rotateX(' + (110 * ease(tSlide)) + 'deg)';
         }
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

         // --- INYECCION DE CARTAS VOLANDO ---
         let c1_peek_end = mapRange(p, 27.0, 27.5, 0, 1);
         let c2_peek_end = mapRange(p, 27.3, 27.8, 0, 1);
         let c3_peek_end = mapRange(p, 27.6, 28.1, 0, 1);
         let c4_peek_end = mapRange(p, 27.9, 28.4, 0, 1);
         
         let endCards = [
             { el: deckClone.querySelector('.card-n1'), peek: c1_peek_end, progRange: [27.5, 28.5] },
             { el: deckClone.querySelector('.card-n2'), peek: c2_peek_end, progRange: [27.8, 28.8] },
             { el: deckClone.querySelector('.card-n3'), peek: c3_peek_end, progRange: [28.1, 29.1] },
             { el: deckClone.querySelector('.card-n4'), peek: c4_peek_end, progRange: [28.4, 29.4] }
         ];

         let cardTable = document.getElementById('card-table');
         let isDesktop = window.innerWidth > 768;

         endCards.forEach((cData, idx) => {
             let c = cData.el;
             if (!c) return;
             let peek = cData.peek;
             let progR = cData.progRange;

             if (peek === 0) {
                 if (c.dataset.endState !== 'deck-rest') {
                     c.dataset.endState = 'deck-rest';
                     let interior = deckClone.querySelector('.interior-cards');
                     if (interior && c.parentNode !== interior) interior.insertBefore(c, interior.firstChild);
                     c.style.position = ''; c.style.left = ''; c.style.top = ''; c.style.margin = '';
                     c.classList.remove('card-on-table', 'card-peeking');
                     c.classList.add('card-in-deck');
                     c.style.transition = 'none';
                     c.style.transform = `translate(-50%, calc(-50% + 15px)) translateZ(${c.dataset.zDepth||6}px) rotate(-90deg) scale(0.85)`;
                     c.style.clipPath = 'inset(0 0 0 10px round 16px)';
                 }
             } else if (peek > 0 && p <= progR[0]) {
                 c.dataset.endState = 'extracting';
                 let interior = deckClone.querySelector('.interior-cards');
                 if (interior && c.parentNode !== interior) {
                     interior.insertBefore(c, interior.firstChild);
                     c.style.position = ''; c.style.left = ''; c.style.top = ''; c.style.margin = '';
                 }
                 c.classList.add('card-peeking');
                 c.classList.remove('card-on-table', 'card-in-deck');
                 c.style.transition = 'none';
                 const y = 15 - 345 * peek; 
                 c.style.transform = `translate(-50%, calc(-50% + ${y}px)) translateZ(${c.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;
                 c.style.clipPath = y > 5 ? 'inset(0 0 0 10px round 16px)' : '';
             } else {
                 c.dataset.endState = 'table';
                 if (c.parentNode !== cardTable) {
                     let slotRef = deckClone.querySelector('#slot-reference-end');
                     if (!slotRef) {
                         slotRef = document.createElement('div');
                         slotRef.id = 'slot-reference-end';
                         slotRef.style.cssText = `position:absolute; left:50%; top:50%; width:1px; height:1px; pointer-events:none; opacity:0; transform: translate(-50%, calc(-50% - 330px)) translateZ(${c.dataset.zDepth||6}px) rotate(-90deg) scale(0.9);`;
                         let interior = deckClone.querySelector('.interior-cards');
                         if (interior) interior.appendChild(slotRef);
                     }
                     if (slotRef && cardTable) {
                         const rect = slotRef.getBoundingClientRect();
                         const tableRect = cardTable.getBoundingClientRect();
                         if (rect.width > 0 || rect.left > 0) {
                             c.dataset.boxLeftEnd = (rect.left - tableRect.left).toString();
                             c.dataset.boxTopEnd  = (rect.top - tableRect.top).toString();
                         }
                     }
                     if (cardTable) cardTable.appendChild(c);
                     c.classList.remove('card-in-deck', 'card-peeking');
                     c.classList.add('card-on-table');
                     c.style.position = 'absolute';
                     c.style.clipPath = '';
                     c.style.transition = 'none';
                 }
                 const startX = parseFloat(c.dataset.boxLeftEnd) || (window.innerWidth / 2);
                 const startY = parseFloat(c.dataset.boxTopEnd) || (window.innerHeight / 2 - 114.75);
                 
                 let pRev = mapRange(p, progR[0], progR[1], 0, 1);
                 pRev = ease(pRev);
                 
                 // Distribuir a los lados
                 const targetX = isDesktop ? (idx % 2 === 0 ? window.innerWidth * 0.15 : window.innerWidth * 0.85) : window.innerWidth / 2;
                 const targetY = isDesktop ? window.innerHeight * (0.3 + (idx * 0.1)) : window.innerHeight * 0.2;
                 const targetRot = isDesktop ? (idx % 2 === 0 ? -10 : 10) : 0;
                 const targetScale = isDesktop ? 1.0 : 0.8;

                 const currentX = startX + (targetX - startX) * pRev;
                 const currentY = startY + (targetY - startY) * pRev;
                 const currentRot = -90 + (targetRot + 90) * pRev;
                 const currentScale = 0.9 + (targetScale - 0.9) * pRev;

                 // Translate Y adjustment for camera down (tExit)
                 const exitY = tExit * 100 * window.innerHeight / 100;

                 c.style.transform = `translate(-50%, -50%) translate(${currentX}px, ${currentY - exitY}px) rotate(${currentRot}deg) scale(${currentScale})`;
                 
                 // Desvanecer cuando aparecen los testimonios HTML
                 let fadeOut = 1 - mapRange(p, 29.2, 29.6, 0, 1);
                 c.style.opacity = fadeOut.toFixed(3);
             }
         });
      }
"""

old_target = """
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

import sys
if old_target.strip() in content:
    content = content.replace(old_target.strip(), new_js.strip())
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected successfully.")
else:
    print("Target block not found!")
    sys.exit(1)
