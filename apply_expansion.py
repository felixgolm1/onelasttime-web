import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Eliminar sección de reseñas HTML
pattern_html = re.compile(r'<!-- Contenedor de Reseñas Cinemáticas -->.*?<!-- FIN Reseñas Cinemáticas -->', re.DOTALL)
content = pattern_html.sub('<!-- FIN Reseñas Cinemáticas -->', content)

# 2. Modificar JS - En updateBoxState, borrar lógica vieja de reseñas
pattern_js_reviews = re.compile(r'let openP = Math\.max.*?// --- TRANSICIÓN A LA REVISTA ---', re.DOTALL)
replacement_js = '''// Rotación extra de volumen para enganchar con carrusel suavemente
      let volRotPre = 0;
      if (prog > 2.2 && prog <= 2.6) {
          volRotPre = mapRange(prog, 2.2, 2.6, 0, 335);
      } else if (prog > 2.6) {
          volRotPre = 335;
      }
      // --- TRANSICIÓN A LA REVISTA ---'''
content = pattern_js_reviews.sub(replacement_js, content)

# 3. Aplicar volRotPre a volume
bad_volume = "const volume = mainDeck.querySelector('.box-3d-volume');"
good_volume = "const volume = mainDeck.querySelector('.box-3d-volume');\n      if (prog <= 2.6 && volume) volume.style.transform = `rotateY(${volRotPre}deg) rotateX(0deg) rotateZ(0deg)`;"
content = content.replace(bad_volume, good_volume)

# 4. Arreglar el bug de hiddenFaces (10.02 -> 3.0)
content = content.replace('if (prog > 10.02) {', 'if (prog > 3.0) {')

# 5. Aplicar los desplazamientos de timeline (-8.02)
replacements = {
    'const maxProg = 37.0;': 'const maxProg = 28.98;',
    'prog > 9.62': 'prog > 2.6',
    'mapRange(prog, 9.62, 10.62': 'mapRange(prog, 2.6, 3.6',
    'prog - 10.62': 'prog - 3.6',
    'prog >= 14.62': 'prog >= 7.6',
    'prog - 15.3': 'prog - 8.28',
    'p - 26.6': 'p - 19.58',
    'prog > 28.2': 'prog > 21.18',
    'prog - 21.98': 'prog - 14.96',
    'prog > 30.2': 'prog > 23.18',
    '(p - 21.98)': '(p - 14.96)',
    'var STEP_END    = 26.6;': 'var STEP_END    = 18.58;',
    'var SHOW_START = 17.43;': 'var SHOW_START = 9.41;',
    'height: 4400vh;': 'height: 3598vh;'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch aplicado con Python (UTF-8)!")
