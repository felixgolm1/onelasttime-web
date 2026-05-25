import sys
with open('3d-test-git.html','r',encoding='utf-8') as f: git=f.read()
with open('3d-test.html','r',encoding='utf-8') as f: current=f.read()

# In git, find the range that contains placeTableSet, placeWineGlass, 
# cardRenderer2 setup, and other missing functions.
# These come AFTER the main initialization and BEFORE the animate loop.

# Find placeTableSet definition in git
s = git.find('  function placeTableSet(')
e = git.find('\n\n  (function loop()', s)
sys.stdout.buffer.write(('placeTableSet in git: ' + str(s) + ' -> loop at: ' + str(e) + '\n').encode('utf-8'))

missing_block = git[s:e]
sys.stdout.buffer.write(('Missing block size: ' + str(len(missing_block)) + '\n').encode('utf-8'))
sys.stdout.buffer.write(('Block start: ' + repr(missing_block[:200]) + '\n').encode('utf-8'))
sys.stdout.buffer.write(('Block end: ' + repr(missing_block[-200:]) + '\n').encode('utf-8'))

# Now insert this block in the current file, right before the clock/loop
insert_marker = '\n  // Clock for render loop timing\n  const clock = new THREE.Clock();'
pos = current.find(insert_marker)
sys.stdout.buffer.write(('Insert position in current: ' + str(pos) + '\n').encode('utf-8'))

if pos > 0 and s > 0 and e > 0:
    new_current = current[:pos] + '\n' + missing_block + '\n' + current[pos:]
    with open('3d-test.html','w',encoding='utf-8') as f: f.write(new_current)
    sys.stdout.buffer.write(('Done! New size: ' + str(len(new_current)) + '\n').encode('utf-8'))
else:
    sys.stdout.buffer.write(b'ERROR: markers not found\n')
