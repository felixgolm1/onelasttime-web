import os

files = ['3d-test.html', 'index.html']

css_addition = """
  /* Fix intro card overflow and hide desktop scrollbar */
  #custom-scroll-track, #custom-scroll-thumb {
    display: none !important;
  }
  #card-morph-group {
    transform: scale(0.85) !important;
  }
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Fix intro card overflow' not in content:
        content = content.replace(
            '@media screen and (max-width: 768px) {',
            f'@media screen and (max-width: 768px) {{\n{css_addition}'
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file}")
    else:
        print(f"Already patched {file}")
