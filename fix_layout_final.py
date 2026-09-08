# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

new_ai = '''      <div id="made-by-ai" style="position: fixed; top: 50%; left: 50%; font-family: 'Inter', sans-serif; font-size: clamp(2.5rem, 8vw, 10rem); font-weight: 700; color: #f4f2ea; letter-spacing: -0.05em; white-space: nowrap; opacity: 1; z-index: 10001; pointer-events: none; visibility: hidden;">
      <span style="position: relative; display: inline-block;">
        <span style="position: absolute; right: 100%; top: 48%; transform: translateY(-50%) rotate(-90deg); margin-right: -0.08em; display: flex; justify-content: space-between; font-size: 0.18em; font-weight: 600; letter-spacing: 0; color: #f4f2ea; opacity: 0.9; width: 4.1em;">
          <span>u</span><span>l</span><span>t</span><span>r</span><span>a</span>
        </span>
        personalizado con 
      </span>
      <span style="color: #c1ff00; position: relative; display: inline-block;">
        IA
        <span style="position: absolute; left: 4%; top: 82%; display: flex; justify-content: space-between; font-size: 0.13em; font-weight: 700; letter-spacing: 0; width: 92%; white-space: nowrap; color: #c1ff00;">
          <span>M</span><span>o</span><span>d</span><span>e</span><span>l</span><span>o</span><span>&nbsp;</span><span>O</span><span>L</span><span>T</span><span>-</span><span>1</span>
        </span>
      </span>
    </div>'''

content = re.sub(r'<div id="made-by-ai"[\s\S]*?</div>', new_ai, content, count=1)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
