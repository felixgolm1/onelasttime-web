import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. txtPR change (fade-in 50% slower, using totalY)
    old_txtPR = 'var txtPR = clamp01((startR - slideY) / startR);'
    new_txtPR = 'var durR = (window.innerWidth <= 768 || window._cIsMobile) ? 15 : 40;\n        var txtPR = clamp01((startR - (slideY + contentY)) / durR);'
    content = content.replace(old_txtPR, new_txtPR)

    # 2. exitProgR change (fade-out 1cm higher / 5 units more in contentY)
    old_exitProgR = 'var exitProgR = Math.max(0, Math.min(1, (Math.abs(contentY) - 15) / 40));'
    new_exitProgR = 'var exitStartR = (window.innerWidth <= 768 || window._cIsMobile) ? 21 : 15;\n             var exitProgR = Math.max(0, Math.min(1, (Math.abs(contentY) - exitStartR) / 40));'
    content = content.replace(old_exitProgR, new_exitProgR)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
