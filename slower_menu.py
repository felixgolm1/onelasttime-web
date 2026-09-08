import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Sidebar transition
content = content.replace(
    "transition: right 0.7s cubic-bezier(0.16, 1, 0.3, 1);",
    "transition: right 1.1s cubic-bezier(0.16, 1, 0.3, 1);"
)

# Overlay transition
content = content.replace(
    "transition: opacity 0.6s ease;",
    "transition: opacity 0.9s ease;"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
