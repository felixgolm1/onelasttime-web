import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS for 3D card
content = content.replace(
'''    .card-wrap {
      position: absolute;
      width: 280px; height: 160px;
      touch-action: none;
      user-select: none; -webkit-user-select: none;
      pointer-events: auto !important;
      cursor: grab !important;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      border-radius: 16px;
    }''',
'''    .card-wrap {
      position: absolute;
      width: 280px; height: 160px;
      touch-action: none;
      user-select: none; -webkit-user-select: none;
      pointer-events: auto !important;
      cursor: grab !important;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      border-radius: 16px;
      transform-style: preserve-3d;
    }'''
)

content = content.replace(
'''    .card-face {
      width: 100%; height: 100%;
      background:
        url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E"),
        linear-gradient(135deg, #fdfcfa 0%, #f4f2ea 100%);
      background-color: #fdfcfa; /* Fallback sólido que evita transparencias */
      border-radius: 16px; padding: 1.5rem 2rem;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center; text-align: center;
      /* Shadow más intensa para que las cartas se vean sobre el fondo oscuro */
      box-shadow:
        0 2px 4px rgba(0,0,0,0.15),
        0 8px 24px rgba(0,0,0,0.35),
        0 20px 60px rgba(0,0,0,0.4),
        inset 0 0 0 1.5px rgba(255,255,255,0.8);
      pointer-events: auto !important;
      cursor: grab !important;
      position: relative; overflow: hidden;
    }''',
'''    .card-face {
      background:
        url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E"),
        linear-gradient(135deg, #fdfcfa 0%, #f4f2ea 100%);
      background-color: #fdfcfa; /* Fallback sólido que evita transparencias */
      border-radius: 16px; padding: 1.5rem 2rem;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center; text-align: center;
      /* Shadow más intensa para que las cartas se vean sobre el fondo oscuro */
      box-shadow:
        0 2px 4px rgba(0,0,0,0.15),
        0 8px 24px rgba(0,0,0,0.35),
        0 20px 60px rgba(0,0,0,0.4),
        inset 0 0 0 1.5px rgba(255,255,255,0.8);
      pointer-events: auto !important;
      cursor: grab !important;
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      overflow: hidden;
    }
    .card-front {
      z-index: 2;
      transform: rotateY(0deg);
    }
    .card-back {
      transform: rotateY(180deg);
    }'''
)

# HTML changes for card 1
content = content.replace(
'''        <!-- Cartas reales extraíbles — heredan perspectiva 3D del volumen -->
        <div class="card-wrap card-n1 card-in-deck" data-rot="0">
          <div class="card-face">
            <div class="card-question">ANNA, ¿QUÉ HARIAS SI SUPIERAS QUE NO VAS A FRACASAR?</div>
            <div class="card-footer"><img src="assets/img/logo one last time.png" alt="One Last Time" class="footer-logo"></div>
          </div>
        </div>''',
'''        <!-- Cartas reales extraíbles — heredan perspectiva 3D del volumen -->
        <div class="card-wrap card-n1 card-in-deck" data-rot="0">
          <div class="card-face card-front">
            <div class="card-question">ANNA, ¿QUÉ HARIAS SI SUPIERAS QUE NO VAS A FRACASAR?</div>
            <div class="card-footer"><img src="assets/img/logo one last time.png" alt="One Last Time" class="footer-logo"></div>
          </div>
          <div class="card-face card-back">
             <div style="font-weight: 700; font-size: 0.70rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 1rem; color: #000000;">LA RESPUESTA DE ELSA</div>
             <div class="card-question" style="text-align: center; color: #000000;">Me encantaria tener mi propio estudio de baile para ayudar a las personas a expresarse y liberar energia bailando</div>
          </div>
        </div>'''
)

# JS logic for card-n1 flip
content = content.replace(
'''          let move_in = 0, move_out = 0;
          if (prog <= 3.2) {
             move_in = mapRange(prog, 3.0, 3.2, 0, 0.5);
          } else if (prog <= 3.4) {
             move_in = mapRange(prog, 3.2, 3.4, 0.5, 0.92);
          } else if (prog <= 4.4) {
             move_in = mapRange(prog, 3.4, 4.4, 0.92, 1);
          } else {
             move_in = 1;
             move_out = mapRange(prog, 4.4, 4.6, 0, 1);
          }

          let rot_p = 0;
          if (prog <= 3.2) {
             rot_p = mapRange(prog, 3.0, 3.2, 0, 0.5);
          } else if (prog <= 3.4) {
             rot_p = mapRange(prog, 3.2, 3.4, 0.5, 0.92);
          } else if (prog <= 4.4) {
             rot_p = mapRange(prog, 3.4, 4.4, 0.92, 1);
          } else {
             rot_p = 1;
          }

          let blur_p = mapRange(prog, 3.0, 3.1, 0, 1);

          let currentScale = 0.65 + move_in * (1.1 - 0.65);
          let currentRotY = -90 + rot_p * 90;
          
          c1.style.filter = lur(px);
          
          if (move_out === 0) {''',
'''          let move_in = 0, move_out = 0;
          let flipRotation = 0;
          if (prog <= 3.2) {
             move_in = mapRange(prog, 3.0, 3.2, 0, 1.0);
          } else if (prog <= 3.5) {
             move_in = 1.0;
             flipRotation = mapRange(prog, 3.2, 3.5, 0, 180);
          } else if (prog <= 3.9) {
             move_in = 1.0;
             flipRotation = 180;
          } else if (prog <= 4.2) {
             move_in = 1.0;
             flipRotation = 180 + mapRange(prog, 3.9, 4.2, 0, 180);
          } else if (prog <= 4.4) {
             move_in = 1.0;
             flipRotation = 360;
          } else {
             move_in = 1;
             flipRotation = 360;
             move_out = mapRange(prog, 4.4, 4.6, 0, 1);
          }

          let rot_p = 0;
          if (prog <= 3.2) {
             rot_p = mapRange(prog, 3.0, 3.2, 0, 1.0);
          } else {
             rot_p = 1;
          }

          let currentScale = 0.65 + move_in * (1.1 - 0.65);
          let currentRotY = -90 + rot_p * 90;
          currentRotY += flipRotation;
          
          c1.style.filter = ''; // Eliminamos el desenfoque

          // Workaround hiper-robusto para evitar bugs de backface-visibility en algunos navegadores
          let isBackVisible = (currentRotY % 360) > 90 && (currentRotY % 360) < 270;
          const frontFace = c1.querySelector('.card-front');
          const backFace = c1.querySelector('.card-back');
          if (frontFace) frontFace.style.opacity = isBackVisible ? '0' : '1';
          if (backFace) backFace.style.opacity = isBackVisible ? '1' : '0';
          
          if (move_out === 0) {'''
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 2 done")
