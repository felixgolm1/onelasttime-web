# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

new_obj = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none; margin-bottom: 40px;" class="dynamic-lines-list">
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Conocernos a&uacute;n m&aacute;s</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mejorar la comunicaci&oacute;n entre nosotrxs</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Celebrar nuestro aniversario de pareja</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Desconectar de la rutina riendo</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Tener una conversaci&oacute;n profunda</div></li>
          <li style="display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Conseguir otra cita</div></li>
        </ul>'''

# Replace from <ul... to </ul> right before <hr style="border: none
content = re.sub(r'<ul style="color: rgba\(255,255,255,0\.9\); font-family: \'Inter\', sans-serif; font-size: 0\.95rem; font-weight: 400; line-height: 1\.5; padding-left: 24px; margin: 0; list-style-type: none; margin-bottom: 40px;">.*?</ul>', new_obj, content, flags=re.DOTALL)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
