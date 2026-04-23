import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = {
    'animReady = true present': 'animReady = true' in text,
    '_runIntroAnim present': '_runIntroAnim' in text,
    'startIntroAnim present': 'startIntroAnim' in text,
    'No dangling corrupt line': 'con z-index:10004 (por encima' not in text or '// ' + 'con z-index:10004' in text,
    'DEBUG_PANEL absent': 'DEBUG_PANEL' not in text,
    'sc-title present (HTML)': '<h2 id="sc-title"' in text,
    '4 PASOS in makeCardBackTex': "ctx.fillText('4 PASOS'" in text,
    'targetRect uses morphGroup': "const targetRect = morphGroup.getBoundingClientRect();" in text,
}

for check, result in checks.items():
    status = 'OK' if result else 'FAIL'
    print(f'[{status}] {check}')

# Also check no JS syntax errors - count script blocks
script_blocks = re.findall(r'<script.*?>(.*?)</script>', text, re.DOTALL)
print(f'\n{len(script_blocks)} script blocks found')
for i, b in enumerate(script_blocks):
    count = 0
    for c in b:
        if c == '{': count += 1
        elif c == '}': count -= 1
    print(f'  Block {i}: brackets {"OK" if count == 0 else "UNBALANCED (" + str(count) + ")"}, {len(b)} chars')
