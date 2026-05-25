# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_html = """<!-- Fondo Oscurecido en la base para el texto -->
          <div class="mag-ui" style="position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0) 100%); z-index: 1;"></div>
          <div class="mag-ui" style="position: absolute; top: 0; left: 0; width: 100%; height: 35%; background: linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 100%); z-index: 1;"></div>

          <!-- Nueva Capa UI estilo RISE -->
          <div class="mag-ui" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; z-index: 2; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column;">
              
              <!-- Cabecera RISE -->
              <div style="text-align: center; position: relative; margin-top: -15px;">
                  <h1 style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 8rem; color: #fdf5e6; margin: 0; line-height: 0.8; letter-spacing: -0.02em; font-weight: 700; position: relative; display: inline-block; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);">RISE<span style="position: absolute; top: -5px; right: -18px; width: 12px; height: 12px; background: #fdf5e6; border-radius: 50%; box-shadow: 1px 1px 4px rgba(0,0,0,0.5);"></span></h1>
                  <div style="position: absolute; right: 0; top: 7.2rem; font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #fdf5e6; font-weight: 600; letter-spacing: 0.05em; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">ISSUE NO. 00124</div>
              </div>

              <!-- Bloque Central -->
              <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; flex-grow: 1; position: relative;">
                  
                  <!-- Texto Izquierdo (We Are So Cooked!) -->
                  <div style="text-align: left; margin-top: 60px;">
                      <div style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 1.8rem; color: #fdf5e6; margin-bottom: -15px; letter-spacing: 0.02em; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);">We Are So</div>
                      <div style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 3.5rem; color: #fdf5e6; font-weight: 700; text-shadow: 2px 2px 8px rgba(0,0,0,0.7);">Cooked!</div>
                      <div style="font-family: 'Inter', sans-serif; font-size: 0.55rem; color: #fdf5e6; letter-spacing: 0.05em; max-width: 200px; margin-top: 15px; line-height: 1.4; text-shadow: 1px 1px 4px rgba(0,0,0,0.8);">
                          ORYZO IS TAKING EVERYONE'S JOBS...<br>AND REPLACING THEM WITH AI!
                      </div>
                  </div>

                  <!-- Caja Derecha (25 AI Slop) -->
                  <div style="border: 2px solid rgba(253, 245, 230, 0.8); padding: 15px; text-align: center; width: 90px; margin-top: -80px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); background: rgba(0,0,0,0.1);">
                      <div style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 3.5rem; color: #fdf5e6; line-height: 1; text-shadow: 2px 2px 6px rgba(0,0,0,0.5);">25</div>
                      <div style="font-family: 'Inter', sans-serif; font-size: 0.45rem; color: #fdf5e6; letter-spacing: 0.05em; margin-top: 8px; line-height: 1.4; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
                          AI SLOP IDEAS<br>FOR THIS<br>WINTER
                      </div>
                  </div>
              </div>

              <!-- Bloque Inferior -->
              <div style="display: flex; justify-content: space-between; align-items: flex-end; width: 100%; margin-bottom: 5px;">
                  
                  <!-- Circulo Izquierdo (No 6) -->
                  <div style="width: 75px; height: 75px; border: 2px solid rgba(253, 245, 230, 0.8); border-radius: 50%; display: flex; justify-content: center; align-items: center; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); background: rgba(0,0,0,0.1);">
                      <div style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 1.8rem; color: #fdf5e6; margin-top: 5px; text-shadow: 2px 2px 6px rgba(0,0,0,0.5);">N<sup style="font-size: 0.9rem; margin-left: 2px;">o</sup>6</div>
                  </div>

                  <!-- Texto Derecho & Codigo de Barras -->
                  <div style="text-align: right;">
                      <div style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 1.6rem; color: #fdf5e6; letter-spacing: 0.05em; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);">ORYZO-1</div>
                      <div style="font-family: 'Inter', sans-serif; font-size: 0.4rem; color: #fdf5e6; letter-spacing: 0.05em; max-width: 170px; margin-top: 8px; margin-left: auto; line-height: 1.4; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
                          AN OPEN-WEIGHT MODEL DESIGNED TO BE<br>LIGHTWEIGHT AND EASY TO CARRY.
                      </div>
                      <!-- Codigo de Barras Simulado -->
                      <div style="margin-top: 15px; display: flex; justify-content: flex-end; gap: 3px; height: 35px; align-items: flex-end;">
                          <div style="width: 4px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 2px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 5px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 1px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 4px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 2px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 5px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 1px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 3px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 2px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 4px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 2px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 3px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 2px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                          <div style="width: 4px; background: #fdf5e6; height: 100%; border-radius: 1px;"></div>
                      </div>
                  </div>
              </div>
          </div>
"""

text_to_replace = re.search(r'<!-- Fondo Oscurecido en la base para el texto -->[\s\S]*?<!-- Bottom Title -->[\s\S]*?</div>[\s\n]*</div>', text)
if text_to_replace:
    updated_text = text.replace(text_to_replace.group(0), new_html)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("UI Replaced!")
else:
    print("Could not find the target HTML to replace.")
