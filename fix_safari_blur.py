import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix CSS
content = content.replace(
    "backdrop-filter: blur(var(--head-blur));",
    "transform: translateZ(0);\n      backdrop-filter: blur(var(--head-blur));"
)
content = content.replace(
    "backdrop-filter: blur(var(--sub-blur));",
    "transform: translateZ(0);\n        backdrop-filter: blur(var(--sub-blur));"
)

# Fix GSAP
content = content.replace(
    "scrollTl.to('#headline', { '--head-blur': '0px', '--head-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);",
    "scrollTl.fromTo('#headline', { '--head-blur': '10px', '--head-alpha': 0.05 }, { '--head-blur': '0px', '--head-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
)
content = content.replace(
    "scrollTl.to('#subheadline', { '--sub-blur': '0px', '--sub-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);",
    "scrollTl.fromTo('#subheadline', { '--sub-blur': '6px', '--sub-alpha': 0.05 }, { '--sub-blur': '0px', '--sub-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
