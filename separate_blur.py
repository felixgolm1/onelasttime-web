import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS
old_css = r"""    #blur-bg-head \{
      position: absolute;
      top: -2rem; bottom: -2rem; left: -2rem; right: -2rem;
      z-index: -1;
      pointer-events: none;
      transform: translate3d\(0,0,0\) rotate\(0\.001deg\);
      -webkit-transform: translate3d\(0,0,0\) rotate\(0\.001deg\);
      backdrop-filter: blur\(10px\);
      -webkit-backdrop-filter: blur\(10px\);
      background: rgba\(0, 0, 0, 0\.05\);
      mask-image: radial-gradient\(ellipse at center, rgba\(0,0,0,1\) 30%, rgba\(0,0,0,0\) 70%\);
      -webkit-mask-image: radial-gradient\(ellipse at center, rgba\(0,0,0,1\) 30%, rgba\(0,0,0,0\) 70%\);
    \}"""

new_css = """    .blur-bg-head {
      position: absolute;
      top: -1.5rem; bottom: -1.5rem; left: -1.5rem; right: -1.5rem;
      z-index: -1;
      pointer-events: none;
      transform: translate3d(0,0,0) rotate(0.001deg);
      -webkit-transform: translate3d(0,0,0) rotate(0.001deg);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      background: rgba(0, 0, 0, 0.05);
      mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
      -webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
    }"""

content = re.sub(old_css, new_css, content)

# 2. Replace HTML
old_html = r"""    <div id="headline">
      <div id="blur-bg-head"></div>
      <h1>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">EXPERIMENTA LA CENA</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">MÁS TRANSFORMADORA</span></span>
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">QUE HAS TENIDO JAMÁS</span></span>
      </h1>
        <hr class="headline-divider">
        <span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="headline-sub oh-inner" style="display:block; margin:0;">En tu restaurante favorito o en casa</p></span>
    </div>"""

# Ensure unicode matches
old_html_regex = r"""<div id="headline">\s*<div id="blur-bg-head"></div>\s*<h1>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">EXPERIMENTA LA CENA</span></span>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">M[^S]+S TRANSFORMADORA</span></span>\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">QUE HAS TENIDO JAM[^S]+S</span></span>\s*</h1>\s*<hr class="headline-divider">\s*<span style="display:block; overflow:hidden; padding-bottom:4px;"><p class="headline-sub oh-inner" style="display:block; margin:0;">En tu restaurante favorito o en casa</p></span>\s*</div>"""

new_html = """<div id="headline">
      <div style="position:relative; width:100%;">
        <div class="blur-bg-head"></div>
        <h1 style="position:relative; z-index:1; margin:0;">
          <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">EXPERIMENTA LA CENA</span></span>
          <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">MÁS TRANSFORMADORA</span></span>
          <span style="display:block; overflow:hidden; padding-bottom:4px;"><span class="oh-inner" style="display:block;">QUE HAS TENIDO JAMÁS</span></span>
        </h1>
      </div>
      <hr class="headline-divider" style="position:relative; z-index:2;">
      <div style="position:relative; width:100%;">
        <div class="blur-bg-head" style="top: -1rem; bottom: -1rem;"></div>
        <span style="display:block; overflow:hidden; padding-bottom:4px; position:relative; z-index:1;"><p class="headline-sub oh-inner" style="display:block; margin:0;">En tu restaurante favorito o en casa</p></span>
      </div>
    </div>"""

# Let's replace the HTML precisely.
content_before = content
content = re.sub(old_html_regex, new_html, content)
if content == content_before:
    print("HTML not replaced")
else:
    print("HTML replaced")

# 3. Replace GSAP
content = content.replace("scrollTl.to('#blur-bg-head', { opacity: 0,", "scrollTl.to('.blur-bg-head', { opacity: 0,")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
