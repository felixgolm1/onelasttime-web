import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 20vh to -5vh
    content = content.replace(
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 20vh !important; } }',
        '@media (max-width: 768px) { #oryzo-deck-container { margin-top: -5vh !important; } }'
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
