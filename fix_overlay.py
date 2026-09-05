import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

pattern = r'<span style="color: #ccff00; font-weight: 600; display: block; font-size: 14px; margin-bottom: 6px;">Tú defines el objetivo y el contexto\.</span>\s*¿Romper la monotonía\? ¿Celebrar un hito\? ¿Comunicaros mejor\? ¿Conseguir una 2ª cita\?<br>\s*Lo que quieras\. Las cartas hacen el resto'

replacement = '''<span style="color: #ccff00; font-weight: 700; display: block; font-size: 15px; margin-bottom: 6px;">Haz que cada cena cuente.</span>
          Reconecta despu&eacute;s de un bache, sal de la rutina o celebra un hito.<br>Pero no lo dejes al azar.'''

# Just in case there are HTML entities in the source file, let's also try an entity-based pattern:
pattern2 = r'<span style="color: #ccff00; font-weight: 600; display: block; font-size: 14px; margin-bottom: 6px;">T&uacute; defines el objetivo y el contexto\.</span>\s*&iquest;Romper la monoton&iacute;a\? &iquest;Celebrar un hito\? &iquest;Comunicaros mejor\? &iquest;Conseguir una 2&ordf; cita\?<br>\s*Lo que quieras\. Las cartas hacen el resto'

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
elif re.search(pattern2, content):
    content = re.sub(pattern2, replacement, content)
else:
    # Let's just find the div that contains it and replace it.
    div_start = content.find('<span style="color: #ccff00; font-weight: 600; display: block; font-size: 14px; margin-bottom: 6px;">')
    if div_start != -1:
        div_end = content.find('</div>', div_start)
        old_text = content[div_start:div_end]
        content = content.replace(old_text, replacement + '\n        ')

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)

print("Done")
