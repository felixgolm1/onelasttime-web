import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('z-index: 100; /* Por encima de la caja (10), por debajo del tooltip y la carta zoomeada */', 'z-index: 30000; /* Por encima de TODO */')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated z-index to 30000")
