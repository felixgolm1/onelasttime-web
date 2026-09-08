# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Insert glass-who before glass-objectives
glass_who_html = '''
    <!-- Recuadro Glassmorphism de Quien (Paso 2) -->
    <div id="glass-who" style="position: fixed; top: 0; right: 0; height: 100vh; width: 30vw; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-left: 1px solid rgba(255, 255, 255, 0.1); border-radius: 0; padding: 0 2.5vw 0 30px; opacity: 0; pointer-events: none; z-index: 10005; visibility: hidden; box-shadow: -5px 0 30px rgba(0,0,0,0.15); display: flex; flex-direction: column; justify-content: center;">
      <h3 style="color: #ccff00; font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; margin-bottom: 24px; letter-spacing: 0.05em;">Ejemplos de compa&ntilde;&iacute;a</h3>
      <ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none;">
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con tu pareja de hace 10 a&ntilde;os?</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con tu prometidx?</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con esa cita de Bumble que pinta demasiado bien?</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con tu compi de trabajo favoritx?</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con el ligue del viaje a Bali con el que haces m&aacute;s videollamadas de las que est&aacute;s dispuestx a reconocer?</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con la que siempre te saca 2 kil&oacute;metros en el <i>run club</i>?</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> &iquest;Con tu <i>crush</i> del ascensor al que nunca le pasas del "buenos d&iacute;as"?</li>
        <li style="position: relative; color: rgba(255,255,255,0.7);"><span style="position: absolute; left: -20px; color: rgba(204,255,0,0.7);">&#8226;</span> &iquest;Con tu ex? (Solo para valientes... o insensatxs).</li>
      </ul>
    </div>
'''
content = content.replace('<!-- Recuadro Glassmorphism de Objetivos (Paso 3) -->', glass_who_html + '\n    <!-- Recuadro Glassmorphism de Objetivos (Paso 3) -->')

# 2. Add gsap.set('#glass-who')
content = content.replace("gsap.set('#glass-objectives', { opacity: 0, autoAlpha: 0 });", "gsap.set('#glass-who', { opacity: 0, autoAlpha: 0 });\n      gsap.set('#glass-objectives', { opacity: 0, autoAlpha: 0 });")

# 3. Modify panData animation for glass-who
old_glass_anim = '''// Animacion de la caja glass-objectives en el Paso 3
          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
          }'''

new_glass_anim = '''// Animacion de la caja glass-who en el Paso 2
          if (i === 1) {
            scrollTl.to('#glass-who', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
          } else {
            scrollTl.to('#glass-who', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
          }

          // Animacion de la caja glass-objectives en el Paso 3
          if (i === 2) {
            scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
          } else {
            scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
          }'''
content = content.replace(old_glass_anim, new_glass_anim)

# 4. Modify panData coordinates
content = content.replace("{ x: '-26vw', y:  '20vh', r:  -9 },", "{ x: '-34vw', y:  '20vh', r:  -9 },")
content = content.replace("{ x:  '24vw', y: '-26vh', r: -18 },", "{ x:  '34vw', y: '-26vh', r: -18 },")

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
