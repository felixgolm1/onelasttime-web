import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update logo size in mobile CSS
mobile_logo_css = """
  #nav-logo img:first-child {
    height: 44px !important;
  }
  #nav-logo img:last-child {
    height: 22px !important;
  }
"""

# Inject after #nav-logo rule
target_nav_logo = """#nav-logo {
    left: 5% !important;
    top: 8%;
  }"""
if target_nav_logo in content:
    content = content.replace(target_nav_logo, target_nav_logo + "\n" + mobile_logo_css)
else:
    print("Warning: could not find nav-logo target.")

# 2. Update headline size
target_headline_h1 = """#headline h1 {
    text-align: center !important;
  }"""
new_headline_h1 = """#headline h1 {
    text-align: center !important;
    font-size: 1.55rem !important;
  }"""
if target_headline_h1 in content:
    content = content.replace(target_headline_h1, new_headline_h1)
else:
    print("Warning: could not find headline h1 target.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done adjusting logo size and headline size.")
