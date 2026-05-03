import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = '''    .oryzo-review-panel {
      position: absolute;
      top: 0; /* Centrado permanentemente */
      left: 0;
      width: 100%;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10%;
      box-sizing: border-box;
      opacity: 0; /* Oculto por defecto */
      pointer-events: none; /* No bloquea clicks */
      color: white;
      z-index: 1000;
    }'''

new_css = '''    .oryzo-review-panel {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10%;
      box-sizing: border-box;
      opacity: 0;
      pointer-events: none;
      color: white;
      z-index: 1000;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 40%);
    }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated CSS with gradient background.")
else:
    print("WARNING: old_css not found!")
