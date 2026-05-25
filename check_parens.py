import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
if not scripts:
    print("NO SCRIPTS FOUND!")
    exit()

main_script = scripts[-1]
main_script = re.sub(r'//.*', '', main_script)
main_script = re.sub(r'/\*.*?\*/', '', main_script, flags=re.DOTALL)

lines = main_script.split('\n')

open_p = 0
for i, line in enumerate(lines):
    open_p += line.count('(')
    open_p -= line.count(')')

print(f"Final paren count: {open_p}")
