with open('3d-test-git.html','r',encoding='utf-8') as f: git=f.read()
# The animate loop starts at 507089 in git
# But there's initialization code BEFORE it (between ~493854 and 507089)
# In our current file we skipped this block
# Let's see what's in git between char 493854 and 507089
missing_block = git[493000:507089]
print('=== MISSING BLOCK ===')
print(repr(missing_block[:3000]))
