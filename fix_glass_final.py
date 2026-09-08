# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Remove the joke text from #sc-3
old_sc3 = '''<div class="sc-card" id="sc-3">
          <div class="sc-num">3</div>
          <div class="sc-desc">Dinos <b style="color: #ccff00;">tu objetivo</b> y haremos matem\u00e1ticamente imposible que no lo consigas</div>
          <div style="color: #ffffff; font-size: 0.75rem; font-family: 'Inter', sans-serif; font-weight: 400; opacity: 0.7; margin-top: 1rem; line-height: 1.3;">*Todav\u00eda no hemos descubierto c\u00f3mo conseguir que te paguen la cena. Pero estamos trabajando en ello.</div>
        </div>'''
new_sc3 = '''<div class="sc-card" id="sc-3">
          <div class="sc-num">3</div>
          <div class="sc-desc">Dinos <b style="color: #ccff00;">tu objetivo</b> y haremos matem&aacute;ticamente imposible que no lo consigas</div>
        </div>'''
content = content.replace(old_sc3, new_sc3)
# Just in case the unicode is slightly different, let's use regex for sc-3
content = re.sub(
    r'<div class="sc-card" id="sc-3">\s*<div class="sc-num">3</div>\s*<div class="sc-desc">Dinos <b style="color: #ccff00;">tu objetivo</b> y haremos matem.*?ticamente imposible que no lo consigas</div>\s*<div style="color: #ffffff; font-size: 0.75rem; font-family: \'Inter\', sans-serif; font-weight: 400; opacity: 0.7; margin-top: 1rem; line-height: 1.3;">\*Todav.*?a no hemos descubierto c.*?mo conseguir que te paguen la cena. Pero estamos trabajando en ello.</div>\s*</div>',
    new_sc3,
    content,
    flags=re.DOTALL
)

# 2. Update the glass-objectives box
old_glass_regex = r'<div id="glass-objectives".*?</ul>\s*</div>'

new_glass = '''<div id="glass-objectives" style="position: fixed; top: 50%; left: 0; transform: translateY(-50%); width: 28vw; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.1); border-left: none; border-radius: 0 24px 24px 0; padding: 40px 30px 40px 2.5vw; opacity: 0; pointer-events: none; z-index: 10005; visibility: hidden; box-shadow: 5px 10px 30px rgba(0,0,0,0.15);">
      <h3 style="color: #ccff00; font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; margin-bottom: 24px; letter-spacing: 0.05em;">Ejemplos de objetivos</h3>
      <ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none; margin-bottom: 28px;">
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Desconectar de la rutina riendo</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Tener una conversaci&oacute;n profunda</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conseguir otra cita</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mejorar la comunicaci&oacute;n entre nosotrxs</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Celebrar nuestro aniversario de pareja</li>
        <li style="position: relative; color: rgba(255,255,255,0.7);"><span style="position: absolute; left: -20px; color: rgba(204,255,0,0.7);">&#8226;</span> Literalmente lo que quieras (excepto conseguir que te paguen la cena, en eso a&uacute;n estamos trabajando).</li>
      </ul>
      <hr style="border: none; border-top: 1px dashed rgba(255,255,255,0.25); margin: 0 0 28px 0;">
      <p style="color: #fff; font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 500; line-height: 1.4; margin: 0;">
        <span style="color: #ccff00; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; letter-spacing: 0.02em; display: block; margin-bottom: 4px;">A grandes promesas,<br>grandes compromisos:</span>
        Si no lo consigues, esta experiencia corre de nuestra cuenta y os regalamos otra.
      </p>
    </div>'''

content = re.sub(old_glass_regex, new_glass, content, flags=re.DOTALL)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
