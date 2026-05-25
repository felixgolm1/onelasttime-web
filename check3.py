import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find where setupScrollAnim is CALLED
for i, line in enumerate(lines):
    if 'setupScrollAnim()' in line:
        print(f'L{i+1}: {line.strip()[:100]}')

print()
# Find where the smoothScrollLoop is STARTED (called)
for i, line in enumerate(lines):
    if 'smoothScrollLoop()' in line and 'function' not in line:
        print(f'smoothScrollLoop() call at L{i+1}: {line.strip()[:80]}')

print()
# The issue might be that tryReveal never calls setupScrollAnim because animReady or gltfReady never becomes true
# Look at what sets animReady
for i, line in enumerate(lines):
    if 'animReady' in line and '=' in line:
        print(f'animReady at L{i+1}: {line.strip()[:80]}')
