import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Delete variables
content = re.sub(r'let cardRenderer2 = null;\s*let cardScene2 = null;\s*let cardCam2 = null;\s*', '', content)

# Delete initCardRenderer
content = re.sub(r'function initCardRenderer\(\) \{.*?\}(?=\s*// Cargar texturas)', '', content, flags=re.DOTALL)

# Delete resize
content = re.sub(r'if \(cardRenderer2\) \{\s*cardRenderer2\.setSize\(window\.innerWidth, window\.innerHeight\);\s*cardCam2\.aspect = window\.innerWidth / window\.innerHeight;\s*cardCam2\.updateProjectionMatrix\(\);\s*\}\s*', '', content)

# Delete call
content = re.sub(r'if \(!cardRenderer2\) initCardRenderer\(\);\s*', '', content)

# Delete render loop
content = re.sub(r'// Render separado de las cartas GLB en su canvas transparente\s*if \(cardRenderer2 && cardScene2 && cardCam2.*?\)\s*\{\s*cardRenderer2\.render\(cardScene2, cardCam2\);\s*\}\s*', '', content, flags=re.DOTALL)

# Delete WebGL canvas from HTML if present
content = re.sub(r'<canvas id="card-canvas".*?></canvas>', '', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 3 done")
