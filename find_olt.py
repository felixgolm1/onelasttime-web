import re

with open('temp_test.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for olt-card-div in context
idx = text.find('olt-card-div')
while idx != -1:
    ctx = text[max(0, idx-100):idx+300]
    with open(f'olt_ctx_{idx}.txt', 'w', encoding='utf-8') as out:
        out.write(ctx)
    print(f'Found at {idx}')
    idx = text.find('olt-card-div', idx+1)
