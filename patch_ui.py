import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject #mobile-menu-pill into #nav-logo
nav_logo_old = """<div id="nav-logo" style="display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
    <img src="assets/img/logo%20one%20last%20time.png\""""

nav_logo_new = """<div id="nav-logo" style="display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
    <div id="mobile-menu-pill" style="display: none;">+ MENU</div>
    <img src="assets/img/logo%20one%20last%20time.png\""""

if nav_logo_old in content:
    content = content.replace(nav_logo_old, nav_logo_new)
else:
    print("Warning: Could not find #nav-logo block to inject menu pill.")


# 2. Add mobile CSS rules
mobile_css = """
  #cta-top-container { display: none !important; }
  
  #mobile-menu-pill {
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
  }

  #nav-logo {
    left: 5% !important;
    top: 5% !important;
  }

  #headline {
    top: 15% !important;
    left: 5% !important;
    right: 5% !important;
    max-width: 100% !important;
    transform: translateZ(1000px);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 !important;
  }
  #headline h1 {
    text-align: center !important;
  }
  .headline-sub {
    text-align: center !important;
  }

  #subheadline {
    top: auto !important;
    bottom: 22% !important;
    left: 5% !important;
    right: 5% !important;
    transform: none;
  }
  #subheadline p {
    text-align: center !important;
    margin: 0 !important;
  }
"""

content = content.replace(
    "@media screen and (max-width: 768px) {",
    "@media screen and (max-width: 768px) {\n" + mobile_css
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done patching UI.")
