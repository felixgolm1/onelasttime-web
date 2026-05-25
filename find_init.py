import sys
with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

# Check if placeTableSet is defined and called
import re
defs = [m.start() for m in re.finditer(r'function placeTableSet', text)]
calls = [m.start() for m in re.finditer(r'placeTableSet\(', text)]
sys.stdout.buffer.write(('placeTableSet defs: ' + str(defs) + '\n').encode('utf-8'))
sys.stdout.buffer.write(('placeTableSet calls: ' + str(calls) + '\n').encode('utf-8'))

# Check if smoothScrollLoop is called
ssl_def = [m.start() for m in re.finditer(r'function smoothScrollLoop|smoothScrollLoop\s*=', text)]
ssl_call = [m.start() for m in re.finditer(r'smoothScrollLoop\(\)', text)]
sys.stdout.buffer.write(('smoothScrollLoop defs: ' + str(ssl_def) + '\n').encode('utf-8'))
sys.stdout.buffer.write(('smoothScrollLoop calls: ' + str(ssl_call) + '\n').encode('utf-8'))

# Check what the render/loop update does with prog
prog_use = text.find('prog += (targetProg')
sys.stdout.buffer.write(('prog lerp at: ' + str(prog_use) + '\n').encode('utf-8'))
if prog_use > 0:
    sys.stdout.buffer.write(repr(text[prog_use-200:prog_use+400]).encode('utf-8'))
