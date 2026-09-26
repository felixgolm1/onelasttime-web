import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Move left text higher up to reduce the gap with 'conecta'
    content = content.replace(
        '<div id="oryzo-text-left" style="flex:1; align-self: flex-start; margin-top: 30vh;">',
        '<div id="oryzo-text-left" style="flex:1; align-self: flex-start; margin-top: 15vh;">'
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
