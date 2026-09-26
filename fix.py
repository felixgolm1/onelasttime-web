import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. E_TOP
    content = content.replace(
        'var S_TOP = 48,  E_TOP = 27;',
        'var S_TOP = 48,  E_TOP = (window.innerWidth <= 768 || window._cIsMobile) ? 16 : 27;'
    )

    # 2. E_LEFT
    content = content.replace(
        'var S_LEFT = 50, E_LEFT = 72;',
        'var S_LEFT = 50, E_LEFT = (window.innerWidth <= 768 || window._cIsMobile) ? 67 : 72;'
    )

    # 3. txtP
    content = content.replace(
        'var txtP = clamp01((65 - slideY) / 40);',
        'var startL = (window.innerWidth <= 768 || window._cIsMobile) ? 51 : 65;\n        var txtP = clamp01((startL - slideY) / 40);'
    )

    # 4. txtPR
    content = content.replace(
        'var txtPR = clamp01((40 - slideY) / 40);',
        'var startR = (window.innerWidth <= 768 || window._cIsMobile) ? 18 : 40;\n        var txtPR = clamp01((startR - slideY) / startR);'
    )

    # 5. Right text alignment & transform
    content = content.replace(
        '#oryzo-text-right { text-align: right !important; }',
        '#oryzo-text-right { text-align: right !important; position: relative !important; left: -67px !important; }\n    #oryzo-text-right-gradient { text-align: right !important; width: 100% !important; transform-origin: right center !important; }'
    )

    # Remove the JS overwrite of transformOrigin
    content = content.replace(
        'textGradR.style.transformOrigin = "left center";',
        ''
    )

    # 6. Change escuchales to escuchalxs (with correct unicode)
    content = content.replace(
        'escúchales a ellxs',
        'escúchalxs a ellxs'
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
