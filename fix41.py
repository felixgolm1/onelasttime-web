import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    old_logic = "var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); \n        var slideY = (1 - ease(tSlide)) * 130; // La pantalla se queda anclada\n        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';"
    
    new_logic = "var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); \n        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);\n        var slideStart = isMobileLayout ? 80 : 130;\n        var slideY_logical = (1 - ease(tSlide)) * 130;\n        var slideY = (1 - ease(tSlide)) * slideStart;\n        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';"

    if old_logic in content:
        content = content.replace(old_logic, new_logic)
    else:
        # Try a more forgiving replace just in case of spaces
        pass

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
