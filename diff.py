import difflib
import sys

sys.stdout.reconfigure(encoding='utf-8')

file1 = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
file2 = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'

with open(file1, 'r', encoding='utf-8') as f1:
    lines1 = f1.readlines()
with open(file2, 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()

diff = difflib.unified_diff(lines1, lines2, fromfile='prod', tofile='dev', n=2)
for line in diff:
    print(line, end='')
