import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total = len(lines)
print(f'Total lines: {total}')

# The problem: lines 4917 to 5035 are corrupted/duplicated
# Line 4917 (index 4916) has the broken comment
# The duplicate magazine block runs from 4918 to 5035

# We need to:
# 1. Replace line 4917 with the original correct code
# 2. Delete lines 4918 to 5035 (the injected + duplicate block)
# 3. Keep 5036+ as is (but the second 'if (magazineScene)' at 5087 is fine)

# The correct replacement for line 4917 is the original box comment + code:
fix_4917 = '           // El magazine-scene tiene un scale(0.85), por lo que el recuadro de 466x626 en realidad mide 396.1x532.1 pixeles en pantalla.\n'
fix_4918 = '           // Escala objetivo X = 396.1 / 89.74 = 4.414\n'
fix_4919 = '           // Escala objetivo Y = 532.1 / 329.41 = 1.615\n'
fix_4920 = '           boxScaleX = 1 + (4.414 - 1) * tX;\n'
fix_4921 = '           boxScaleY = 1 + (1.615 - 1) * tY;\n'
fix_4922 = '           shiftX = -44.87 * boxScaleX;\n'

# Build new lines list
new_lines = (
    lines[:4916] +  # keep lines 1-4916
    [fix_4917, fix_4918, fix_4919, fix_4920, fix_4921, fix_4922] +  # fix 4917-4922
    lines[5035:]  # skip corrupted block (lines 4918-5035 = indices 4917-5034), continue from 5036
)

print(f'New total lines: {len(new_lines)}')

# Verify fix
print('New lines 4916-4930:')
for i in range(4915, 4930):
    print(f'{i+1}: {repr(new_lines[i][:100])}')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Repair done!')
