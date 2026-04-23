import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print(f'Total lines: {len(lines)}')

# Find the HTML sections to remove
# Section 2: concept-2-section (lines ~1824-1854)
# Section 1: concept-1-section (lines ~1856-1886)
# We'll find them by content

new_lines = []
skip = False
skip_depth = 0
i = 0
removed_sections = []

while i < len(lines):
    line = lines[i]
    stripped = line.strip()
    
    # Detect start of concept-1 or concept-2 HTML section
    if '<!-- CONCEPTO 2: AURA' in line or '<!-- CONCEPTO 1: MAPA' in line:
        skip = True
        section_start = i
        skip_depth = 0
        removed_sections.append(f'Removed HTML section starting line {i+1}: {stripped[:60]}')
    
    if skip:
        # Count section tags to find closing </section>
        skip_depth += line.count('<section') - line.count('</section')
        if '</section>' in line and skip_depth <= 0:
            skip = False
            i += 1
            continue
        i += 1
        continue
    
    new_lines.append(line)
    i += 1

for r in removed_sections:
    print(r)
print(f'Lines after HTML removal: {len(new_lines)}')

text2 = '\n'.join(new_lines)

# Remove CSS blocks for concept-1 and concept-2
css_patterns = [
    (r'/\* --- CONCEPT 2 SECTION --- \*/', r'/\* ── FLIP SIDE TEXTS'),
    (r'/\* --- CONCEPT 1 SECTION --- \*/', r'/\* ── FLIP SIDE TEXTS'),
]

# Remove CSS from "/* --- CONCEPT 2 SECTION --- */" to just before "/* ── FLIP SIDE TEXTS"
m2 = re.search(r'/\* --- CONCEPT 2 SECTION --- \*/', text2)
m_flip = re.search(r'/\* ── FLIP SIDE TEXTS', text2)
if m2 and m_flip:
    text2 = text2[:m2.start()] + text2[m_flip.start():]
    print('Removed CSS concept-2 + concept-1 block')

# Remove JS functions: initNeuralCanvas, initConcept1, initConcept2
# Find and remove initConcept2() call and function
# Find "function initConcept2()" to "initConcept2();" (the call at end)
def remove_js_function(text, fname):
    # Find function definition
    pattern = rf'// ── CONCEPT [12] [\w& \/]+\n\s*function {fname}\(\)'
    m = re.search(pattern, text)
    if not m:
        # Try simpler
        pattern2 = rf'function {fname}\(\)'
        m = re.search(pattern2, text)
    if not m:
        print(f'  {fname}: function NOT found')
        return text
    
    start = m.start()
    # Back up to include the comment before
    comment_start = text.rfind('\n', 0, start)
    # Find the matching closing brace
    depth = 0
    pos = m.start()
    found_open = False
    for ci, ch in enumerate(text[m.start():]):
        if ch == '{':
            depth += 1
            found_open = True
        elif ch == '}':
            depth -= 1
            if found_open and depth == 0:
                func_end = m.start() + ci + 1
                break
    
    # Also remove the call at end: fname();\n
    text_after = text[func_end:]
    call_pattern = rf'\s*{fname}\(.*?\);\s*\n'
    text_after2 = re.sub(call_pattern, '\n', text_after, count=1)
    
    # Remove the comment line(s) before the function
    before = text[:start]
    # Remove comment block before
    comment_match = re.search(r'(// ── CONCEPT [123] [^\n]+\n\s*)', before[::-1])
    
    removed_text = text[start:func_end]
    print(f'  {fname}: removed {len(removed_text)} chars')
    return text[: start] + text_after2

# Remove the sections in right order
for fname in ['initNeuralCanvas', 'initConcept2', 'initConcept1']:
    text2 = remove_js_function(text2, fname)

# Also remove the section comment headings in JS
text2 = re.sub(r'// ── CONCEPT [123][^\n]*\n\s*(?=function)', '', text2)
text2 = re.sub(r'\s*initNeuralCanvas\(\);\s*\n', '\n', text2)
text2 = re.sub(r'\s*initConcept2\(\);\s*\n', '\n', text2)
text2 = re.sub(r'\s*initConcept1\(\);\s*\n', '\n', text2)
text2 = re.sub(r'\s*setTimeout\(initConcept1,\s*\d+\);\s*// delay start[^\n]*\n', '\n', text2)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text2)

new_line_count = text2.count('\n') + 1
print(f'Final line count: {new_line_count}')
print('Done!')
