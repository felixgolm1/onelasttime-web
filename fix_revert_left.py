import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

pattern = re.compile(r'<h1>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">LA CENA M\u00c1S</span></span>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">TRANSFORMADORA</span></span>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">DE TU VIDA</span></span>\s*</h1>', re.DOTALL)

original_headline = '''<h1>
      <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">EXPERIMENTA LA CENA</span></span>
      <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">M\u00c1S TRANSFORMADORA</span></span>
      <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">QUE HAS TENIDO JAM\u00c1S</span></span>
    </h1>'''

content = pattern.sub(original_headline, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
