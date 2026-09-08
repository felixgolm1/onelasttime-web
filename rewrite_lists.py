# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Replace the first list (glass-who)
old_who_list = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none;">
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mi mujer con la que ya hemos compartido 40 a&ntilde;os y 2 hijxs</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mi pareja de hace m&aacute;s de 7 a&ntilde;os</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> La cita de Bumble que pinta demasiado bien</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mi compi de trabajo con quien ya hace 3 meses que compartimos m&aacute;s que trabajo</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> El ligue del viaje a Bali con el que hago videollamadas cada semana</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> La que siempre me saca 2 kil&oacute;metros en el <i>run club</i></li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> El <i>crush</i> del ascensor con el que por fin hemos pasado del "hola que tal"</li>
        <li style="position: relative; color: rgba(255,255,255,0.7);"><span style="position: absolute; left: -20px; color: rgba(204,255,0,0.7);">&#8226;</span> Mi ex (solo para valientes... o insensatxs).</li>
      </ul>'''

new_who_list = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none;">
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mi mujer con la que ya hemos compartido 40 a&ntilde;os y 2 hijxs</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mi pareja de hace m&aacute;s de 7 a&ntilde;os</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>La cita de Bumble que pinta demasiado bien</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mi compi de trabajo con quien ya hace 3 meses que compartimos m&aacute;s que trabajo</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>El ligue del viaje a Bali con el que hago videollamadas cada semana</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>La que siempre me saca 2 kil&oacute;metros en el <i>run club</i></span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>El <i>crush</i> del ascensor con el que por fin hemos pasado del "hola que tal"</span></div></li>
        <li class="mask-li" style="color: rgba(255,255,255,0.7); overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: rgba(204,255,0,0.7);">&#8226;</span><span>Mi ex (solo para valientes... o insensatxs).</span></div></li>
      </ul>'''

content = content.replace(old_who_list, new_who_list)

# Replace the second list (glass-objectives)
old_obj_list = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none; margin-bottom: 40px;">
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mejorar la comunicaci&oacute;n entre nosotrxs</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Reirnos un buen rato</li>
          <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Recordar todo lo que hemos vivido</li>
          <li style="position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Ayudarnos mutuamente a crecer</li>
        </ul>'''

new_obj_list = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none; margin-bottom: 40px;">
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Conocernos a&uacute;n m&aacute;s</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mejorar la comunicaci&oacute;n entre nosotrxs</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Reirnos un buen rato</span></div></li>
          <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Recordar todo lo que hemos vivido</span></div></li>
          <li class="mask-li" style="overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Ayudarnos mutuamente a crecer</span></div></li>
        </ul>'''

content = content.replace(old_obj_list, new_obj_list)

# Also wrap the <p> and <hr> in objectives
old_p = '''<p style="color: rgba(255,255,255,0.8); font-family: 'Inter', sans-serif; font-size: 0.85rem; line-height: 1.4; margin-bottom: 24px; padding-right: 10px;">Puede ser literalmente lo que quieras con la especificidad que quieras (excepto conseguir que te paguen la cena, en eso a&uacute;n estamos trabajando):</p>'''
new_p = '''<div style="overflow: hidden; margin-bottom: 24px; padding-right: 10px;"><p class="glass-mask-inner" style="color: rgba(255,255,255,0.8); font-family: 'Inter', sans-serif; font-size: 0.85rem; line-height: 1.4; margin: 0;">Puede ser literalmente lo que quieras con la especificidad que quieras (excepto conseguir que te paguen la cena, en eso a&uacute;n estamos trabajando):</p></div>'''
content = content.replace(old_p, new_p)

old_hr = '''<hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 0 0 16px 0;">
        <p style="color: rgba(255,255,255,0.6); font-family: 'Inter', sans-serif; font-size: 0.8rem; line-height: 1.4; margin: 0;">
          <strong style="color: #ccff00; font-weight: 600;">Garant&iacute;a del 100%:</strong> Si no conseguimos crear un juego que os encante, os devolvemos el dinero de la cena. Literalmente.
        </p>'''
new_hr = '''<div style="overflow: hidden; margin-bottom: 16px;"><hr class="glass-mask-inner" style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 0;"></div>
        <div style="overflow: hidden;"><p class="glass-mask-inner" style="color: rgba(255,255,255,0.6); font-family: 'Inter', sans-serif; font-size: 0.8rem; line-height: 1.4; margin: 0;">
          <strong style="color: #ccff00; font-weight: 600;">Garant&iacute;a del 100%:</strong> Si no conseguimos crear un juego que os encante, os devolvemos el dinero de la cena. Literalmente.
        </p></div>'''
content = content.replace(old_hr, new_hr)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
