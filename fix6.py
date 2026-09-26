import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_transform = "oryzoDeck.style.transform = 'translateY(' + (tExitBox * 80) + 'vh)';"
    
    new_transform = """var isMob = window.innerWidth <= 768 || window._cIsMobile;
        var boxEnterY = 0;
        if (isMob) {
            var totalYForBox = slideY + (typeof contentY !== 'undefined' ? contentY : 0);
            var boxDelayProg = clamp01(((-5) - totalYForBox) / 30); 
            boxEnterY = (1 - boxDelayProg) * 110;
        }
        var boxTotalY = boxEnterY + (tExitBox * 80);
        oryzoDeck.style.transform = 'translateY(' + boxTotalY + 'vh)';"""

    content = content.replace(old_transform, new_transform)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
