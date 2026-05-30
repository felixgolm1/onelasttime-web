import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Eliminar sección de reseñas HTML 1
pattern_html = re.compile(r'<!-- Contenedor de Reseñas Cinemáticas -->.*?<!-- FIN Reseñas Cinemáticas -->', re.DOTALL)
content = pattern_html.sub('<!-- FIN Reseñas Cinemáticas -->', content)

# 2. Anular la apertura de la caja y añadir volRotPre, SIN BORRAR NADA MÁS.
bad_open = "let openP = Math.max(0, Math.min(1, (prog - 2.2) / 0.4));"
good_open = '''let openP = 0; // ANULADO para que la caja no se abra.
      let volRotPre = 0;
      if (prog > 2.2 && prog <= 2.6) {
          volRotPre = mapRange(prog, 2.2, 2.6, 0, 335);
      } else if (prog > 2.6) {
          volRotPre = 335;
      }'''
content = content.replace(bad_open, good_open)

# 3. Aplicar volRotPre a volume
bad_volume = "const volume = mainDeck.querySelector('.box-3d-volume');"
good_volume = "const volume = mainDeck.querySelector('.box-3d-volume');\n      if (prog <= 2.6 && volume) volume.style.transform = `rotateY(${volRotPre}deg) rotateX(0deg) rotateZ(0deg)`;"
content = content.replace(bad_volume, good_volume)

# 4. BUGFIX ORIGINAL: Cara trasera de 4 PASOS se asomaba durante el carrusel
content = content.replace('if (prog > 10.02) {', 'if (prog > 2.6) {')

# 5. SALTO CUÁNTICO
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
content = content.replace("function smoothScrollLoop() {\n        const lerpF = 0.40;", jump_logic)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Quantum V3 aplicado con precisión de cirujano (sin borrar código necesario).")
