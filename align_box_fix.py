import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r"""             let magScene = document.getElementById\('magazine-scene'\);
             let magW = magScene \? magScene\.offsetWidth \* 0\.77 : 396\.1;
             let magH = magScene \? magScene\.offsetHeight \* 0\.77 : 532\.1;
             let baseW = window\._cIsMobile \? 88\.489 : 89\.74;
             let baseH = window\._cIsMobile \? 275\.18 : 329\.41;
             let targetScaleX = magW / baseW;
             let targetScaleY = magH / baseH;
             boxScaleX = 1 \+ \(targetScaleX - 1\) \* tX;
             boxScaleY = 1 \+ \(targetScaleY - 1\) \* tY;
             shiftX = -\( \(window\._cIsMobile \? 88\.489 : 89\.74\) / 2 \) \* boxScaleX;
          \} else if \(transP > 0\.85\) \{
             let magScene = document.getElementById\('magazine-scene'\);
             let magW = magScene \? magScene\.offsetWidth \* 0\.77 : 396\.1;
             let magH = magScene \? magScene\.offsetHeight \* 0\.77 : 532\.1;
             let baseW = window\._cIsMobile \? 88\.489 : 89\.74;
             let baseH = window\._cIsMobile \? 275\.18 : 329\.41;
             boxScaleX = magW / baseW;
             boxScaleY = magH / baseH;
             shiftX = -\( \(window\._cIsMobile \? 88\.489 : 89\.74\) / 2 \) \* boxScaleX;
          \}
          mainDeck\.style\.transform = `translateX\(\$\{shiftX\}px\) scaleX\(\$\{boxScaleX\}\) scaleY\(\$\{boxScaleY\}\)`;"""

replacement = """             let magScene = document.getElementById('magazine-scene');
             let magW = magScene ? magScene.offsetWidth * 0.77 : 396.1;
             let magH = magScene ? magScene.offsetHeight * 0.77 : 532.1;
             if (window._cIsMobile) { magW *= 1.10; magH *= 1.10; }
             let baseW = window._cIsMobile ? 88.489 : 89.74;
             let baseH = window._cIsMobile ? 275.18 : 329.41;
             let targetScaleX = magW / baseW;
             let targetScaleY = magH / baseH;
             boxScaleX = 1 + (targetScaleX - 1) * tX;
             boxScaleY = 1 + (targetScaleY - 1) * tY;
             shiftX = -( (window._cIsMobile ? 88.489 : 89.74) / 2 ) * boxScaleX;
          } else if (transP > 0.85) {
             let magScene = document.getElementById('magazine-scene');
             let magW = magScene ? magScene.offsetWidth * 0.77 : 396.1;
             let magH = magScene ? magScene.offsetHeight * 0.77 : 532.1;
             if (window._cIsMobile) { magW *= 1.10; magH *= 1.10; }
             let baseW = window._cIsMobile ? 88.489 : 89.74;
             let baseH = window._cIsMobile ? 275.18 : 329.41;
             boxScaleX = magW / baseW;
             boxScaleY = magH / baseH;
             shiftX = -( (window._cIsMobile ? 88.489 : 89.74) / 2 ) * boxScaleX;
          }
          
          let shiftY = 0;
          if (window._cIsMobile) {
             let vh = window.innerHeight;
             let yMain = (0.46 * vh) - 127 + (275.18 / 2);
             let yRecuadro = (0.50 * vh) - (0.056 * vh); // -5.6vh from CSS
             let deltaY = yRecuadro - yMain;
             let tY = transP <= 0.85 ? (transP / 0.85) : 1;
             shiftY = deltaY * tY;
          }
          
          mainDeck.style.transform = `translate(${shiftX}px, ${shiftY}px) scaleX(${boxScaleX}) scaleY(${boxScaleY})`;"""

content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
