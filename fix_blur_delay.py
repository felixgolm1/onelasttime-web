import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the GSAP Reveal UI block
block_start = content.find('// Reveal UI perif')
if block_start != -1:
    block_end = content.find('});', block_start) + 3
    block = content[block_start:block_end]
    content = content.replace(block, "")
    print("Removed block")
else:
    print("Block not found")

# 2. Change z-index of #loader to 10000020
if "z-index:10001;" in content:
    content = content.replace("z-index:10001;", "z-index:10000020;")
    print("Changed loader z-index")
else:
    print("z-index:10001; not found")

# 3. Change opacity: 0 to opacity: 1 in CSS
# We will just replace opacity: 0; with opacity: 1; in the specific blocks
ids_to_fix = [
    r'(#headline\s*\{[^}]*?)opacity:\s*0;',
    r'(#subheadline\s*\{[^}]*?)opacity:\s*0;',
    r'(#nav-logo\s*\{[^}]*?)opacity:\s*0;',
    r'(#nav-menu\s*\{[^}]*?)opacity:\s*0;',
    r'(#cta-bottom-container\s*\{[^}]*?)opacity:\s*0;',
    r'(#mobile-menu-pill\s*\{[^}]*?)opacity:\s*0;',
    r'(\.scroll-indicator\s*\{[^}]*?)opacity:\s*0;'
]

for pattern in ids_to_fix:
    content = re.sub(pattern, r'\1opacity: 1;', content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
