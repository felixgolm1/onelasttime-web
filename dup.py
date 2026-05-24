import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the container
start_marker = '<div class="oryzo-reviews-container">'
start_idx = content.find(start_marker)
script_start = content.find('<script>', start_idx)
end_idx = content.rfind('</div>', start_idx, script_start)

# Extract reviews
reviews_html = content[start_idx:end_idx]

# Modify IDs
reviews_html = re.sub(r'id="review-panel-(\d+)"', r'id="end-review-panel-\1"', reviews_html)
reviews_html = re.sub(r'id="rev(\d+)-quote"', r'id="end-rev\1-quote"', reviews_html)
reviews_html = reviews_html.replace('class="oryzo-reviews-container"', 'id="end-reviews-container" class="oryzo-reviews-container" style="position:absolute; top: 100vh; left:0; width:100vw; height:100vh; pointer-events:none;"')

# Insert before end marker
end_marker = '<!-- ══ FIN SECCIÓN ORYZO ══════════════════════════════ -->'
content = content.replace(end_marker, reviews_html + '\n    </div>\n    ' + end_marker)

# Update maxProg
content = content.replace('const maxProg = 28.6;', 'const maxProg = 30.6;')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
