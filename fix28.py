import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Move box up by 15vh to close the gap
    content = re.sub(
        r'@media \(max-width: 768px\) \{ #oryzo-deck-container \{ margin-top: [^\}]+ \} \}',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 60vh !important; } }',
        content
    )

    # Adjust clamp to maintain the exact final position (-6.5vh)
    content = content.replace(
        'boxTotalY += Math.max(-81.5, _cntY);',
        'boxTotalY += Math.max(-66.5, _cntY);'
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
