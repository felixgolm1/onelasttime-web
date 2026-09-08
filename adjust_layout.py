import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove <br> in subheadline
content = content.replace("?<br>Nah,", "? Nah,")

# 2. Extract #mobile-menu-pill from inside #nav-logo
old_nav_html = """<div id="nav-logo" style="display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
    <div id="mobile-menu-pill" style="display: none;">+ MENU</div>"""
new_nav_html = """<div id="mobile-menu-pill" style="display: none; position: fixed; z-index: 10000020;">+ MENU</div>
  <div id="nav-logo" style="display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">"""
if old_nav_html in content:
    content = content.replace(old_nav_html, new_nav_html)
else:
    print("Warning: Could not extract mobile-menu-pill.")

# 3. Update CSS rules for mobile
# Find the #mobile-menu-pill rule
old_pill_css = """#mobile-menu-pill {
    display: flex !important;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    border-radius: 20px;
    padding: 6px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
    backdrop-filter: blur(4px);
  }"""
new_pill_css = """#mobile-menu-pill {
    display: flex !important;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    border-radius: 20px;
    padding: 6px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
    backdrop-filter: blur(4px);
    position: fixed !important;
    top: 4% !important;
    right: 5% !important;
    left: auto !important;
  }"""
if old_pill_css in content:
    content = content.replace(old_pill_css, new_pill_css)
else:
    print("Warning: Could not update pill CSS.")

# Find the #nav-logo rule
old_logo_css = """#nav-logo {
    left: 5% !important;
    top: 5% !important;
  }"""
new_logo_css = """#nav-logo {
    left: 5% !important;
    top: 4% !important;
  }"""
if old_logo_css in content:
    content = content.replace(old_logo_css, new_logo_css)
else:
    print("Warning: Could not update logo CSS.")

# Find the #headline rule
old_headline_css = """#headline {
    top: 18% !important;"""
new_headline_css = """#headline {
    top: 14% !important;"""
if old_headline_css in content:
    content = content.replace(old_headline_css, new_headline_css)
else:
    print("Warning: Could not update headline CSS.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done adjusting layout.")
