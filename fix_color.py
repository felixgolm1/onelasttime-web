# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('color: rgba(255,255,255,0.6); font-size: 14px; font-weight: 500; margin-bottom: 6px;', 'color: #ffffff; font-size: 14px; font-weight: 500; margin-bottom: 6px;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Changed color to white")
