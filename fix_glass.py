import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

html_box = '''
    <!-- Recuadro Glassmorphism de Objetivos (Paso 3) -->
    <div id="glass-objectives" style="position: fixed; top: 50%; left: 6vw; transform: translateY(-50%); width: 25vw; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 35px 30px; opacity: 0; pointer-events: none; z-index: 10005; visibility: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
      <h3 style="color: #ccff00; font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; margin-bottom: 24px; letter-spacing: 0.05em;">Ejemplos de objetivos</h3>
      <ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none;">
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Desconectar de la rutina riendo</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Tener una conversaci&oacute;n profunda</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conseguir otra cita</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mejorar la comunicaci&oacute;n entre nosotrxs</li>
        <li style="position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Celebrar nuestro aniversario de pareja</li>
      </ul>
    </div>
'''

# Insert HTML right before <div id="sc-detail-global"
content = content.replace('<div id="sc-detail-global"', html_box + '\n    <div id="sc-detail-global"')

# Insert GSAP set
gsap_set = "gsap.set(scCta,   { opacity: 0 });"
new_gsap_set = "gsap.set(scCta,   { opacity: 0 });\n      gsap.set('#glass-objectives', { opacity: 0, autoAlpha: 0 });"
content = content.replace(gsap_set, new_gsap_set)

# Insert animation logic inside panData.forEach
target_loop = "scrollTl.to(otherCards,  { opacity: 0.15, duration: PAN, ease: 'power1.inOut' }, t);"
new_loop_addition = '''scrollTl.to(otherCards,  { opacity: 0.15, duration: PAN, ease: 'power1.inOut' }, t);
        
        // Animacion de la caja glass-objectives en el Paso 3
        if (i === 2) {
          scrollTl.to('#glass-objectives', { autoAlpha: 1, duration: PAN, ease: 'power1.inOut' }, t);
        } else {
          scrollTl.to('#glass-objectives', { autoAlpha: 0, duration: PAN, ease: 'power1.inOut' }, t);
        }'''
content = content.replace(target_loop, new_loop_addition)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
