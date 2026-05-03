import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find card-morph-group in HTML with surrounding context
idx = text.find('card-morph-group')
while idx != -1:
    ctx = text[max(0,idx-60):idx+200]
    with open(f'morph_{idx}.txt', 'w', encoding='utf-8') as f2:
        f2.write(ctx)
    idx = text.find('card-morph-group', idx+1)
    
print('searched')
