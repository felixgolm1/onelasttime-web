import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

s = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)[2]

# function to strip comments
def strip_comments(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text

lines = s.split('\n')
open_count = 0
for i, line in enumerate(lines):
    clean = strip_comments(line)
    open_count += clean.count('{')
    open_count -= clean.count('}')
    if open_count < 0:
        print(f"Error at line {i}: closed without open")
        break

print(f"Final open count: {open_count}")
