import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace scroll-indicator bottom
content = content.replace('bottom: 3.2rem !important;', 'bottom: 3% !important;')

# Replace cta-bottom-container bottom
content = content.replace('bottom: 6.5rem !important;', 'bottom: calc(3% + 3.3rem) !important;')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
