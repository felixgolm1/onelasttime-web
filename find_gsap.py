import re
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find the GSAP onUpdate for the main timeline
match = re.search(r'ScrollTrigger\.create\(\{[\s\S]*?onUpdate:\s*\(self\)\s*=>\s*\{([\s\S]*?)\}\s*\}[)]', text)
if match:
    print('Found onUpdate. Length:', len(match.group(1)))
    # print lines related to portalP or magazine
    lines = match.group(1).split('\n')
    for i, line in enumerate(lines):
        if 'portalP' in line or 'magazine' in line or 'mag-ui' in line or '15.0' in line:
            print(f'{i}: {line.strip()}')
