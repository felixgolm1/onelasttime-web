import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update #subheadline bottom from 28% to 18%
content = content.replace(
    "bottom: 28% !important;",
    "bottom: 18% !important;"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done lowering subheadline.")
