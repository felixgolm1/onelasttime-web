import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# These variables are used in the render loop but must be declared before it
needed = ['mouseNX', 'mouseNY', 'mouseRawX', 'mouseRawY', 'CAM_BASE', 'CAM_LOOK', 'scrollTl', 'cssRenderer', 'cardRenderer2', 'cardScene2', 'cardCam2', 'globalGlbCard', 'cardCanvasEl']
for var in needed:
    decl_lines = []
    for i, line in enumerate(lines):
        if re.search(r'(const|let|var)\s+' + var + r'\b', line):
            decl_lines.append(i+1)
    if decl_lines:
        print(f'{var}: declared at lines {decl_lines}')
    else:
        print(f'{var}: *** NOT DECLARED ***')
