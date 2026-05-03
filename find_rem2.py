import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find neural-canvas references in CSS
for term in ['neural-canvas', 'concept-1', 'concept-2', 'concept1', 'concept2']:
    idx = 0
    while True:
        idx = text.find(term, idx)
        if idx == -1:
            break
        line = text[:idx].count('\n') + 1
        ctx = text[max(0,idx-30):idx+80].replace('\n','\\n')
        print(f'Line {line}: ...{ctx}...')
        idx += 1
