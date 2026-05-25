import sys, re
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix updateGlobalScenes so op3D fades out between 15.5 and 16.0
old_op3d = "let op3D = 1;"
new_op3d = """let op3D = 1;
      if (typeof prog !== 'undefined' && prog > 15.5) {
          op3D = Math.max(0, 1.0 - (prog - 15.5) / 0.5);
      }"""
text = text.replace(old_op3d, new_op3d)

# Also check if there's any other hardcoded 16 limit.
# Find where customScrollTrack max is calculated.
with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed updateGlobalScenes.")
