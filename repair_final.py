import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The broken section is lines 4917 to ~5073 (the entire messed up block)
# We need to:
# 1. Fix line 4917: restore the original comment
# 2. Remove lines 4918-5072 (the injected magazine block + duplicate)
# 3. Keep from line 5073 onwards

# First find the end of the duplicate block
end_of_duplicate = None
for i in range(5030, 5090):
    if '} else {' in lines[i] or 'overlay.style.opacity' in lines[i]:
        continue
    if 'if (magazineScene)' in lines[i]:
        end_of_duplicate = i
        print(f'Found if (magazineScene) at line {i+1}: {repr(lines[i][:80])}')
        break

# Let's check what's at line 5060-5075
print('Lines 5060-5080:')
for i in range(5059, 5080):
    print(f'{i+1}: {repr(lines[i][:100])}')
