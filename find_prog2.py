import re, sys
with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

# Find targetProg declaration
hits = [(m.start(), text[m.start():m.start()+200]) for m in re.finditer(r'\btargetProg\s*=\s*[^=]', text)]
sys.stdout.buffer.write(b'targetProg assignments:\n')
for pos, ctx in hits[:5]:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx[:150]) + '\n').encode('utf-8'))

# Find prog declaration (let/const/var)
hits2 = [(m.start(), text[m.start():m.start()+200]) for m in re.finditer(r'(?:let|const|var)\s+prog\b', text)]
sys.stdout.buffer.write(b'\nprog declaration:\n')
for pos, ctx in hits2[:5]:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx[:150]) + '\n').encode('utf-8'))

# Find if the main animation block starts with DOMContentLoaded or just runs
hits3 = [(m.start(), text[m.start():m.start()+200]) for m in re.finditer(r'DOMContentLoaded|window\.onload', text)]
sys.stdout.buffer.write(b'\nDOMContentLoaded:\n')
for pos, ctx in hits3[:5]:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx[:150]) + '\n').encode('utf-8'))
