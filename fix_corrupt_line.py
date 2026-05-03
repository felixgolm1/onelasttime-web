with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

bad_line = None
for i, line in enumerate(lines):
    # The broken text is on its own line with just " con z-index:10004" etc
    stripped = line.strip()
    if stripped.startswith('con z-index') and not stripped.startswith('//'):
        bad_line = i
        print(f'Found bad line at {i+1}: {repr(line)}')

if bad_line is not None:
    del lines[bad_line]
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Removed bad line')
else:
    print('Bad line not found, checking again...')
    for i, line in enumerate(lines):
        if 'con z-index:10004' in line and not line.strip().startswith('//'):
            print(f'Line {i+1}: {repr(line)}')
