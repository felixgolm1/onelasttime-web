dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    text = f.read()

old_palette = '''      // ==== PALETA DE COLORES ====
      vec3 cold = vec3(0.05, 0.10, 0.55);  // Azul profundo (inactivo)
      vec3 mid  = vec3(0.60, 0.05, 0.70);  // Violeta (activacion inicial)
      vec3 warm = vec3(1.00, 0.35, 0.00);  // Naranja vivo (activo)
      vec3 hot  = vec3(1.00, 0.92, 0.10);  // Amarillo brillante (maxima activacion)

      vec3 heatColor = mix(cold, mid,  smoothstep(0.15, 0.45, heat));
      heatColor      = mix(heatColor, warm, smoothstep(0.45, 0.72, heat));
      heatColor      = mix(heatColor, hot,  smoothstep(0.72, 1.00, heat));'''

new_palette = '''      // ==== PALETA DE COLORES (estilo fMRI / Oryzo) ====
      // 6 paradas de color con degradado muy suave:
      // Azul noche -> Azul electrico -> Cian -> Verde -> Amarillo -> Naranja -> Rojo vivo
      vec3 c0 = vec3(0.00, 0.00, 0.22);   // azul noche (reposo total)
      vec3 c1 = vec3(0.00, 0.30, 0.90);   // azul electrico
      vec3 c2 = vec3(0.00, 0.75, 0.85);   // cian
      vec3 c3 = vec3(0.10, 0.88, 0.30);   // verde
      vec3 c4 = vec3(0.95, 0.92, 0.00);   // amarillo
      vec3 c5 = vec3(1.00, 0.45, 0.00);   // naranja
      vec3 c6 = vec3(1.00, 0.05, 0.05);   // rojo vivo (activacion maxima)

      // Interpolacion con 6 segmentos iguales (0..1 dividido en 6 tramos)
      float s = heat * 6.0;
      vec3 heatColor;
      if      (s < 1.0) heatColor = mix(c0, c1, smoothstep(0.0, 1.0, s));
      else if (s < 2.0) heatColor = mix(c1, c2, smoothstep(0.0, 1.0, s - 1.0));
      else if (s < 3.0) heatColor = mix(c2, c3, smoothstep(0.0, 1.0, s - 2.0));
      else if (s < 4.0) heatColor = mix(c3, c4, smoothstep(0.0, 1.0, s - 3.0));
      else if (s < 5.0) heatColor = mix(c4, c5, smoothstep(0.0, 1.0, s - 4.0));
      else              heatColor = mix(c5, c6, smoothstep(0.0, 1.0, s - 5.0));'''

if old_palette in text:
    text = text.replace(old_palette, new_palette)
    with open(dev_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Palette updated to fMRI/Oryzo style!")
else:
    print("Could not find palette block")
