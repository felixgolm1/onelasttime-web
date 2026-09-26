import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the #thermal-overlay css injection
target = '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 63vh !important; } #conecta-transition-text { top: 15vh !important; } #thermal-overlay { height: 95vh !important; } }'
replacement = '@media (max-width: 768px) { #oryzo-deck-container { margin-top: 61.5vh !important; } #conecta-transition-text { top: 15vh !important; } }'

content = content.replace(target, replacement)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
