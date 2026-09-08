import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #headline CSS using regex
pattern = r"#headline\s*\{[\s\S]*?padding:\s*1\.6rem 2rem;\s*\}"

new_css = """#headline {
      --head-blur: 10px;
      --head-alpha: 0;
      position: fixed;
      left: 5%;
      top: 50%;
      transform: translateY(-50%) translateZ(1000px);
      z-index: 100000;
      max-width: 40vw;
      opacity: 0;
      padding: 1.6rem 2rem;
    }
    #headline::before {
      content: '';
      position: absolute;
      top: -2rem; bottom: -2rem; left: -2rem; right: -2rem;
      z-index: -1;
      pointer-events: none;
      backdrop-filter: blur(var(--head-blur));
      -webkit-backdrop-filter: blur(var(--head-blur));
      background: rgba(0, 0, 0, var(--head-alpha));
      mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
      -webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
    }"""

content = re.sub(pattern, new_css, content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
