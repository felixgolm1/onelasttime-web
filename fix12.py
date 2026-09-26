import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change margin-top to 75vh
    content = content.replace(
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 8vh !important; } }',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 75vh !important; } }'
    )

    # 2. Update the JS block to move with _cntY fully (speed 1.0)
    old_js = """boxEnterY = (1 - boxDelayProg) * 110;
        }
        var boxTotalY = boxEnterY + (tExitBox * 80);
        oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""
        
    new_js = """boxEnterY = (1 - boxDelayProg) * 70;
        }
        var boxTotalY = boxEnterY + (tExitBox * 80);
        if (isMob) { boxTotalY += _cntY; }
        oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
