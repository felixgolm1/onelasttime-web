# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. We will rewrite the lists to have a simpler structure for our JS
old_who = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none;">
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mi mujer con la que ya hemos compartido 40 a&ntilde;os y 2 hijxs</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mi pareja de hace m&aacute;s de 7 a&ntilde;os</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>La cita de Bumble que pinta demasiado bien</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>Mi compi de trabajo con quien ya hace 3 meses que compartimos m&aacute;s que trabajo</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>El ligue del viaje a Bali con el que hago videollamadas cada semana</span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>La que siempre me saca 2 kil&oacute;metros en el <i>run club</i></span></div></li>
        <li class="mask-li" style="margin-bottom: 16px; overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: #ccff00;">&#8226;</span><span>El <i>crush</i> del ascensor con el que por fin hemos pasado del "hola que tal"</span></div></li>
        <li class="mask-li" style="color: rgba(255,255,255,0.7); overflow: hidden;"><div class="glass-mask-inner" style="display: flex;"><span style="flex-shrink: 0; width: 20px; color: rgba(204,255,0,0.7);">&#8226;</span><span>Mi ex (solo para valientes... o insensatxs).</span></div></li>
      </ul>'''

new_who = '''<ul style="color: rgba(255,255,255,0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 0; margin: 0; list-style-type: none;" class="dynamic-lines-list">
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mi mujer con la que ya hemos compartido 40 a&ntilde;os y 2 hijxs</div></li>
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mi pareja de hace m&aacute;s de 7 a&ntilde;os</div></li>
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">La cita de Bumble que pinta demasiado bien</div></li>
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mi compi de trabajo con quien ya hace 3 meses que compartimos m&aacute;s que trabajo</div></li>
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">El ligue del viaje a Bali con el que hago videollamadas cada semana</div></li>
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">La que siempre me saca 2 kil&oacute;metros en el <i>run club</i></div></li>
        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">El <i>crush</i> del ascensor con el que por fin hemos pasado del "hola que tal"</div></li>
        <li style="color: rgba(255,255,255,0.7); display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-mask-line" style="color: rgba(204,255,0,0.7);">&#8226;</div></div><div class="dyn-text">Mi ex (solo para valientes... o insensatxs).</div></li>
      </ul>'''

content = content.replace(old_who, new_who)

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

old_p = '''<div style="overflow: hidden; margin-bottom: 24px; padding-right: 10px;"><p class="glass-mask-inner" style="color: rgba(255,255,255,0.8); font-family: 'Inter', sans-serif; font-size: 0.85rem; line-height: 1.4; margin: 0;">Puede ser literalmente lo que quieras con la especificidad que quieras (excepto conseguir que te paguen la cena, en eso a&uacute;n estamos trabajando):</p></div>'''
new_p = '''<div class="dyn-text" style="color: rgba(255,255,255,0.8); font-family: 'Inter', sans-serif; font-size: 0.85rem; line-height: 1.4; margin-bottom: 24px; padding-right: 10px;">Puede ser literalmente lo que quieras con la especificidad que quieras (excepto conseguir que te paguen la cena, en eso a&uacute;n estamos trabajando):</div>'''
content = content.replace(old_p, new_p)

old_hr = '''<div style="overflow: hidden; margin-bottom: 16px;"><hr class="glass-mask-inner" style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 0;"></div>
        <div style="overflow: hidden;"><p class="glass-mask-inner" style="color: rgba(255,255,255,0.6); font-family: 'Inter', sans-serif; font-size: 0.8rem; line-height: 1.4; margin: 0;">
          <strong style="color: #ccff00; font-weight: 600;">Garant&iacute;a del 100%:</strong> Si no conseguimos crear un juego que os encante, os devolvemos el dinero de la cena. Literalmente.
        </p></div>'''
new_hr = '''<div style="overflow: hidden; margin-bottom: 16px;"><hr class="glass-mask-line" style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 0;"></div>
        <div class="dyn-text" style="color: rgba(255,255,255,0.6); font-family: 'Inter', sans-serif; font-size: 0.8rem; line-height: 1.4; margin: 0;">
          <strong style="color: #ccff00; font-weight: 600;">Garant&iacute;a del 100%:</strong> Si no conseguimos crear un juego que os encante, os devolvemos el dinero de la cena. Literalmente.
        </div>'''
content = content.replace(old_hr, new_hr)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
