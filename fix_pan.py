import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Revert divisor trick
content = re.sub(
    r'let divisor = 900;\n\s*if \(targetProg < 0\.60\) divisor = 4500;\n\s*else if \(targetProg >= 2\.5 && targetProg <= 9\.62\) divisor = 8000;',
    'let divisor = 900;\n        if (targetProg < 0.08) divisor = 8000;',
    content
)

content = re.sub(
    r'let divisorT = 450;\n\s*if \(targetProg < 0\.60\) divisorT = 2250;\n\s*else if \(targetProg >= 2\.5 && targetProg <= 9\.62\) divisorT = 4000;',
    'let divisorT = 450;\n        if (targetProg < 0.08) divisorT = 4000;',
    content
)

# 2. Increase PAN and HOLD
content = re.sub(
    r'const PAN\s*=\s*0\.05;\s*\n\s*const HOLD\s*=\s*0\.025;',
    'const PAN  = 0.20;\n      const HOLD = 0.10;',
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
