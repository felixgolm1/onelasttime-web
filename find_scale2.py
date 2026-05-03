import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'_baseScaleFact', text))
print(f'Found {len(matches)} occurrences')

results = []
for m in matches:
    ctx = text[max(0, m.start()-60):m.end()+200]
    results.append(ctx)

with open('scale_usages.txt', 'w', encoding='utf-8') as out:
    for i, r in enumerate(results):
        out.write(f'--- {i} ---\n')
        out.write(r)
        out.write('\n\n')

print('Written to scale_usages.txt')
