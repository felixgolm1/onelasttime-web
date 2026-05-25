with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print('=== Lines around 4920-4960 ===')
for i in range(4918, 4960):
    print(f'{i+1}: {lines[i][:110]}')
