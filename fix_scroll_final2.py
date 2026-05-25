import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace wheel divisor
content = re.sub(
    r'let divisor = 900;\n\s*if \(targetProg < 0\.08\) divisor = 8000;\n\s*// Restauramos el "espacio" perdido de la intro \(la carta girando "4 PASOS"\)\n\s*else if \(targetProg < 0\.60\) divisor = 4500;',
    'let divisor = 900;\n        if (targetProg < 0.60) divisor = 4500;\n        else if (targetProg >= 2.5 && targetProg <= 9.62) divisor = 8000;',
    content
)

# Replace touchmove divisor
content = re.sub(
    r'let divisorT = 450;\n\s*if \(targetProg < 0\.08\) divisorT = 4000;\n\s*else if \(targetProg < 0\.60\) divisorT = 2250;',
    'let divisorT = 450;\n        if (targetProg < 0.60) divisorT = 2250;\n        else if (targetProg >= 2.5 && targetProg <= 9.62) divisorT = 4000;',
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
