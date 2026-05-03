import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('</style>')
print(content[idx-100:idx+50])
