# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find and replace the entire magazine JS animation block
old_js = re.search(r'if \(magazineScene\) \{[\s\S]*?magazineScene\.style\.opacity = 1;[\s\S]*?// 1\. Letras de RISE[\s\S]*?const magContent = magazineScene\.querySelector\(\'\.magazine-content\'\);[\s\S]*?magContent\.style\.backgroundPosition = `center \$\{bgPos\}%`;\n           \}\n         \}', text)

if old_js:
    print("Found magazine JS block, length:", len(old_js.group(0)))
else:
    print("NOT FOUND - searching for smaller chunk")
    # Try smaller
    test = re.search(r'const magContent = magazineScene', text)
    print("magContent line found:", bool(test))
