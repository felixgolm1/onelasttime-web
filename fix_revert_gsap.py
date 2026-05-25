import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Revert PAN and HOLD
content = re.sub(
    r'const PAN\s*=\s*0\.80;\s*\n\s*const HOLD\s*=\s*0\.40;',
    'const PAN  = 0.05;\n      const HOLD = 0.025;',
    content
)

# 2. Revert Text Animations
pattern = r"const stepTextData = detailStepTexts\[i\];[\s\S]*?scrollTl\.set\(stepTextData\.wrapper, \{ pointerEvents: 'none' \}, t \+ PAN \+ HOLD \+ \(0\.02 \* MULT\)\);\s*\}"

replacement = '''        const stepTextData = detailStepTexts[i];
        if (stepTextData && stepTextData.lines.length > 0) {
          // Ajustar la aparicin del texto en el Paso 3.
          // El Paso 2 tiene ~24 palabras. Su fade out tarda 0.015s + (24 * 0.0005s de stagger) = 0.027s.
          // Empezamos justo en 0.028s para no solaparnos ni dejar huecos.
          let textDelay = (i === 2) ? 0.028 : 0.035;
  
          // Hacer el contenedor seleccionable solo cuando estǭ activo
          scrollTl.set(stepTextData.wrapper, { pointerEvents: 'auto' }, t + textDelay);
  
          // Slide up L?NEAS INDIVIDUALES (empieza despuǸs del fade out del anterior)
          scrollTl.to(stepTextData.lines, {
            y: '0%',
            opacity: 1,
            duration: 0.015,
            ease: 'power2.out',
            stagger: 0.002
          }, t + textDelay);
  
          // Fade in ICONO (sin slide)
          if (stepTextData.icons && stepTextData.icons.length > 0) {
            scrollTl.to(stepTextData.icons, {
              opacity: 1,
              duration: 0.015,
              ease: 'power2.out'
            }, t + textDelay);
          }
  
          // Desvanecer PALABRA A PALABRA en cascada desde abajo a la derecha hacia arriba a la izquierda
          scrollTl.to(stepTextData.words, {
            opacity: 0,
            duration: 0.015,
            ease: 'none',
            stagger: { each: 0.0005, from: 'end' } // Ultra-rǭpido para desaparecer completamente antes de 0.035s
          }, t + PAN + HOLD);
  
          // Fade Out ICONO
          if (stepTextData.icons && stepTextData.icons.length > 0) {
            scrollTl.to(stepTextData.icons, {
              opacity: 0,
              duration: 0.015,
              ease: 'power2.out'
            }, t + PAN + HOLD);
          }
  
          // Desactivar interaccin
          scrollTl.set(stepTextData.wrapper, { pointerEvents: 'none' }, t + PAN + HOLD + 0.02);
        }'''

content = re.sub(pattern, replacement, content)

# 3. Revert Global Box detail animation
content = re.sub(
    r"scrollTl\.to\(detailGlobal, \{ opacity: 0, duration: 0\.034 \* 16, ease: 'none' \}, t\);",
    "scrollTl.to(detailGlobal, { opacity: 0, duration: 0.034, ease: 'none' }, t);",
    content
)

# 4. Add the massive scroll divisor for the entire intro (up to prog = 0.50)
content = re.sub(
    r'let divisor = 900;\n\s*if \(targetProg < 0\.08\) divisor = 8000;',
    'let divisor = 900;\n        if (targetProg < 0.50) divisor = 6000;',
    content
)

content = re.sub(
    r'let divisorT = 450;\n\s*if \(targetProg < 0\.08\) divisorT = 4000;',
    'let divisorT = 450;\n        if (targetProg < 0.50) divisorT = 3000;',
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
