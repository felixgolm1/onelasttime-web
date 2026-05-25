import re, sys
with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

hits = [(m.start(), text[m.start():m.start()+200]) for m in re.finditer(r'scrollTl\s*=', text)]
for pos, ctx in hits:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx) + '\n').encode('utf-8'))

# Find body height setup
bh = text.find('document.body.style.height')
sys.stdout.buffer.write(('body height at: ' + str(bh) + '\n').encode('utf-8'))
if bh > 0:
    sys.stdout.buffer.write(repr(text[bh-50:bh+200]).encode('utf-8'))

# Find how the page creates scroll space
for kw in ['totalHeight', 'vh)', 'scrollHeight', 'window.innerHeight * ']:
    pos = text.find(kw)
    sys.stdout.buffer.write(('\n' + kw + ' at: ' + str(pos) + '\n').encode('utf-8'))
    if pos > 0:
        sys.stdout.buffer.write(repr(text[pos-30:pos+150]).encode('utf-8'))
