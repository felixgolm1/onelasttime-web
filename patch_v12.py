import os
import re

dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    text = f.read()

# We need to ensure globalBrainMesh and brainUniforms are defined.
# The safest place is immediately after the last <script> tag before any code.

vars_inject = """
  let globalBrainMesh;
  const brainUniforms = {
    uProgress: { value: 0.0 },
    uTime: { value: 0.0 }
  };
"""

# Let's find the last occurrence of `<script>` and insert the variables right after it.
# To do this safely, we can split by `<script>` and modify the last chunk.

parts = text.rsplit('<script>', 1)
if len(parts) == 2:
    parts[1] = vars_inject + "\n" + parts[1]
    new_text = "<script>".join(parts)
    
    with open(dev_file, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Variables securely injected at the top of the last script block!")
else:
    print("Could not find script block")

