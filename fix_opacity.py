with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'const smallContainer = document\.querySelector\(\'\.scroll-indicator-container\'\);\s*if \(smallContainer\) \{[\s\S]*?\}\s*\}\s*\}', text)

new_logic = """const smallContainer = document.querySelector('.scroll-indicator-container');
           if (smallContainer) {
              Array.from(smallContainer.children).forEach(child => {
                  if (child.id !== 'magazine-scene') {
                      if (uiFade < 1) {
                          // Force hide during magazine expansion
                          child.style.opacity = uiFade;
                      } else {
                          // Clean up our forced opacity so GSAP can control it again
                          if (child.style.opacity === '1') {
                              child.style.opacity = '';
                          }
                      }
                  }
              });
           }
        }"""

if match:
    text = text.replace(match.group(0), new_logic)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Opacity override fixed!")
else:
    print("Match not found")
