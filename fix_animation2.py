with open("3d-test.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_ciencia = False
in_reset = False

for i, line in enumerate(lines):
    if '// 3. CIENCIA - slide UP como "RISE" en Oryzo' in line:
        in_ciencia = True
        new_lines.append('              // 3. CIENCIA - slide UP escalonado\n')
        new_lines.append('              { const baseP = Math.min(Math.max(mapRange(exitP, 0.05, 0.55, 0, 1), 0), 1);\n')
        new_lines.append('                const globalOpacity = Math.max(0, 1 - mapRange(baseP, 0.2, 1.0, 0, 1));\n')
        new_lines.append("                applyExit('mag-ciencia', '', globalOpacity);\n")
        new_lines.append('                document.querySelectorAll(\'[id="mag-ciencia"]\').forEach(container => {\n')
        new_lines.append("                  container.querySelectorAll('.ciencia-letter').forEach((letter, idx) => {\n")
        new_lines.append('                    const stagger = idx * 0.08;\n')
        new_lines.append('                    const startP = stagger;\n')
        new_lines.append('                    const endP = 0.5 + stagger;\n')
        new_lines.append('                    const letterP = Math.min(Math.max(mapRange(exitP, startP, endP, 0, 1), 0), 1);\n')
        new_lines.append('                    const easeUp = 1 - Math.pow(1 - letterP, 2);\n')
        new_lines.append('                    letter.style.transform = 	ranslateY(px);\n')
        new_lines.append('                  });\n')
        new_lines.append('                });\n')
        new_lines.append('              }\n')
        continue
    
    if in_ciencia:
        if '}' in line and 'applyExit' not in line and 'easeUp' not in line and 'mapRange' not in line:
            in_ciencia = False # done skipping
        continue

    if "['mag-saber-mas','mag-natgeo','mag-ciencia','mag-col-left','mag-col-right','mag-bottom'].forEach(id => {" in line:
        in_reset = True
        new_lines.append(line)
        continue
        
    if in_reset:
        if '});' in line and lines[i+1].strip() == '}':
            new_lines.append(line)
            new_lines.append("              document.querySelectorAll('.ciencia-letter').forEach(el => el.style.transform = '');\n")
            in_reset = False
            continue
            
    new_lines.append(line)

with open("3d-test.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)