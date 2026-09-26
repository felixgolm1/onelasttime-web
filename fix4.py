import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_to_add = '\n  @media (max-width: 768px) { #oryzo-deck-container { margin-top: 20vh !important; } }\n'
    
    # Insert right after #oryzo-text-right-gradient rule
    target = ' margin-right: 0 !important; }'
    content = content.replace(target, target + css_to_add)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
