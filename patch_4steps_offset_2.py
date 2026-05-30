import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# var tOpen = clamp01((p - 28.2) / 0.3);
content = content.replace("var tOpen = clamp01((p - 28.2) / 0.3);", "var tOpen = clamp01((p - 27.8) / 0.3);")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replace 28.2 OK")
