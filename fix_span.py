import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"\.review-author span \{\s*display: flex !important;\s*flex-direction: column !important;\s*align-items: center !important;\s*gap: 4px !important;\s*font-size: 0\.5rem !important;\s*margin-top: 4px !important;\s*text-transform: none !important;\s*\}"

replacement = '''.review-author span {
          display: block !important;
          text-align: center !important;
          font-size: 0.5rem !important;
          margin-top: 4px !important;
          text-transform: none !important;
          line-height: 1.2 !important;
        }'''

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    print('REPLACED')
else:
    print('TARGET NOT FOUND')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
