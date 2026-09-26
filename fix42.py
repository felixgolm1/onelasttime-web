import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'var slideY = \(1 - ease\(tSlide\)\) \* 130;\s*// La pantalla se queda anclada\s*oryzoSec\.style\.transform = \'translateY\(\' \+ slideY \+ \'vh\)\';'
    
    replacement = '''var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var slideStart = isMobileLayout ? 80 : 130;
        var slideY_logical = (1 - ease(tSlide)) * 130;
        var slideY = (1 - ease(tSlide)) * slideStart;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh);'''
    
    content = re.sub(pattern, replacement, content)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
