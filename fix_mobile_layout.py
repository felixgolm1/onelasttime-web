import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update scroll-indicator in mobile CSS
old_scroll = """  #cta-bottom-container {
    bottom: 6.5rem !important;
  }"""
new_scroll = """  #cta-bottom-container {
    bottom: 6.5rem !important;
  }
  .scroll-indicator {
    bottom: 3.2rem !important;
  }"""
if old_scroll in content:
    content = content.replace(old_scroll, new_scroll)
    print("Replaced scroll indicator position")

# 2. Update line-height of subheadline p
old_sub = """  #subheadline p {
    text-align: center !important;
    margin: 0 !important;
    font-size: 1.4rem !important;
  }"""
new_sub = """  #subheadline p {
    text-align: center !important;
    margin: 0 !important;
    font-size: 1.4rem !important;
    line-height: 1.05 !important;
  }"""
if old_sub in content:
    content = content.replace(old_sub, new_sub)
    print("Replaced subheadline line height")

# 3. Show headline-divider in mobile CSS
old_head = """  .headline-sub {
    text-align: center !important;
  }"""
new_head = """  .headline-sub {
    text-align: center !important;
  }
  .headline-divider {
    width: 75% !important;
    margin: 0.8rem 0 !important;
  }"""
if old_head in content:
    content = content.replace(old_head, new_head)
    print("Replaced headline-divider")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
