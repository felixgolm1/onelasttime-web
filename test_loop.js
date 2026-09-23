const window = {_ch: 1080, _cw: 1920, _cIsMobile: false};
const document = {documentElement: {clientWidth: 1920}};
let prog = 0.5;
let gx=0, gy=0;
let mgEl = {};
function smoothScrollLoop() {

        try {

        const lerpF = 0.40;

        

        // SALTO CUÁNTICO DE TIMELINE

        if (!window.isAutoScrolling) {

            if (targetProg > 2.20 && targetProg < 9.62) {

                if (prog <= 2.20) {

                    targetProg = 9.62;

                    prog = 9.62;

                } else {

                    targetProg = 2.20;

                    prog = 2.20;

                }

            }

            

            // ANTI-LODO (Warp Lerp): Evita que la fricción interpole a través del salto

            if (prog <= 2.20 && targetProg >= 9.62) {

                prog = 9.62;

            } else if (prog >= 9.62 && targetProg <= 2.20) {

                prog = 2.20;

            }

        }



      if (Math.abs(targetProg - prog) > 0.000005 || window.isAutoScrolling) {

        if (!window.isAutoScrolling) {

            if (Math.abs(targetProg - prog) > 10) { prog = targetProg; } else { prog += (targetProg - prog) * lerpF; }

            if (Math.abs(targetProg - prog) <= 0.000005) prog = targetProg;

        }

        sessionStorage.setItem('dev_prog', prog);

        scrollTl.progress(Math.min(1, prog / 2.2));

        if (window.cssRenderer && window.scene && window.camera) { window.cssRenderer.render(window.scene, window.camera); }

        updateBoxState();

        updateFaceSwap();

        updateGlobalScenes();



          const debugProg = document.getElementById('debug-scroll-prog');

          if (debugProg) debugProg.innerText = (prog >= 9.62 ? prog - 7.42 : prog).toFixed(2);





          // Ã¢â€€ Edge glow: matemáticamente atado a prog

          const eg = document.getElementById('edge-glow');

          if (eg) {

            let startP = 1.54;

            let endP = 2.19;

            

            if (prog >= startP && prog <= endP) {

              if (prog < startP + 0.03) {

                // Fade in rápido (0.03 unidades)

                eg.style.opacity = mapRange(prog, startP, startP + 0.03, 0, 1);

              } else if (prog > endP - 0.03) {

                // Fade out rápido (0.03 unidades)

                eg.style.opacity = mapRange(prog, endP - 0.03, endP, 1, 0);

              } else {

                // Plateau (100% visible)

                eg.style.opacity = 1;

              }

            } else {

              eg.style.opacity = 0;

            }

          }

        }



        // SAFEGUARD PERMANENTE: corre SIEMPRE cada frame (incluso cuando el scroll está parado)

        // Evita que GSAP deje stOverlay / detailGlobal visibles fuera de su rango correcto

        if (stOverlay) stOverlay.style.opacity = (prog >= 0.923 && prog <= 2.20) ? '1' : '0';

        const _dg = document.getElementById('sc-detail-global');

        if (_dg) _dg.style.opacity = (prog >= 0.923 && prog <= 2.20) ? '' : '0';





      

      // Actualizar posición de la barra de scroll custom estilo Oryzo

      const scrollThumb = document.getElementById('custom-scroll-thumb');

        if (scrollThumb && !window.isDraggingThumb) {

          let fakeProg = prog;

          if (prog >= 9.62) fakeProg = prog - 7.42;

          let fakeMax = maxProg - 7.42;

          const scrollPercent = Math.max(0, Math.min(1, fakeProg / fakeMax));

          // Asumimos un track de 100vh y thumb de 29vh, nos queda 71vh de recorrido libre

          scrollThumb.style.transform = `translateY(${scrollPercent * (window.innerWidth <= 768 ? 85 : 71)}vh)`;

        }

      

      // Ã¢â€€Ã¢â€€ THERMAL CURTAIN Ã¢â€€Ã¢â€€ incondicional, ejecuta cada frame Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€

      {

        const _tP = Math.min(1, Math.max(0, ((prog + 0.5) - 16.27) / (17.2 - 16.27)));

        const _tc = document.getElementById('thermal-canvas');

        if (_tc) {

          if (_tP <= 0) {

            _tc.style.display = 'none';

          } else {

            const _vw = window.innerWidth, _vh = window.innerHeight;

            _tc.width  = _vw;

            _tc.height = _vh;

            _tc.style.position      = 'fixed';

            _tc.style.top           = '0';

            _tc.style.left          = '0';

            _tc.style.width         = '100%';

            _tc.style.height        = '100%';

            _tc.style.zIndex        = '9999999';

            _tc.style.display       = 'block';

            _tc.style.pointerEvents = 'none';

            const _ctx = _tc.getContext('2d');

            _ctx.clearRect(0, 0, _vw, _vh);

            _ctx.fillStyle = 'rgba(200, 0, 130, 0.95)';

            _ctx.fillRect(0, _vh - Math.round(_vh * _tP), _vw, Math.round(_vh * _tP));

          }

        }

      }



      // Ã¢â€€Ã¢â€€ THERMAL OVERLAY Ã¢â€€Ã¢â€€ máscara gradiente suave en el overlay (sin línea dura)

      {

        var _tPdiv = Math.min(1, Math.max(0, ((prog + 0.5) - 16.27) / (16.8 - 16.27)));

        window._brainScrollProg = prog;

        if (window._updateNeuralText) window._updateNeuralText(prog);

        var _tOvr  = document.getElementById('thermal-overlay');

        var _mOvr  = document.getElementById('mag-breakout-overlay');

        // Siempre limpiar la máscara del mag-breakout

        if (_mOvr) { _mOvr.style.webkitMaskImage = ''; _mOvr.style.maskImage = ''; }

        if (_tOvr) {

          var _showOverlay = (prog + 0.5) >= 15.35;

          if (!_showOverlay) {

            _tOvr.style.display = 'none';

          } else {

            _tOvr.style.display = 'block';

            if (prog < 48.6) {

                _tOvr.style.opacity  = '1';

            }

            _tOvr.style.webkitMaskImage = '';

            _tOvr.style.maskImage = '';

            var _bgEl  = document.getElementById('thermal-bg');

            var _silWr = document.getElementById('thermal-model-wrap');

            var _vigEl = document.getElementById('thermal-vignette');

            if (_tPdiv <= 0) {

              if (_bgEl)  { _bgEl.style.opacity = '0';  _bgEl.style.webkitMaskImage = '';  _bgEl.style.maskImage = ''; }

              if (_silWr) { _silWr.style.opacity = '0'; _silWr.style.webkitMaskImage = ''; _silWr.style.maskImage = ''; }

              if (_vigEl) { _vigEl.style.opacity = '0'; _vigEl.style.webkitMaskImage = ''; _vigEl.style.maskImage = ''; }

            } else {

              var _vis = Math.round(_tPdiv * 115);

              var _se  = 4;

              var _lo  = Math.max(0, Math.min(100, _vis - _se));

              var _hi  = Math.max(0, Math.min(100, _vis + _se));

              var _mv  = 'linear-gradient(to bottom left, black 0%, black ' + _lo + '%, transparent ' + _hi + '%)';

              var _bgOp = Math.min(1, _tPdiv / 0.15);

              if (_bgEl)  { _bgEl.style.opacity = String(_bgOp);  _bgEl.style.webkitMaskImage = _mv;  _bgEl.style.maskImage = _mv; }

              if (_silWr) { _silWr.style.opacity = String(_bgOp); _silWr.style.webkitMaskImage = _mv; _silWr.style.maskImage = _mv; }

              if (_vigEl) { _vigEl.style.opacity = String(_bgOp); _vigEl.style.webkitMaskImage = _mv; _vigEl.style.maskImage = _mv; }

            }

            // Sincronizar posición de la silueta con el modelo real

            var _sil = document.getElementById('thermal-silhouette');

            var _realModel = document.getElementById('mag-model-clone');

            // --- FIX DE SINCRONIZACIÓN ---

            // Como mag-model-clone se creó antes de aplicar los transforms del carrusel,

            // actualizamos su posición y tamaño AQUÍ basándonos en la revista ya transformada:

            var _magScene = document.getElementById('magazine-scene');

            var _magEl = document.querySelectorAll('.carousel-track-large .carousel-item')[8];

            if (_realModel && _magScene && _magEl) {

                var _magR = _magEl.getBoundingClientRect();

                var _modelH = _magR.height * 1.38;

                var _origImg = _magEl.querySelector('img[src*="modelo-sin-fondo"]') || _magScene.querySelector('.carousel-track-large img[src*="modelo-sin-fondo"]');

                if (_origImg && _origImg.naturalHeight) {

                    var _ar = _origImg.naturalWidth / _origImg.naturalHeight;

                    var _modelW = _modelH * _ar;

                    var _modelT = _magR.top;

                    var _modelL = _magR.left + _magR.width / 2 - _modelW / 2;

                    _realModel.style.left = _modelL + 'px';

                    _realModel.style.top = _modelT + 'px';

                    _realModel.style.width = _modelW + 'px';

                    _realModel.style.height = _modelH + 'px';

                }

            }

            // -----------------------------

            if (_sil && _realModel) {

              var _r = _realModel.getBoundingClientRect();

              _sil.style.position = 'absolute';

              _sil.style.left     = _r.left   + 'px';

              _sil.style.top      = _r.top    + 'px';

              _sil.style.width    = _r.width  + 'px';

              _sil.style.height   = _r.height + 'px';

              _sil.style.transform = 'none';

            }

          }

        }

      }



      // Sincronizar reveal del cerebro 3D con el barrido termico

      if (typeof window._updateBrainReveal === 'function') {

        window._updateBrainReveal(_tPdiv, (_tPdiv <= 0) ? null : ('linear-gradient(to bottom left, black 0%, black ' + _lo + '%, transparent ' + _hi + '%)'));

      }



      // (Llamada a updateBoxState movida antes de updateGlobalScenes para sincronizar bounds correctamente)

      // updateBoxState();



      // Ã¢â€€Ã¢â€€ SINC CSS card ? GLB 3D overlay Ã¢â€€Ã¢â€€ (siempre, cada frame)

      if (globalGlbCard && cardCanvasEl && document.getElementById('card-morph-group')) {

          const mgEl = document.getElementById('card-morph-group');



          mgEl.style.opacity = '0'; // CSS card siempre oculta â€â€ reemplazada por la 3D



          mgEl.style.opacity = '0'; // CSS card siempre oculta â€ â€  reemplazada por la 3D



          // Ã¢â€ €Ã¢â€ € CROSSFADE carta Ã¢â€ â€  caja Ã¢â€ €Ã¢â€ €

          // Cuando mainDeck es display:'block', la carta se desvanece exactamente al ritmo

          // que la caja aparece: cardCanvas.opacity = 1 - mainDeck.opacity.

          // Así nunca hay un "vacío" entre carta oculta y caja visible.

          const mainDeckEl = document.getElementById('mainDeck');

          const dealerPile = document.getElementById('dealer-pile-wrap');

          

          // Ocultar la baraja secundaria cuando la carta 3D la tape completamente

          if (dealerPile) {

              // La carta 3D se hace grande y las tapa. Una vez tapadas (prog > 0.05) las ocultamos.

              dealerPile.style.visibility = prog > 0.05 ? 'hidden' : 'visible';

          }



          if (mainDeckEl && mainDeckEl.style.display === 'block') {

              const mdOp = parseFloat(mainDeckEl.style.opacity || '0');

              cardCanvasEl.style.transition = 'none';

              cardCanvasEl.style.opacity    = String(Math.max(0, 1 - mdOp));

              globalGlbCard.visible         = mdOp < 0.99;

              if (mdOp >= 0.99) {

                  requestAnimationFrame(smoothScrollLoop);

                  return;  // caja completamente visible, carta totalmente oculta

              }

          }



          // Detectar scatter cuando los 3 flips terminan (rotationY Ã¢â€°Â¤ Ã¢Ëâ€539Â°)

          // Con 3 flips el destino es -540Â°; el umbral de -179Â° disparaba tras el 1er flip

          // haciendo que la carta GLB se desacoplara y el scroll pareciera muerto.

          const flipRotY  = gsap.getProperty(mgEl, 'rotationY') || 0;

          const inScatter = (prog >= 0.08 && flipRotY <= -539.5) || prog > 1.22;

          // Solo forzar opacity=1 y visible=true cuando el crossfade NO está activo

          // (si mainDeck es visible, el crossfade ya gestiona opacity y visible arriba)

          if (!mainDeckEl || mainDeckEl.style.display !== 'block') {

              cardCanvasEl.style.opacity = '1';

              globalGlbCard.visible      = true;

          }



          const scIntroEl = document.getElementById('sc-intro');

          if (!inScatter) {

              // Ã¢â€ €Ã¢â€ € Tracking pre-scatter (Fase 1 zoom + Fase 2 flip) Ã¢â€ €Ã¢â€ €

              // Usamos propiedades GSAP (x/y/scaleY) en lugar de getBoundingClientRect.

              // getBoundingClientRect incluye la distorsión de perspectiva CSS 3D (rotationY),

              // lo que hace que el centro y el tamaño del rect oscilen durante el flip.

              // Las propiedades x/y de GSAP son translaciones puras ? sin distorsión.

              //    mgEl natural CSS center = (50vw, 50vh) [fixed, inset:0, flex-centered]

              //    GSAP x/y = offset aplicado encima del centro natural

              //    En Fase 2 (flip): GSAP x=0, y=0 ? posición constante en centro

              smoothScrollLoop._lockedCard = null;

              if (scIntroEl) scIntroEl.style.visibility = 'hidden';

              cardCanvasEl.style.transform = 'none';



              const DIST = 6.0;

              const vH   = 2 * Math.tan((42 * Math.PI / 180) / 2) * DIST;

              const vW   = vH * (window._cw / window._ch);



              // Posición: centro natural (50vw,50vh) + offset GSAP (sin perspectiva)

              const gx    = gsap.getProperty(mgEl, 'x')      || 0;

              const gy    = gsap.getProperty(mgEl, 'y')      || 0;

              const gSY   = gsap.getProperty(mgEl, 'scaleY') || 1;

              let driftY = 0;
              if (typeof prog !== 'undefined') {
                  if (prog > 0.60 && prog < 0.88) {
                      let phase1Prog = (prog - 0.60) / 0.28;
                      let ease = phase1Prog < 0.5 ? 2 * phase1Prog * phase1Prog : 1 - Math.pow(-2 * phase1Prog + 2, 2) / 2;
                      driftY = ease * (-window._ch * 0.045);
                  } else if (prog >= 0.88) {
                      driftY = -window._ch * 0.045;
                  }
              }

              const screenCX = document.documentElement.clientWidth / 2 + gx;

              const screenCY = window._ch / 2 + gy + driftY;

              const ndcX  =  (screenCX / window._cw)  * 2 - 1;

              const ndcY  = -(screenCY / window._ch) * 2 + 1;

              globalGlbCard.position.set(ndcX * vW / 2, ndcY * vH / 2, -DIST);



              // Smooth zoom: gSY=1.0 (mesa) ? gSY=1.22 (scatter entry)

              // Mismo rango que scrollTl Phase 1 â€â€ la pantalla se va poniendo negra a la vez

              if (globalGlbCard._baseScaleFact && gSY > 0) {

                  const _GS_SC  = 1.22;

                  const _baseGSY = window._cIsMobile ? 0.90 : 1.0;

            const _t = Math.max(0, Math.min(1, (gSY - _baseGSY) / (_GS_SC - _baseGSY)));

                  const _scSmall = globalGlbCard._baseScaleFact * (window._cIsMobile ? 0.5 : 0.65);

                  const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * (window._cIsMobile ? (1.0/_GS_SC) : 0.90);

                  globalGlbCard.scale.setScalar(_scSmall + _t * (_scLarge - _scSmall));

              }





              const rx = gsap.getProperty(mgEl, 'rotationX') || 0;

              const ry = gsap.getProperty(mgEl, 'rotationY') || 0;

              const rz = gsap.getProperty(mgEl, 'rotation')  || 0;

              globalGlbCard.rotation.set(

                  rx * Math.PI / 180,

                  -ry * Math.PI / 180,

                  -rz * Math.PI / 180

              );



          } else {

              // Ã¢â€€Ã¢â€€ Scatter / 4 pasos Ã¢â€€Ã¢â€€

              if (scIntroEl) scIntroEl.style.visibility = 'hidden';



              // Snapshot una sola vez al entrar al scatter.

              // Importante: NO usar globalGlbCard.scale.x en cold-load porque el GLB

              // todavía tiene su escala por defecto, no la calculada desde el CSS card.

              // Calculamos la misma fórmula que usaría el bloque !inScatter.

              if (!smoothScrollLoop._lockedCard) {

                  const _mgEl2 = document.getElementById('card-morph-group');

                  const _gSY2  = Math.abs(gsap.getProperty(_mgEl2, 'scaleY') || 1);

                  // Replica exactamente la fórmula de !inScatter: _baseScaleFact * |gSY| * 0.90

                  // Funciona en cold-load porque globalGlbCard._baseScaleFact siempre está disponible

                  // tras la carga del GLB (independiente de si !inScatter ha corrido)

                  const _snapScale = (globalGlbCard._baseScaleFact > 0)

                        ? (globalGlbCard._baseScaleFact * (window._cIsMobile ? 1.0 : (_gSY2 * 0.90)))

                      : Math.abs(globalGlbCard.scale.x);   // fallback solo si el GLB aún no ha cargado

                  smoothScrollLoop._lockedCard = {

                      rotBaseZ: +2.5 * Math.PI / 180,

                      scale:    _snapScale

                  };

              }

              const lc = smoothScrollLoop._lockedCard;



              // Detectar flip-back ANTES del posicionamiento

              const scBoardRY   = gsap.getProperty(scBoard, 'rotationY') || 0;

              const inFlipBack  = Math.abs(scBoardRY) > 5;



              // Posición: flip-back ? screen center (= mainDeck, z-index lo cubre) / scatter ? scIntroEl

              cardCanvasEl.style.transform = 'none';

              const DIST = 6.0;

              const vH   = 2 * Math.tan((42 * Math.PI / 180) / 2) * DIST;

              const vW   = vH * (window._cw / window._ch);

              if (inFlipBack) {
                    let tP = 0;
                    if (prog >= 13.62) tP = Math.max(0, Math.min(1, (prog - 13.62) / 1.0));
                    
                    let flipProg = Math.max(0, Math.min(1, (prog - 1.30) / 0.27));
                    let easeFlip = flipProg * flipProg; // ease-in cuadratico
                    
                    const initialCY = window._ch * 0.5; // HTML card center (50vh)
                    const finalCY = window._cIsMobile ? (window._ch * 0.46) : (window._ch * 0.455);
                    const baseCY = initialCY + easeFlip * (finalCY - initialCY);
                    
                    const baseNdcY = -(baseCY / window._ch) * 2 + 1;
                    const startY = baseNdcY * vH / 2;
                    
                    let endX = vW * 0.28;
                    let endY = -vH * 0.22;
                    globalGlbCard.position.set(tP * endX, startY + tP * (endY - startY), -DIST);
                } else if (scIntroEl) {

                  const scRect = scIntroEl.getBoundingClientRect();

                  if (scRect.width > 0 && scRect.height > 0) {

                      const screenCX = scRect.left + scRect.width  / 2;

                      const screenCY = scRect.top  + scRect.height / 2;

                      const ndcX =  (screenCX / window._cw)  * 2 - 1;

                      const ndcY = -(screenCY / window._ch) * 2 + 1;

                      globalGlbCard.position.set(ndcX * vW / 2, ndcY * vH / 2, -DIST);

                  }

              }





              if (!inFlipBack) {

                  // Ã¢â€€Ã¢â€€ SCATTER normal (4 pasos / macro-cámara) Ã¢â€€Ã¢â€€

                  const boardRotDeg = gsap.getProperty(scBoard, 'rotation') || 0;

                  const totalRz     = lc.rotBaseZ + boardRotDeg * Math.PI / 180;

                  globalGlbCard.rotation.set(0, Math.PI, totalRz, 'XYZ');



                  const boardScale = gsap.getProperty(scBoard, 'scaleX') || 1;

                  // Compensacion de perspectiva: al alejarse del centro, la camara 3D lo hace ver mas pequeno.

                  // Calculamos la distancia real a la lente y escalamos proporcionalmente para mantener tamano visual 2D constante.

                  const currentDist = Math.sqrt(

                      Math.pow(globalGlbCard.position.x, 2) + 

                      Math.pow(globalGlbCard.position.y, 2) + 

                      Math.pow(DIST, 2)

                  );

                  const perspectiveComp = currentDist / DIST;

                  

                  globalGlbCard.scale.setScalar(lc.scale * boardScale * perspectiveComp);



              } else {

                  const scBoardScale = gsap.getProperty(scBoard, 'scaleX') || 0.66;

                  const scIntroRot2D = scIntroEl ? (gsap.getProperty(scIntroEl, 'rotation') || 0) : -90;

                  let tP = 0;



                  // Modificador de escala para que desaparezca durante el carrusel y YA NO reaparezca

                  let scaleMod = 1.0;

                  if (prog >= 2.2) {

                      scaleMod = 0.00001; // oculto al aparecer mainDeck y no reaparece en carrusel

                  }

                  

                  // REAPARECER AL FINAL DEL SCROLL

                  if (window._finalPolProg > 0) {

                      scaleMod = Math.max(0.00001, window._finalPolProg);

                  }

                  

                  globalGlbCard.visible = scaleMod > 0.01;



                  // Rotación: De giro de caja a plana contra la revista (ligeramente torcida Z=15deg)

                  let startRotY = -Math.PI + scBoardRY * Math.PI / 180;

                  let endRotY = -Math.PI;

                  let startRotZ = lc.rotBaseZ + scIntroRot2D * Math.PI / 180;

                  let endRotZ = 12 * Math.PI / 180;



                  globalGlbCard.rotation.set(

                      0,

                      startRotY + tP * (endRotY - startRotY),

                      startRotZ + tP * (endRotZ - startRotZ),

                      'XYZ'

                  );



                  // Escala: Se encoge a tamaño de imagen impresa

                  let startScale = lc.scale * scBoardScale;

                  let endScale = startScale * 0.45;

                  globalGlbCard.scale.setScalar((startScale + tP * (endScale - startScale)) * scaleMod);

                  

                  // AL FINAL DEL SCROLL: forzar posición al centro de la mesa izquierda

                  if (window._finalPolProg > 0) {

                      let fp = window._finalPolProg;

                      // Transición hacia la mesa izquierda

                      globalGlbCard.position.set((1-fp) * 20 + fp * -7.0, 0, (1-fp) * -20);

                      globalGlbCard.rotation.set(0, 0, (12 + fp * -102) * Math.PI / 180);

                      // Escala base normal de la caja

                      globalGlbCard.scale.setScalar(lc.scale * scaleMod * 0.9);

                  }

              }



          }   // Ã¢â€€Ã¢â€€ fin else scatter Ã¢â€€Ã¢â€€

      }   // Ã¢â€€Ã¢â€€ fin if (globalGlbCard) Ã¢â€€Ã¢â€€



      updateNavState(prog);

      const line = document.getElementById('nav-progress-line');

      if (line && window.targetNavWidth !== undefined && window.fullNavLineWidth) {

          if (typeof window.lerpedNavWidth === 'undefined') {

              window.lerpedNavWidth = window.targetNavWidth;

          }

          window.lerpedNavWidth += (window.targetNavWidth - window.lerpedNavWidth) * 0.05;

          let percentRight = (window.lerpedNavWidth / window.fullNavLineWidth) * 100;

          percentRight = Math.max(0, Math.min(100, percentRight));

          line.style.clipPath = `inset(0 ${100 - percentRight}% 0 0)`;

      }

      } catch(err) { 

            if(!window.didAlertErr) { 

                var eD = document.createElement('div'); 

                eD.style.cssText = 'position:fixed;inset:0;background:red;color:white;z-index:99999999;font-size:30px;padding:50px;'; 

                eD.innerText = 'CRASH: ' + err.message + '\n' + err.stack; 

                document.body.appendChild(eD); 

                window.didAlertErr = true; 

            } 

        }

requestAnimationFrame(smoothScrollLoop);

    }



    smoothScrollLoop();



    // --- Snap Lock: pausa real en cada imagen del carrusel ---

    let _snapLockPoint = null;   // snap point actualmente bloqueado

    let _snapLockTicks = 0;      // ticks restantes para escapar

    const SNAP_LOCK_TICKS = 0;  // ticks de scroll necesarios para pasar al siguiente slide



    
console.log(" Syntax OK\);