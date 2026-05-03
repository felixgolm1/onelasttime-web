import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

css_to_remove_mobile = 'background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0) 80%);'
content = content.replace(css_to_remove_mobile, 'background: none;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated mobile CSS correctly.")
