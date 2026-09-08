import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #headline top to 20%
content = content.replace(
    "#headline {\n    top: 25% !important;",
    "#headline {\n    top: 20% !important;"
)

# 2. Update #subheadline bottom to 28%
content = content.replace(
    "bottom: 22% !important;",
    "bottom: 28% !important;"
)

# 3. Update #subheadline p font size
target_subheadline_p = """#subheadline p {
    text-align: center !important;
    margin: 0 !important;
  }"""
new_subheadline_p = """#subheadline p {
    text-align: center !important;
    margin: 0 !important;
    font-size: 1.4rem !important;
  }"""
if target_subheadline_p in content:
    content = content.replace(target_subheadline_p, new_subheadline_p)
else:
    print("Warning: Could not find target #subheadline p rule.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done making final layout adjustments.")
