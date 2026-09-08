import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

# Slow down devProg (text & photo reveal) from 6.0 to 8.0
text = text.replace(
    "let devProg = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 6.0));",
    "let devProg = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 8.0));"
)

# Slow down zoomP from 6.0 to 8.0
text = text.replace(
    "zoomP = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 6.0));",
    "zoomP = Math.max(0, Math.min(1, (localP - START_3D_REVEAL) / 8.0));"
)

# Delay CTA convergence from 34.5 to 36.5 (so it happens after the new slower zoom)
text = text.replace(
    "// Convergencia del Logo y CTA al seguir haciendo scroll DESPUS del zoom (de 34.5 a 36.5)",
    "// Convergencia del Logo y CTA al seguir haciendo scroll DESPUES del zoom (de 36.5 a 38.5)"
)
text = text.replace(
    "var convergeP = Math.max(0, Math.min(1, (localP - 34.5) / 1.0));",
    "var convergeP = Math.max(0, Math.min(1, (localP - 36.5) / 1.0));"
)
text = text.replace(
    "window._isFinalCtaCentered = (localP >= 35.5);",
    "window._isFinalCtaCentered = (localP >= 37.5);"
)
text = text.replace(
    "if (localP < 34.5) {",
    "if (localP < 36.5) {"
)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(text)
