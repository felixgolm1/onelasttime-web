import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Revert left headline
current_headline = '''      <h1>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">LA CENA M\u00c1S</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">TRANSFORMADORA</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">DE TU VIDA</span></span>
      </h1>'''

original_headline = '''      <h1>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">EXPERIMENTA LA CENA</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">M\u00c1S TRANSFORMADORA</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">QUE HAS TENIDO JAM\u00c1S</span></span>
      </h1>'''

content = content.replace(current_headline, original_headline)

# Revert right subtitle
current_right = '<p>\u00bfOtra cena hablando del trabajo?<br>\u00bfOtra cita superficial?<br>Rompe el guion y hag\u00e1mosla inolvidable.</p>'
original_right = '<p>\u00bfOtra cena m\u00e1s con tu pareja u otra cita?<br>Nah, hag\u00e1mosla inolvidable</p>'
content = content.replace(current_right, original_right)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
