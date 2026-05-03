import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'_baseScaleFact', text))
print(f'Found {len(matches)} occurrences')
for m in matches:
    ctx = text[max(0, m.start()-100):m.end()+300]
    print('---')
    print(ctx[:300])
