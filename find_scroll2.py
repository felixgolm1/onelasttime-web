import re, sys
with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

# Find how scrollTl.progress is SET (not just read)
hits = [(m.start(), text[m.start():m.start()+200]) for m in re.finditer(r'scrollTl\.progress\s*\(', text)]
sys.stdout.buffer.write(b'scrollTl.progress calls:\n')
for pos, ctx in hits:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx) + '\n').encode('utf-8'))

# Find scroll event listener
hits2 = [(m.start(), text[m.start():m.start()+300]) for m in re.finditer(r"addEventListener\s*\(\s*['\"]scroll", text)]
sys.stdout.buffer.write(b'\nscroll listeners:\n')
for pos, ctx in hits2:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx) + '\n').encode('utf-8'))

# Find how body is given scroll height
hits3 = [(m.start(), text[m.start():m.start()+200]) for m in re.finditer(r'TOTAL_PAGES|totalPages|NUM_PAGES|scrollPages', text)]
sys.stdout.buffer.write(b'\nPages:\n')
for pos, ctx in hits3[:5]:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx) + '\n').encode('utf-8'))
