import re

with open('temp_test.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'animReady = true', text))
print(f'animReady = true occurrences: {len(matches)}')
for i, m in enumerate(matches):
    ctx = text[max(0, m.start()-200):m.end()+300]
    # write to file to avoid encoding issues
    with open(f'anim_ctx_{i}.txt', 'w', encoding='utf-8') as out:
        out.write(ctx)
    print(f'Context {i} written to anim_ctx_{i}.txt')
