import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure margin-top is 75vh
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 75vh !important; } }',
        content
    )

    # 2. Fix the JS to just add _cntY homogenously (no Math.max, no boxEnterY)
    old_js = """var boxTotalY = (tExitBox * 80);
          if (isMob) { boxTotalY += Math.max(-30, _cntY); }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
          
    new_js = """var boxTotalY = (tExitBox * 80);
          if (isMob) { boxTotalY += _cntY; }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
