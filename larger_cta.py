import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

mobile_css = """  #cta-bottom-container {
    bottom: 6.5rem !important;
  }"""
new_mobile_css = """  #cta-bottom-container {
    bottom: 6.5rem !important;
    padding: 0 0.4rem !important;
  }
  #heroCta {
    padding: 1.45rem 2rem !important;
  }"""

if mobile_css in content:
    content = content.replace(mobile_css, new_mobile_css)
    print("Replaced!")
else:
    print("Not found, using regex...")
    content = re.sub(r'#cta-bottom-container\s*\{\s*bottom: 6\.5rem !important;\s*\}', new_mobile_css, content)
    print("Done regex")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
