import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find concept-1-section and concept-2-section
for term in ['concept-1-section', 'c1-heatmap', 'concept-2-section', 'c2-card', 'La dimensi', 'Escribe tu refle']:
    idx = text.find(term)
    if idx != -1:
        ctx = text[max(0,idx-30):idx+80]
        with open('tmp_search.txt', 'w', encoding='utf-8') as out:
            out.write(ctx)
        # Find line number
        line_num = text[:idx].count('\n') + 1
        print(f'{term!r:40s} line {line_num}')
    else:
        print(f'{term!r:40s} NOT FOUND')
