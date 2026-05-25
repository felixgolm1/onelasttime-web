import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the shadow fade logic to also include the flaps
old_logic = """
        // Fade out the physical box shadow before it flattens into the magazine cover
        let shadowCast = mainDeck.querySelector('.box-shadow-cast');
        if (shadowCast) {
          if (prog > 9.62) {
            let sP = mapRange(prog, 9.62, 10.02, 0, 1);
            shadowCast.style.opacity = (1 - sP).toString();
          } else {
            shadowCast.style.opacity = '1';
          }
        }
"""

new_logic = """
        // Fade out the physical box shadow AND protruding flaps before it flattens into the magazine cover
        let shadowCast = mainDeck.querySelector('.box-shadow-cast');
        let flaps = mainDeck.querySelectorAll('.box-flap, .tuck-lip, .dust-flap');
        
        if (prog > 9.62) {
          let sP = mapRange(prog, 9.62, 10.02, 0, 1);
          let invSp = (1 - sP).toString();
          if (shadowCast) shadowCast.style.opacity = invSp;
          flaps.forEach(flap => flap.style.opacity = invSp);
        } else {
          if (shadowCast) shadowCast.style.opacity = '1';
          flaps.forEach(flap => flap.style.opacity = '1');
        }
"""

content = content.replace(old_logic.strip(), new_logic.strip())

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
