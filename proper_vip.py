import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Find style
style_start = idx.find('<style>\n    .vip-pill {')
style_end = idx.find('</style>', style_start) + 8
vip_style = idx[style_start:style_end]

# Find overlay
overlay_start = idx.find('<div id="vip-overlay"')
# The overlay ends right before the script that checks for the password
overlay_end = idx.find('<script>\n    // Comprobar si ya esta desbloqueado', overlay_start)
vip_overlay = idx[overlay_start:overlay_end]

# Find script
script_start = idx.find('<script>\n    // Comprobar si ya esta desbloqueado')
script_end = idx.find('</script>', script_start) + 9
vip_script = idx[script_start:script_end]

# Change localStorage to sessionStorage
vip_script = vip_script.replace('localStorage.getItem', 'sessionStorage.getItem')
vip_script = vip_script.replace('localStorage.setItem', 'sessionStorage.setItem')

vip_code = vip_style + '\n' + vip_overlay + '\n' + vip_script

# Verify length so we don't accidentally get 794KB again
if len(vip_code) > 20000:
    print(f"Error: vip_code is too large ({len(vip_code)} bytes).")
    exit(1)

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

body_tag = '<body class="bg-black text-white">'
head_tag = '</head>'

if 'vip-overlay' not in content:
    if body_tag in content:
        content = content.replace(body_tag, body_tag + '\n' + vip_code)
    else:
        content = content.replace(head_tag, head_tag + '\n' + vip_code)
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected into 3d-test.html successfully")
else:
    print("Already there")
