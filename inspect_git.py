with open('3d-test-git.html','r',encoding='utf-8') as f: git=f.read()
with open('3d-test.html','r',encoding='utf-8') as f: current=f.read()

# Show last part of git file to understand structure
print('=== GIT LAST 3000 chars ===')
print(git[-3000:])
