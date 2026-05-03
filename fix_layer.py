import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Z-index of container
content = content.replace('z-index: 30000; /* Por encima de TODO */', 'z-index: 10005; /* Encima del 3D (10004) pero debajo del menu (10010) */')

# Remove the linear gradient from review-panel
css_to_remove = 'background: linear-gradient(to right, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 70%);'
content = content.replace(css_to_remove, 'background: none;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS correctly.")
