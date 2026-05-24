import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to change:
# let cardTable = document.getElementById('card-table');
# to:
# let cardTable = document.getElementById('oryzo-section');

old_1 = "let cardTable = document.getElementById('card-table');"
new_1 = "let cardTable = document.getElementById('oryzo-section');"

old_2 = """
                 // Translate Y adjustment for camera down (tExit)
                 const exitY = tExit * 100 * window.innerHeight / 100;

                 c.style.transform = `translate(-50%, -50%) translate(${currentX}px, ${currentY - exitY}px) rotate(${currentRot}deg) scale(${currentScale})`;
"""
new_2 = """
                 // No need for tExit adjustment because we append to oryzo-section which already moves up!
                 c.style.transform = `translate(-50%, -50%) translate(${currentX}px, ${currentY}px) rotate(${currentRot}deg) scale(${currentScale})`;
"""

import sys

modified = False
if old_1 in content:
    content = content.replace(old_1, new_1)
    modified = True
if old_2 in content:
    content = content.replace(old_2, new_2)
    modified = True

if modified:
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed z-index and coordinate logic successfully.")
else:
    print("Could not find the target strings!")
    sys.exit(1)
