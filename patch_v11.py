import os

dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Inject the variables right after the `<script>` tag that starts the main logic.
# The main logic is usually in the last `<script>` tag or after `document.addEventListener('DOMContentLoaded', async () => {`

vars_inject = """
  let globalBrainMesh;
  const brainUniforms = {
    uProgress: { value: 0.0 },
    uTime: { value: 0.0 }
  };
"""

text = text.replace("document.addEventListener('DOMContentLoaded', async () => {", "document.addEventListener('DOMContentLoaded', async () => {\n" + vars_inject)

with open(dev_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Vars Injected!")
