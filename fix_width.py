import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change width: 100% to max-width: 300px in the inline styles of the button
content = content.replace('width: 100%;', 'width: 300px;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated width")
