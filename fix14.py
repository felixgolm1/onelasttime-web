import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the boxEnterY logic
    content = re.sub(r'var boxEnterY = 0;\s*if \(isMob\) \{\s*var _tCam = clamp01\(\(p - 21\.7\) / 3\.0\);\s*var _txtY = 130 - \(ease\(_tCam\) \* 230\);\s*var _cntY = Math\.min\(0, _txtY - slideY\);\s*var totalYForBox = slideY \+ _cntY;\s*var boxDelayProg = clamp01\(\(\(-5\) - totalYForBox\) / 30\); \s*boxEnterY = \(1 - boxDelayProg\) \* 70;\s*\}\s*var boxTotalY = boxEnterY \+ \(tExitBox \* 80\);', 'if (isMob) {\n            var _tCam = clamp01((p - 21.7) / 3.0);\n            var _txtY = 130 - (ease(_tCam) * 230);\n            var _cntY = Math.min(0, _txtY - slideY);\n        }\n        var boxTotalY = (tExitBox * 80);', content)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
