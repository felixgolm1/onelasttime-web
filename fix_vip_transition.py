import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos la funcion toggleVipMode
search_target = "document.getElementById('vip-form-container').style.opacity = '0';"
replacement = "document.getElementById('vip-form-container').style.animation = 'none';\n    document.getElementById('vip-form-container').style.opacity = '0';"

if search_target in content:
    content = content.replace(search_target, replacement)
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed abrupt transition")
else:
    print("Could not find the target string")
