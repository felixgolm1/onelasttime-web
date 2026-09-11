import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Original left block:
old_left = """  <div id="flip-left-text">
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">UNA EXPERIENCIA</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">CON CARTAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">CONVERSACIONALES</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">ULTRA-PERSONALIZADAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">A VOSOTRXS DOS</span></div></div>
  </div>"""

# New left block:
new_left = """  <div id="flip-left-text">
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">UNA EXPERIENCIA CON CARTAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">CONVERSACIONALES</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">ULTRA-PERSONALIZADAS</span></div></div>
    <div class="flt-line"><div class="flt-oh"><span class="flt-in">A VOSOTRXS DOS</span></div></div>
  </div>"""

content = content.replace(old_left, new_left)

# Original right block:
old_right = """  <div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os unirán</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">como nunca antes</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">cuestan dos cheesecakes</span></div></div>
    </div>"""

# New right block:
new_right = """  <div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os unirán como nunca antes</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que cuestan dos cheesecakes</span></div></div>
    </div>"""

content = content.replace(old_right, new_right)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
