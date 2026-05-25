# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Restore HTML of magazine-content
# Find the broken HTML with mag-frame
html_match = re.search(r'<div class="magazine-content"[^>]*>[\s\n]*<!-- Marco y fondo que no se expande -->[\s\n]*<div class="mag-frame"[^>]*></div>[\s\n]*<!-- Contenedor interno[^>]*>', text)
if html_match:
    original_html = """<div class="magazine-content" style="background: url('assets/img/modelo-sin-fondo.png') center 15% / 250% no-repeat; background-color: #06020F; border: 12px solid #f9cc10; justify-content: flex-start; padding: 10px; position: relative; box-shadow: inset 0 0 0 2px #fff; width: 100%; height: 100%;">"""
    text = text.replace(html_match.group(0), original_html)

# 2. Fix JS logic
js_match = re.search(r'const magContent = magazineScene\.querySelector\(\'\.magazine-content\'\);[\s\S]*?magContent\.style\.backgroundPosition = `center \$\{bgPos\}%`;\n           \}', text)

if js_match:
    new_js = """const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              // El recuadro CENTRAL se expande a pantalla completa
              if (easeP > 0) {
                  magContent.style.position = 'fixed';
                  magContent.style.left = '50vw';
                  magContent.style.top = '50vh';
                  magContent.style.transform = 'translate(-50%, -50%)';
                  magContent.style.zIndex = '10000';
                  magContent.style.width = `${baseW + (window.innerWidth - baseW) * easeP}px`;
                  magContent.style.height = `${baseH + (window.innerHeight - baseH) * easeP}px`;
              } else {
                  magContent.style.position = 'relative';
                  magContent.style.left = 'auto';
                  magContent.style.top = 'auto';
                  magContent.style.transform = 'none';
                  magContent.style.zIndex = '2';
                  magContent.style.width = '100%';
                  magContent.style.height = '100%';
              }

              // Anclamos los textos para que NO se desparramen al expandirse el recuadro
              const magUIs = magContent.querySelectorAll('.mag-ui, .mag-ui-title');
              magUIs.forEach(el => {
                  if (easeP > 0) {
                      el.style.width = `${baseW}px`;
                      el.style.height = `${baseH}px`;
                      el.style.left = '50%';
                      el.style.top = '50%';
                      if (el.classList.contains('mag-ui')) {
                          el.style.transform = `translate(-50%, -50%) scale(${1 + expandP * 0.05})`;
                      } else {
                          el.style.transform = `translate(-50%, -50%)`;
                      }
                  } else {
                      el.style.width = '100%';
                      el.style.height = '100%';
                      el.style.left = '0';
                      el.style.top = '0';
                      if (el.classList.contains('mag-ui')) {
                          el.style.transform = `scale(1)`;
                      } else {
                          el.style.transform = `none`;
                      }
                  }
              });

              // Deshacemos las lineas blancas
              const svgLines = magazineScene.querySelectorAll('line');
              svgLines.forEach(line => {
                  line.style.strokeDasharray = '2000';
                  line.style.strokeDashoffset = `${2000 * easeP}`;
              });

              // Hacemos desaparecer el borde amarillo a medida que se expande
              magContent.style.borderColor = `rgba(249, 204, 16, ${uiFade})`;
              magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;
              
              // El fondo negro SE MANTIENE, porque es el fondo de la chica
              magContent.style.backgroundColor = `#06020F`;

              // Zoom effect: La foto de la chica se adapta (250% -> 100%)
              const bgSize = 250 - (150 * easeP);
              const bgPos = 15 + (35 * easeP);
              magContent.style.backgroundSize = `${bgSize}%`;
              magContent.style.backgroundPosition = `center ${bgPos}%`;
           }"""
    text = text.replace(js_match.group(0), new_js)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Magazine fixed fully!")
