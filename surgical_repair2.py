with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Lines 4921-4955:')
for i in range(4920, 4955):
    print(repr(lines[i][:100]))
