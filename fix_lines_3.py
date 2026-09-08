# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_obj = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none; margin-bottom: 40px;">
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Conocernos a&uacute;n m&aacute;s</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mejorar la comunicaci&oacute;n entre nosotrxs</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Celebrar nuestro aniversario de pareja</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Desconectar de la rutina riendo</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Tener una conversaci&oacute;n profunda</span></div></li>
          <li class="mask-li" style="overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Conseguir otra cita</span></div></li>
        </ul>'''

new_obj = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none; margin-bottom: 40px;" class="dynamic-lines-list">
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Conocernos a&uacute;n m&aacute;s</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mejorar la comunicaci&oacute;n entre nosotrxs</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Celebrar nuestro aniversario de pareja</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Desconectar de la rutina riendo</div></li>
          <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Tener una conversaci&oacute;n profunda</div></li>
          <li style="display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Conseguir otra cita</div></li>
        </ul>'''

content = content.replace(old_obj, new_obj)

# What if it's the older original one?
old_obj_2 = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none; margin-bottom: 40px;">
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mejorar la comunicaci&oacute;n entre nosotrxs</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Celebrar nuestro aniversario de pareja</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Desconectar de la rutina riendo</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Tener una conversaci&oacute;n profunda</li>
          <li style="position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conseguir otra cita</li>
        </ul>'''
content = content.replace(old_obj_2, new_obj)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
