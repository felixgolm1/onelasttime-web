import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_right_pattern = r'<div id="flip-right-text">\s*<div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que te conectar\u00e1n</span></div></div>\s*<div class="flt-line"><div class="flt-oh"><span class="flt-in-up">inmediatamente con quien las uses</span></div></div>\s*<div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>\s*<div class="flt-line"><div class="flt-oh"><span class="flt-in-up">te costar\u00e1 el cheesecake</span></div></div>\s*</div>'

new_right = '''<div id="flip-right-text">
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">Que os unir\u00e1n</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">como nunca antes</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">por menos de lo que</span></div></div>
      <div class="flt-line"><div class="flt-oh"><span class="flt-in-up">cuestan dos cheesecakes</span></div></div>
    </div>'''

content = re.sub(old_right_pattern, new_right, content, flags=re.DOTALL)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
