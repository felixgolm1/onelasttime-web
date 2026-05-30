import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if 'Contenedor de' in line and 'Cinem' in line:
        start_idx = i
        break

if start_idx != -1:
    for i in range(start_idx + 1, len(lines)):
        # Buscamos el final justo antes del script que divide el texto en caracteres
        if '<script>' in lines[i] and 'Dividir texto en caracteres' in lines[i+1]:
            # Retrocedemos un par de líneas para borrar solo el contenedor
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx]

content = "".join(lines)

bad_open = "let openP = Math.max(0, Math.min(1, (prog - 2.2) / 0.4));"
good_open = "let openP = 0; // ANULADO para que la caja no se abra en los testimonios"
content = content.replace(bad_open, good_open)

content = content.replace('if (prog > 10.02) {', 'if (prog > 2.6) {')

jump_logic = '''function smoothScrollLoop() {
        const lerpF = 0.40;
        
        // SALTO CUÁNTICO DE TIMELINE
        if (targetProg > 2.6 && targetProg < 9.62) {
            if (prog <= 2.6) {
                targetProg = 9.62;
                prog = 9.62;
            } else {
                targetProg = 2.6;
                prog = 2.6;
            }
        }
'''
content = re.sub(r'function smoothScrollLoop\(\) \{\s*const lerpF = 0\.40;', jump_logic, content)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Absolute Zero Patch v3 aplicado con precisión de milímetro.")
