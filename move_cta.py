import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of translateX(-22px) in the CTA span
content = content.replace("transform: translateX(-22px)", "transform: translateX(-14px)")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
