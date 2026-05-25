import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
main_script = scripts[2]

main_script = re.sub(r'//.*', '', main_script)
main_script = re.sub(r'/\*.*?\*/', '', main_script, flags=re.DOTALL)

lines = main_script.split('\n')

# Find the block with the extra brace by tracking indentation
open_c = 0
for i, line in enumerate(lines):
    old_c = open_c
    open_c += line.count('{')
    open_c -= line.count('}')
    if open_c < 0:
        print(f"Error: Negative brace count at line {i}: {line}")
        break

print(f"Final open count: {open_c}")

# Print the open brace stack! Let's print the line numbers of all open braces.
brace_stack = []
for i, line in enumerate(lines):
    for char in line:
        if char == '{':
            brace_stack.append(i)
        elif char == '}':
            if brace_stack:
                brace_stack.pop()
                
print("Unclosed braces at line numbers relative to script:")
for b in brace_stack:
    print(f"Line {b}: {lines[b]}")
