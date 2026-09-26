import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure margin-top is 75vh for the box
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 75vh !important; } }',
        content
    )

    # 2. Fix the Box JS to clamp at -30
    old_box_js = """var boxTotalY = (tExitBox * 80);
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
          
    new_box_js = """var boxTotalY = (tExitBox * 80);
          if (isMob) { boxTotalY += Math.max(-30, _cntY); }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
    content = content.replace(old_box_js, new_box_js)

    # 3. Clamp the Right Text transform at -30
    old_text_js = """if (oryzoTxtR) oryzoTxtR.style.transform = 'translateY(' + contentY + 'vh)';"""
    new_text_js = """if (oryzoTxtR) {
          var rTextY = (window.innerWidth <= 768 || window._cIsMobile) ? Math.max(-30, contentY) : contentY;
          oryzoTxtR.style.transform = 'translateY(' + rTextY + 'vh)';
        }"""
    content = content.replace(old_text_js, new_text_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
