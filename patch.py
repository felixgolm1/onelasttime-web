import re

with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. DUPLICATE rev2 logic for rev3
rev2StartStr = "const rev2 = document.getElementById('review-panel-2');"
rev2Start = html.find(rev2StartStr)

rev2EndStr = "// Lógica Extracción CARTA 1"
rev2End = html.find(rev2EndStr, rev2Start)

if rev2Start != -1 and rev2End != -1:
    rev2Block = html[rev2Start:rev2End]
    
    rev3Block = rev2Block.replace('rev2', 'rev3')
    rev3Block = rev3Block.replace('review-panel-2', 'review-panel-3')
    rev3Block = rev3Block.replace('4.72', '6.52')
    rev3Block = rev3Block.replace('6.32', '8.12')
    
    html = html[:rev2End] + rev3Block + '\n      ' + html[rev2End:]
else:
    print("Could not find rev2 block")

# 2. DUPLICATE c2 extraction logic for c3
c2StartStr = "// Lógica de extracción de c2"
c2Start = html.find(c2StartStr)

tableCardsFadeStr = "// ─ Fade de cartas en la mesa"
c2End = html.find(tableCardsFadeStr, c2Start)

if c2Start != -1 and c2End != -1:
    while html[c2End-1] in [' ', '\n']:
        c2End -= 1
        
    c2Block = html[c2Start:c2End]
    
    c3Block = c2Block.replace('c2', 'c3')
    c3Block = c3Block.replace('fakeCard2', 'fakeCard3')
    c3Block = c3Block.replace('nth-child(1)', 'nth-child(2)')
    
    c3Block = c3Block.replace('4.72', '6.52')
    c3Block = c3Block.replace('5.12', '6.92')
    c3Block = c3Block.replace('5.52', '7.32')
    c3Block = c3Block.replace('6.02', '7.82')
    c3Block = c3Block.replace('6.62', '8.42')
    c3Block = c3Block.replace('5.02', '6.82')
    c3Block = c3Block.replace('5.22', '7.02')
    c3Block = c3Block.replace('5.82', '7.62')
    
    html = html[:c2End] + '\n\n      ' + c3Block + html[c2End:]
else:
    print("Could not find c2 block")

with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Patched successfully")
