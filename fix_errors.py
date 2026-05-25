with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Buscamos magContent.style.borderColor hasta backgroundColor =
match = re.search(r'magContent\.style\.borderColor =[\s\S]*?gba\(6, 2, 15, \);', text)

if match:
    correct = """magContent.style.borderColor = `rgba(249, 204, 16, ${uiFade})`;
              magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;
              magContent.style.backgroundColor = `rgba(6, 2, 15, ${uiFade})`;"""
    text = text.replace(match.group(0), correct)
    
    # Also fix boxShadow if there's another one
    match2 = re.search(r'magContent\.style\.boxShadow = inset 0 0 0 2px rgba\(255, 255, 255, \);', text)
    if match2:
        text = text.replace(match2.group(0), "magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;")

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed!")
else:
    print("Not found")
