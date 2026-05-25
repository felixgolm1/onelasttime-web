with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total = len(lines)
print(f'Total lines before: {total}')

# Find exact end lines for each block (0-indexed)
# We'll scan for specific markers

def find_line(marker, start=0):
    for i in range(start, len(lines)):
        if marker in lines[i]:
            return i
    return -1

def find_block_end(start_idx, end_marker, max_search=200):
    for i in range(start_idx, min(start_idx + max_search, len(lines))):
        if end_marker in lines[i]:
            return i
    return -1

# === MAP ALL BLOCKS ===

# 1. brain-label CSS: lines 1516-1534 (idx 1515-1533)
brain_css_start = find_line('.brain-label {')
# Find the </style> after it
brain_css_end = find_block_end(brain_css_start, '</style>', 30)
print(f'Brain CSS: lines {brain_css_start+1} to {brain_css_end+1}')

# 2. CSS2DRenderer script
css2d_line = find_line('CSS2DRenderer.js')
print(f'CSS2DRenderer script: line {css2d_line+1}')

# 3. BRAIN PROGRESS LOGIC blocks (there are 3 copies, find them all)
bpl_lines = []
idx = 0
while True:
    i = find_line('// ==== BRAIN PROGRESS LOGIC ====', idx)
    if i < 0:
        break
    # Find the end of this block (look for '        }' after the if/else)
    end = find_block_end(i, '        } else {', 60)
    if end < 0:
        end = find_block_end(i, '        }', 60)
    # Find 'else { if (brainCanvasEl)' to get the full else block too
    else_end = find_block_end(end, '        }', 10)
    bpl_lines.append((i, else_end))
    print(f'BRAIN PROGRESS LOGIC: lines {i+1} to {else_end+1}')
    idx = i + 1

# 4. Brain globals: line 7184 to line 7193
bg_start = find_line('// ===== BRAIN GLOBALS =====')
# Goes to just before initBrainRenderer
init_start = find_line('(function initBrainRenderer()')
print(f'Brain globals: lines {bg_start+1} to {init_start-1+1}')

# 5. initBrainRenderer to first })(); at ~7597
init_end = find_block_end(init_start, '  })();', 500)
print(f'initBrainRenderer IIFE: lines {init_start+1} to {init_end+1}')

# 6. Magazine-to-brain loop: line 7604 inside main loop
# This is the (function loop() block that includes the brain transition
# The main loop starts at 7599 and ends at 7696
loop_start = find_line('(function loop()')
loop_end = find_block_end(loop_start, '  })();', 200)
print(f'Main animation loop: lines {loop_start+1} to {loop_end+1}')

# 7. brain-annotations CSS: line 7748
bann_css = find_line('#brain-annotations{position')
# Find closing </style>
bann_css_end = find_block_end(bann_css, '</style>', 20)
print(f'brain-annotations CSS: lines {bann_css+1} to {bann_css_end+1}')

# 8. brain-annotations HTML + script
bann_html = find_line('id="brain-annotations"')
bann_html_end = find_line("window.updateBrainAnnotations=updateBrainAnnotations", bann_html)
bann_html_end = find_block_end(bann_html_end, '</script>', 5)
print(f'brain-annotations HTML+script: lines {bann_html+1} to {bann_html_end+1}')
