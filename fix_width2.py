import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# specifically target the vip-submit-btn inline style
search = "style=\"padding: 1.2rem 2rem !important; height: auto; width: 100%; box-sizing: border-box;"
replace = "style=\"padding: 1.2rem 2rem !important; height: auto; width: 300px; box-sizing: border-box;"

if search in content:
    content = content.replace(search, replace)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed button width")
else:
    print("Could not find the specific style string")
