import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Left block replace
old_left = '''    <div id="flip-left-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">UNA EXPERIENCIA</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">CON CARTAS</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">CONVERSACIONALES</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">ULTRA-PERSONALIZADAS</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">A TI</span></div></div>
    </div>'''

new_left = '''    <div id="flip-left-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">UNA EXPERIENCIA</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">CON CARTAS</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">CONVERSACIONALES</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">ULTRA-PERSONALIZADAS</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in">A VOSOTRXS DOS</span></div></div>
    </div>'''

# Right block replace
old_right = '''    <div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que te conectar\u00e1n</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">inmediatamente con quien las uses</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">te costar\u00e1 el cheesecake</span></div></div>
    </div>'''

new_right = '''    <div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os conectar\u00e1n</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">a otro nivel</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">os costar\u00e1 el cheesecake</span></div></div>
    </div>'''

content = content.replace(old_left, new_left)
content = content.replace(old_right, new_right)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
