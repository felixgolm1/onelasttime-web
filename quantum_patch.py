import re

# 1. Leemos el archivo original puro de git
with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Eliminar sección de reseñas HTML (desde el comentario hasta el fin)
pattern_html = re.compile(r'<!-- Contenedor de Reseñas Cinemáticas -->.*?<!-- FIN Reseñas Cinemáticas -->', re.DOTALL)
content = pattern_html.sub('<!-- FIN Reseñas Cinemáticas -->', content)

# 3. Modificar JS en updateBoxState (Eliminar el openP de los testimonios 1 y meter nuestra rotación de volumen)
pattern_js_reviews = re.compile(r'let openP = Math\.max\(0, Math\.min\(1, \(prog - 2\.2\) / 0\.4\)\);.*?// --- TRANSICIÓN A LA REVISTA ---', re.DOTALL)
replacement_js = '''// Rotación extra de volumen para enganchar con carrusel suavemente
      let volRotPre = 0;
      if (prog > 2.2 && prog <= 2.6) {
          volRotPre = mapRange(prog, 2.2, 2.6, 0, 335);
      } else if (prog > 2.6) {
          volRotPre = 335;
      }
      // --- TRANSICIÓN A LA REVISTA ---'''
content = pattern_js_reviews.sub(replacement_js, content)

# 4. Aplicar volRotPre al volumen de la caja ANTES del carrusel
bad_volume = "const volume = mainDeck.querySelector('.box-3d-volume');"
good_volume = "const volume = mainDeck.querySelector('.box-3d-volume');\n      if (prog <= 2.6 && volume) volume.style.transform = `rotateY(${volRotPre}deg) rotateX(0deg) rotateZ(0deg)`;"
content = content.replace(bad_volume, good_volume)

# 5. BUGFIX ORIGINAL: Cara trasera de 4 PASOS se asomaba durante el carrusel
# La ocultábamos en 10.02, pero el carrusel salta a 9.62. La ocultamos antes de llegar al carrusel, ej. en prog > 2.6 (ya ha pasado la caja plana extraRot)
content = content.replace('if (prog > 10.02) {', 'if (prog > 2.6) {')

# 6. INYECTAR SALTO CUÁNTICO
# Dentro de smoothScrollLoop, inyectamos la lógica que salta de 2.6 a 9.62.
# Buscamos "function smoothScrollLoop() {\n        const lerpF = 0.40;"
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

# Sobrescribimos el archivo con los cambios aplicados en memoria en UTF-8 inmaculado
with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Quantum Patch aplicado con éxito!")
