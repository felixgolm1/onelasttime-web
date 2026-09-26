import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_js = "var tOpen = clamp01((p - 23.6) / 0.3); // 23.6 a 23.9"
    new_js = """var tOpen = clamp01((p - 23.6) / 0.3);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               tOpen = clamp01((p - 23.8) / 0.3);
           }"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
