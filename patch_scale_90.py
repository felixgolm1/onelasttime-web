import re

file = '3d-test.html'

with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Change CSS scale from 0.80 to 0.90
content = content.replace(
    "#card-morph-group, .sc-card { transform: scale(0.80); transform-origin: center center; }",
    "#card-morph-group, .sc-card { transform: scale(0.90); transform-origin: center center; }"
)

# Change GSAP scale from 0.80 to 0.90
content = content.replace(
    "scaleX: window.matchMedia('(max-width: 768px)').matches ? 0.80 : 1, scaleY: window.matchMedia('(max-width: 768px)').matches ? 0.80 : 1",
    "scaleX: window.matchMedia('(max-width: 768px)').matches ? 0.90 : 1, scaleY: window.matchMedia('(max-width: 768px)').matches ? 0.90 : 1"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
