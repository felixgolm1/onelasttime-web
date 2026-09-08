import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #headline CSS
old_css = """    #headline {
      position: fixed;
      left: 4.5%;
      top: 50%;
      transform: translateY(-50%) translateZ(1000px);
      z-index: 100000;
      max-width: 48vw;
      background: rgba(0, 0, 0, 0.05);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 3px;
      padding: 1.6rem 2rem;
      opacity: 0;
    }"""

new_css = """    #headline {
      --head-blur: 8px;
      --head-alpha: 0.05;
      position: fixed;
      left: 4.5%;
      top: 50%;
      transform: translateY(-50%) translateZ(1000px);
      z-index: 100000;
      max-width: 48vw;
      padding: 1.6rem 2rem;
      opacity: 0;
    }
    #headline::before {
      content: '';
      position: absolute;
      top: -3rem; bottom: -3rem; left: -3rem; right: -3rem;
      z-index: -1;
      pointer-events: none;
      backdrop-filter: blur(var(--head-blur));
      -webkit-backdrop-filter: blur(var(--head-blur));
      background: rgba(0, 0, 0, var(--head-alpha));
      mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 75%);
      -webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 75%);
    }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced CSS")
else:
    print("Failed to find CSS")

# 2. Update GSAP animation
old_js = "scrollTl.to('#headline', { borderColor: 'rgba(255,255,255,0)', backdropFilter: 'blur(0px)', webkitBackdropFilter: 'blur(0px)', duration: 0.08, ease: 'power2.inOut' }, 0);"
new_js = "scrollTl.to('#headline', { '--head-blur': '0px', '--head-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);"

if old_js in content:
    content = content.replace(old_js, new_js)
    print("Replaced JS")
else:
    print("Failed to find JS")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
