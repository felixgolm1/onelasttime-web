with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total = len(lines)

# Things to remove (0-indexed):
# 1. CSS2DRenderer script tag at line 2629 (idx 2628)
# 2. Brain CSS styles: lines 1516-1534 (idx 1515-1533) - .brain-label styles
# 3. Brain globals + initBrainRenderer IIFE: lines 7184-7597 (idx 7183-7596)
# 4. Brain render in main loop: lines 7679-7688 (idx 7678-7687)
# 5. Brain transition loop block: lines 7599-7657 (idx 7598-7656)
# 6. Brain annotations HTML+script: lines 7747-7805 (idx 7746-7804)
# 7. The #brain-annotations CSS block: lines 7747-7759 (idx 7746-7758)
# 8. BRAIN PROGRESS LOGIC blocks in scroll handler (lines 5031-5076, 5340-5376, 5440-5476)

# Let's do this carefully, working bottom-up to preserve line numbers
# Step 1: Find exact line ranges for each block

for i, line in enumerate(lines):
    line_stripped = line.strip()
    if '.brain-label {' in line:
        print(f'brain-label CSS starts at line {i+1}')
    if '#b-label-1 b' in line:
        print(f'b-label styles end around line {i+1}')
    if 'CSS2DRenderer.js' in line:
        print(f'CSS2DRenderer script at line {i+1}')
    if '// ===== BRAIN GLOBALS =====' in line:
        print(f'Brain globals start at line {i+1}')
    if '(function initBrainRenderer()' in line:
        print(f'initBrainRenderer starts at line {i+1}')
    if '// ==== BRAIN PROGRESS LOGIC ====' in line:
        print(f'BRAIN PROGRESS LOGIC at line {i+1}')
    if '// ===== MAGAZINE TO BRAIN TRANSITION =====' in line:
        print(f'Magazine to brain transition at line {i+1}')
    if 'id="brain-annotations"' in line:
        print(f'brain-annotations HTML at line {i+1}')
    if "window.updateBrainAnnotations=updateBrainAnnotations" in line:
        print(f'updateBrainAnnotations end at line {i+1}')
    if '#brain-annotations{position' in line:
        print(f'brain-annotations CSS at line {i+1}')
    if '// ===== BRAIN RENDER =====' in line:
        print(f'BRAIN RENDER in main loop at line {i+1}')
