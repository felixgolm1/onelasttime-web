import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <div id="headline">
old_head = '<div id="headline">'
new_head = '<div id="headline" style="--head-blur: 10px; --head-alpha: 0.05;">'
if old_head in content:
    content = content.replace(old_head, new_head)
    print("Replaced headline HTML")

# Replace <div id="subheadline">
old_sub = '<div id="subheadline">'
new_sub = '<div id="subheadline" style="--sub-blur: 6px; --sub-alpha: 0.05;">'
if old_sub in content:
    content = content.replace(old_sub, new_sub)
    print("Replaced subheadline HTML")

# Also fix the CSS so there's no conflict or just leave it, it's fine since inline overrides CSS.
# Let's also update the mobile CSS to make sure it's not overriding the variables.

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
