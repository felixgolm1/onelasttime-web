# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Use regex to find the UL block of glass-who
ul_regex = r'<ul style="color: rgba\(255,255,255,0\.9\); font-family: \'Inter\', sans-serif; font-size: 0\.95rem; font-weight: 400; line-height: 1\.5; padding-left: 24px; margin: 0; list-style-type: none;">(.*?)</ul>'

new_ul_content = '''
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mi mujer con la que ya hemos compartido 40 a&ntilde;os y 2 hijxs</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mi pareja de hace m&aacute;s de 7 a&ntilde;os</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> La cita de Bumble que pinta demasiado bien</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Mi compi de trabajo con quien ya hace 3 meses que compartimos m&aacute;s que trabajo</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> El ligue del viaje a Bali con el que hago videollamadas cada semana</li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> La que siempre me saca 2 kil&oacute;metros en el <i>run club</i></li>
        <li style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> El <i>crush</i> del ascensor con el que por fin hemos pasado del "hola que tal"</li>
        <li style="position: relative; color: rgba(255,255,255,0.7);"><span style="position: absolute; left: -20px; color: rgba(204,255,0,0.7);">&#8226;</span> Mi ex (solo para valientes... o insensatxs).</li>
      '''

content = re.sub(ul_regex, '<ul style="color: rgba(255,255,255,0.9); font-family: \'Inter\', sans-serif; font-size: 0.95rem; font-weight: 400; line-height: 1.5; padding-left: 24px; margin: 0; list-style-type: none;">' + new_ul_content + '</ul>', content, flags=re.DOTALL, count=1)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
