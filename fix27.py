import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The current code block:
    #             var totalYForBox = slideY + _cntY;
    #             var boxDelayProg = clamp01(((-5) - totalYForBox) / 30); 
    #             boxEnterY = (1 - boxDelayProg) * 110;
    #         }
    #         var boxTotalY = boxEnterY + (tExitBox * 80);
    #         oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';

    content = re.sub(
        r'var boxDelayProg = clamp01\(\(\(-5\) - totalYForBox\) / 30\); \s*boxEnterY = \(1 - boxDelayProg\) \* 110;\s*\}\s*var boxTotalY = boxEnterY \+ \(tExitBox \* 80\);\s*oryzoDeck\.style\.transform = \'translateY\(\' \+ boxTotalY \+ \'vh\)\';',
        '''var boxDelayProg = clamp01(((-5) - totalYForBox) / 30);
              // boxEnterY = (1 - boxDelayProg) * 110;
          }
          var boxTotalY = (tExitBox * 80);
          if (isMob) {
              boxTotalY += Math.max(-81.5, _cntY);
          } else {
              boxTotalY += boxEnterY;
          }
          oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';''',
        content,
        flags=re.DOTALL
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
