# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Prefix is currently: font-size: 14px;
content = content.replace('font-size: 14px; font-weight: 500; margin-bottom: 6px;', 'font-size: 17px; font-weight: 500; margin-bottom: 8px;')

# Link is currently: font-size: 14px;
content = content.replace('color: #ccff00; font-size: 14px; font-weight: 600;', 'color: #ccff00; font-size: 17px; font-weight: 600;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Increased font size by 20%")
