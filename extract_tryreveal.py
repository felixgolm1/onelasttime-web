import re

with open('temp_test.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find tryReveal in temp_test.js
idx = text.find('function tryReveal()')
if idx == -1:
    print('tryReveal not found!')
else:
    ctx = text[idx:idx+2000]
    with open('tryreveal_orig.txt', 'w', encoding='utf-8') as out:
        out.write(ctx)
    print(f'tryReveal found at {idx}, written 2000 chars')
