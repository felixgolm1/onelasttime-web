import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for mobile glass boxes
css_to_add = """
      @media (max-width: 768px) {
        #glass-who, #glass-objectives {
          top: auto !important;
          bottom: calc(3% + 6.5rem) !important;
          height: 38vh !important;
          width: 90vw !important;
          left: 5vw !important;
          right: auto !important;
          padding: 1.5rem !important;
          border: 1px solid rgba(255,255,255,0.1) !important;
          border-radius: 16px !important;
          overflow-y: auto !important;
          pointer-events: auto !important;
          justify-content: flex-start !important;
          box-shadow: 0 -10px 30px rgba(0,0,0,0.3) !important;
        }
      }
    </style>
"""
content = content.replace("    </style>\n</head>", css_to_add + "</head>")

# 2. Update panData for step 2 and 3
bad_js = """    const panData = [
      { x: isM ? '31.2vw'  : '26vw',  y: isM ? '28.8vh' : '24vh', r:  16 },
      { x: isM ? '-40.8vw' : '-34vw', y: isM ? '24vh'   : '20vh', r:  -9 },
      { x:  '34vw', y: '-34vh', r: -18 },
      { x: '-26vw', y: '-24vh', r:  12 },
    ];"""

good_js = """    const panData = [
      { x: isM ? '31.2vw'  : '26vw',  y: isM ? '28.8vh' : '24vh', r:  16 },
      { x: isM ? '-40.8vw' : '-34vw', y: isM ? '8vh'    : '20vh', r:  -9 },
      { x:  '34vw', y: isM ? '-44vh' : '-34vh', r: -18 },
      { x: '-26vw', y: '-24vh', r:  12 },
    ];"""

content = content.replace(bad_js, good_js)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
