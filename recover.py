with open('3d-test.html','r',encoding='utf-8') as f: current=f.read()
with open('3d-test-git.html','r',encoding='utf-8') as f: git=f.read()

print('Current (truncated):', len(current))
print('Git version:', len(git))

# Find where the GLTF brain loader starts in git version
glb_marker = '  // Cargar brain GLB'
git_glb = git.find(glb_marker)
print('GLB in git at:', git_glb)

if git_glb < 0:
    # No brain GLB in git -- use a different marker
    # Find the render loop start as split point
    render_marker = '  // === RENDER LOOP ==='
    git_render = git.find(render_marker)
    print('Render loop in git at:', git_render)
    # Find same marker in current (truncated)
    cur_render = current.find(render_marker)
    print('Render loop in current at:', cur_render)
else:
    # GLB exists in git, find its END
    # After GLB loader, look for render loop or other unique marker
    after_glb = git.find('  (function animate()', git_glb)
    print('animate() in git at:', after_glb)
    # Find same in current
    after_cur = current.find('  (function animate()')
    print('animate() in current at:', after_cur)
    
    if after_glb > 0 and after_cur < 0:
        # The tail starts at after_glb in git, and we need to append it to current
        tail = git[after_glb:]
        print('Tail length:', len(tail))
        print('Tail start:', repr(tail[:100]))
        combined = current + tail
        with open('3d-test.html','w',encoding='utf-8') as f: f.write(combined)
        print('RECOVERED! New size:', len(combined))
    elif after_cur > 0:
        print('animate() already in current, file may be OK')
    else:
        print('Need different marker')

# Check what's at the end of the current file
print('Current file last 150:', repr(current[-150:]))
# Check git last 150
print('Git file last 150:', repr(git[-150:]))
