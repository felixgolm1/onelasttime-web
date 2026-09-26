import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 21 to 33 for exitStartR
    old_exitProgR = 'var exitStartR = (window.innerWidth <= 768 || window._cIsMobile) ? 21 : 15;'
    new_exitProgR = 'var exitStartR = (window.innerWidth <= 768 || window._cIsMobile) ? 33 : 15;'
    content = content.replace(old_exitProgR, new_exitProgR)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
