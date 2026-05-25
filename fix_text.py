import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to stretch the durations of the text animations inside panData.forEach
target_block = '''        const stepTextData = detailStepTexts[i];
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

# Since there are encoding issues, let's use regex with wildcards for the text strings
pattern = r"const stepTextData = detailStepTexts\[i\];[\s\S]*?scrollTl\.set\(stepTextData\.wrapper, \{ pointerEvents: 'none' \}, t \+ PAN \+ HOLD \+ 0\.02\);\s*\}"

replacement = '''        const stepTextData = detailStepTexts[i];
        if (stepTextData && stepTextData.lines.length > 0) {
          // El timeline se ha multiplicado por 16 (PAN de 0.05 a 0.80)
          // Escalamos los tiempos de las animaciones de texto proporcionalmente
          const MULT = 16;
          let textDelay = ((i === 2) ? 0.028 : 0.035) * MULT;
  
          scrollTl.set(stepTextData.wrapper, { pointerEvents: 'auto' }, t + textDelay);
  
          // Slide up LINEAS INDIVIDUALES
          scrollTl.to(stepTextData.lines, {
            y: '0%',
            opacity: 1,
            duration: 0.015 * MULT,
            ease: 'power2.out',
            stagger: 0.002 * MULT
          }, t + textDelay);
  
          // Fade in ICONO
          if (stepTextData.icons && stepTextData.icons.length > 0) {
            scrollTl.to(stepTextData.icons, {
              opacity: 1,
              duration: 0.015 * MULT,
              ease: 'power2.out'
            }, t + textDelay);
          }
  
          // Desvanecer PALABRA A PALABRA
          scrollTl.to(stepTextData.words, {
            opacity: 0,
            duration: 0.015 * MULT,
            ease: 'none',
            stagger: { each: 0.0005 * MULT, from: 'end' }
          }, t + PAN + HOLD);
  
          // Fade Out ICONO
          if (stepTextData.icons && stepTextData.icons.length > 0) {
            scrollTl.to(stepTextData.icons, {
              opacity: 0,
              duration: 0.015 * MULT,
              ease: 'power2.out'
            }, t + PAN + HOLD);
          }
  
          // Desactivar interaccion
          scrollTl.set(stepTextData.wrapper, { pointerEvents: 'none' }, t + PAN + HOLD + (0.02 * MULT));
        }'''

content = re.sub(pattern, replacement, content)

# Also scale the detailGlobal fade out
content = re.sub(
    r"scrollTl\.to\(detailGlobal, \{ opacity: 0, duration: 0\.034, ease: 'none' \}, t\);",
    "scrollTl.to(detailGlobal, { opacity: 0, duration: 0.034 * 16, ease: 'none' }, t);",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
