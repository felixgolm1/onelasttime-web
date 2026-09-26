import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 24.0 to 23.89
    old_js = """var tOpen = clamp01((p - 23.6) / 0.3);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               tOpen = clamp01((p - 24.0) / 0.2); // Abre muy rapido justo cuando se queda solo
           }"""
           
    new_js = """var tOpen = clamp01((p - 23.6) / 0.3);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               tOpen = clamp01((p - 23.89) / 0.25); // Exigencia milimetrica
           }"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
