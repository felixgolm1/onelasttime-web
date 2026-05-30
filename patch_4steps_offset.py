import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. tSlide
content = content.replace("var tSlide = clamp01((p - 26.6) / 1.6);", "var tSlide = clamp01((p - 26.2) / 1.6);")
# 2. tCamera
content = content.replace("var tCamera = clamp01((p - 26.6) / 3.0);", "var tCamera = clamp01((p - 26.2) / 3.0);")
# 3. localP
content = content.replace("let localP = p - 26.0;", "let localP = p - 25.6;")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replace OK")
