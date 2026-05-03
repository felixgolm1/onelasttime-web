import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all remaining references to concept-1 and concept-2
for term in ['concept-1', 'concept-2', 'c1-', 'c2-', 'concept1', 'concept2', 
             'initConcept', 'initNeural', 'neural-canvas', 'c1_', 'c2_']:
    count = text.count(term)
    if count > 0:
        idx = text.find(term)
        line = text[:idx].count('\n') + 1
        print(f'{term!r:30s} x{count}  first at line {line}')
