import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update nav-logo top
content = content.replace(
    "#nav-logo {\n    left: 5% !important;\n    top: 4% !important;\n  }",
    "#nav-logo {\n    left: 5% !important;\n    top: 10% !important;\n  }"
)

# Update headline top
content = content.replace(
    "#headline {\n    top: 14% !important;",
    "#headline {\n    top: 25% !important;"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done spacing updates.")
