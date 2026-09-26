import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_logic = """        // 1. Translación fluida de la sección (hasta el centro de la pantalla)
        var tSlide = clamp01((p - 21.7) / 1.6); // Termina en 23.3, justo cuando empieza a abrirse
        // Empieza a bajar (38.6) con el carrusel y termina de desaparecer del todo (40.76)
        var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); 
        var slideY = (1 - ease(tSlide)) * 130; // La pantalla se queda anclada
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';"""

    new_logic = """        // 1. Translación fluida de la sección (hasta el centro de la pantalla)
        var tSlide = clamp01((p - 21.7) / 1.6); // Termina en 23.3, justo cuando empieza a abrirse
        // Empieza a bajar (38.6) con el carrusel y termina de desaparecer del todo (40.76)
        var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); 
        
        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var slideStart = isMobileLayout ? 80 : 130;
        var slideY_logical = (1 - ease(tSlide)) * 130; // Para el thermal overlay
        var slideY = (1 - ease(tSlide)) * slideStart;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';"""

    content = content.replace(old_logic, new_logic)

    # Now update scrollUpVh and tCamera
    old_cam = """        // Sincronizamos el fondo morado 
        window._scrollUpVh = 130 - slideY;
        // Fase de salida (la cámara baja continuamente)
        var tCamera = clamp01((p - 21.7) / 3.0);
        var textY = 130 - (ease(tCamera) * 230);
        var contentY = Math.min(0, textY - slideY);"""

    new_cam = """        // Sincronizamos el fondo morado usando la variable logica para no romper el thermal overlay
        window._scrollUpVh = 130 - slideY_logical;
        // Fase de salida (la cámara baja continuamente)
        var tCamera = clamp01((p - 21.7) / 3.0);
        var textDist = isMobileLayout ? 180 : 230;
        var textY = slideStart - (ease(tCamera) * textDist);
        var contentY = Math.min(0, textY - slideY);"""

    content = content.replace(old_cam, new_cam)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
