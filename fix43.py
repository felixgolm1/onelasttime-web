import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        "oryzoSec.style.transform = 'translateY(' + slideY + 'vh);",
        "oryzoSec.style.transform = 'translateY(' + slideY + 'vh)';"
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
