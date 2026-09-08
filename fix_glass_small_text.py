# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Fix bullet point
content = content.replace('trabajando).</li>', 'trabajando)</li>')

# Fix GLB scale
content = content.replace('globalGlbCard.scale.setScalar(lc.scale * boardScale);', 'globalGlbCard.scale.setScalar(lc.scale * boardScale * 1.25);')

# Fix font size of guarantee only
old_p = '''<p style="color: #fff; font-family: 'Inter', sans-serif; font-size: 2.1rem; font-weight: 700; line-height: 1.2; margin: 0; text-align: right; text-transform: uppercase;">
        SI NO LO CONSIGUES, ESTA EXPERIENCIA CORRE DE NUESTRA CUENTA Y OS REGALAMOS OTRA.
      </p>'''

new_p = '''<p style="color: #fff; font-family: 'Inter', sans-serif; font-size: 1.25rem; font-weight: 700; line-height: 1.3; margin: 0; text-align: right; text-transform: uppercase;">
        SI NO LO CONSIGUES, ESTA EXPERIENCIA CORRE DE NUESTRA CUENTA Y OS REGALAMOS OTRA.
      </p>'''

content = content.replace(old_p, new_p)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
