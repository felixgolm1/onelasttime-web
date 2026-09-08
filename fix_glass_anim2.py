# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Add classes to the HTML items
# In glass-who:
# The subtitle is missing, it's just ul. Wait, glass-who doesn't have a subtitle.
content = content.replace('<li style="margin-bottom: 16px; position: relative;">', '<li class="glass-who-item" style="margin-bottom: 16px; position: relative;">')
content = content.replace('<li style="position: relative; color: rgba(255,255,255,0.7);">', '<li class="glass-who-item" style="position: relative; color: rgba(255,255,255,0.7);">')

# In glass-objectives:
content = content.replace('<p style="color: rgba(255,255,255,0.8);', '<p class="glass-obj-item" style="color: rgba(255,255,255,0.8);')
content = content.replace('<li class="glass-who-item" style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>', '<li class="glass-obj-item" style="margin-bottom: 16px; position: relative;"><span style="position: absolute; left: -20px; color: #ccff00;">&#8226;</span> Conocernos a&uacute;n m&aacute;s</li>')
# Wait, I did a global replace for <li style... so they both have glass-who-item now!
# Let's fix that.
