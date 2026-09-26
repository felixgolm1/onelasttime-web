import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. thermal-overlay height
    content = content.replace(
        '<div id="thermal-overlay" style="display:none;position:fixed;top:0;left:0;width:100%;height:130vh;',
        '<div id="thermal-overlay" style="display:none;position:fixed;top:0;left:0;width:100%;height:95vh;'
    )

    # 2. thermal-canvas height
    content = content.replace(
        "tc.style.width = '100%'; tc.style.height = '130vh';",
        "tc.style.width = '100%'; tc.style.height = '95vh';"
    )
    content = content.replace(
        "var extendedVh = window._ch * 1.3;",
        "var extendedVh = window._ch * 0.95;"
    )

    # 3. oryzo-section update logic
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
        var slideY = (1 - ease(tSlide)) * 95; // Recortado de 130 a 95
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
        // La baraja de cartas baja independientemente de la pantalla (80vh es suficiente para ocultarla)
        var isMob = window.innerWidth <= 768 || window._cIsMobile;
          var boxEnterY = 0;
          if (isMob) {
              var _tCam = clamp01((p - 21.7) / 3.0);
                var _txtY = 95 - (ease(_tCam) * 195); // Recortado a 95
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
        window._scrollUpVh = 95 - slideY; // Mueve la silueta 95vh
        // Fase de salida (la cámara baja continuamente)
        var tCamera = clamp01((p - 21.7) / 3.0);
        var textY = 95 - (ease(tCamera) * 195);
        var contentY = Math.min(0, textY - slideY);"""

    # Because of encoding (cámara, Translación), we should use regex or careful matching
    # I will replace specific small lines instead to avoid encoding issues.

    lines_to_replace = {
        "var slideY = (1 - ease(tSlide)) * 130;": "var slideY = (1 - ease(tSlide)) * 95;",
        "var _txtY = 130 - (ease(_tCam) * 230);": "var _txtY = 95 - (ease(_tCam) * 195);",
        "window._scrollUpVh = 130 - slideY;": "window._scrollUpVh = 95 - slideY;",
        "var textY = 130 - (ease(tCamera) * 230);": "var textY = 95 - (ease(tCamera) * 195);"
    }

    for old, new in lines_to_replace.items():
        content = content.replace(old, new)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
