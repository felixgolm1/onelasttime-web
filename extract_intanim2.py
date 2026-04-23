import re

with open('temp_test.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the startIntroAnim IIFE block
idx = text.find('(function startIntroAnim()')
if idx == -1:
    print('Not found!')
else:
    ctx = text[idx:idx+4000]
    with open('intro_anim_full.txt', 'w', encoding='utf-8') as out:
        out.write(ctx)
    print(f'Written {len(ctx)} chars - startIntroAnim found at {idx}')
