import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r"let flipProg = Math\.max\(0, Math\.min\(1, \(prog - 1\.30\) / 0\.27\)\);"
replacement = r"let flipProg = Math.max(0, Math.min(1, (prog - 2.20) / (9.62 - 2.20)));"

content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
