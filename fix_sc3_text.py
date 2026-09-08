# -*- coding: utf-8 -*-
import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_text = 'Dinos <b style="color: #ccff00;">tu objetivo</b> y haremos matem&aacute;ticamente imposible que no lo consigas'
new_text = 'Danos <b style="color: #ccff00;">el contexto y tu objetivo</b> y haremos matem&aacute;ticamente imposible que no lo consigas'

content = content.replace(old_text, new_text)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
