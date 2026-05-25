with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div[^>]*magazine-content[^>]*>', text)
if m:
    print(m.group(0))
