import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_lines = []
in_bad_block = False
for i, line in enumerate(lines):
    if "Anti-deformaci" in line or "Anti-deformación" in line:
        in_bad_block = True
        continue
    
    if in_bad_block:
        if "if (heroCta) {" in line:
            in_bad_block = False
            # Insert the clean code right here
            clean_lines.append("        // Anti-deformación del texto: contrarrestamos la escala del padre pero aplicamos un aumento proporcional\n")
            clean_lines.append("        const faceLeftSpan = mainDeck.querySelector('.face-left span');\n")
            clean_lines.append("        if (faceLeftSpan) {\n")
            clean_lines.append("            let textScale = 1;\n")
            clean_lines.append("            if (transP >= 0.4) {\n")
            clean_lines.append("                let tScaleText = Math.max(0, Math.min(1, (transP - 0.4) / 0.45));\n")
            clean_lines.append("                textScale = 1 + (1.2 * tScaleText); // Crece hasta un 2.2x de su tamaño original\n")
            clean_lines.append("            }\n")
            clean_lines.append("            // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.\n")
            clean_lines.append("            faceLeftSpan.style.transform = `rotate(90deg) scaleX(${textScale/boxScaleY}) scaleY(${textScale/boxScaleX})`;\n")
            clean_lines.append("        }\n\n")
            clean_lines.append(line)
        continue
    
    clean_lines.append(line)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(clean_lines)

print("Cleaned file.")
