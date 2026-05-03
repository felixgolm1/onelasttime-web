import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find smoothScrollLoop function definition
idx = text.find('function smoothScrollLoop()')
if idx == -1:
    idx = text.find('smoothScrollLoop()')
print(f'smoothScrollLoop at {idx}')

# Find inScatter logic
idx2 = text.find('inScatter')
print(f'inScatter at {idx2}')

ctx = text[idx2-100:idx2+2000]
with open('inScatter.txt', 'w', encoding='utf-8') as out:
    out.write(ctx)
print('Written to inScatter.txt')
