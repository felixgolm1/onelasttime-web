# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("toggle.innerHTML = 'Ya tengo un c&oacute;digo';", "toggle.innerHTML = 'Ya tengo el c&oacute;digo';")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated text")
