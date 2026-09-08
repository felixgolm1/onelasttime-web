# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_list = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none; margin-bottom: 40px;">
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mejorar la comunicaci&oacute;n entre nosotrxs</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Celebrar nuestro aniversario de pareja</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Desconectar de la rutina riendo</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Tener una conversaci&oacute;n profunda</li>
          <li style="position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conseguir otra cita</li>
        </ul>'''

new_list = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none; margin-bottom: 40px;">
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Conocernos a&uacute;n m&aacute;s</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mejorar la comunicaci&oacute;n entre nosotrxs</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Celebrar nuestro aniversario de pareja</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Desconectar de la rutina riendo</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Tener una conversaci&oacute;n profunda</span></div></li>
          <li class="mask-li" style="overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Conseguir otra cita</span></div></li>
        </ul>'''

content = content.replace(old_list, new_list)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
