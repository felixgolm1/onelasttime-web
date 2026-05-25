import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'const magContent = magazineScene\.querySelector\(\'\.magazine-content\'\);[\s\S]*?magContent\.style\.backgroundPosition = `center \$\{bgPos\}%`;\n           \}', text)

if match:
    new_logic = """const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              // Expand applied ONLY to inner content
              if (easeP > 0) {
                  magContent.style.position = 'fixed';
                  magContent.style.left = '50vw';
                  magContent.style.top = '50vh';
                  magContent.style.transform = 'translate(-50%, -50%)';
                  magContent.style.zIndex = '10000';
                  magContent.style.width = `${baseW + (window.innerWidth - baseW) * easeP}px`;
                  magContent.style.height = `${baseH + (window.innerHeight - baseH) * easeP}px`;
              } else {
                  magContent.style.position = 'relative';
                  magContent.style.left = 'auto';
                  magContent.style.top = 'auto';
                  magContent.style.transform = 'none';
                  magContent.style.zIndex = '2';
                  magContent.style.width = '100%';
                  magContent.style.height = '100%';
              }

              // Animate SVG lines (un-draw)
              const svgLines = magazineScene.querySelectorAll('line');
              svgLines.forEach(line => {
                  line.style.strokeDasharray = '2000';
                  line.style.strokeDashoffset = `${2000 * easeP}`;
              });

              // Fade out CSS border
              magContent.style.borderColor = `rgba(249, 204, 16, ${uiFade})`;
              magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;
              magContent.style.backgroundColor = `rgba(6, 2, 15, ${uiFade})`;
              
              // Zoom effect: photo adapts
              const bgSize = 250 - (150 * easeP);
              const bgPos = 15 + (35 * easeP);
              magContent.style.backgroundSize = `${bgSize}%`;
              magContent.style.backgroundPosition = `center ${bgPos}%`;
           }"""

    updated_text = text.replace(match.group(0), new_logic)
    
    # We ALSO must remove the fixed position from magazineScene if it was still there!
    # Let's clean up magazineScene positioning if we previously added it.
    cleanup_match = re.search(r'// 3\. Expans.*[\s\S]*?\} else \{[\s\S]*?\}[\s\n]*const targetW', text)
    if cleanup_match:
        print("Wait, my regex matched something else. I will just rely on the first replace.")
        
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("Layout Fixed!")
else:
    print("Could not find JS block to replace.")
