import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace _t definition in both places
content = re.sub(
    r"const _t\s*=\s*Math\.max\(0,\s*Math\.min\(1,\s*\(gSY - 1\.0\)\s*/\s*\(_GS_SC - 1\.0\)\)\);",
    r"const _baseGSY = window.matchMedia('(max-width: 768px)').matches ? 0.90 : 1.0;\n            const _t = Math.max(0, Math.min(1, (gSY - _baseGSY) / (_GS_SC - _baseGSY)));",
    content
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced logic with regex")
