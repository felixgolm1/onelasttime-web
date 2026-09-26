import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Delay the box opening to p=23.6
    old_js = "var tOpen = clamp01((p - 23.3) / 0.3); // 23.3 a 23.6"
    new_js = "var tOpen = clamp01((p - 23.6) / 0.3); // 23.6 a 23.9"

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
