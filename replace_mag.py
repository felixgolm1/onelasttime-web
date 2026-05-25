import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Buscamos el div magazine-content y todo su contenido hasta el cierre del div principal
pattern = r'(<div class="magazine-content">).*?(<div class="mag-footer-columns">.*?</div>\s*</div>)'

new_content = """<div class="magazine-content" style="background: url('assets/img/ciencia_bg.png') center/cover; border: 12px solid #f9cc10; justify-content: flex-start; padding: 10px; position: relative; box-shadow: inset 0 0 0 2px #fff;">
          <!-- Fondo Oscurecido en la base para el texto -->
          <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 45%; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0) 100%); z-index: 1;"></div>
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 35%; background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%); z-index: 1;"></div>

          <!-- Cabecera -->
          <div style="width: 100%; text-align: center; z-index: 2; margin-top: 10px;">
            <div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 1.3rem; color: #fff; letter-spacing: 0.1em; margin-bottom: -10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">SABER MÁS</div>
            <h1 style="font-family: 'Inter', sans-serif; font-weight: 900; font-size: 5.2rem; color: #fff; letter-spacing: -0.04em; margin: 0; line-height: 0.9; text-shadow: 2px 2px 6px rgba(0,0,0,0.8); transform: scaleY(1.1);">CIENCIA</h1>
          </div>

          <!-- Nat Geo Logo -->
          <div style="width: 100%; display: flex; align-items: center; gap: 8px; z-index: 2; padding-left: 5px; margin-top: 15px;">
            <div style="width: 18px; height: 24px; border: 3px solid #f9cc10;"></div>
            <div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 0.5rem; color: #fff; line-height: 1.1; text-transform: uppercase;">National<br>Geographic</div>
          </div>

          <!-- Columnas Laterales -->
          <div style="display: flex; justify-content: space-between; width: 100%; z-index: 2; margin-top: auto; margin-bottom: 20px; padding: 0 10px;">
            <!-- Izquierda -->
            <div style="width: 45%; text-align: left; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">
              <div style="margin-bottom: 12px;">
                <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 0.7rem; color: #f9cc10; line-height: 1.1;">EL CEREBRO<br>GOLOSO</div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.55rem; color: #fff; line-height: 1.1;">CONTROLAR<br>LA ANSIEDAD<br>DE COMER</div>
              </div>
              <div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 0.7rem; color: #f9cc10; line-height: 1.1;">LOS SECRETOS<br>DEL SUEÑO</div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.55rem; color: #fff; line-height: 1.1;">QUE PASA<br>CUANDO<br>DORMIMOS</div>
              </div>
            </div>
            <!-- Derecha -->
            <div style="width: 45%; text-align: right; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">
              <div style="margin-bottom: 12px;">
                <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 0.7rem; color: #f9cc10; line-height: 1.1;">BACTERIAS<br>AMIGAS</div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.55rem; color: #fff; line-height: 1.1;">NUESTRA<br>DEFENSA<br>INTERIOR</div>
              </div>
              <div style="margin-bottom: 12px;">
                <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 0.7rem; color: #f9cc10; line-height: 1.1;">TÓXICOS<br>A LA CARTA</div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.55rem; color: #fff; line-height: 1.1;">¿QUÉ AMENAZAS<br>ESCONDEN LOS<br>ALIMENTOS?</div>
              </div>
              <div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 0.7rem; color: #f9cc10; line-height: 1.1;">HOGARES<br>ESPACIALES</div>
                <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.55rem; color: #fff; line-height: 1.1;">LA NUEVA<br>CONQUISTA<br>DE LA LUNA</div>
              </div>
            </div>
          </div>

          <!-- Bottom Title -->
          <div style="width: 100%; text-align: center; z-index: 2; margin-bottom: 5px;">
            <h2 style="font-family: 'Inter', sans-serif; font-weight: 900; font-size: 3.2rem; color: #fff; line-height: 0.9; margin: 0; letter-spacing: -0.03em; text-shadow: 2px 2px 8px rgba(0,0,0,0.9);">RETRASAR EL<br>ENVEJECIMIENTO</h2>
            <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 0.9rem; color: #f9cc10; margin-top: 6px; letter-spacing: 0.05em; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); background: #000; padding: 4px 0; display: inline-block; width: 100%;">EL RETO DE LA BIOMEDICINA</div>
          </div>
        </div>"""

if re.search(pattern, text, re.DOTALL):
    new_text = re.sub(pattern, new_content, text, flags=re.DOTALL)
    with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replace successful!")
else:
    print("Pattern not found!")
