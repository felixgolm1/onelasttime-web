import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the slide logic block and inject our clip-path logic.
# The block looks like this:
'''
        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var travelDist = isMobileLayout ? 95 : 130;
        
        var slideY = (1 - ease(tSlide)) * travelDist;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
'''

target = '''        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var travelDist = isMobileLayout ? 95 : 130;
        
        var slideY = (1 - ease(tSlide)) * travelDist;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';'''

replacement = '''        var isMobileLayout = (window.innerWidth <= 768 || window._cIsMobile);
        var travelDist = isMobileLayout ? 95 : 130;
        
        var slideY = (1 - ease(tSlide)) * travelDist;
        oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
        
        // CROP THERMAL OVERLAY DYNAMICALLY TO AVOID OVERLAP IN MOBILE
        var _thOvr = document.getElementById('thermal-overlay');
        if (_thOvr) {
            if (isMobileLayout) {
                var cropVh = tSlide * 35; // gradually crop up to 35vh
                _thOvr.style.clipPath = 'inset(0 0 ' + cropVh.toFixed(2) + 'vh 0)';
            } else {
                _thOvr.style.clipPath = 'none';
            }
        }'''

if target in content:
    content = content.replace(target, replacement)
else:
    print('TARGET NOT FOUND!')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
