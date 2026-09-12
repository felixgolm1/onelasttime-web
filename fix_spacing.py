import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

bad_js = """    const sData = [
      { el: sc1, x: '-26vw', y: '-24vh', r: -16 },
      { el: sc2, x:  '26vw', y: '-20vh', r:   9 },
      { el: sc3, x: '-24vw', y:  '26vh', r:  18 },
      { el: sc4, x:  '26vw', y:  '24vh', r: -12 },
    ];
    const panData = [
      { x:  '26vw', y:  '24vh', r:  16 },
      { x: '-34vw', y:  '20vh', r:  -9 },
      { x:  '34vw', y: '-34vh', r: -18 },
      { x: '-26vw', y: '-24vh', r:  12 },
    ];"""

good_js = """    const isM = window._cIsMobile;
    const sData = [
      { el: sc1, x: isM ? '-31.2vw' : '-26vw', y: isM ? '-28.8vh' : '-24vh', r: -16 },
      { el: sc2, x: isM ? '31.2vw'  : '26vw',  y: isM ? '-24vh'   : '-20vh', r:   9 },
      { el: sc3, x: '-24vw', y:  '26vh', r:  18 },
      { el: sc4, x:  '26vw', y:  '24vh', r: -12 },
    ];
    const panData = [
      { x: isM ? '31.2vw'  : '26vw',  y: isM ? '28.8vh' : '24vh', r:  16 },
      { x: isM ? '-40.8vw' : '-34vw', y: isM ? '24vh'   : '20vh', r:  -9 },
      { x:  '34vw', y: '-34vh', r: -18 },
      { x: '-26vw', y: '-24vh', r:  12 },
    ];"""

content = content.replace(bad_js, good_js)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
