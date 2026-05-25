import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
main_script = scripts[-1]

main_script = re.sub(r'//.*', '', main_script)
main_script = re.sub(r'/\*.*?\*/', '', main_script, flags=re.DOTALL)

lines = main_script.split('\n')

open_c = 0
for i, line in enumerate(lines):
    open_c += line.count('{')
    open_c -= line.count('}')

print(f"Final open count: {open_c}")
