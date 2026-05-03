import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = "const loaderBar = document.getElementById('loader-bar');"
replacement = "let globalGlbCard = null;\n  let cardCanvasEl = null;\n  " + target

content = content.replace(target, replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 7 done")
