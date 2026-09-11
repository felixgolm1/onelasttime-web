import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add mobile CSS
css_to_add = """
    @media (max-width: 768px) {
      #flip-left-text {
        top: 20% !important;
        left: 0 !important;
        width: 100% !important;
        text-align: center;
      }
      #flip-right-text {
        top: 75% !important;
        right: 0 !important;
        left: 0 !important;
        width: 100% !important;
        text-align: center;
      }
      #flip-left-text .flt-line, #flip-right-text .flt-line {
        justify-content: center !important;
      }
    }
"""

# Find a good place to insert the CSS (before the closing </style> tag)
idx_style = content.find('</style>')
if idx_style != -1:
    content = content[:idx_style] + css_to_add + content[idx_style:]


# 2. Change GSAP animations
# gsap.set
content = content.replace("gsap.set('#flip-left-text',  { autoAlpha: 0, yPercent: -50, y: -40 });", "gsap.set('#flip-left-text',  { autoAlpha: 0, yPercent: -50, x: -40 });")
content = content.replace("gsap.set('#flip-right-text', { autoAlpha: 0, yPercent: -50, y:  40 });", "gsap.set('#flip-right-text', { autoAlpha: 0, yPercent: -50, x:  40 });")

# scrollTl.fromTo left
left_fromto_old = """    scrollTl.fromTo('#flip-left-text',
      { y: -40 },
      { y: 40, duration: 0.60, ease: 'none' },
      0
    );"""
left_fromto_new = """    scrollTl.fromTo('#flip-left-text',
      { x: -40 },
      { x: 40, duration: 0.60, ease: 'none' },
      0
    );"""
content = content.replace(left_fromto_old, left_fromto_new)

# scrollTl.fromTo right
right_fromto_old = """    scrollTl.fromTo('#flip-right-text',
      { y: 40 },
      { y: -40, duration: 0.60, ease: 'none' },
      0
    );"""
right_fromto_new = """    scrollTl.fromTo('#flip-right-text',
      { x: 40 },
      { x: -40, duration: 0.60, ease: 'none' },
      0
    );"""
content = content.replace(right_fromto_old, right_fromto_new)


with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
