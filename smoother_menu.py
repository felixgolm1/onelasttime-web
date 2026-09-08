import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Sidebar transition
content = content.replace("transition: right 0.5s cubic-bezier(0.22, 1, 0.36, 1);", "transition: right 0.7s cubic-bezier(0.16, 1, 0.3, 1);")

# Overlay transition (from my previous global replace, let's just make all '0.5s ease' related to opacity longer)
content = content.replace("transition: opacity 0.5s ease;", "transition: opacity 0.6s ease;")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
