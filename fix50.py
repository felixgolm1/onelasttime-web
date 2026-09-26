import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Make cardsOpen = 0 globally
    content = content.replace(
        'let cardsOpen = mapFlap(eOpen, 0.5, 1.0, 0, 1);',
        'let cardsOpen = 0; // mapFlap(eOpen, 0.5, 1.0, 0, 1);'
    )
    # Also remove the redundant mobile check to avoid confusion
    pattern_cardsOpen_mobile = r'\s*if\s*\(\s*window\.innerWidth\s*<=\s*768\s*\|\|\s*window\._cIsMobile\s*\)\s*\{\s*cardsOpen\s*=\s*0;\s*//\s*Evita\s*que\s*asomen\s*durante\s*la\s*apertura\s*de\s*solapas\s*\}'
    content = re.sub(pattern_cardsOpen_mobile, '', content)

    # 2. Make localP_raw globally p - 21.60
    pattern_localP = r'let localP_raw = p - 21\.1;\s*if\s*\(\s*window\.innerWidth\s*<=\s*768\s*\|\|\s*window\._cIsMobile\s*\)\s*\{\s*localP_raw\s*=\s*p - 21\.60;\s*//[^\n]+\n\s*\}'
    content = re.sub(pattern_localP, 'let localP_raw = p - 21.60;', content)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
