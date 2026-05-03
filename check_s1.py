import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(content[75451:75451+500])
