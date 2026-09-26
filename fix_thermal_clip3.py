import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"oryzoSec\.style\.transform = 'translateY\(' \+ slideY \+ 'vh\)';"
replacement = '''oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';
        
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

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
else:
    print('TARGET NOT FOUND 3!')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
