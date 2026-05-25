content = open('3d-test.html', 'r', encoding='utf-8').read()

# Find the end-reviews-container block
start_marker = 'id="end-reviews-container"'
idx_start_id = content.find(start_marker)
# Walk back to the '<div'
idx_start = content.rfind('<div', 0, idx_start_id)

# Find the closing comment that comes right after end-reviews-container
end_near = '<!-- \u2550\u2550 FIN SECCI\u00d3N ORYZO'
idx_comment = content.find(end_near, idx_start)
if idx_comment == -1:
    end_near = 'FIN SECCI'
    idx_comment = content.find(end_near, idx_start)

print('idx_start:', idx_start)
print('idx_comment:', idx_comment)

# Find the last </div> before the comment (this closes end-reviews-container)
idx_end = content.rfind('</div>', idx_start, idx_comment)
idx_end_full = idx_end + len('</div>')

block = content[idx_start:idx_end_full]
print('Block starts with:', repr(block[:100]))
print('Block ends with:', repr(block[-60:]))
print('Block length:', len(block))

# Fix inline style from absolute/100vh to fixed/inset:0
old_style = 'position:absolute; top: 100vh; left:0; width:100vw; height:100vh; pointer-events:none;'
new_style = 'position:fixed; inset:0; pointer-events:none; z-index:10007;'
block_fixed = block.replace(old_style, new_style)
if old_style in block:
    print('Style replaced OK')
else:
    print('WARNING: old style not found, trying partial match')
    # Try simpler replacement
    block_fixed = block.replace('position:absolute; top: 100vh;', 'position:fixed; top:0;')
    block_fixed = block_fixed.replace('width:100vw; height:100vh; ', '')

# Remove from current position (the indent before <div stays clean)
content_no_block = content[:idx_start].rstrip() + '\n' + content[idx_end_full:]

# Add block right before </body>
body_close = content_no_block.rfind('</body>')
content_final = content_no_block[:body_close] + '\n' + block_fixed + '\n' + content_no_block[body_close:]

open('3d-test.html', 'w', encoding='utf-8').write(content_final)
print('Done. New size:', len(content_final))
