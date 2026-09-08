import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_html = '<div id="mobile-menu-pill" style="display: none; position: fixed; z-index: 1000000000; transition: all 0.3s ease;">MENU</div>'
new_html = '<div id="mobile-menu-pill" style="display: none; position: fixed; z-index: 1000000000; transition: all 0.3s ease;"><span id="menu-dot" style="display:inline-block; width:4px; height:4px; background-color:currentColor; border-radius:50%; margin-right:6px;"></span><span id="menu-text">MENU</span></div>'

if old_html in content:
    content = content.replace(old_html, new_html)
    print("Replaced HTML")
else:
    print("Failed to find HTML")

old_close = "pill.innerHTML = 'MENU';"
new_close = "document.getElementById('menu-text').innerHTML = 'MENU';"

if old_close in content:
    content = content.replace(old_close, new_close)
    print("Replaced close logic")

old_open = "pill.innerHTML = 'CERRAR';"
new_open = "document.getElementById('menu-text').innerHTML = 'CERRAR';"

if old_open in content:
    content = content.replace(old_open, new_open)
    print("Replaced open logic")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
