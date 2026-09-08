# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_glass_regex = r'<div id="glass-objectives".*?</div>'

new_glass = '''<div id="glass-objectives" style="position: fixed; top: 0; left: 0; height: 100vh; width: 30vw; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-right: 1px solid rgba(255, 255, 255, 0.1); border-radius: 0; padding: 0 30px 0 2.5vw; opacity: 0; pointer-events: none; z-index: 10005; visibility: hidden; box-shadow: 5px 0 30px rgba(0,0,0,0.15); display: flex; flex-direction: column; justify-content: center;">
      <h3 style="color: #ccff00; font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; margin-bottom: 24px; letter-spacing: 0.05em;">Ejemplos de objetivos</h3>
      <ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none; margin-bottom: 40px;">
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Desconectar de la rutina riendo</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Tener una conversaci&oacute;n profunda</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conseguir otra cita</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mejorar la comunicaci&oacute;n entre nosotrxs</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Celebrar nuestro aniversario de pareja</li>
        <li style="position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Literalmente lo que quieras (excepto conseguir que te paguen la cena, en eso a&uacute;n estamos trabajando).</li>
      </ul>
      <hr style="border: none; border-top: 1px dashed rgba(255,255,255,0.25); margin: 0 0 40px 0;">
      <p style="color: #fff; font-family: 'Inter', sans-serif; font-size: 2.1rem; font-weight: 700; line-height: 1.2; margin: 0; text-align: right; text-transform: uppercase;">
        SI NO LO CONSIGUES, ESTA EXPERIENCIA CORRE DE NUESTRA CUENTA Y OS REGALAMOS OTRA.
      </p>
    </div>'''

content = re.sub(old_glass_regex, new_glass, content, flags=re.DOTALL)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
