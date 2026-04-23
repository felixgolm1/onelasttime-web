import re

with open('temp_test.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the _runIntroAnim block
idx = text.find('window._runIntroAnim')
if idx == -1:
    print('Not found!')
else:
    # Get context around it
    ctx = text[max(0, idx-3000):idx+500]
    with open('intro_anim_block.txt', 'w', encoding='utf-8') as out:
        out.write(ctx)
    print(f'Written {len(ctx)} chars to intro_anim_block.txt')
