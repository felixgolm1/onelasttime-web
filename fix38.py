import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Revert left text to 30vh
    content = content.replace(
        '<div id="oryzo-text-left" style="flex:1; align-self: flex-start; margin-top: 15vh;">',
        '<div id="oryzo-text-left" style="flex:1; align-self: flex-start; margin-top: 30vh;">'
    )

    # 2. Add media query to push conecta down by 15vh on mobile
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: 63vh !important; \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 63vh !important; } #conecta-transition-text { top: 15vh !important; } }',
        content
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
