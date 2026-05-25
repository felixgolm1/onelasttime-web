import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace wheel listener
old_wheel = '''      window.addEventListener('wheel', e => {
        e.preventDefault();
        const cappedDY = Math.sign(e.deltaY) * Math.min(Math.abs(e.deltaY), 60);
        // Reducimos el divisor (de 1200 a 900) para un scroll general mǭs ǭgil
        const divisor  = targetProg < 0.08 ? 8000 : 900;
        let rawDelta = cappedDY / divisor;'''

new_wheel = '''      window.addEventListener('wheel', e => {
        e.preventDefault();
        const cappedDY = Math.sign(e.deltaY) * Math.min(Math.abs(e.deltaY), 60);
        // Divisor dinamico: scroll normal a 900, pero el TRIPLE de lento (2700) en los 4 pasos para dar mas espacio
        let divisor = 900;
        if (targetProg < 0.08) divisor = 8000;
        else if (targetProg >= 2.5 && targetProg <= 9.62) divisor = 2700;
        
        let rawDelta = cappedDY / divisor;'''

# Handle encoding issues by doing a line by line replacement logic or regex
import re
content = re.sub(r'const divisor\s*=\s*targetProg < 0\.08 \? 8000 : 900;', 'let divisor = 900;\n        if (targetProg < 0.08) divisor = 8000;\n        else if (targetProg >= 2.5 && targetProg <= 9.62) divisor = 2700;', content)


content = re.sub(r'const divisorT\s*=\s*targetProg < 0\.08 \? 4000 : 450;[^\n]*', 'let divisorT = 450;\n        if (targetProg < 0.08) divisorT = 4000;\n        else if (targetProg >= 2.5 && targetProg <= 9.62) divisorT = 1350;', content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
