import re

files = ['terminos.html', 'privacidad.html', 'garantia.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the header style
    # We want to remove background: rgba(0,0,0,0.5); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.05);
    # and replace with background: transparent;
    
    # Let's just use regex to replace the specific style block of the header
    pattern = r'backdrop-filter:\s*blur\(10px\);\s*-webkit-backdrop-filter:\s*blur\(10px\);\s*background:\s*rgba\(0,0,0,0\.5\);\s*border-bottom:\s*1px\s+solid\s+rgba\(255,255,255,0\.05\);'
    replacement = r'background: transparent; border-bottom: none; pointer-events: none;'
    
    # Wait, if I add pointer-events: none to the header, the links inside won't be clickable!
    # I should NOT add pointer-events: none to the header. 
    replacement = r'background: transparent; border-bottom: none;'
    
    text = re.sub(pattern, replacement, text)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {file}')
