import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        'if (isMob) { boxTotalY += _cntY; }',
        'if (isMob) { boxTotalY += Math.max(-29.5, _cntY); }'
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
