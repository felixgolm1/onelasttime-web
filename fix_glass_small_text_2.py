# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Fix font size of guarantee using regex
content = re.sub(
    r'(<p style="[^"]*?font-size:\s*)2\.1rem(;\s*font-weight:\s*700;\s*line-height:\s*)1\.2(;[^"]*?text-align:\s*right;[^"]*?">)',
    r'\g<1>1.25rem\g<2>1.3\g<3>',
    content
)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
