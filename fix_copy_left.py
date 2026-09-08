import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

pattern = re.compile(r'<h1>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">EXPERIMENTA LA CENA</span></span>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">M\u00c1S TRANSFORMADORA</span></span>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">QUE HAS TENIDO JAM\u00c1S</span></span>\s*</h1>\s*<hr class="headline-divider">\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="headline-sub oh-inner" style="display:block; margin:0;">En tu restaurante favorito, o en casa</p></span>', re.DOTALL)

new_headline = '''<h1>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">LA CENA M\u00c1S</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">TRANSFORMADORA</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">DE TU VIDA</span></span>
      </h1>
      <hr class="headline-divider">
      <span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="headline-sub oh-inner" style="display:block; margin:0;">En tu restaurante favorito o en casa</p></span>'''

content = pattern.sub(new_headline, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
