import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add the CSS crop
    content = content.replace(
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 63vh !important; } #conecta-transition-text { top: 15vh !important; } }',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 63vh !important; } #conecta-transition-text { top: 15vh !important; } #thermal-overlay { height: 95vh !important; } }'
    )

    # 2. Update the JS math
    old_oryzo = """        // 1. Translación fluida de la sección (hasta el centro de la pantalla)
        var tSlide = clamp01((p - 21.7) / 1.6); // Termina en 23.3, justo cuando empieza a abrirse
        // Empieza a bajar (38.6) con el carrusel y termina de desaparecer del todo (40.76)
        var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); 
        var slideY = (1 - ease(tSlide)) * 130; // La pantalla se queda anclada
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
        // La baraja de cartas baja independientemente de la pantalla (80vh es suficiente para ocultarla)
        var isMob = window.innerWidth <= 768 || window._cIsMobile;
          var boxEnterY = 0;
          if (isMob) {
              var _tCam = clamp01((p - 21.7) / 3.0);
                var _txtY = 130 - (ease(_tCam) * 230);
                var _cntY = Math.min(0, _txtY - slideY);
                var totalYForBox = slideY + _cntY;
              var boxDelayProg = clamp01(((-5) - totalYForBox) / 30);
                // boxEnterY = (1 - boxDelayProg) * 110;
            }
            var boxTotalY = (tExitBox * 80);
            if (isMob) {
                boxTotalY += Math.max(-69.5, _cntY);
            } else {
                boxTotalY += boxEnterY;
            }
            oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';
        oryzoSec.style.pointerEvents = tSlide > 0.5 ? 'auto' : 'none';
        oryzoSec.style.visibility = tSlide > 0 ? 'visible' : 'hidden';
        // Sincronizamos el fondo morado 
        window._scrollUpVh = 130 - slideY;
        // Fase de salida (la cámara baja continuamente)
        var tCamera = clamp01((p - 21.7) / 3.0);
        var textY = 130 - (ease(tCamera) * 230);
        var contentY = Math.min(0, textY - slideY);"""

    new_oryzo = """        // 1. Translación fluida de la sección (hasta el centro de la pantalla)
        var tSlide = clamp01((p - 21.7) / 1.6); // Termina en 23.3, justo cuando empieza a abrirse
        // Empieza a bajar (38.6) con el carrusel y termina de desaparecer del todo (40.76)
        var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); 
        
        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var travelDist = isMobileLayout ? 95 : 130;
        
        var slideY = (1 - ease(tSlide)) * travelDist;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
        // La baraja de cartas baja independientemente de la pantalla (80vh es suficiente para ocultarla)
        var isMob = window.innerWidth <= 768 || window._cIsMobile;
          var boxEnterY = 0;
          if (isMob) {
              var _tCam = clamp01((p - 21.7) / 3.0);
                var _textDist = isMobileLayout ? 195 : 230;
                var _txtY = travelDist - (ease(_tCam) * _textDist);
                var _cntY = Math.min(0, _txtY - slideY);
                var totalYForBox = slideY + _cntY;
              var boxDelayProg = clamp01(((-5) - totalYForBox) / 30);
                // boxEnterY = (1 - boxDelayProg) * 110;
            }
            var boxTotalY = (tExitBox * 80);
            if (isMob) {
                boxTotalY += Math.max(-69.5, _cntY);
            } else {
                boxTotalY += boxEnterY;
            }
            oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';
        oryzoSec.style.pointerEvents = tSlide > 0.5 ? 'auto' : 'none';
        oryzoSec.style.visibility = tSlide > 0 ? 'visible' : 'hidden';
        // Sincronizamos el fondo morado 
        window._scrollUpVh = travelDist - slideY;
        // Fase de salida (la cámara baja continuamente)
        var tCamera = clamp01((p - 21.7) / 3.0);
        var textDist = isMobileLayout ? 195 : 230;
        var textY = travelDist - (ease(tCamera) * textDist);
        var contentY = Math.min(0, textY - slideY);"""

    # We will use exactly replacing the small chunks to avoid encoding issues
    content = content.replace(
        "var slideY = (1 - ease(tSlide)) * 130; // La pantalla se queda anclada",
        "var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);\n        var travelDist = isMobileLayout ? 95 : 130;\n        var slideY = (1 - ease(tSlide)) * travelDist;"
    )

    content = content.replace(
        "var _txtY = 130 - (ease(_tCam) * 230);",
        "var _txtY = travelDist - (ease(_tCam) * (isMobileLayout ? 195 : 230));"
    )

    content = content.replace(
        "window._scrollUpVh = 130 - slideY;",
        "window._scrollUpVh = travelDist - slideY;"
    )

    content = content.replace(
        "var textY = 130 - (ease(tCamera) * 230);",
        "var textY = travelDist - (ease(tCamera) * (isMobileLayout ? 195 : 230));"
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
