import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r"""                    let flipProg = Math\.max\(0, Math\.min\(1, \(prog - 1\.30\) / 0\.27\)\);
                    let easeFlip = flipProg \* flipProg; // ease-in cuadratico
                    const initialCY = window\._ch \* 0\.5; // HTML card center \(50vh\)
                    const finalCY = window\._cIsMobile \? \(window\._ch \* 0\.46\) : \(window\._ch \* 0\.455\);
                    const baseCY = initialCY \+ easeFlip \* \(finalCY - initialCY\);"""

replacement = """                    let flipProg = Math.max(0, Math.min(1, (prog - 1.30) / 0.27));
                    let easeFlip = flipProg * flipProg; // ease-in cuadratico
                    let dropProg = Math.max(0, Math.min(1, (prog - 1.65) / 0.25));
                    let riseProg = Math.max(0, Math.min(1, (prog - 2.20) / (9.62 - 2.20)));
                    const initialCY = window._ch * 0.5; // HTML card center (50vh)
                    const peakCY = window._cIsMobile ? (window._ch * 0.46) : (window._ch * 0.455);
                    const baseCY = initialCY 
                                 + (easeFlip * (peakCY - initialCY)) 
                                 - (dropProg * (peakCY - initialCY))
                                 + (riseProg * (peakCY - initialCY));"""

content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
