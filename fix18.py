import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace oxTotalY += Math.max(-30, _cntY); with oxTotalY += _cntY;
    content = content.replace(
        'if (isMob) { boxTotalY += Math.max(-30, _cntY); }',
        'if (isMob) { boxTotalY += _cntY; }'
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
