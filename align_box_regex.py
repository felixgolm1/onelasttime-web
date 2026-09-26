import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's use a simpler regex that just finds the block based on some keywords.

pattern = re.compile(
    r"(          if \(transP <= 0\.85\) \{.+?)(mainDeck\.style\.transform = `translateX\(\$\{shiftX\}px\) scaleX\(\$\{boxScaleX\}\) scaleY\(\$\{boxScaleY\}\)`;)",
    re.DOTALL
)

def replacer(match):
    code = match.group(1)
    
    # Inject the scaling for magW and magH
    code = code.replace(
        "let magH = magScene ? magScene.offsetHeight * 0.77 : 532.1;",
        "let magH = magScene ? magScene.offsetHeight * 0.77 : 532.1;\n             if (window._cIsMobile) { magW *= 1.10; magH *= 1.10; }"
    )
    
    # Append the shiftY logic at the end of the block
    new_transform = """
          let shiftY = 0;
          if (window._cIsMobile) {
             let vh = window.innerHeight;
             let yMain = (0.46 * vh) - 127 + (275.18 / 2);
             let yRecuadro = (0.50 * vh) - (0.056 * vh);
             let deltaY = yRecuadro - yMain;
             let tY = transP <= 0.85 ? (transP / 0.85) : 1;
             shiftY = deltaY * tY;
          }
          mainDeck.style.transform = `translate(${shiftX}px, ${shiftY}px) scaleX(${boxScaleX}) scaleY(${boxScaleY})`;"""
          
    return code + new_transform

content = pattern.sub(replacer, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
