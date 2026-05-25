import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract the main script block (the big one with 776 opens/closes)
import re
script_matches = list(re.finditer(r'<script[^>]*>(.*?)</script>', text, re.DOTALL))
main_script = None
main_script_start_line = 0
for m in script_matches:
    content = m.group(1)
    if len(content) > 100000:  # The big script
        main_script = content
        main_script_start_line = text[:m.start()].count('\n') + 1
        print(f'Found main script: starts at HTML line {main_script_start_line}, length {len(content)}')
        break

if main_script:
    lines = main_script.split('\n')
    # Look at very beginning of script
    print('\nFirst 5 lines of main script:')
    for i in range(min(5, len(lines))):
        print(f'  {i+1}: {lines[i][:80]}')
    
    # Check for outer IIFE
    first_nonblank = next((l.strip() for l in lines[:20] if l.strip()), '')
    print(f'\nFirst non-blank: {first_nonblank[:80]}')
    
    # Check where 'scene' and 'camera' are declared
    for i, line in enumerate(lines):
        if re.search(r'(const|let|var)\s+scene\b', line):
            print(f'scene declared at script line {i+1}: {line.strip()[:80]}')
        if re.search(r'(const|let|var)\s+camera\b', line):
            print(f'camera declared at script line {i+1}: {line.strip()[:80]}')
