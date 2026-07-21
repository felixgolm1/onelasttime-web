import re

def main():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # We need to re-add a SAFE fade out for the UI at the end, WITHOUT breaking the GSAP intro.
    
    # We find where polProg is calculated
    search_str = "let polProg = Math.max(0, Math.min(1, (prog - 54.0) / 7.0));"
    
    safe_fade = """
              // Fade out UI at the very end to reveal 3D canvas (and prevent CTA overlap)
              if (prog > 30.0) {
                  ['nav-logo', 'nav-menu', 'cta-top-container', 'cta-bottom-container', 'headline', 'subheadline'].forEach(id => {
                      const el = document.getElementById(id);
                      if (el) {
                          el.style.opacity = 1 - polProg;
                          el.style.pointerEvents = polProg > 0 ? 'none' : '';
                      }
                  });
              }
"""
    
    if search_str in html and safe_fade not in html:
        html = html.replace(search_str, search_str + safe_fade)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
