import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

# 1. Slow down devProg (text & photo reveal) and zoomP from 8.0 to 10.5
text = text.replace(
    "let devProg = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 8.0));",
    "let devProg = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 10.5));"
)
text = text.replace(
    "zoomP = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 8.0));",
    "zoomP = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 10.5));"
)

# 2. Shift all convergence points by +2.5 (from 36.5 to 39.0)
text = text.replace(
    "var convergeP = Math.max(0, Math.min(1, (localP - 36.5) / 1.0));",
    "var convergeP = Math.max(0, Math.min(1, (localP - 39.0) / 1.0));"
)
text = text.replace(
    "window._isFinalCtaCentered = (localP >= 37.5);",
    "window._isFinalCtaCentered = (localP >= 40.0);"
)
text = text.replace(
    "if (localP < 36.5) {",
    "if (localP < 39.0) {"
)
text = text.replace(
    "var scrollIndP = Math.max(0, Math.min(1, (localP - 36.5) / 1.4));",
    "var scrollIndP = Math.max(0, Math.min(1, (localP - 39.0) / 1.4));"
)
text = text.replace(
    "var fadeBgP = Math.max(0, Math.min(1, (localP - 36.5) / 1.3));",
    "var fadeBgP = Math.max(0, Math.min(1, (localP - 39.0) / 1.3));"
)

# 3. Increase maxProg by 2.5
text = text.replace(
    "const maxProg = 59.0;",
    "const maxProg = 61.5;"
)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(text)
