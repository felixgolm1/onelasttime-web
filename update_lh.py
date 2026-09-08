import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """  #subheadline p {
    text-align: center !important;
    margin: 0 !important;
    font-size: 1.4rem !important;
    line-height: 1.05 !important;
  }"""

new_css = """  #subheadline p {
    text-align: center !important;
    margin: 0 !important;
    font-size: 1.4rem !important;
    line-height: 1.15 !important;
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced!")
else:
    print("Not found!")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
