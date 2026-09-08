import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """          // Reveal UI periférico
          gsap.to(['#nav-logo', '#nav-menu', '#mobile-menu-pill', '#cta-top-container', '#cta-bottom-container', '.scroll-indicator', '#headline', '#subheadline'], {
            opacity: 1,
            duration: 1.5,
            ease: 'power2.out',
            stagger: 0.15
          });"""

new_code = """          // Reveal UI periférico
          gsap.to(['#nav-logo', '#nav-menu', '#mobile-menu-pill', '#cta-top-container', '#cta-bottom-container', '.scroll-indicator', '#headline', '#subheadline'], {
            opacity: 1,
            duration: 1.5,
            ease: 'power2.out',
            stagger: 0.15,
            onComplete: function() {
              // Safari bug fix: force repaint of backdrop-filters after opacity animation finishes
              var h = document.getElementById('blur-bg-head');
              if (h) { h.style.display = 'none'; h.offsetHeight; h.style.display = 'block'; }
              var s = document.getElementById('blur-bg-sub');
              if (s) { s.style.display = 'none'; s.offsetHeight; s.style.display = 'block'; }
            }
          });"""

if old_code in content:
    content = content.replace(old_code, new_code)
    print("Replaced!")
else:
    # try matching without accent
    old_code_2 = """          // Reveal UI perifǸrico
          gsap.to(['#nav-logo', '#nav-menu', '#mobile-menu-pill', '#cta-top-container', '#cta-bottom-container', '.scroll-indicator', '#headline', '#subheadline'], {
            opacity: 1,
            duration: 1.5,
            ease: 'power2.out',
            stagger: 0.15
          });"""
    # let's just use regex
    pattern = r"// Reveal UI perif[^]*?gsap\.to\(\['#nav-logo'[^]*?stagger:\s*0\.15\s*\}\);"
    new_code_regex = """// Reveal UI periferico
          gsap.to(['#nav-logo', '#nav-menu', '#mobile-menu-pill', '#cta-top-container', '#cta-bottom-container', '.scroll-indicator', '#headline', '#subheadline'], {
            opacity: 1,
            duration: 1.5,
            ease: 'power2.out',
            stagger: 0.15,
            onComplete: function() {
              // Safari bug fix: force repaint of backdrop-filters after opacity animation finishes
              var h = document.getElementById('blur-bg-head');
              if (h) { h.style.display = 'none'; h.offsetHeight; h.style.display = 'block'; }
              var s = document.getElementById('blur-bg-sub');
              if (s) { s.style.display = 'none'; s.offsetHeight; s.style.display = 'block'; }
            }
          });"""
    content = re.sub(r"// Reveal UI perif.*?\s*gsap\.to\(\['#nav-logo',.*?stagger:\s*0\.15\s*\}\);", new_code_regex, content, flags=re.DOTALL)
    print("Replaced with regex!")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
