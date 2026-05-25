# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Buscamos h1 de RISE
match = re.search(r'<h1 style="font-family: \'Playfair Display\', \'Times New Roman\', serif;[^>]+>RISE<span[^>]+></span></h1>', text)

if match:
    new_h1 = """<h1 style="font-family: 'Playfair Display', 'Times New Roman', serif; font-size: 8rem; color: #fdf5e6; margin: 0; line-height: 0.8; letter-spacing: -0.02em; font-weight: 700; position: relative; display: inline-block; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);">
        <span class="rise-l" style="display:inline-block; transition: none;">R</span><span class="rise-l" style="display:inline-block; transition: none;">I</span><span class="rise-l" style="display:inline-block; transition: none;">S</span><span class="rise-l" style="display:inline-block; transition: none;">E</span>
        <span class="rise-dot" style="position: absolute; top: -5px; right: -18px; width: 12px; height: 12px; background: #fdf5e6; border-radius: 50%; box-shadow: 1px 1px 4px rgba(0,0,0,0.5); display:inline-block; transition: none;"></span>
    </h1>"""
    
    updated_text = text.replace(match.group(0), new_h1)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("RISE HTML Updated!")
else:
    print("Could not find RISE h1.")
