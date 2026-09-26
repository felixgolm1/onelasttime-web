import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1
    content = re.sub(
        r'var tSlide = clamp01\(\(p - 21\.7\) / 1\.6\);.*var tExitBox = clamp01\(\(p - 38\.6\) / \(40\.76 - 38\.6\)\);\s*var slideY = \(1 - ease\(tSlide\)\) \* 130;\s*oryzoSec\.style\.transform = \'translateY\(\' \+ slideY \+ \'vh\)\';',
        '''var tSlide = clamp01((p - 21.7) / 1.6);
        var tExitBox = clamp01((p - 38.6) / (40.76 - 38.6)); 
        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var slideStart = isMobileLayout ? 80 : 130;
        var slideY_logical = (1 - ease(tSlide)) * 130;
        var slideY = (1 - ease(tSlide)) * slideStart;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';''',
        content,
        flags=re.DOTALL
    )

    # 2
    content = re.sub(
        r'window\._scrollUpVh = 130 - slideY;\s*.*var tCamera = clamp01\(\(p - 21\.7\) / 3\.0\);\s*var textY = 130 - \(ease\(tCamera\) \* 230\);\s*var contentY = Math\.min\(0, textY - slideY\);',
        '''window._scrollUpVh = 130 - slideY_logical;
        var tCamera = clamp01((p - 21.7) / 3.0);
        var textDist = isMobileLayout ? 180 : 230;
        var textY = slideStart - (ease(tCamera) * textDist);
        var contentY = Math.min(0, textY - slideY);''',
        content,
        flags=re.DOTALL
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
