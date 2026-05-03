import re

with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update maxProg
html = html.replace('const maxProg = 8.34;', 'const maxProg = 10.14;')

# 2. Add c4_peek logic
c3_peek_str = "let c3_peek = mapRange(prog, 6.02, 6.52, 0, 1);"
if c3_peek_str in html:
    c4_peek_str = c3_peek_str + "\n\n      // Fases CARTA 4\n      let c4_peek = mapRange(prog, 7.82, 8.32, 0, 1);"
    html = html.replace(c3_peek_str, c4_peek_str)
else:
    print("Could not find c3_peek")

# 3. Add c4 selector
c3_sel_str = "const c3 = mainDeck.querySelector('.card-n3') || document.querySelector('.card-on-table.card-n3');"
if c3_sel_str in html:
    c4_sel_str = c3_sel_str + "\n      const c4 = mainDeck.querySelector('.card-n4') || document.querySelector('.card-on-table.card-n4');"
    html = html.replace(c3_sel_str, c4_sel_str)
else:
    print("Could not find c3 selector")

# 4. Duplicate rev3 logic for rev4
rev3StartStr = "const rev3 = document.getElementById('review-panel-3');"
rev3Start = html.find(rev3StartStr)

rev3EndStr = "// Lógica Extracción CARTA 1"
rev3End = html.find(rev3EndStr, rev3Start)

if rev3Start != -1 and rev3End != -1:
    rev3Block = html[rev3Start:rev3End]
    
    rev4Block = rev3Block.replace('rev3', 'rev4')
    rev4Block = rev4Block.replace('review-panel-3', 'review-panel-4')
    rev4Block = rev4Block.replace('6.52', '8.32')
    rev4Block = rev4Block.replace('8.12', '9.92')
    
    html = html[:rev3End] + rev4Block + '\n      ' + html[rev3End:]
else:
    print("Could not find rev3 block")

# 5. Duplicate c3 extraction logic for c4
c3StartStr = "// Lógica de extracción de c3"
c3Start = html.find(c3StartStr)

tableCardsFadeStr = "// ─ Fade de cartas en la mesa"
c3End = html.find(tableCardsFadeStr, c3Start)

if c3Start != -1 and c3End != -1:
    while html[c3End-1] in [' ', '\n']:
        c3End -= 1
        
    c3Block = html[c3Start:c3End]
    
    c4Block = c3Block.replace('c3', 'c4')
    c4Block = c4Block.replace('fakeCard3', 'fakeCard4')
    c4Block = c4Block.replace('nth-child(2)', 'nth-child(3)')
    
    # We must be careful not to double replace if values overlap.
    # Fortunately, the values we need to replace are all distinct floats as strings.
    # Let's map them safely.
    # 6.52 -> 8.32
    # 6.92 -> 8.72
    # 7.32 -> 9.12
    # 7.82 -> 9.62
    # 8.42 -> 10.22
    # 6.82 -> 8.62
    # 7.02 -> 8.82
    # 7.62 -> 9.42
    
    mapping = {
        '6.52': '8.32',
        '6.92': '8.72',
        '7.32': '9.12',
        '7.82': '9.62',
        '8.42': '10.22',
        '6.82': '8.62',
        '7.02': '8.82',
        '7.62': '9.42'
    }
    
    # Simple regex replace to only match the exact numbers
    for old_val, new_val in mapping.items():
        c4Block = re.sub(r'(?<!\d)' + re.escape(old_val) + r'(?!\d)', new_val, c4Block)
    
    html = html[:c3End] + '\n\n      ' + c4Block + html[c3End:]
else:
    print("Could not find c3 block")

with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Patched 4th card successfully")
