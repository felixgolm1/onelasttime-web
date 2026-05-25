import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find setupScrollAnim
for i, line in enumerate(lines):
    if 'function setupScrollAnim' in line:
        print(f'setupScrollAnim at L{i+1}')
        # Print 20 lines
        for j in range(i, min(i+20, len(lines))):
            print(f'  L{j+1}: {lines[j][:90]}')
        break

print()
# Check what's between lines 3565-3580 (where prog and maxProg are set up)
print('=== prog setup area ===')
for i in range(3570, 3605):
    print(f'L{i+1}: {lines[i][:100]}')
