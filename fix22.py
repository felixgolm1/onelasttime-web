import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Set margin-top to 45vh exactly where they want it fixed
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 45vh !important; } }',
        content
    )

    # Remove _cntY completely so it stays perfectly fixed at 45vh
    old_js = """var boxTotalY = (tExitBox * 80);
          if (isMob) { boxTotalY += _cntY; }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
          
    new_js = """var boxTotalY = (tExitBox * 80);
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
