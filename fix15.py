import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply the Math.max clamping to boxTotalY
    old_js = """var boxTotalY = (tExitBox * 80);
          if (isMob) { boxTotalY += _cntY; }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
          
    new_js = """var boxTotalY = (tExitBox * 80);
          if (isMob) { boxTotalY += Math.max(-30, _cntY); }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
