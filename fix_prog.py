import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('if (prog >= 16.0) {', 'if (prog >= 15.8) {')
text = text.replace('const bProg = Math.max(0, Math.min(1, (prog - 16.0) / 4.0));', 'const bProg = Math.max(0, Math.min(1, (prog - 15.8) / 4.2));')

# Make sure op3D fades out completely
text = text.replace('Math.max(0, 1.0 - (prog - 15.5) / 0.5);', 'Math.max(0, 1.0 - (prog - 15.0) / 0.8);')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated prog limits.")
