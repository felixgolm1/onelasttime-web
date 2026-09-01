
// Ã¢â€€Ã¢â€€ CONTROLADOR SECCIÓN NEUROCIENCIA â€â€ wipe Oryzo scroll-driven Ã¢â€€Ã¢â€€
// Barrido de máscara de gradiente 100% vinculado al scroll.
// Título: barre izquierda→derecha. Párrafo: barre derecha→izquierda.
// Todo computado en cada frame desde window._brainScrollProg. Cero timers.
(function() {
  var SHOW_START = 16.93;
  var SHOW_FADE  = 17.08;
  var STEP_START = 17.0;
  var STEP_END    = 21.6;  // Reducido ~50% (4 pasos de 1.15)
  var NUM_STEPS   = 4;
  var STEP_SIZE   = (STEP_END - STEP_START) / NUM_STEPS; // 1.15 por paso
  var TRANS_ENTRY = 0.40; // duracion animacion de ENTRADA (reducida)
  var TRANS_EXIT  = 0.50; // duracion animacion de SALIDA  (reducida)
  var TRANS       = TRANS_ENTRY; // alias â€â€ usado solo para fade-in del card
  var FEATHER     = 55;   // % de suavidad del gradiente

  function mapRange(p, inMin, inMax, outMin, outMax) {
      let t = Math.max(0, Math.min(1, (p - inMin) / (inMax - inMin)));
      return outMin + t * (outMax - outMin);
  }

  var SRCS = [
    'assets/brain_zona1_vta.png',
    'assets/brain_zona2_acc.png',
    'assets/brain_zona3_hipotalamo.png',
    'assets/brain_zona4_caudado.png'
  ];

  var brain  = document.getElementById('brain-2d-wrap');
  var card   = document.getElementById('neuro-card');
  var imgA   = document.getElementById('brain-img-a');
  var imgB   = document.getElementById('brain-img-b');
  var slides = [document.getElementById('nsl-0'), document.getElementById('nsl-1'),
                document.getElementById('nsl-2'), document.getElementById('nsl-3')];
  var dots   = [document.getElementById('ndot-0'), document.getElementById('ndot-1'),
                document.getElementById('ndot-2'), document.getElementById('ndot-3')];

  if (!imgA || !imgB) return;

  // Quitar la transición CSS de los slides â€â€ el scroll lo maneja todo
  slides.forEach(function(sl) {
    if (sl) sl.style.transition = 'none';
  });

  // Extraer label, h3 y último p de cada slide
  var slideEls = slides.map(function(sl) {
    if (!sl) return null;
    var h3    = sl.querySelector('h3');
    var ps    = sl.querySelectorAll('p');
    var label = ps.length > 0 ? ps[0] : null;                   // "CORTEZA PREFRONTAL" etc.
    var para  = ps.length > 1 ? ps[ps.length - 1] : null;       // párrafo descriptivo
    return { el: sl, label: label, h3: h3, para: para };
  });

  // Ã¢â€€Ã¢â€€ Aplicar máscara Oryzo â€â€ gradiente puro sin zonas sólidas Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
  // Fórmula: la franja de degradado siempre ocupa el 100% del elemento.
  // Sólo se desplaza su posición. Nunca hay una zona sólida → ningún borde visible.
  //   showFrac = 1 → gradiente completamente fuera (todo visible)
  //   showFrac = 0.5 → gradiente centrado (fade suave de esquina a esquina)
  //   showFrac = 0 → gradiente completamente fuera (todo oculto)
  // dir: 'ltr' = 135deg (top-left→bottom-right) | 'rtl' = 315deg (opuesto)
  function applyMask(el, showFrac, dir) {
    if (!el) return;
    var X   = showFrac * 200 - 100; // -100 (todo oculto) → +100 (todo visible)
    var deg = (dir === 'ltr') ? '135deg' : '315deg';
    // black = muestra, transparent = oculta. La franja siempre es de 100%.
    var mask = 'linear-gradient(' + deg + ', black ' + X.toFixed(1) + '%, transparent ' + (X + 100).toFixed(1) + '%)';
    el.style.webkitMaskImage = mask;
    el.style.maskImage = mask;
  }

  // Ã¢â€€Ã¢â€€ LABEL GLOBAL: Efecto decodificación random (scramble) Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
  var SCRAMBLE_GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#*+^~!';
  function applyGlobalScramble(el, frac, finalStr, isExit) {
    if (!el) return;
    
    el.style.transform = ''; // Mantener fijo siempre
    
    if (frac >= 0.999) { 
      el.textContent = finalStr; 
      el.style.color = '#fff';
      el.style.textShadow = '';
      return; 
    }
    
    var N = finalStr.length;
    var numResolved = Math.floor(frac * N);
    var resolvedStr = '';
    var randomStr = '';
    for(var i=0; i<N; i++) {
      var isResolved = isExit ? (i >= N - numResolved) : (i < numResolved);
      if (finalStr[i] === ' ') {
        if (isResolved) resolvedStr += ' ';
        else randomStr += ' ';
      } else if (isResolved) {
        resolvedStr += finalStr[i];
      } else {
        // Pseudo-random index tied exactly to scroll fraction
        var speed = 300 + i * 23;
        var offset = i * 73;
        var charIdx = Math.floor(frac * speed + offset) % SCRAMBLE_GLYPHS.length;
        randomStr += SCRAMBLE_GLYPHS[charIdx];
      }
    }
    
    if (isExit) {
      el.innerHTML = '<span style="color:#ccff00; text-shadow:0 0 10px rgba(204,255,0,0.6);">' + randomStr + '</span>' + 
                     '<span style="color:#fff; text-shadow:none;">' + resolvedStr + '</span>';
    } else {
      el.innerHTML = '<span style="color:#fff; text-shadow:none;">' + resolvedStr + '</span>' + 
                     '<span style="color:#ccff00; text-shadow:0 0 10px rgba(204,255,0,0.6);">' + randomStr + '</span>';
    }
                   
    el.style.color = '';
    el.style.textShadow = '';
  }

  // Ã¢â€€Ã¢â€€ ENTRADA H3/P: clip-path reveal de abajo hacia arriba Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
  // El stagger (STAGGER_IN) entre label→h3→para crea el efecto cascada.
  // Cada bloque usa un clip recto (inset) â€â€ sin inclinar nada.
  function applyEntryReveal(el, entryFrac) {
    if (!el) return;
    if (entryFrac >= 0.999) {
      el.style.clipPath        = '';
      el.style.transform       = '';
      el.style.webkitMaskImage = '';
      el.style.maskImage       = '';
      return;
    }
    var clip = (1 - entryFrac) * 110;
    var ty   = (1 - entryFrac) * 10;
    el.style.clipPath        = 'inset(0 0 ' + clip.toFixed(1) + '% 0)';
    el.style.transform       = 'translateY(' + ty.toFixed(1) + 'px)';
    el.style.webkitMaskImage = '';
    el.style.maskImage       = '';
  }



  // Ã¢â€€Ã¢â€€ STAGGER de entrada: cada elemento empieza más tarde que el anterior Ã¢â€€Ã¢â€€
  // n=0 label (más rápido), n=1 h3, n=2 para (más lento)
  // STAGGER: cuánto del rango de entryFrac se retrasa cada elemento
  var STAGGER_IN = 0.22;
  var LEAD_IN    = 1 - 2 * STAGGER_IN; // fracción que usa cada elemento para ir 0→1

  function staggerFrac(ef, n) {
    // Elemento n empieza cuando ef = n*STAGGER_IN y termina cuando ef = n*STAGGER_IN + LEAD_IN
    return clamp01((ef - n * STAGGER_IN) / LEAD_IN);
  }

  // Ã¢â€€Ã¢â€€ SALIDA: limpia clip y aplica gradient mask wipe Ã¢â€€Ã¢â€€
  function applyExitMask(el, exitFrac, dir) {
    if (!el) return;
    el.style.clipPath  = '';
    el.style.transform = '';
    applyMask(el, 1 - exitFrac, dir);
  }

  // Ã¢â€€Ã¢â€€ Aplicar estado completo del slide (entry y exit separados) Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
  function applySlide(sIdx, entryFrac, exitFrac) {
    var d = slideEls[sIdx];
    if (!d) return;
    var totalFrac = entryFrac * (1 - exitFrac);
    d.el.style.opacity = totalFrac > 0.005 ? '1' : '0';
    if (exitFrac > 0.005) {
      // SALIDA: gradient mask wipe (Oryzo)
      applyExitMask(d.h3,    exitFrac, 'ltr');
      applyExitMask(d.para,  exitFrac, 'rtl');
    } else {
      // ENTRADA: clip-path para h3 y para
      applyEntryReveal(d.h3,       staggerFrac(entryFrac, 1)); // medio
      applyEntryReveal(d.para,     staggerFrac(entryFrac, 2)); // más lento
    }
  }


  // Ã¢â€€Ã¢â€€ Imagen del cerebro: crossfade discreto al cambiar step dominante Ã¢â€€Ã¢â€€Ã¢â€€
  var curImgStep = -1;
  var frontIsA   = true;

  function setImg(s) {
    if (s === curImgStep) return;
    curImgStep = s;
    var front = frontIsA ? imgA : imgB;
    var back  = frontIsA ? imgB : imgA;
    back.src            = SRCS[s];
    back.style.opacity  = '1';
    front.style.opacity = '0';
    frontIsA = !frontIsA;
  }

  function clamp01(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  // Ease in-out cuadrático â€â€ suaviza el barrido sin distorsionar el mapeo de scroll
  function ease(t) { return t < 0.5 ? 2*t*t : 1 - Math.pow(-2*t+2,2)/2; }

  function updateReviewPanelInternals(panel, pRev) {
      if (!panel._charsLeft) {
          panel._charsLeft = Array.from(panel.querySelectorAll('.review-left-quote .char'));
          panel._charsLeft.forEach(c => c.style.transition = 'none');
      }
      if (!panel._charsRight) {
          panel._charsRight = Array.from(panel.querySelectorAll('.review-quote .char'));
          panel._charsRight.forEach(c => c.style.transition = 'none');
      }
      if (!panel._stars) {
          panel._stars = Array.from(panel.querySelectorAll('.star'));
          panel._stars.forEach(s => s.style.transition = 'none');
      }
      if (!panel._img) { 
          panel._img = panel.querySelector('.review-img-col img');
          if (panel._img) {
              panel._img.style.willChange = 'transform, filter, opacity';
              panel._img.style.transition = 'none';
          }
      }
      if (!panel._ratingNum) panel._ratingNum = panel.querySelector('.rating-number');

      // 1. Texto Izquierdo (Historia) - Ajustado a ~2cm visibles (0.12)
      let readPLeft = mapRange(pRev, 0.12, 0.28, 0, 1);
      readPLeft = Math.max(0, Math.min(1, readPLeft));
      if (panel._charsLeft && panel._charsLeft.length > 0) {
         const totalL = panel._charsLeft.length;
         const gradL = Math.max(10, Math.floor(totalL * 0.15)); 
         panel._charsLeft.forEach((c, i) => {
             let charStart = i / totalL;
             let charEnd = Math.min(1, (i + gradL) / totalL); 
             let cP = mapRange(readPLeft, charStart, charEnd, 0, 1);
             cP = Math.max(0, Math.min(1, cP));
             c.style.opacity = (0.15 + (0.85 * cP)).toString();
         });
      }

      // 2. Estrellas
      if (false && panel._stars && panel._stars.length > 0) {
         let starP = mapRange(pRev, 0.28, 0.38, 0, 1); 
         starP = Math.max(0, Math.min(1, starP));
         const totalStars = panel._stars.length;
         let currentScore = 0;
         panel._stars.forEach((s, i) => {
             let threshold = (i + 0.5) / totalStars; 
             if (starP > threshold) { s.style.opacity = '1'; currentScore++; } 
             else { s.style.opacity = '0.2'; }
         });
         if (panel._ratingNum) panel._ratingNum.innerText = '[' + currentScore + '/5]';
      }

      // 3. Texto Derecho (Reseña) - Ajustado en cascada
      let readPRight = mapRange(pRev, 0.30, 0.46, 0, 1);
      readPRight = Math.max(0, Math.min(1, readPRight));
      if (panel._charsRight && panel._charsRight.length > 0) {
         const totalR = panel._charsRight.length;
         const gradR = Math.max(10, Math.floor(totalR * 0.15)); 
         panel._charsRight.forEach((c, i) => {
             let charStart = i / totalR;
             let charEnd = Math.min(1, (i + gradR) / totalR); 
             let cP = mapRange(readPRight, charStart, charEnd, 0, 1);
             cP = Math.max(0, Math.min(1, cP));
             c.style.opacity = (0.15 + (0.85 * cP)).toString();
         });
      }

      // 4. Imagen - Intacta
      if (panel._img) {
         let imgP = mapRange(pRev, 0.30, 0.46, 0, 1); 
         imgP = Math.max(0, Math.min(1, imgP));
         let scale = 1.0 + (0.3 * imgP);
         let brightness = 0.3 + (0.7 * imgP);
         panel._img.style.transform = "scale(" + scale + ") translateZ(0)"; 
         panel._img.style.opacity = brightness.toString(); 
      }
  }

  function tick() {
    var p = window._brainScrollProg || 0;

    // Fade in/out del card y el cerebro 2D
    var fadeT = p >= SHOW_START
      ? clamp01((p - SHOW_START) / (SHOW_FADE - SHOW_START))
      : 0;
    if (brain) brain.style.opacity = String(fadeT);
    if (card)  card.style.opacity  = String(fadeT);

    // Global Label Logic
    var gLabel = document.getElementById('global-brain-label');
    if (gLabel) {
      // Fade in smoothly right before step 0
      var pM = p + 0.5;
      var activeProg = clamp01((pM - 17.3)/0.2);
      gLabel.style.opacity = activeProg.toString();
      
      if (activeProg > 0) {
        var BRAIN_LABELS = [
          "ÁREA TEGMENTAL VENTRAL",
          "CORTEZA CINGULADA",
          "HIPOTÁLAMO",
          "NÚCLEO CAUDADO"
        ];
        var cIdx = Math.max(0, Math.min(3, Math.floor((p - STEP_START) / STEP_SIZE)));
        var pStart = STEP_START + cIdx * STEP_SIZE;
        var pEnd   = pStart + STEP_SIZE - TRANS_EXIT;
        var entryF = clamp01((p - pStart) / TRANS_ENTRY);
        var exitF  = (cIdx === 3) ? 0 : clamp01((p - pEnd) / TRANS_EXIT);
        
        var lEntry = staggerFrac(entryF, 0);
        var labelFrac = 0;
        var isExitPhase = false;
        if (lEntry < 1) {
          labelFrac = lEntry;
        } else if (exitF > 0) {
          isExitPhase = true;
          // Retrasar el scramble de salida hasta que el fade-out esté al 50%
          labelFrac = exitF <= 0.5 ? 1 : 1 - ((exitF - 0.5) * 2);
        } else {
          labelFrac = 1;
        }
        
        applyGlobalScramble(gLabel, labelFrac, BRAIN_LABELS[cIdx], isExitPhase);
      }
    }

    // entryFrac y exitFrac por separado â€â€ entrada clip reveal, salida mask wipe
    var entryFracs = [1, 0, 0, 0];
    var exitFracs  = [0, 0, 0, 0];

    for (var s = 0; s < NUM_STEPS; s++) {
      var boundary     = STEP_START + (s + 1) * STEP_SIZE;
      var prevBoundary = STEP_START + s * STEP_SIZE;
      exitFracs[s]  = (s === NUM_STEPS - 1) ? 0.0 : ease(clamp01((p - (boundary - TRANS_EXIT))  / TRANS_EXIT));
      entryFracs[s] = ease(clamp01((p - prevBoundary) / TRANS_ENTRY));
    }

    var domStep = 0, domVal = -1;
    for (var i = 0; i < NUM_STEPS; i++) {
      var sf = entryFracs[i] * (1 - exitFracs[i]);
      if (sf > domVal) { domVal = sf; domStep = i; }
    }
    setImg(domStep);

    for (var j = 0; j < NUM_STEPS; j++) {
      applySlide(j, entryFracs[j], exitFracs[j]);
      if (dots[j]) {
        var isActive = (j === domStep);
        dots[j].style.background = isActive ? '#ff8c42' : 'rgba(255,255,255,.2)';
        dots[j].style.transform  = isActive ? 'scale(1.4)' : 'scale(1)';
      }
    }

    // Ã¢â€€Ã¢â€€ LÓGICA DE LA SECCIÓN ORYZO Ã¢â€€Ã¢â€€
    var oryzoSec = document.getElementById('oryzo-section');
    var oryzoTxtL = document.getElementById('oryzo-text-left');
    var oryzoTxtR = document.getElementById('oryzo-text-right');
    var oryzoDeck = document.getElementById('oryzo-deck-container');

    if (oryzoSec && oryzoTxtL && oryzoTxtR && oryzoDeck) {
      // 1. Translación fluida de la sección (hasta el centro de la pantalla)
      var tSlide = clamp01((p - 21.7) / 1.6); // Termina en 23.3, justo cuando empieza a abrirse
      // Empieza a bajar (38.6) con el carrusel y termina de desaparecer del todo (40.76)
      var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); 
      var slideY = (1 - ease(tSlide)) * 130; // La pantalla se queda anclada
      oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
      
      // La baraja de cartas baja independientemente de la pantalla (80vh es suficiente para ocultarla)
      oryzoDeck.style.transform = 'translateY(' + (tExitBox * 80) + 'vh)';
      oryzoSec.style.pointerEvents = tSlide > 0.5 ? 'auto' : 'none';
      oryzoSec.style.visibility = tSlide > 0 ? 'visible' : 'hidden';

      // Sincronizamos el fondo morado 
      window._scrollUpVh = 130 - slideY;

      // Fase de salida (la cámara baja continuamente)
      var tCamera = clamp01((p - 21.7) / 3.0);
      var textY = 130 - (ease(tCamera) * 230);
      var contentY = Math.min(0, textY - slideY);
      var conectaTxt = document.getElementById('conecta-transition-text');
      
      if (oryzoTxtL) oryzoTxtL.style.transform = 'translateY(' + contentY + 'vh)';
      if (oryzoTxtR) oryzoTxtR.style.transform = 'translateY(' + contentY + 'vh)';
      if (conectaTxt) conectaTxt.style.transform = 'translate(-50%, calc(-50% + ' + contentY + 'vh))';

      // 2. Baraja - animacion de apertura
      var deckClone = document.getElementById('oryzo-deck-clone');
      if (!deckClone) {
          deckClone = document.createElement('div');
          deckClone.innerHTML = '<div class="box-3d-volume"></div><div class="box-flap"></div><div class="dust-flap left"></div><div class="dust-flap right"></div><div class="tuck-lip"></div><div class="interior-cards"><div class="interior-card"></div><div class="interior-card"></div><div class="interior-card"></div><div class="interior-card"></div><div class="interior-card"></div><div class="interior-card"></div></div><div class="card-n1" style="display:none;"></div><div class="card-n2" style="display:none;"></div><div class="card-n3" style="display:none;"></div><div class="card-n4" style="display:none;"></div>';
      }
      if (deckClone) {
         var volume = deckClone.querySelector('.box-3d-volume');
         if (volume) {
           volume.style.setProperty('transition', 'none', 'important');
           var rotY = -25; // Fija, sin rotar durante la apertura
           volume.style.setProperty('transform', 'rotateX(0deg) rotateY(' + rotY + 'deg) rotateZ(0deg)', 'important');
         }
         
         // Helper function for mapping ranges just for the flaps if needed
         function mapFlap(val, inMin, inMax, outMin, outMax) {
             let t = (val - inMin) / (inMax - inMin);
             t = Math.max(0, Math.min(1, t));
             return outMin + t * (outMax - outMin);
         }
         
         // tOpen: animacion de apertura SEPARADA de la subida â€â€ arranca cuando la caja ya es visible
         var tOpen = clamp01((p - 23.3) / 0.3); // 23.3 a 23.6
         // tClose: cierra la caja a la misma velocidad en p = 30.79
         var tClose = clamp01((p - 30.79) / 0.3);
         let eOpen = ease(tOpen) * (1 - ease(tClose));
         if(deckClone) {
           let df1 = deckClone.querySelector('.interior-cards .interior-card:nth-child(1)');
           if(df1) df1.style.transform = `translateZ(6px) translateY(${-60 * eOpen}px)`;
           let df2 = deckClone.querySelector('.interior-cards .interior-card:nth-child(2)');
           if(df2) df2.style.transform = `translateZ(8px) translateY(${-50 * eOpen}px)`;
           let df3 = deckClone.querySelector('.interior-cards .interior-card:nth-child(3)');
           if(df3) df3.style.transform = `translateZ(10px) translateY(${-40 * eOpen}px)`;
           let df4 = deckClone.querySelector('.interior-cards .interior-card:nth-child(4)');
           if(df4) df4.style.transform = `translateZ(12px) translateY(${-30 * eOpen}px)`;
           let df5 = deckClone.querySelector('.interior-cards .interior-card:nth-child(5)');
           if(df5) df5.style.transform = `translateZ(14px) translateY(${-20 * eOpen}px)`;
           let df6 = deckClone.querySelector('.interior-cards .interior-card:nth-child(6)');
           if(df6) df6.style.transform = `translateZ(16px) translateY(${-10 * eOpen}px)`;
         }

         // La tapa principal (90 a 180)
         var topFlap = deckClone.querySelector('.box-flap');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            let flapRot = mapFlap(eOpen, 0.0, 0.5, 90, 180);
            topFlap.style.transform = 'translateZ(0px) rotateX(' + flapRot + 'deg)';
         }
         // Solapas de polvo (-90 a -180)
         var dustLeft = deckClone.querySelector('.dust-flap.left');
         var dustRight = deckClone.querySelector('.dust-flap.right');
         let dustRot = mapFlap(eOpen, 0.4, 0.8, -90, -180);
         if (dustLeft) {
            dustLeft.style.transition = 'none';
            dustLeft.style.transform = 'rotateX(' + dustRot + 'deg)';
         }
         if (dustRight) {
            dustRight.style.transition = 'none';
            dustRight.style.transform = 'rotateX(' + dustRot + 'deg)';
         }
         // Solapa interior (tuck-lip) (-92 a -5)
         var tuckLip = deckClone.querySelector('.tuck-lip');
         if (tuckLip) {
            tuckLip.style.transition = 'none';
            let lipRot = mapFlap(eOpen, 0.05, 0.5, -92, -5);
            tuckLip.style.transform = 'rotateX(' + lipRot + 'deg)';
         }

         // --- REPLICA EXACTA DE TESTIMONIOS CON localP = p - 21.5 ---
         let localP = p - 21.1;
         // Cache card refs: una vez movidas a endCardTable, querySelector devuelve null â€â€ necesitamos la referencia persistente
         if (!window._ecCache || window._ecCache._deck !== deckClone) {
           window._ecCache = {
             _deck: deckClone,
             ec1: deckClone.querySelector('.card-n1'),
             ec2: deckClone.querySelector('.card-n2'),
             ec3: deckClone.querySelector('.card-n3'),
             ec4: deckClone.querySelector('.card-n4')
           };
         }
         // Actualizar solo las que aún no se han encontrado (por si el DOM tarda)
         if (!window._ecCache.ec1) window._ecCache.ec1 = deckClone.querySelector('.card-n1');
         if (!window._ecCache.ec2) window._ecCache.ec2 = deckClone.querySelector('.card-n2');
         if (!window._ecCache.ec3) window._ecCache.ec3 = deckClone.querySelector('.card-n3');
         if (!window._ecCache.ec4) window._ecCache.ec4 = deckClone.querySelector('.card-n4');
         let ec1 = window._ecCache.ec1;
         let ec2 = window._ecCache.ec2;
         let ec3 = window._ecCache.ec3;
         let ec4 = window._ecCache.ec4;
     // Contenedor dedicado para las cartas - identico a #card-table
     if (!window._endCardTable) {
       var ect = document.createElement('div');
       ect.id = 'end-card-table';
       ect.style.cssText = 'position:fixed;inset:0;z-index:10000001;pointer-events:none;perspective:1200px;';
       document.body.appendChild(ect);
       window._endCardTable = ect;
     }
     var endCardTable = window._endCardTable;
         let ec1_peek = mapRange(localP, 2.5, 3.0, 0, 1);
         let ec2_peek = mapRange(localP, 4.22, 4.72, 0, 1);
         let ec3_peek = mapRange(localP, 6.02, 6.52, 0, 1);
         let ec4_peek = mapRange(localP, 7.82, 8.32, 0, 1);

         if (localP >= 2.2) {
           // CARTA 1
           if (ec1) {
             if (ec1_peek === 0) {
               if (ec1.dataset.endState !== 'deck-rest') {
                 ec1.dataset.endState = 'deck-rest';
                  ec1.style.opacity='1';
                 const ei1 = deckClone.querySelector('.interior-cards');
                 if (ei1 && ec1.parentNode !== ei1) ei1.insertBefore(ec1, ei1.firstChild);
                 ec1.style.position=''; ec1.style.left=''; ec1.style.top=''; ec1.style.margin='';
                 ec1.classList.remove('card-on-table','card-peeking'); ec1.classList.add('card-in-deck');
                 ec1.style.transition='none';
                 ec1.style.clipPath='inset(0 0 0 10px round 16px)';
               }
               const popY1 = -60 * eOpen; ec1.style.transform='translate(-50%, calc(-50% + '+popY1+'px)) translateZ(40px) rotate(-90deg) scale(0.81)';
             } else if (ec1_peek > 0 && localP <= 3.0) {
               ec1.style.opacity='1';ec1.dataset.endState='extracting';
               const ei1b=deckClone.querySelector('.interior-cards');
               if(ei1b&&ec1.parentNode!==ei1b){ei1b.insertBefore(ec1,ei1b.firstChild);ec1.style.position='';ec1.style.left='';ec1.style.top='';ec1.style.margin='';}
               ec1.classList.add('card-peeking'); ec1.classList.remove('card-on-table','card-in-deck');
               ec1.style.transition='none';
               const ey1=-35-295*ec1_peek;
               ec1.style.transform='translate(-50%, calc(-50% + '+ey1+'px)) translateZ(40px) rotate(-90deg) scale(0.9)';
               ec1.style.clipPath=ey1>5?'inset(0 0 0 10px round 16px)':'';
             } else {
               ec1.style.opacity='1';ec1.dataset.endState='table';
               if(ec1.parentNode!==oryzoSec){
                  const _dcr1=deckClone.getBoundingClientRect();
                  ec1.dataset.boxLeftEnd=(_dcr1.left+_dcr1.width/2).toString();
                  ec1.dataset.boxTopEnd=(_dcr1.top+_dcr1.height/2-330).toString();
                  oryzoSec.appendChild(ec1);ec1.classList.remove('card-in-deck','card-peeking');ec1.classList.add('card-on-table');ec1.style.position='fixed';ec1.style.clipPath='';ec1.style.transition='none';
               }
               const sX1=parseFloat(ec1.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY1=parseFloat(ec1.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD1=window.innerWidth>768,zS1=iD1?1.1:0.97,zX1=window.innerWidth/2,zY1=window.innerHeight/2-(iD1?100:150);
               let mi1=0,mo1=0;
               if(localP<=3.4)mi1=mapRange(localP,3.0,3.4,0,0.8);
               else if(localP<=3.8)mi1=mapRange(localP,3.4,3.8,0.8,1.0);
               else if(localP<=4.3){mi1=1.0;mo1=0;}
               else{mi1=1.0;mo1=mapRange(localP,4.3,4.9,0,1);}
               let rp1=0,hp1=0;
               if(localP>3.8&&localP<=4.3)hp1=mapRange(localP,3.8,4.3,0,1);else if(localP>4.3)hp1=1.0;
               if(localP<=3.3)rp1=mapRange(localP,3.0,3.3,0,0.85);
               else if(localP<=3.5)rp1=mapRange(localP,3.3,3.5,0.85,0.95);
               else if(localP<=3.8)rp1=mapRange(localP,3.5,3.8,0.95,1.0);
               else if(localP<=4.9)rp1=mapRange(localP,3.8,4.9,1.0,0.95);
               else rp1=0.95;
               let rz1=-90+(90*rp1),ry1=335+(25*rp1),fp1=mapRange(localP,3.5,4.1,0,1),rx1=fp1*180;
               let cx1,cy1,cs1,sha1;
               if(mo1===0){cx1=sX1+(zX1-sX1)*mi1;cy1=sY1+(zY1-sY1)*mi1+(60*hp1);cs1=0.9+(zS1-0.9)*mi1;sha1=0.16+(0.4-0.16)*mi1;}
               else{cx1=zX1-(window.innerWidth*1.5)*mo1;cy1=zY1+60+(window.innerHeight*1.5)*mo1;cs1=zS1;sha1=0.4-(0.4-0.16)*mo1;rx1+=120*mo1;ry1+=90*mo1;rz1-=60*mo1;}
               if(localP>3.0){ec1.style.transition='none';ec1.style.left=cx1+'px';ec1.style.top=cy1+'px';ec1.style.transform='translate(-50%,-50%) rotateY('+ry1+'deg) rotateX('+rx1+'deg) rotateZ('+rz1+'deg) scale('+cs1+')';ec1.style.boxShadow='0 8px 16px rgba(0,0,0,'+(sha1*0.75)+'),0 40px 80px rgba(0,0,0,'+sha1+')';const ef1=ec1.querySelector('.card-front'),eb1=ec1.querySelector('.card-back');if(ef1&&eb1){if(rx1>90){ef1.style.display='none';eb1.style.display='flex';}else{ef1.style.display='flex';eb1.style.display='none';}}ec1.style.zIndex='10020';}
             }
           }
            // CARTA 2
           const efc2=deckClone.querySelector('.interior-cards .interior-card:nth-child(1)');
           if(ec2){
             if(ec2_peek===0){if(efc2)efc2.style.opacity='0';if(ec2.dataset.endState!=='deck-rest'){ec2.dataset.endState='deck-rest';ec2.style.opacity='1';const ei2=deckClone.querySelector('.interior-cards');if(ei2&&ec2.parentNode!==ei2)ei2.insertBefore(ec2,ei2.firstChild);ec2.style.position='';ec2.style.left='';ec2.style.top='';ec2.style.margin='';ec2.classList.remove('card-on-table','card-peeking');ec2.classList.add('card-in-deck');ec2.style.transition='none';ec2.style.clipPath='inset(0 0 0 10px round 16px)';}const popY2 = -50 * eOpen; ec2.style.transform='translate(-50%, calc(-50% + '+popY2+'px)) translateZ(46px) rotate(-90deg) scale(0.81)';}
             else if(ec2_peek>0&&localP<=4.72){if(efc2)efc2.style.opacity='0';ec2.style.opacity='1';ec2.dataset.endState='extracting';const ei2b=deckClone.querySelector('.interior-cards');if(ei2b&&ec2.parentNode!==ei2b){ei2b.insertBefore(ec2,ei2b.firstChild);ec2.style.position='';ec2.style.left='';ec2.style.top='';ec2.style.margin='';}ec2.classList.add('card-peeking');ec2.classList.remove('card-on-table','card-in-deck');ec2.style.transition='none';const ey2=-35-295*ec2_peek;ec2.style.transform='translate(-50%, calc(-50% + '+ey2+'px)) translateZ(46px) rotate(-90deg) scale(0.9)';ec2.style.clipPath=ey2>5?'inset(0 0 0 10px round 16px)':'';}
             else{if(efc2)efc2.style.opacity='0';ec2.style.opacity='1';ec2.dataset.endState='table';if(ec2.parentNode!==oryzoSec){const _dcr2=deckClone.getBoundingClientRect();ec2.dataset.boxLeftEnd=(_dcr2.left+_dcr2.width/2).toString();ec2.dataset.boxTopEnd=(_dcr2.top+_dcr2.height/2-330).toString();oryzoSec.appendChild(ec2);ec2.classList.remove('card-in-deck','card-peeking');ec2.classList.add('card-on-table');ec2.style.position='fixed';ec2.style.clipPath='';ec2.style.transition='none';}
               const sX2=parseFloat(ec2.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY2=parseFloat(ec2.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD2=window.innerWidth>768,zS2=iD2?1.1:0.97,zX2=window.innerWidth/2,zY2=window.innerHeight/2-(iD2?100:150);
               let mi2=0,mo2=0;if(localP<=5.12)mi2=mapRange(localP,4.72,5.12,0,0.8);else if(localP<=5.52)mi2=mapRange(localP,5.12,5.52,0.8,1.0);else if(localP<=6.02){mi2=1.0;mo2=0;}else{mi2=1.0;mo2=mapRange(localP,6.02,6.62,0,1);}
               let rp2=0,hp2=0;if(localP>5.52&&localP<=6.02)hp2=mapRange(localP,5.52,6.02,0,1);else if(localP>6.02)hp2=1.0;if(localP<=5.02)rp2=mapRange(localP,4.72,5.02,0,0.85);else if(localP<=5.22)rp2=mapRange(localP,5.02,5.22,0.85,0.95);else if(localP<=5.52)rp2=mapRange(localP,5.22,5.52,0.95,1.0);else if(localP<=6.62)rp2=mapRange(localP,5.52,6.62,1.0,0.95);else rp2=0.95;
               let rz2=-90+(90*rp2),ry2=335+(25*rp2),fp2=mapRange(localP,5.22,5.82,0,1),rx2=fp2*180;
               let cx2,cy2,cs2,sha2;if(mo2===0){cx2=sX2+(zX2-sX2)*mi2;cy2=sY2+(zY2-sY2)*mi2+(60*hp2);cs2=0.9+(zS2-0.9)*mi2;sha2=0.16+(0.4-0.16)*mi2;}else{cx2=zX2+(window.innerWidth*1.5)*mo2;cy2=zY2+60+(window.innerHeight*1.5)*mo2;cs2=zS2;sha2=0.4-(0.4-0.16)*mo2;rx2+=120*mo2;ry2-=90*mo2;rz2+=60*mo2;}
               if(localP>4.72){ec2.style.transition='none';ec2.style.left=cx2+'px';ec2.style.top=cy2+'px';ec2.style.transform='translate(-50%,-50%) rotateY('+ry2+'deg) rotateX('+rx2+'deg) rotateZ('+rz2+'deg) scale('+cs2+')';ec2.style.boxShadow='0 8px 16px rgba(0,0,0,'+(sha2*0.75)+'),0 40px 80px rgba(0,0,0,'+sha2+')';const ef2=ec2.querySelector('.card-front'),eb2=ec2.querySelector('.card-back');if(ef2&&eb2){if(rx2>90){ef2.style.display='none';eb2.style.display='flex';}else{ef2.style.display='flex';eb2.style.display='none';}}ec2.style.zIndex='10019';}
             }
           }
           // CARTA 3
           const efc3=deckClone.querySelector('.interior-cards .interior-card:nth-child(2)');
           if(ec3){
             if(ec3_peek===0){if(efc3)efc3.style.opacity='0';if(ec3.dataset.endState!=='deck-rest'){ec3.dataset.endState='deck-rest';ec3.style.opacity='1';const ei3=deckClone.querySelector('.interior-cards');if(ei3&&ec3.parentNode!==ei3)ei3.insertBefore(ec3,ei3.firstChild);ec3.style.position='';ec3.style.left='';ec3.style.top='';ec3.style.margin='';ec3.classList.remove('card-on-table','card-peeking');ec3.classList.add('card-in-deck');ec3.style.transition='none';const popY3 = -40 * eOpen; ec3.style.transform='translate(-50%, calc(-50% + '+popY3+'px)) translateZ(52px) rotate(-90deg) scale(0.81)';ec3.style.clipPath='inset(0 0 0 10px round 16px)';}const popY3 = -40 * eOpen; ec3.style.transform='translate(-50%, calc(-50% + '+popY3+'px)) translateZ(52px) rotate(-90deg) scale(0.81)';}
             else if(ec3_peek>0&&localP<=6.52){if(efc3)efc3.style.opacity='0';ec3.style.opacity='1';ec3.dataset.endState='extracting';const ei3b=deckClone.querySelector('.interior-cards');if(ei3b&&ec3.parentNode!==ei3b){ei3b.insertBefore(ec3,ei3b.firstChild);ec3.style.position='';ec3.style.left='';ec3.style.top='';ec3.style.margin='';}ec3.classList.add('card-peeking');ec3.classList.remove('card-on-table','card-in-deck');ec3.style.transition='none';const ey3=-35-295*ec3_peek;ec3.style.transform='translate(-50%, calc(-50% + '+ey3+'px)) translateZ(52px) rotate(-90deg) scale(0.9)';ec3.style.clipPath=ey3>5?'inset(0 0 0 10px round 16px)':'';}
             else{if(efc3)efc3.style.opacity='0';ec3.style.opacity='1';ec3.dataset.endState='table';if(ec3.parentNode!==oryzoSec){const _dcr3=deckClone.getBoundingClientRect();ec3.dataset.boxLeftEnd=(_dcr3.left+_dcr3.width/2).toString();ec3.dataset.boxTopEnd=(_dcr3.top+_dcr3.height/2-330).toString();oryzoSec.appendChild(ec3);ec3.classList.remove('card-in-deck','card-peeking');ec3.classList.add('card-on-table');ec3.style.position='fixed';ec3.style.clipPath='';ec3.style.transition='none';}
               const sX3=parseFloat(ec3.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY3=parseFloat(ec3.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD3=window.innerWidth>768,zS3=iD3?1.1:0.97,zX3=window.innerWidth/2,zY3=window.innerHeight/2-(iD3?100:150);
               let mi3=0,mo3=0;if(localP<=6.92)mi3=mapRange(localP,6.52,6.92,0,0.8);else if(localP<=7.32)mi3=mapRange(localP,6.92,7.32,0.8,1.0);else if(localP<=7.82){mi3=1.0;mo3=0;}else{mi3=1.0;mo3=mapRange(localP,7.82,8.42,0,1);}
               let rp3=0,hp3=0;if(localP>7.32&&localP<=7.82)hp3=mapRange(localP,7.32,7.82,0,1);else if(localP>7.82)hp3=1.0;if(localP<=6.82)rp3=mapRange(localP,6.52,6.82,0,0.85);else if(localP<=7.02)rp3=mapRange(localP,6.82,7.02,0.85,0.95);else if(localP<=7.32)rp3=mapRange(localP,7.02,7.32,0.95,1.0);else if(localP<=8.42)rp3=mapRange(localP,7.32,8.42,1.0,0.95);else rp3=0.95;
               let rz3=-90+(90*rp3),ry3=335+(25*rp3),fp3=mapRange(localP,7.02,7.62,0,1),rx3=fp3*180;
               let cx3,cy3,cs3,sha3;if(mo3===0){cx3=sX3+(zX3-sX3)*mi3;cy3=sY3+(zY3-sY3)*mi3+(60*hp3);cs3=0.9+(zS3-0.9)*mi3;sha3=0.16+(0.4-0.16)*mi3;}else{cx3=zX3;cy3=zY3+60+(window.innerHeight*1.5)*mo3;cs3=zS3;sha3=0.4-(0.4-0.16)*mo3;rx3+=120*mo3;ry3-=90*mo3;rz3+=60*mo3;}
               if(localP>6.52){ec3.style.transition='none';ec3.style.left=cx3+'px';ec3.style.top=cy3+'px';ec3.style.transform='translate(-50%,-50%) rotateY('+ry3+'deg) rotateX('+rx3+'deg) rotateZ('+rz3+'deg) scale('+cs3+')';ec3.style.boxShadow='0 8px 16px rgba(0,0,0,'+(sha3*0.75)+'),0 40px 80px rgba(0,0,0,'+sha3+')';const ef3=ec3.querySelector('.card-front'),eb3=ec3.querySelector('.card-back');if(ef3&&eb3){if(rx3>90){ef3.style.display='none';eb3.style.display='flex';}else{ef3.style.display='flex';eb3.style.display='none';}}ec3.style.zIndex='10018';}
             }
           }
           // CARTA 4
           const efc4=deckClone.querySelector('.interior-cards .interior-card:nth-child(3)');
           if(ec4){
             if(ec4_peek===0){if(efc4)efc4.style.opacity='0';if(ec4.dataset.endState!=='deck-rest'){ec4.dataset.endState='deck-rest';ec4.style.opacity='1';const ei4=deckClone.querySelector('.interior-cards');if(ei4&&ec4.parentNode!==ei4)ei4.insertBefore(ec4,ei4.firstChild);ec4.style.position='';ec4.style.left='';ec4.style.top='';ec4.style.margin='';ec4.classList.remove('card-on-table','card-peeking');ec4.classList.add('card-in-deck');ec4.style.transition='none';const popY4 = -30 * eOpen; ec4.style.transform='translate(-50%, calc(-50% + '+popY4+'px)) translateZ(58px) rotate(-90deg) scale(0.81)';ec4.style.clipPath='inset(0 0 0 10px round 16px)';}const popY4 = -30 * eOpen; ec4.style.transform='translate(-50%, calc(-50% + '+popY4+'px)) translateZ(58px) rotate(-90deg) scale(0.81)';}
             else if(ec4_peek>0&&localP<=8.32){if(efc4)efc4.style.opacity='0';ec4.style.opacity='1';ec4.dataset.endState='extracting';const ei4b=deckClone.querySelector('.interior-cards');if(ei4b&&ec4.parentNode!==ei4b){ei4b.insertBefore(ec4,ei4b.firstChild);ec4.style.position='';ec4.style.left='';ec4.style.top='';ec4.style.margin='';}ec4.classList.add('card-peeking');ec4.classList.remove('card-on-table','card-in-deck');ec4.style.transition='none';const ey4=-35-295*ec4_peek;ec4.style.transform='translate(-50%, calc(-50% + '+ey4+'px)) translateZ(58px) rotate(-90deg) scale(0.9)';ec4.style.clipPath=ey4>5?'inset(0 0 0 10px round 16px)':'';}
             else{if(efc4)efc4.style.opacity='0';ec4.style.opacity='1';ec4.dataset.endState='table';if(ec4.parentNode!==oryzoSec){const _dcr4=deckClone.getBoundingClientRect();ec4.dataset.boxLeftEnd=(_dcr4.left+_dcr4.width/2).toString();ec4.dataset.boxTopEnd=(_dcr4.top+_dcr4.height/2-330).toString();oryzoSec.appendChild(ec4);ec4.classList.remove('card-in-deck','card-peeking');ec4.classList.add('card-on-table');ec4.style.position='fixed';ec4.style.clipPath='';ec4.style.transition='none';}
               const sX4=parseFloat(ec4.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY4=parseFloat(ec4.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD4=window.innerWidth>768,zS4=iD4?1.1:0.97,zX4=window.innerWidth/2,zY4=window.innerHeight/2-(iD4?100:150);
               let mi4=0,mo4=0;if(localP<=8.72)mi4=mapRange(localP,8.32,8.72,0,0.8);else if(localP<=9.12)mi4=mapRange(localP,8.72,9.12,0.8,1.0);else if(localP<=9.62){mi4=1.0;mo4=0;}else{mi4=1.0;mo4=mapRange(localP,9.62,10.22,0,1);}
               let rp4=0,hp4=0;if(localP>9.12&&localP<=9.62)hp4=mapRange(localP,9.12,9.62,0,1);else if(localP>9.62)hp4=1.0;if(localP<=8.62)rp4=mapRange(localP,8.32,8.62,0,0.85);else if(localP<=8.82)rp4=mapRange(localP,8.62,8.82,0.85,0.95);else if(localP<=9.12)rp4=mapRange(localP,8.82,9.12,0.95,1.0);else if(localP<=10.22)rp4=mapRange(localP,9.12,10.22,1.0,0.95);else rp4=0.95;
               let rz4=-90+(90*rp4),ry4=335+(25*rp4),fp4=mapRange(localP,8.82,9.42,0,1),rx4=fp4*180;
               let cx4,cy4,cs4,sha4;if(mo4===0){cx4=sX4+(zX4-sX4)*mi4;cy4=sY4+(zY4-sY4)*mi4+(60*hp4);cs4=0.9+(zS4-0.9)*mi4;sha4=0.16+(0.4-0.16)*mi4;}else{cx4=zX4;cy4=zY4+60-(window.innerHeight*1.5)*mo4;cs4=zS4;sha4=0.4-(0.4-0.16)*mo4;rx4+=120*mo4;ry4-=90*mo4;rz4+=60*mo4;}
               if(localP>8.32){ec4.style.transition='none';ec4.style.left=cx4+'px';ec4.style.top=cy4+'px';ec4.style.transform='translate(-50%,-50%) rotateY('+ry4+'deg) rotateX('+rx4+'deg) rotateZ('+rz4+'deg) scale('+cs4+')';ec4.style.boxShadow='0 8px 16px rgba(0,0,0,'+(sha4*0.75)+'),0 40px 80px rgba(0,0,0,'+sha4+')';const ef4=ec4.querySelector('.card-front'),eb4=ec4.querySelector('.card-back');if(ef4&&eb4){if(rx4>90){ef4.style.display='none';eb4.style.display='flex';}else{ef4.style.display='flex';eb4.style.display='none';}}ec4.style.zIndex='10017';}
             }
           }
           // REVIEWS FINALES â€â€ slide-up identico a testimonios
           var eRev1=document.getElementById('end-review-panel-1');
           var eRev2=document.getElementById('end-review-panel-2');
           var eRev3=document.getElementById('end-review-panel-3');
           var eRev4=document.getElementById('end-review-panel-4');
           if(eRev1){if(localP>3.0&&localP<4.6){var eRp1=mapRange(localP,3.0,4.6,0,1);eRev1.style.transform='translateY('+mapRange(localP,3.0,4.6,window.innerHeight*1.5,-window.innerHeight*1.5)+'px)';eRev1.style.opacity=eRp1>0.85?mapRange(eRp1,0.85,1.0,1,0):1; updateReviewPanelInternals(eRev1, eRp1);}else eRev1.style.opacity='0';}
           if(eRev2){if(localP>4.72&&localP<6.32){var eRp2=mapRange(localP,4.72,6.32,0,1);eRev2.style.transform='translateY('+mapRange(localP,4.72,6.32,window.innerHeight*1.5,-window.innerHeight*1.5)+'px)';eRev2.style.opacity=eRp2>0.85?mapRange(eRp2,0.85,1.0,1,0):1; updateReviewPanelInternals(eRev2, eRp2);}else eRev2.style.opacity='0';}
           if(eRev3){if(localP>6.52&&localP<8.12){var eRp3=mapRange(localP,6.52,8.12,0,1);eRev3.style.transform='translateY('+mapRange(localP,6.52,8.12,window.innerHeight*1.5,-window.innerHeight*1.5)+'px)';eRev3.style.opacity=eRp3>0.85?mapRange(eRp3,0.85,1.0,1,0):1; updateReviewPanelInternals(eRev3, eRp3);}else eRev3.style.opacity='0';}
           if(eRev4){if(localP>8.32&&localP<9.92){var eRp4=mapRange(localP,8.32,9.92,0,1);eRev4.style.transform='translateY('+mapRange(localP,8.32,9.92,window.innerHeight*1.5,-window.innerHeight*1.5)+'px)';eRev4.style.opacity=eRp4>0.85?mapRange(eRp4,0.85,1.0,1,0):1; updateReviewPanelInternals(eRev4, eRp4);}else eRev4.style.opacity='0';}



            // -- IMG STRIP CAROUSEL -- cortina per-slide estilo Oryzo
            (function(){
              var isCont    = document.getElementById('img-strip-container');
              var isWrapper = document.getElementById('img-strip-wrapper');
              var isTrack   = document.getElementById('img-strip-track');
              if (!isCont || !isWrapper || !isTrack) return;
              var IS_ENTER  = 9.7;
              var IS_CENTER = 10.48; // 3x mas lento (duración 0.78 localP)
              var IS_END    = 17.5;  // 6 slides: 5a imagen centrada con margen final
              var slides = isTrack.children;
              isWrapper.style.clipPath = 'none';
              isWrapper.style.transform = 'none';
              if (localP >= IS_ENTER) {
                isCont.style.opacity = '1';
                if (localP <= IS_CENTER) {
                  // FASE 1: todas las slides revelan a la vez con cortina izq->der
                  var sep = mapRange(localP, IS_ENTER, IS_CENTER, 0, 1);
                  sep = Math.max(0, Math.min(1, sep));
                  sep = sep < 0.5 ? 2*sep*sep : 1 - Math.pow(-2*sep+2,2)/2;
                  var clipR = (1 - sep) * 100;
                  for (var s = 0; s < slides.length; s++) {
                    slides[s].style.clipPath = 'inset(0 ' + clipR + '% 0 0)';
                  }
                  isTrack.style.transform = 'translateX(0.5cm)';
                  // En fase de entrada, resetear parallax a base
                  var _ptTopF1 = document.getElementById('parallax-text-top');
                  var _ptBotF1 = document.getElementById('parallax-text-bot');
                  var _ptxBase = 'translateX(calc(-50% + 0.55cm))';
                  if (_ptTopF1) _ptTopF1.style.transform = _ptxBase;
                  if (_ptBotF1) _ptBotF1.style.transform = _ptxBase;
                } else {
                  // FASE 2: clip-path individual por posicion en el viewport
                  var ssp = mapRange(localP, IS_CENTER, IS_END, 0, 1);
                  ssp = Math.max(0, Math.min(1, ssp));
                  ssp = ssp < 0.5 ? 2*ssp*ssp : 1 - Math.pow(-2*ssp+2,2)/2;
                  // calc: ancho total track 300vw + 2.5cm gap. Meta final para alinear 6a imagen = -200vw - 3cm
                  isTrack.style.transform = 'translateX(calc(0.5cm - ' + (ssp * 175) + 'vw - ' + (ssp * 3.5) + 'cm))';
                  // Parallax: textos se mueven al 85% de la velocidad del track (15% de contrarretraso)
                  var _pxVw = (ssp * 200 * 0.075).toFixed(2);
                  var _pxCm = (ssp * 3.5  * 0.075).toFixed(3);
                  var _ptx  = 'translateX(calc(-50% + 0.55cm + ' + _pxVw + 'vw + ' + _pxCm + 'cm))';
                  var _ptTop = document.getElementById('parallax-text-top');
                  var _ptBot = document.getElementById('parallax-text-bot');
                  if (_ptTop) _ptTop.style.transform = _ptx;
                  if (_ptBot) _ptBot.style.transform = _ptx;
                  var vpW = window.innerWidth;
                  for (var s2 = 0; s2 < slides.length; s2++) {
                    var rect = slides[s2].getBoundingClientRect();
                    if (rect.left >= vpW) {
                      slides[s2].style.clipPath = 'inset(0 100% 0 0)';
                    } else if (rect.left > 0) {
                      var visF = Math.max(0, Math.min(1, (vpW - rect.left) / rect.width));
                      slides[s2].style.clipPath = 'inset(0 ' + ((1 - visF) * 100) + '% 0 0)';
                    } else {
                      slides[s2].style.clipPath = 'none';
                    }
                    // Pan imagen slide 2 (pareja sofa) según posición en viewport
                    if (s2 === 2) {
                      var _s2Pan = document.getElementById('slide2-pan-img');
                      if (_s2Pan) {
                        var _panFull = vpW - rect.width; // rect.left donde el slide esta 100% visible
                        var _pf2 = Math.max(0, Math.min(1, (_panFull - rect.left) / (_panFull + rect.width)));
                        _s2Pan.style.transform = 'translateX(' + (-_pf2 * 50).toFixed(2) + '%)';
                        // Subrayado animado en 'compromiso' sincronizado con scroll
                        var _ulEl = document.getElementById('compromiso-underline');
                        if (_ulEl) {
                          var _ulP = Math.max(0, Math.min(1, _pf2 * 2));
                          _ulEl.style.transform = 'scaleY(' + _ulP.toFixed(3) + ')';
                        }
                      }
                    }
                    // Efecto iris en slide 3 (paseo) - crece solo cuando slide esta 100% visible
                    if (s2 === 3) {
                      var _s3 = document.getElementById('slide3-iris-img');
                      if (_s3) {
                        var _irisFullStart = vpW - rect.width;
                        var _maxR3 = rect.width * 1.4;
                        // Fase entrada: iris 5px -> 60px mientras el slide entra (clip reveal)
                        var _entryP = Math.max(0, Math.min(1, (vpW - rect.left) / rect.width));
                        var _entryEase = _entryP * _entryP * (3 - 2 * _entryP);
                        var _rEntry = 5 + _entryEase * 55;
                        // Fase pan: iris 60px -> maxR mientras el slide se desplaza
                        var _pf3 = Math.max(0, Math.min(1, (_irisFullStart - rect.left) / (_irisFullStart + rect.width)));
                        var _ease3 = _pf3 * _pf3 * (3 - 2 * _pf3);
                        var _r3 = (rect.left > _irisFullStart) ? _rEntry : (60 + _ease3 * (_maxR3 - 60));
                        _s3.style.clipPath = 'circle(' + _r3.toFixed(1) + 'px at 45% 64%)';
                        // Parallax alternado en el texto del slide3
                        var _off3 = (_pf3 * 3).toFixed(2);
                        var _c1 = document.getElementById('slide3-copy-1'); if (_c1) _c1.style.transform = 'translateX(-' + _off3 + 'vw)';
                        var _c2 = document.getElementById('slide3-copy-2'); if (_c2) _c2.style.transform = 'translateX(-' + _off3 + 'vw)';
                        var _c3 = document.getElementById('slide3-copy-3'); if (_c3) _c3.style.transform = 'translateX(' + _off3 + 'vw)';

                      }
                    }
                    // Efecto noooooche en slide 4 (durmiendo)
                    if (s2 === 4) {
                      var _ifsS4 = vpW - rect.width;
                      var _pfS4 = Math.max(0, Math.min(1, (_ifsS4 - rect.left) / (_ifsS4 + rect.width)));
                      var _nochePara = document.getElementById('slide4-noche');
                      if (_nochePara) {
                        var _oCount = Math.min(8, Math.floor(_pfS4 * 9) + 1);
                        _nochePara.innerHTML = 'o toda la n' + 'o'.repeat(_oCount) + 'che';
                      }
                    }
                  }
                }
                  // Ã¢â€€Ã¢â€€ EXIT PHASE: img-strip sube por arriba, logo OLT sube desde abajo Ã¢â€€Ã¢â€€
                  var IS_EXIT_END = 20.0;
                  var IS_P1_FADE_IN_END = 20.5;
                  var IS_P1_LIGHT_END   = 21.5;
                  var IS_P1_COUNT_END   = 22.5;
                  var IS_P1_STRIKE_END  = 23.5;
                  var IS_P1_REVERSE_END = 25.0; 
                  var IS_P2_EXPAND_END  = 26.0;
                  var IS_P2_GUARANTEE_END = 27.5; 
                  var IS_P2_END         = 29.0;
                  var IS_P3_FADE_IN_END = 30.0;
                  var IS_FINAL_END      = 34.0;
                  var IS_FLASH_START    = 28.0;
                  var IS_FLASH_PEAK     = 28.5;
                  var IS_FLASH_END      = 30.0;
                  var IS_TABLE_ZOOM_END = 32.9;
                  
                  var _exitP  = Math.max(0, Math.min(1, (localP - IS_END) / (IS_EXIT_END - IS_END)));
                  var _exitEA = _exitP < 0.5 ? 2*_exitP*_exitP : 1 - Math.pow(-2*_exitP+2,2)/2;
                  

                  
                  // Variables de fase
                  var _p1FadeInP = Math.max(0, Math.min(1, (localP - IS_EXIT_END) / (IS_P1_FADE_IN_END - IS_EXIT_END)));
                  var _p1LightP  = Math.max(0, Math.min(1, (localP - IS_P1_FADE_IN_END) / (IS_P1_LIGHT_END - IS_P1_FADE_IN_END)));
                  var _p1CountP  = Math.max(0, Math.min(1, (localP - IS_P1_LIGHT_END) / (IS_P1_COUNT_END - IS_P1_LIGHT_END)));
                  var _p1StrikeP = Math.max(0, Math.min(1, (localP - IS_P1_COUNT_END) / (IS_P1_STRIKE_END - IS_P1_COUNT_END)));
                  var _p1ReverseP = Math.max(0, Math.min(1, (localP - IS_P1_STRIKE_END) / (IS_P1_REVERSE_END - IS_P1_STRIKE_END)));
                  var _p2ExpandP = Math.max(0, Math.min(1, (localP - IS_P1_REVERSE_END) / (IS_P2_EXPAND_END - IS_P1_REVERSE_END)));
                  var _p2GuaranteeP = Math.max(0, Math.min(1, (localP - IS_P2_EXPAND_END) / (IS_P2_GUARANTEE_END - IS_P2_EXPAND_END)));
                  var _p2FadeOutP = Math.max(0, Math.min(1, (localP - IS_P2_END) / (IS_P3_FADE_IN_END - IS_P2_END)));
                  
                  var _p3FadeInP = Math.max(0, Math.min(1, (localP - IS_P2_END) / (IS_P3_FADE_IN_END - IS_P2_END)));
                  var _finalP    = Math.max(0, Math.min(1, (localP - IS_P3_FADE_IN_END) / (IS_FINAL_END - IS_P3_FADE_IN_END)));

                  // El carrusel sigue subiendo sin limite
                  var _carUpP = Math.max(0, (localP - IS_END) / (IS_EXIT_END - IS_END));
                  isCont.style.transform = 'translateY(' + (-_carUpP * 100).toFixed(2) + 'vh)';
                  
                  // Fade out del scroll indicator: desaparece justo al final del scroll
                  var _scrollInd = document.querySelector('.scroll-indicator');
                  // if (_scrollInd) _scrollInd.style.opacity = Math.max(0, 1 - _finalP * 1.15).toFixed(3);
                  
                  // Fase de entrada de Logo y CTA movida al final de la función para unificar la lógica

                  
                  // ----- PHASE 1 & 2: Dynamic -----
                  var _oltPhaseDyn = document.getElementById('olt-phase-dynamic');
                  if (_oltPhaseDyn) {
                      var blurAmount = Math.sin(_p3FadeInP * Math.PI) * 20;
                      var opDyn = _p1FadeInP;
                      if (localP >= 28.5) opDyn = 0; // Hide at flash peak
                      _oltPhaseDyn.style.opacity = opDyn.toFixed(2);
                      _oltPhaseDyn.style.filter = 'blur(' + blurAmount.toFixed(1) + 'px)';
                      
                      // Ajustar la posición vertical al aparecer la garantía
                      var dynOffsetY = _p1ReverseP * 40; // Sube hasta 40px progresivamente
                      _oltPhaseDyn.style.transform = 'translate(-50%, calc(-50% - ' + dynOffsetY + 'px))';
                      
                      // Iluminación de la pregunta
                      var questionP = document.getElementById('p1-question');
                      if (questionP) {
                          // El usuario pidió que no desaparezca la pregunta, por lo que su opacidad principal será 1
                          questionP.style.opacity = '1';

                          var chars = questionP.querySelectorAll('.char');
                          if (chars.length > 0) {
                              var blurLen = 15;
                              var fillIndex = Math.floor(_p1LightP * (chars.length + blurLen));
                              chars.forEach(function(char, idx) {
                                  var dist = fillIndex - idx;
                                  if (dist < 0) {
                                      char.style.opacity = '0.15';
                                      char.style.color = '';
                                      char.style.textShadow = 'none';
                                  } else if (dist < blurLen) {
                                      var ratio = dist / blurLen;
                                      var opC = 0.15 + 0.85 * Math.pow(ratio, 0.8);
                                      char.style.opacity = opC.toFixed(2);
                                      var r = Math.round(204 + 51 * ratio);
                                      var g = 255;
                                      var b = Math.round(255 * ratio);
                                      char.style.color = 'rgb(' + r + ',' + g + ',' + b + ')';
                                      char.style.textShadow = 'none';
                                  } else {
                                      char.style.opacity = '1';
                                      char.style.color = '#ffffff';
                                      char.style.textShadow = 'none';
                                  }
                              });
                          }
                      }
                      
                      // Contador y Regresión
                      var dynRow = document.getElementById('dynamic-pricing-row');
                      var counterContainer = document.getElementById('p1-counter-container');
                      var counterSpan = document.getElementById('p1-counter');
                      var strikeLine = document.getElementById('p1-strikethrough');
                      var dpLeft = document.getElementById('dp-left');
                      var dpRight = document.getElementById('dp-right');

                      if (dynRow && counterSpan && strikeLine && counterContainer) {
                          // El precio se queda fijo en su línea
                          dynRow.style.transform = 'translate(-50%, 30px)';
                          
                          // Opacity is tied to _p1FadeInP
                          var counterOp = Math.min(1, _p1FadeInP * 2.0);
                          if (localP >= 28.5) counterOp = 0; // Hide at flash peak
                          counterContainer.style.opacity = counterOp.toFixed(2);
                          dynRow.style.opacity = counterOp.toFixed(2);
                          
                          // Counter Logic
                          var countSteps = [0, 1, 10, 100, 10000, 100000, 1000000];
                          if (_p1CountP < 1) {
                              var stepIdx = Math.min(countSteps.length - 1, Math.floor(_p1CountP * countSteps.length));
                              var countVal = countSteps[stepIdx];
                              counterSpan.innerText = '¿' + countVal.toLocaleString('es-ES') + '€?';
                              counterSpan.style.color = (_p1CountP === 0) ? 'rgba(255, 255, 255, 0.15)' : '#ffffff';
                              strikeLine.style.width = '0%';
                          } else if (_p1StrikeP < 1) {
                              counterSpan.innerText = '¿No está a la venta?';
                              counterSpan.style.color = '#ffffff';
                              strikeLine.style.width = '0%';
                          } else {
                              // Reverse phase
                              strikeLine.style.width = '0%';
                              if (_p1ReverseP < 0.5) {
                                  // 1.000.000 down to 10
                                  var revSteps = [1000000, 100000, 10000, 1000, 100, 10];
                                  var revP = _p1ReverseP * 2.0; // 0 to 1
                                  var stepIdx = Math.min(revSteps.length - 1, Math.floor(revP * revSteps.length));
                                  var countVal = revSteps[stepIdx];
                                  counterSpan.innerText = countVal.toLocaleString('es-ES') + '€';
                                  counterSpan.style.color = '#ffffff';
                              } else {
                                  // Enteros 9, 8 hasta precio final 7,99
                                  var intSteps = ['9', '8', '7,99'];
                                  var decP = (_p1ReverseP - 0.5) * 2.0; // 0 to 1
                                  var stepIdx = Math.min(intSteps.length - 1, Math.floor(decP * intSteps.length));
                                  var countVal = intSteps[stepIdx];
                                  counterSpan.innerText = countVal + '€';
                                  counterSpan.style.color = '#ffffff';
                              }
                          }
                          
                          // Expansión lateral (Centrado)
                          if (dpLeft && dpRight) {
                              var maxWLeft = 200; 
                              var maxWRight = 800; // Increased to ensure it fits the whole sentence
                              dpLeft.style.maxWidth = (_p1ReverseP * maxWLeft) + 'px';
                              dpLeft.style.opacity = _p1ReverseP.toFixed(2);
                              dpRight.style.maxWidth = (_p1ReverseP * maxWRight) + 'px';
                              dpRight.style.opacity = _p1ReverseP.toFixed(2);
                          }
                      }
                      
                      // Guarantee Phase
                      var guaranteeRow = document.getElementById('p2-guarantee');
                      if (guaranteeRow) {
                          guaranteeRow.style.opacity = _p1ReverseP.toFixed(2);
                          
                          var leafLeft = document.getElementById('leaf-left');
                          var leafRight = document.getElementById('leaf-right');
                          if (leafLeft && leafRight) {
                              var leafOp = 0.15 + 0.85 * _p1ReverseP;
                              leafLeft.style.opacity = leafOp.toFixed(2);
                              leafRight.style.opacity = leafOp.toFixed(2);
                          }
                      }
                  }
                  
                  // ----- PHASE 3: Reflexión Final -----
                  var _oltText = document.getElementById('olt-final-text');
                  if (_oltText) {
                    var blurAmountText = Math.sin(_p3FadeInP * Math.PI) * 20;
                    var _finalOp = _p3FadeInP > 0.5 ? 1 : 0;
                    var _eraseFP = Math.min(1, _finalP * 2);
                    if (_eraseFP >= 1) _finalOp = 0;
                    
                    if (_p3FadeInP > 0) {
                        _oltText.style.transform = 'translate(-50%, calc(-50% + 2cm))';
                    }
                    _oltText.style.opacity = _finalOp.toFixed(2);
                    _oltText.style.filter = 'blur(' + blurAmountText.toFixed(1) + 'px)';
                    
                    var charsF = _oltText.querySelectorAll('.char');
                    if (charsF.length > 0) {
                      var total = charsF.length;
                      var eraseHalf = (_eraseFP * total) / 2;
                      for (var k = 0; k < total; k++) {
                        if (_eraseFP >= 1 || k < eraseHalf || k >= total - eraseHalf) {
                          charsF[k].style.opacity = '0';
                        } else {
                          charsF[k].style.opacity = '1';
                        }
                      }
                    }
                  }
                  
                  // ----- PHASE 4: Fade out UI and Reveal 3D Table -----
                  
                  var START_3D_REVEAL = 28.5; // El peak del flash
                  var END_3D_REVEAL = 32.9;
                  
                  // Flash effects
                  var FLASH_START = 27.5;
                  var FLASH_PEAK = 28.5;
                  var FLASH_END = 29.5;
                  var flashOpacity = 0;
                  if (localP >= FLASH_START && localP <= FLASH_PEAK) {
                      flashOpacity = (localP - FLASH_START) / (FLASH_PEAK - FLASH_START);
                  } else if (localP > FLASH_PEAK && localP <= FLASH_END) {
                      flashOpacity = 1.0 - ((localP - FLASH_PEAK) / (FLASH_END - FLASH_PEAK));
                  }
                  
                  var tFlash = document.getElementById('transition-flash');
                  if (!tFlash) {
                      tFlash = document.createElement('div');
                      tFlash.id = 'transition-flash';
                      tFlash.style.position = 'fixed';
                      tFlash.style.top = '0';
                      tFlash.style.left = '0';
                      tFlash.style.width = '100vw';
                      tFlash.style.height = '100vh';
                      tFlash.style.background = '#ffffff';
                      tFlash.style.zIndex = '5'; // Above phase-dynamic (1), below logo/cta (10)
                      tFlash.style.pointerEvents = 'none';
                      tFlash.style.opacity = '0';
                      var logoReveal = document.getElementById('olt-logo-reveal');
                      if (logoReveal) {
                          logoReveal.appendChild(tFlash);
                      } else {
                          document.body.appendChild(tFlash);
                      }
                  }
                  tFlash.style.opacity = flashOpacity.toFixed(3);
                  
                  var fadeProg = 0;
                  if (localP > START_3D_REVEAL) {
                      // Instant cut while hidden by flash
                      fadeProg = 1;
                  }
                  
                  
                  // DEBUG INJECT
                  var debugEl = document.getElementById('debug-scroll-prog');
                  if (debugEl) {
                      debugEl.innerHTML = "p:" + (p >= 9.62 ? p - 7.42 : p).toFixed(2) + " locP:" + localP.toFixed(2) + " clss:" + document.body.classList.contains("hide-all-cards-final-scene") + " isRet:" + ("OK");
                  }
                  
                  var EARLY_FADE_START = 27.5;
                  var earlyFadeProg = 0;
                  if (localP > EARLY_FADE_START) {
                      earlyFadeProg = Math.min(1, (localP - EARLY_FADE_START) / 1.0);
                  }
                  
                  var oryzoBg = document.getElementById('oryzo-bg');
                  var magClone = document.getElementById('mag-model-clone');
                  
                  if (localP > EARLY_FADE_START) {
                      document.body.classList.add("hide-all-cards-final-scene");
                      if (typeof globalGlbCard !== "undefined" && globalGlbCard) { globalGlbCard.visible = false; }
                      if (typeof cards !== 'undefined' && Array.isArray(cards)) {
                          cards.forEach(function(c) { if (c) c.visible = false; });
                      }
                      if (typeof window.polaroidMesh !== 'undefined' && window.polaroidMesh) { window.polaroidMesh.visible = true; }
                      if (window.polaroidPhotoMat) {
                          // localP va de START_3D_REVEAL (28.5) en adelante
                          // Ralentizado un 50% (antes 4.0, ahora 6.0) para que tarde más en revelar
                          let devProg = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 6.0));
                          window.polaroidPhotoMat.uniforms.uProgress.value = devProg;
                          if (window.polaroidTextMat && window.polaroidTextMat.uniforms) {
                              let textProgress = Math.min(1.0, devProg / 0.75);
                              window.polaroidTextMat.uniforms.uWriteProgress.value = textProgress;
                          }
                          // Sincronizar video de la polaroid
                          const pVid = window.polaroidVideoEl;
                          if (pVid && pVid.duration) {
                              // El video avanza hasta el final del scroll (8.0 unidades desde START_3D_REVEAL)
                              let vidProg = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 8.0));
                              pVid.currentTime = vidProg * pVid.duration;
                              if (window.polaroidPhotoMat && window.polaroidPhotoMat.uniforms.tDiffuse.value) {
                                  window.polaroidPhotoMat.uniforms.tDiffuse.value.needsUpdate = true;
                              }
                          }
                      }
                      if (oryzoBg) oryzoBg.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      if (magClone) magClone.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      
                      var _strip = document.getElementById('img-strip-container');
                      if (_strip) _strip.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      
                      var _thermal = document.getElementById('thermal-overlay');
                      if (_thermal) _thermal.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      
                      var _oryzoSec = document.getElementById('oryzo-section');
                      if (_oryzoSec) _oryzoSec.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      var _deckC = document.getElementById('oryzo-deck-clone');
                      if (_deckC) _deckC.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      var _endT = document.getElementById('end-card-table');
                      if (_endT) _endT.style.opacity = (1 - earlyFadeProg).toFixed(3);
                      var _cCanvas = document.getElementById('card-canvas');
                      if (_cCanvas) _cCanvas.style.opacity = (1 - earlyFadeProg).toFixed(3);
                  }
                  
                  if (localP > START_3D_REVEAL) {
                      var _scOverlay = document.getElementById('scene-overlay');
                      if (_scOverlay) _scOverlay.style.opacity = (1 - fadeProg).toFixed(3);
                      
                      // Ponemos el fondo gris oscuro para tapar el verde del body
                      // (Se controla dinámicamente en la sección de convergencia más abajo)
                  } else {
                      document.body.classList.remove("hide-all-cards-final-scene");
                      if (typeof globalGlbCard !== "undefined" && globalGlbCard) { globalGlbCard.visible = true; }
                      if (typeof cards !== 'undefined' && Array.isArray(cards)) {
                          cards.forEach(function(c) { if (c) c.visible = true; });
                      }
                      if (typeof window.polaroidMesh !== 'undefined' && window.polaroidMesh) { window.polaroidMesh.visible = false; }
                      var _strip = document.getElementById('img-strip-container');
                      if (_strip) _strip.style.opacity = '1';
                      var _thermal = document.getElementById('thermal-overlay');
                      if (_thermal) _thermal.style.opacity = '1';
                      var _scOverlay = document.getElementById('scene-overlay');
                      if (_scOverlay) _scOverlay.style.opacity = '1';
                      if (oryzoBg) oryzoBg.style.opacity = '1';
                      if (magClone) magClone.style.opacity = '1';
                      var _oryzoSec = document.getElementById('oryzo-section');
                      if (_oryzoSec) _oryzoSec.style.opacity = '1';
                      var _deckC = document.getElementById('oryzo-deck-clone');
                      if (_deckC) _deckC.style.opacity = '1';
                      var _endT = document.getElementById('end-card-table');
                      if (_endT) _endT.style.opacity = '1';
                      var _cCanvas = document.getElementById('card-canvas');
                      if (_cCanvas) _cCanvas.style.opacity = '1';
                      if (typeof renderer !== 'undefined') {
                          renderer.setClearColor(0x0d0b09, 1); // restaurar fondo original en lugar de transparente
                      }
                      if (typeof scene !== 'undefined') {
                          scene.background = null;
                      }
                      var _c = document.getElementById('c');
                      if (_c) {
                          _c.style.backgroundColor = 'transparent';
                          _c.style.opacity = '1';
                          _c.style.transition = ''; // Restaurar transition si scrollea hacia arriba
                      }
                  }
                  
                  var sInd = document.querySelector('.scroll-indicator');
                  if (sInd) {
                      var scrollIndP = Math.max(0, Math.min(1, (localP - 34.5) / 1.4));
                      sInd.style.opacity = (1 - scrollIndP).toFixed(3);
                  }
                  
                  // 3. Movimiento de camara hacia la mesa 3D
                  // Se fuerza la camara a estar en initialCameraPos inmediatamente
                  var tableZoomOutP = 0;
                  var easeZoom = 0;
                  if (typeof camera !== 'undefined') {
                      var zoomP = 0;
                      if (localP > START_3D_REVEAL) {
                          zoomP = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 6.0));
                      }
                      // Suavizado del zoom (ease-in-out cuadrático)
                      easeZoom = zoomP < 0.5 ? 2 * zoomP * zoomP : -1 + (4 - 2 * zoomP) * zoomP;
                  }
                  window._finalZoomP = easeZoom;
                  window._finalPolProg = tableZoomOutP;
                  
                  // Convergencia del Logo y CTA al seguir haciendo scroll DESPUÉS del zoom (de 34.5 a 36.5)
                  var convergeP = Math.max(0, Math.min(1, (localP - 34.5) / 1.0));
                  
                  // Suavizado ease-out cuadrático para que frenen suavemente
                  var easeConverge = convergeP * (2 - convergeP);
                  
                  var _oltLogoBig = document.getElementById('olt-logo-img-big');
                  var _oltCtaBig = document.getElementById('olt-final-cta');
                  
                  if (localP < 34.5) {
                      // Fase de entrada: de 100vh a 0vh (después del segundo carrusel: IS_END a IS_EXIT_END)
                      if (_oltLogoBig) {
                          _oltLogoBig.style.transform = 'translateY(' + ((1 - _exitEA) * 100).toFixed(2) + 'vh)';
                      }
                      if (_oltCtaBig) {
                          var _ctaP = Math.max(0, Math.min(1, (_exitP - 0.5) / 0.5));
                          _oltCtaBig.style.opacity = _ctaP.toFixed(2);
                          _oltCtaBig.style.pointerEvents = _ctaP > 0 ? 'auto' : 'none';
                          _oltCtaBig.style.transform = 'translateY(' + ((1 - _exitEA) * 100).toFixed(2) + 'vh)';
                      }
                  } else {
                      // Fase de convergencia final (en la escena 3D final)
                      if (_oltLogoBig) {
                          _oltLogoBig.style.transform = 'translateY(' + (easeConverge * 16) + 'vh)';
                      }
                      if (_oltCtaBig) {
                          _oltCtaBig.style.transform = 'translateY(' + (-easeConverge * 30) + 'vh)';
                          _oltCtaBig.style.opacity = '1';
                          _oltCtaBig.style.pointerEvents = 'auto';
                      }
                  }
                  
                  var _oltQuestion = document.getElementById('olt-final-question');
                  if (_oltQuestion) {
                      // El fade de la pregunta va con el convergeP, empieza un poco despues para mayor impacto
                      var qFade = Math.max(0, Math.min(1, (convergeP - 0.2) / 0.8));
                      _oltQuestion.style.opacity = qFade.toFixed(2);
                  }
                  
                  // Fade in del fondo negro-verde (haciendo el gris transparente mediante CSS)
                  var bgAlpha = 1.0 - convergeP;
                  // ANULADO: Hacía que el fondo base se viera verde si se interrumpía el scroll
                  // if (typeof renderer !== 'undefined') {
                  //     renderer.setClearColor(0x000000, 0);
                  // }
                  // En lugar de hacer transparente el canvas (que da bugs en navegadores),
                  // simplemente hacemos aparecer un div verde por encima que tapa todo menos el logo y CTA.
                  var _fakeBg = document.getElementById('fake-bg-fade');
                  if (_fakeBg) {
                      // Hacemos que llegue a 1.0 antes (en localP 35.8) para garantizar el 100% al llegar al final de la página
                      var fadeBgP = Math.max(0, Math.min(1, (localP - 34.5) / 1.3));
                      _fakeBg.style.opacity = fadeBgP;
                  }
                  if (typeof scene !== 'undefined') {
                      scene.background = null; // Necesario para que el clearColor alpha funcione
                  }
                  
              } else {
                isCont.style.opacity = '0';
                isTrack.style.transform = 'translateX(0.5cm)';
                for (var s3 = 0; s3 < slides.length; s3++) {
                  slides[s3].style.clipPath = 'inset(0 100% 0 0)';
                }
                // Reset subrayado compromiso al salir del carrusel
                var _ulReset = document.getElementById('compromiso-underline');
                if (_ulReset) _ulReset.style.transform = 'scaleY(0)';
                  isCont.style.transform = '';
                  var _oltLogoR = document.getElementById('olt-logo-img-big');
                  if (_oltLogoR) _oltLogoR.style.transform = 'translateY(100vh)';
                  var _oltQuestionR = document.getElementById('olt-final-question');
                  if (_oltQuestionR) _oltQuestionR.style.opacity = '0';
                  var _oltTextR = document.getElementById('olt-final-text');
                  if (_oltTextR) {
                      _oltTextR.style.transform = 'translate(-50%, 100vh)';
                      _oltTextR.style.opacity = '0';
                  }
                  var _oltPhase1R = document.getElementById('olt-phase-1');
                  if (_oltPhase1R) _oltPhase1R.style.opacity = '0';
                  var _oltPhase2R = document.getElementById('olt-phase-2');
                  if (_oltPhase2R) _oltPhase2R.style.opacity = '0';
                  var _oltCtaR = document.getElementById('olt-final-cta');
                  if (_oltCtaR) {
                      _oltCtaR.style.transform = 'translateY(100vh)';
                      _oltCtaR.style.opacity = '0';
                      _oltCtaR.style.pointerEvents = 'none';
                  }
                  // Restaurar el scroll indicator al salir de la fase final
                  var _scrollIndR = document.querySelector('.scroll-indicator');
                  if (_scrollIndR) _scrollIndR.style.opacity = '1';
              }
            })();
          } else {
            if (ec1) ec1.style.opacity = '0';
            if (ec2) ec2.style.opacity = '0';
            if (ec3) ec3.style.opacity = '0';
            if (ec4) ec4.style.opacity = '0';
            
            var _eR1 = document.getElementById('end-review-panel-1'); if (_eR1) _eR1.style.opacity = '0';
            var _eR2 = document.getElementById('end-review-panel-2'); if (_eR2) _eR2.style.opacity = '0';
            var _eR3 = document.getElementById('end-review-panel-3'); if (_eR3) _eR3.style.opacity = '0';
            var _eR4 = document.getElementById('end-review-panel-4'); if (_eR4) _eR4.style.opacity = '0';
            
            var _isCont = document.getElementById('img-strip-container'); if (_isCont) _isCont.style.opacity = '0';
            var _oltL = document.getElementById('olt-logo-img-big'); if (_oltL) _oltL.style.transform = 'translateY(100vh)';
            var _oltT = document.getElementById('olt-final-text'); if (_oltT) { _oltT.style.transform = 'translate(-50%, 100vh)'; _oltT.style.opacity = '0'; }
            var _p1 = document.getElementById('olt-phase-1'); if (_p1) _p1.style.opacity = '0';
            var _p2 = document.getElementById('olt-phase-2'); if (_p2) _p2.style.opacity = '0';
            var _oltDyn = document.getElementById('olt-phase-dynamic'); if (_oltDyn) _oltDyn.style.opacity = '0';
            var _oltC = document.getElementById('olt-final-cta'); if (_oltC) { _oltC.style.transform = 'translateY(100vh)'; _oltC.style.opacity = '0'; _oltC.style.pointerEvents = 'none'; }
            var _oltQ = document.getElementById('olt-final-question'); if (_oltQ) _oltQ.style.opacity = '0';
          }
      }
      
      // 3. Reveal de texto tipo Oryzo (letra a letra con difuminado suave)
      var textGrad = document.getElementById('oryzo-text-gradient');
      var textGradR = document.getElementById('oryzo-text-right-gradient');
      
      // Retrasado un pelín respecto al original, basado en textY para un fundido fluido
      var txtP = clamp01((65 - slideY) / 40); 
      var txtPR = clamp01((40 - slideY) / 40); 
      var blurLen = 8; // Difuminado de 8 letras para que sea muy suave
      
      if (textGrad) {
        var chars = textGrad.querySelectorAll('.oryzo-char');
        if (chars.length > 0) {
           var targetIdx = txtP * (chars.length + blurLen) - blurLen;
           for (var i = 0; i < chars.length; i++) {
              var op = 1 - (i - targetIdx) / blurLen;
              chars[i].style.opacity = Math.max(0, Math.min(1, op));
           }
        }
      }
      
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

      // Reviews manejadas arriba en el bloque localP
    }

    requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);
})();

