import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Smoother sidebar transition
content = re.sub(
    r"transition:\s*right\s*0\.4s\s*cubic-bezier\(0\.85,\s*0,\s*0\.15,\s*1\);",
    r"transition: right 0.5s cubic-bezier(0.22, 1, 0.36, 1);",
    content
)

# 2. Add -webkit-tap-highlight-color to #mobile-menu-pill
old_pill_css = """  #mobile-menu-pill {
    display: flex !important;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.1);"""

new_pill_css = """  #mobile-menu-pill {
    -webkit-tap-highlight-color: transparent;
    display: flex !important;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.1);"""

content = content.replace(old_pill_css, new_pill_css)

# 3. Change '+ MENU' to 'MENU' in HTML
content = re.sub(
    r'<div id="mobile-menu-pill"[^>]*>\+ MENU</div>',
    lambda m: m.group(0).replace('+ MENU', 'MENU'),
    content
)

# 4. Change '+ MENU' to 'MENU' in JS
content = content.replace("pill.innerHTML = '+ MENU';", "pill.innerHTML = 'MENU';")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Changes applied!")
