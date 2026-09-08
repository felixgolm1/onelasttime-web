import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search_target = "document.getElementById('vip-form-container').style.opacity = '0';"
replacement = "document.getElementById('vip-form-container').style.animation = 'none';\n    document.getElementById('vip-form-container').style.opacity = '0';"

if search_target in content:
    content = content.replace(search_target, replacement)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed abrupt transition in index.html too")
else:
    print("Could not find the target string in index.html")
