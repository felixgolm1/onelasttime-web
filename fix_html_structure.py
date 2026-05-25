# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Buscamos la capa UI estilo RISE
match = re.search(r'<!-- Nueva Capa UI estilo RISE -->[\s\S]*?<!-- Bloque Central -->', text)

if match:
    new_html = """<!-- Nueva Capa UI estilo RISE -->
          <!-- Título aislado para animación especial -->
          <div class="mag-ui-title" style="position: absolute; width: 100%; top: 10px; left: 0; z-index: 3; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column;">
              <div style="text-align: center; position: relative;">
                  <h1 style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 8rem; color: #fdf5e6; margin: 0; line-height: 0.8; letter-spacing: -0.02em; font-weight: 700; position: relative; display: inline-block; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);">
                    <span class="rise-l" style="display:inline-block; transition: none;">R</span><span class="rise-l" style="display:inline-block; transition: none;">I</span><span class="rise-l" style="display:inline-block; transition: none;">S</span><span class="rise-l" style="display:inline-block; transition: none;">E</span>
                    <span class="rise-dot" style="position: absolute; top: -5px; right: -18px; width: 12px; height: 12px; background: #fdf5e6; border-radius: 50%; box-shadow: 1px 1px 4px rgba(0,0,0,0.5); display:inline-block; transition: none;"></span>
                  </h1>
              </div>
          </div>

          <!-- Resto de textos que hacen fade normal -->
          <div class="mag-ui" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; z-index: 2; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column;">
              <div style="text-align: center; position: relative; margin-top: -15px;">
                  <!-- Espaciador invisible para mantener layout -->
                  <h1 style="font-size: 8rem; margin: 0; line-height: 0.8; opacity: 0;">RISE</h1>
                  <div style="position: absolute; right: 0; top: 7.2rem; font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #fdf5e6; font-weight: 600; letter-spacing: 0.05em; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">ISSUE NO. 00124</div>
              </div>

              <!-- Bloque Central -->"""
    
    updated_text = text.replace(match.group(0), new_html)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("HTML Splitted!")
else:
    print("Could not find HTML block.")
