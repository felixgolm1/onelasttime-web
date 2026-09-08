# -*- coding: utf-8 -*-
import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_text = 'en una de las mejores cenas que hayas tenido jams'
# Be careful with encoding, let's just use regex to replace 'mejores cenas' with 'cenas m&aacute;s memorables'
