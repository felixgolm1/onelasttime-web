# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()
    
idx = html.find("bottomCta.style.pointerEvents = 'auto';\n            }\n        } else {\n               if (bottomCta.classList.contains('smoke-out')) {")
print(idx)
