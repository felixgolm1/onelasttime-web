with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()
print('File size:', len(text))

# PROC_BRAIN is at 493818 in current file
# GLB loader (duplicate) is at 990445
# Goal: keep text[0..493818+len(PROC_BRAIN)] + content AFTER the GLB loader ends

# Find where PROC_BRAIN ends in the current file
pb_start = 493818
pb_end_marker = '    console.log(\'Procedural brain created, vertices:\', cnt);\n  })();\n\n'
pb_end = text.find(pb_end_marker, pb_start)
print('PROC_BRAIN ends at:', pb_end + len(pb_end_marker))
keep_until = pb_end + len(pb_end_marker)

# Now find the end of the GLB loader block in the second half
# The GLB loader ends with '  );\n' and then continuation code
# Let's find '  // Called every frame' which should appear AFTER the GLB loader in the duplicate
glb_s = 990445
after_glb_marker = '\n\n\n\n  // Called every frame to update vertex colors'
after_glb = text.find(after_glb_marker, glb_s)
print('After GLB marker at:', after_glb)

# If not found, try another marker
if after_glb < 0:
    after_glb_marker2 = '  window.updateBrainVertexColors = function(progress, time) {'
    after_glb = text.find(after_glb_marker2, glb_s)
    print('Alt after GLB marker at:', after_glb)

# Our clean result = text[0..keep_until] + text[after_glb..]
clean = text[:keep_until] + text[after_glb:]
print('Clean file size:', len(clean))

with open('3d-test.html','w',encoding='utf-8') as f: f.write(clean)
print('Done')
