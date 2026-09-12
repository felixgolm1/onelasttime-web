import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

bad_html = """<div id="made-by-humans" style="position: fixed; top: 50%; left: 50%; font-family: 'Inter', sans-serif; font-size: clamp(2.5rem, 8vw, 10rem); font-weight: 700; color: #f4f2ea; letter-spacing: -0.05em; white-space: nowrap; opacity: 1; z-index: 10001; pointer-events: none; visibility: hidden;">hecho por personas</div>"""

good_html = """<div id="made-by-humans" style="position: fixed; top: 50%; left: 50%; font-family: 'Inter', sans-serif; font-size: clamp(2.5rem, 8vw, 10rem); font-weight: 700; color: #f4f2ea; letter-spacing: -0.05em; white-space: nowrap; opacity: 1; z-index: 10005; pointer-events: none; visibility: hidden;">hecho por personas</div>"""

content = content.replace(bad_html, good_html)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
