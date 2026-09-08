import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace #headline::before
headline_before_pattern = r"#headline::before\s*\{[\s\S]*?mask-image:[^}]*\}"
new_headline_before = """#blur-bg-head {
      position: absolute;
      top: -2rem; bottom: -2rem; left: -2rem; right: -2rem;
      z-index: -1;
      pointer-events: none;
      transform: translateZ(0);
      -webkit-transform: translateZ(0);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      background: rgba(0, 0, 0, 0.05);
      mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
      -webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
    }"""
content = re.sub(headline_before_pattern, new_headline_before, content)

# 2. Replace #subheadline::before
subheadline_before_pattern = r"#subheadline::before\s*\{[\s\S]*?mask-image:[^}]*\}"
new_subheadline_before = """#blur-bg-sub {
      position: absolute;
      top: -3rem; bottom: -3rem; left: -3rem; right: -3rem;
      z-index: -1;
      pointer-events: none;
      transform: translateZ(0);
      -webkit-transform: translateZ(0);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      background: rgba(0, 0, 0, 0.05);
      -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
      mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
    }"""
content = re.sub(subheadline_before_pattern, new_subheadline_before, content)

# 3. Inject actual divs and remove inline variables
old_headline_html = '<div id="headline" style="--head-blur: 10px; --head-alpha: 0.05;">'
new_headline_html = '<div id="headline">\n      <div id="blur-bg-head"></div>'
content = content.replace(old_headline_html, new_headline_html)

old_subheadline_html = '<div id="subheadline" style="--sub-blur: 6px; --sub-alpha: 0.05;">'
new_subheadline_html = '<div id="subheadline">\n      <div id="blur-bg-sub"></div>'
content = content.replace(old_subheadline_html, new_subheadline_html)

# 4. Update GSAP animations
old_gsap_head = "scrollTl.fromTo('#headline', { '--head-blur': '10px', '--head-alpha': 0.05 }, { '--head-blur': '0px', '--head-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
new_gsap_head = "scrollTl.to('#blur-bg-head', { opacity: 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
content = content.replace(old_gsap_head, new_gsap_head)

old_gsap_sub = "scrollTl.fromTo('#subheadline', { '--sub-blur': '6px', '--sub-alpha': 0.05 }, { '--sub-blur': '0px', '--sub-alpha': 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
new_gsap_sub = "scrollTl.to('#blur-bg-sub', { opacity: 0, duration: 0.08, ease: 'power2.inOut' }, 0);"
content = content.replace(old_gsap_sub, new_gsap_sub)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
