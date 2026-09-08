import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """  #nav-logo {
    left: 2% !important;
    top: 8%;
  }"""

new_css = """  #nav-logo {
    left: 2%;
    top: 8%;
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced!")
else:
    print("Not found!")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
