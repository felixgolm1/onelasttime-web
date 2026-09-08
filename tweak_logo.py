import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update menu pill position
content = content.replace(
    "top: 4% !important;\n    right: 5% !important;",
    "top: 3% !important;\n    right: 4% !important;"
)

# 2. Update nav-logo initial position (remove !important)
content = content.replace(
    "#nav-logo {\n    left: 5% !important;\n    top: 10% !important;\n  }",
    "#nav-logo {\n    left: 5% !important;\n    top: 10%;\n  }"
)

# 3. Update GSAP animation for nav-logo
content = content.replace(
    "scrollTl.to('#nav-logo', { scale: 0.5, transformOrigin: 'top left', ease: 'power1.inOut', duration: 0.08 }, 0);",
    "scrollTl.to('#nav-logo', { scale: 0.5, top: window.matchMedia('(max-width: 768px)').matches ? '3%' : '1.5rem', transformOrigin: 'top left', ease: 'power1.inOut', duration: 0.08 }, 0);"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done tweaking layout and GSAP.")
