with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Fix CSS
css_target = r"#slide1-copy-wrapper \{ margin-left: 0\.5cm !important; \}"
css_rep = "#slide1-copy-wrapper { margin-left: 0 !important; left: 20px !important; }"
content = re.sub(css_target, css_rep, content)

# Fix JS
js_target = r"var STICK_THRESHOLD = -22; // Deja que la caja se deslice 22px mas hacia la izquierda \(mitad del margen visual\) antes de anclarse"
js_rep = "var STICK_THRESHOLD = 0;"
content = re.sub(js_target, js_rep, content)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced CSS and JS!")
