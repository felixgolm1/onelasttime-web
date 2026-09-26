import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Force the margin to 75vh
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 75vh !important; } }',
        content
    )

    # Force the box to clamp at -30
    content = re.sub(
        r'if \(isMob\) \{ boxTotalY \+= [^;]+; \}',
        'if (isMob) { boxTotalY += Math.max(-30, _cntY); }',
        content
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
