import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Bad left block (currently in file):
bad_left = """    <div class="flt-line"><div class="flt-oh"><span class="flt-in">UNA EXPERIENCIA CON CARTAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">CONVERSACIONALES</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">ULTRA-PERSONALIZADAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">A VOSOTRXS DOS</span></div></div>"""

# Restored left block:
good_left = """    <div class="flt-line"><div class="flt-oh"><span class="flt-in">UNA EXPERIENCIA</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">CON CARTAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">CONVERSACIONALES</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">ULTRA-PERSONALIZADAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">A VOSOTRXS DOS</span></div></div>"""

content = content.replace(bad_left, good_left)


# Bad right block:
bad_right = """      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os unirán como nunca antes</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que cuestan dos cheesecakes</span></div></div>"""

# Restored right block:
good_right = """      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os unirán</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">como nunca antes</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">cuestan dos cheesecakes</span></div></div>"""

content = content.replace(bad_right, good_right)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
