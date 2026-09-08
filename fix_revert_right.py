import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Revert the right side lines
old_right = '''<div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os conectar\u00e1n</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">a otro nivel</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">os costar\u00e1 el cheesecake</span></div></div>
    </div>'''
    
new_right = '''<div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que te conectar\u00e1n</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">inmediatamente con quien las uses</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">te costar\u00e1 el cheesecake</span></div></div>
    </div>'''
    
content = content.replace(old_right, new_right)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
