import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("""      transform: translateZ(0);
      backdrop-filter: blur(var(--head-blur));
      -webkit-transform: translateZ(0);
      backdrop-filter: blur(var(--head-blur));""", """      transform: translateZ(0);
      -webkit-transform: translateZ(0);
      backdrop-filter: blur(var(--head-blur));
      -webkit-backdrop-filter: blur(var(--head-blur));""")

content = content.replace("""      transform: translateZ(0);
        backdrop-filter: blur(var(--sub-blur));
      -webkit-transform: translateZ(0);
        backdrop-filter: blur(var(--sub-blur));""", """      transform: translateZ(0);
      -webkit-transform: translateZ(0);
      backdrop-filter: blur(var(--sub-blur));
      -webkit-backdrop-filter: blur(var(--sub-blur));""")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
