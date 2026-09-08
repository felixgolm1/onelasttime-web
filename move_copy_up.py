import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Subheadline replacement
old_css = """  #subheadline {
    top: auto !important;
    bottom: 18% !important;
    left: 5% !important;
    right: 5% !important;
    transform: none;
  }"""

new_css = """  #subheadline {
    top: auto !important;
    bottom: 26% !important;
    left: 5% !important;
    right: 5% !important;
    transform: none;
  }
  #cta-bottom-container {
    bottom: 6.5rem !important;
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced CSS")
else:
    print("Could not find CSS snippet. Trying regex.")
    # Fallback to regex
    content = re.sub(
        r"#subheadline \{\s*top: auto !important;\s*bottom: 18% !important;\s*left: 5% !important;\s*right: 5% !important;\s*transform: none;\s*\}",
        new_css,
        content
    )
    print("Used regex replacement")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

