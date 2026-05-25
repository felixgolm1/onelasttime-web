import re, sys
with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

# Find where prog is SET/updated (the scroll driving variable)
hits = [(m.start(), text[m.start():m.start()+300]) for m in re.finditer(r'\bprog\s*[+\-]?=\s*[^=]', text)]
sys.stdout.buffer.write(b'prog assignments:\n')
for pos, ctx in hits[:8]:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx[:150]) + '\n').encode('utf-8'))

# Find scroll wheel handling
hits2 = [(m.start(), text[m.start():m.start()+300]) for m in re.finditer(r'wheel|WheelEvent|deltaY', text)]
sys.stdout.buffer.write(b'\nWheel events:\n')
for pos, ctx in hits2[:5]:
    sys.stdout.buffer.write((str(pos) + ': ' + repr(ctx[:150]) + '\n').encode('utf-8'))
