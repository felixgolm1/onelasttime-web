with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

# Current file: 496599 bytes = text[0..496598] = first half + PROC_BRAIN  
# But we lost the REST of the file after the PROC_BRAIN
# The rest is still IN the original corrupted 1044892 byte file, after the GLB duplicate
# We need to reconstruct it.

# Let's read the ORIGINAL corrupted backup if it exists, or we need to look at the 
# current truncated file state.
print('Current (truncated) file size:', len(text))
print('Last 200 chars:', repr(text[-200:]))
