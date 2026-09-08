import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """  #nav-logo img:first-child {
    height: 51px !important;
  }
  #nav-logo img:last-child {
    height: 25px !important;
  }"""

new_css = """  #nav-logo img:first-child {
    height: 56px !important;
  }
  #nav-logo img:last-child {
    height: 28px !important;
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced mobile logo CSS!")
else:
    print("Could not find mobile logo CSS")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
