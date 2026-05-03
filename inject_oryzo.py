import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

css = '''
    /* ── ORYZO STYLE REVIEW PANEL ── */
    #oryzo-style-review {
      position: fixed;
      left: 0;
      top: 0;
      width: 100vw;
      height: 100vh;
      z-index: 5; /* Por detrás de la carta (z-index 10) */
      pointer-events: none;
      display: flex;
      flex-direction: column;
      padding: 0 4vw;
      box-sizing: border-box;
      font-family: 'Inter', sans-serif;
    }

    .osr-top-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      border-top: 1px dashed rgba(255,255,255,0.2);
      padding: 1.5rem 0;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: rgba(255,255,255,0.8);
      margin-top: auto; /* Empuja el contenido hacia el centro/abajo */
      margin-bottom: 3rem;
    }

    .osr-top-center .osr-stars { margin-left: 1rem; color: #ffffff; }

    .osr-body {
      display: flex;
      width: 100%;
      gap: 5vw;
      align-items: center;
      margin-bottom: auto; /* Empuja el body hacia arriba para centrarlo */
    }

    .osr-col-left {
      flex: 1.2;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }

    .osr-col-right {
      flex: 1;
      display: flex;
      justify-content: flex-end;
    }

    .osr-stars-small {
      font-size: 0.8rem;
      color: rgba(255,255,255,0.6);
      margin-bottom: 1.5rem;
      letter-spacing: 0.1em;
    }

    .osr-quote {
      position: relative;
      font-family: 'Inter', sans-serif;
      font-size: clamp(1.8rem, 2.5vw, 3rem);
      font-weight: 500;
      line-height: 1.2;
      margin-bottom: 3rem;
      letter-spacing: -0.02em;
    }

    .osr-quote-bg {
      color: rgba(255,255,255,0.15); /* Texto base apagado */
    }

    .osr-quote-fg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      color: #ffffff; /* Texto iluminado */
      /* Inicialmente escondido por la derecha (inset right 100%) */
      clip-path: inset(0% 0% 0% 100%); 
    }

    .osr-highlight {
      color: #cc4400; /* Color naranja/marrón estilo Oryzo */
    }

    .osr-author {
      font-size: 0.75rem;
      font-weight: 600;
      color: rgba(255,255,255,0.5);
      letter-spacing: 0.05em;
    }

    .osr-img-wrapper {
      width: 100%;
      max-width: 500px;
      aspect-ratio: 16/10;
      overflow: hidden;
      position: relative;
    }

    .osr-img-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transform: scale(1.0);
      filter: brightness(0.3); /* Inicialmente oscura */
    }
'''
if '/* ── ORYZO STYLE REVIEW PANEL ── */' not in content:
    content = content.replace('</style>', css + '\n</style>')

html = '''
  <div id="oryzo-style-review">
    <div class="osr-top-line">
      <div class="osr-top-left">RATING & REVIEWS</div>
      <div class="osr-top-center">CUSTOM REVIEWS [ 364 ] <span class="osr-stars">★★★★★ [ 5/5 ]</span></div>
      <div class="osr-top-right">SENSIBLES IN USE</div>
    </div>
    <div class="osr-body">
      <div class="osr-col-left">
        <div class="osr-stars-small">★★★★★ [ 5/5 ]</div>
        <div class="osr-quote">
          <span class="osr-quote-bg">"La utilicé con mi pareja en nuestra cena de aniversario y nos hizo <span class="osr-highlight">abrirnos sobre temas</span> que llevábamos meses esquivando sin darnos cuenta."</span>
          <span class="osr-quote-fg">"La utilicé con mi pareja en nuestra cena de aniversario y nos hizo <span class="osr-highlight">abrirnos sobre temas</span> que llevábamos meses esquivando sin darnos cuenta."</span>
        </div>
        <div class="osr-author">
          ELSA & MICHEL SANTS<br>
          <span style="font-size: 0.65rem; opacity: 0.5; font-weight: 400;">SESIÓN DE ANIVERSARIO</span>
        </div>
      </div>
      <div class="osr-col-right">
        <div class="osr-img-wrapper">
          <img src="assets/img/elsa.png" alt="Elsa">
        </div>
      </div>
    </div>
  </div>
'''
if 'id="oryzo-style-review"' not in content:
    content = content.replace('</body>', html + '\n</body>')

js = '''
    // -- Animación de la Reseña Estilo Oryzo --
    const osr = document.getElementById('oryzo-style-review');
    if (osr) {
      // Movimiento vertical constante de abajo hacia arriba durante todo el flip
      scrollTl.fromTo(osr, 
        { y: '100vh', opacity: 1 },
        { y: '-100vh', duration: 0.80, ease: 'linear' },
        0.08
      );
      
      // Fade out progresivo antes de solaparse con el menú superior
      // El panel llega al centro en t=0.08+0.40=0.48, y llega arriba en t=0.88
      // Fade out justo en el último 20% del viaje (t=0.72 a 0.88)
      scrollTl.to(osr, { opacity: 0, duration: 0.16, ease: 'power2.inOut' }, 0.72);

      // Efecto iluminar texto de DERECHA a IZQUIERDA (inset derecho va de 0 a 100, revelando)
      // inset(top right bottom left) -> inset(0% 0% 0% 100%) es todo oculto desde la izquierda
      // Espera un poco a que el panel suba para iluminarlo
      scrollTl.fromTo('.osr-quote-fg',
        { clipPath: 'inset(0% 0% 0% 100%)' },
        { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.30, ease: 'power1.inOut' },
        0.30 
      );

      // Aumentar imagen un 30% e iluminarla gradualmente
      scrollTl.fromTo('.osr-img-wrapper img',
        { scale: 1.0, filter: 'brightness(0.3)' },
        { scale: 1.3, filter: 'brightness(1.0)', duration: 0.45, ease: 'power1.out' },
        0.25
      );
    }
'''
if 'id=\\\'oryzo-style-review\\\'' not in content and 'id="oryzo-style-review"' not in content.split('// ─ Fase 2:')[1]:
    content = content.replace('// ─ Fase 2: LOS 3 FLIPS CONTINUOS', js + '\n    // ─ Fase 2: LOS 3 FLIPS CONTINUOS')


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected Oryzo layout")
