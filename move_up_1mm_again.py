import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r"transform: translateY\(-5\.6vh\) scale\(1\.10\) !important;"
replacement = r"transform: translateY(-6.1vh) scale(1.10) !important;"

content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
