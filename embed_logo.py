import base64

# Lee el logo PNG
with open('assets/img/logo one last time verde.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

data_url = 'data:image/png;base64,' + b64

# Lee el HTML
html = open('3d-test.html', 'r', encoding='utf-8', errors='replace').read()

# 1. Agrega LOGO_VERDE_IMG justo antes de OLT_LOGO
old_olt = '  const OLT_LOGO = new Image();'
new_block = (
    '  // Logo verde embebido como data URL (evita CORS/taint en file://)\n'
    '  const LOGO_VERDE_IMG = (function(){\n'
    '    const img = new Image();\n'
    "    img.src = '" + data_url + "';\n"
    '    return img;\n'
    '  })();\n'
    '  const OLT_LOGO = new Image();'
)

if old_olt in html:
    html = html.replace(old_olt, new_block, 1)
    print('OLT_LOGO block replaced')
else:
    print('WARNING: OLT_LOGO not found')

# 2. Actualiza makeCardFrontTex
lines = html.split('\n')
start = None
for i, line in enumerate(lines):
    if 'function makeCardFrontTex()' in line:
        start = i
        break

depth = 0
end = None
for i in range(start, len(lines)):
    depth += lines[i].count('{') - lines[i].count('}')
    if depth == 0 and i > start:
        end = i
        break

print(f'makeCardFrontTex: lines {start+1}-{end+1}')

new_func = (
    '  function makeCardFrontTex() {\n'
    '    const W = 760, H = 468;\n'
    "    const c = document.createElement('canvas');\n"
    '    c.width = W; c.height = H;\n'
    "    const ctx = c.getContext('2d');\n"
    "    ctx.fillStyle = '#151515';\n"
    '    ctx.fillRect(0, 0, W, H);\n'
    '    if (LOGO_VERDE_IMG.naturalWidth > 0) {\n'
    '      const lH = 68;\n'
    '      const lW = LOGO_VERDE_IMG.naturalWidth * lH / LOGO_VERDE_IMG.naturalHeight;\n'
    '      ctx.drawImage(LOGO_VERDE_IMG, (W - lW) / 2, 140, lW, lH);\n'
    '    } else {\n'
    "      ctx.fillStyle = '#ccff00';\n"
    "      ctx.textAlign = 'center';\n"
    "      ctx.textBaseline = 'middle';\n"
    "      ctx.font = 'italic bold 44px Georgia, serif';\n"
    "      ctx.fillText('One Last Time', W / 2, 180);\n"
    '    }\n'
    "    ctx.fillStyle = '#ffffff';\n"
    "    ctx.textAlign = 'center';\n"
    "    ctx.textBaseline = 'middle';\n"
    "    ctx.font = 'bold 28px Arial, sans-serif';\n"
    "    ctx.fillText('SI LAS CONVERSACIONES NOS UNEN,', W / 2, 290);\n"
    "    ctx.fillText('HAG\u00c1MOSLAS INOLVIDABLES', W / 2, 340);\n"
    '    const tex = new THREE.CanvasTexture(c);\n'
    '    tex.needsUpdate = true;\n'
    '    return tex;\n'
    '  }'
)

lines[start:end+1] = [new_func]
open('3d-test.html', 'w', encoding='utf-8').write('\n'.join(lines))
print('Done - logo embedded as base64 data URL')
