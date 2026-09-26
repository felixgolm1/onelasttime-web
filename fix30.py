import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Set margin-top to 63vh to fix the 1cm gap physically
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 63vh !important; } }',
        content
    )

    # 2. Adjust clamp to -69.5 so it stops EXACTLY at -6.5vh final position
    content = content.replace(
        'boxTotalY += Math.max(-66.5, _cntY);',
        'boxTotalY += Math.max(-69.5, _cntY);'
    )

    # 3. Delay tOpen to 24.0 so it waits until the text is out of the way
    old_js = """var tOpen = clamp01((p - 23.6) / 0.3);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               tOpen = clamp01((p - 23.8) / 0.3);
           }"""
    new_js = """var tOpen = clamp01((p - 23.6) / 0.3);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               tOpen = clamp01((p - 24.0) / 0.2); // Abre muy rapido justo cuando se queda solo
           }"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
