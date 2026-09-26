import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change margin-top to 8vh
    content = content.replace(
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 65vh !important; } }',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 8vh !important; } }'
    )

    # 2. Revert the JS block
    old_js = """boxEnterY = (1 - boxDelayProg) * 60;
        }
        var boxTotalY = boxEnterY + (tExitBox * 80);
        if (isMob) { boxTotalY += _cntY * 0.5; }
        oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
        
    new_js = """boxEnterY = (1 - boxDelayProg) * 110;
        }
        var boxTotalY = boxEnterY + (tExitBox * 80);
        oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
