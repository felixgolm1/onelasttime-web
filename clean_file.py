import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    # If we are in the corrupted block, skip lines
    if i >= 4846 and i <= 4863:
        if i == 4846:
            # Insert the clean code
            new_lines.append("        // Anti-deformación del texto: contrarrestamos la escala del padre pero aplicamos un aumento proporcional\n")
            new_lines.append("        const faceLeftSpan = mainDeck.querySelector('.face-left span');\n")
            new_lines.append("        if (faceLeftSpan) {\n")
            new_lines.append("            let textScale = 1;\n")
            new_lines.append("            if (transP >= 0.4) {\n")
            new_lines.append("                let tScaleText = Math.max(0, Math.min(1, (transP - 0.4) / 0.45));\n")
            new_lines.append("                textScale = 1 + (1.2 * tScaleText); // Crece hasta un 2.2x de su tamaño original\n")
            new_lines.append("            }\n")
            new_lines.append("            // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.\n")
            new_lines.append("            faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();\n")
            new_lines.append("        }\n")
        continue
    
    # Remove the misplaced injection at 4793-4803 (roughly)
    if "Anti-deformación del texto: contrarrestamos la escala del padre pero aplicamos un aumento proporcional" in line and i < 4846:
        skip = True
    
    if skip:
        if "faceLeftSpan.style.transform =" in line:
            skip = False
        elif "}" in line and lines[i-1].strip().startswith("faceLeftSpan"):
            skip = False
        continue

    new_lines.append(line)

# Wait, let's just do a clean pass over the file and remove all instances of the anti-deformation block,
# then insert it back right before "if (heroCta) {"

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
            clean_lines.append("\n        // Anti-deformación del texto: contrarrestamos la escala del padre pero aplicamos un aumento proporcional\n")
            clean_lines.append("        const faceLeftSpan = mainDeck.querySelector('.face-left span');\n")
            clean_lines.append("        if (faceLeftSpan) {\n")
            clean_lines.append("            let textScale = 1;\n")
            clean_lines.append("            if (transP >= 0.4) {\n")
            clean_lines.append("                let tScaleText = Math.max(0, Math.min(1, (transP - 0.4) / 0.45));\n")
            clean_lines.append("                textScale = 1 + (1.2 * tScaleText); // Crece hasta un 2.2x de su tamaño original\n")
            clean_lines.append("            }\n")
            clean_lines.append("            // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.\n")
            clean_lines.append("            faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();\n")
            clean_lines.append("        }\n\n")
            clean_lines.append(line)
        continue
    
    clean_lines.append(line)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(clean_lines)

print("Cleaned file.")
