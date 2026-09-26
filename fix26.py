import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure margin-top is 75vh for the box in mobile
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 75vh !important; } }',
        content
    )

    # 2. Fix the JS to move homogenously with _cntY and clamp at -81.5
    # The current code in 65d9dab is:
    # var boxDelayProg = clamp01(((-5) - totalYForBox) / 30);
    # var boxEnterY = 0;
    # if (isMob) {
    #     boxEnterY = (1 - boxDelayProg) * 110;
    # }
    # var boxTotalY = boxEnterY + (tExitBox * 80);
    
    old_js = """var boxDelayProg = clamp01(((-5) - totalYForBox) / 30);
          var boxEnterY = 0;
          if (isMob) {
              boxEnterY = (1 - boxDelayProg) * 110;
          }
          var boxTotalY = boxEnterY + (tExitBox * 80);
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    new_js = """var boxDelayProg = clamp01(((-5) - totalYForBox) / 30);
          var boxEnterY = 0;
          var boxTotalY = (tExitBox * 80);
          if (isMob) {
              boxTotalY += Math.max(-81.5, _cntY);
          } else {
              boxTotalY += boxEnterY;
          }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
