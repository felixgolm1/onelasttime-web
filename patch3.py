import sys

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = "lineR.setAttribute('y1', '100%'); lineR.setAttribute('y2', `${100 - (100 * dashP)}%`);\n        }"

scroll_logic = """
        // --- PORTAL EFFECT & BRAIN ---
        let portalP = mapRange(prog, 10.62, 11.62, 0, 1);
        if (portalP > 0) {
            let magScale = 1 + (portalP * 12);
            let magOpacity = mapRange(portalP, 0.4, 1.0, 1, 0);
            magazineScene.style.transform = `translate(-50%, -50%) scale(${0.85 * magScale})`;
            magazineScene.style.opacity = magOpacity;
            
            if (window.brainPivot) {
                window.brainPivot.visible = true;
                let brainOp = mapRange(portalP, 0.5, 1.0, 0, 1);
                
                let rotY = mapRange(prog, 10.62, 15.0, 0, Math.PI * 2);
                window.brainPivot.rotation.y = rotY;
                window.brainPivot.rotation.x = mapRange(prog, 10.62, 15.0, 0, 0.3);
                
                let heatP = mapRange(prog, 11.62, 15.0, 0, 1);
                if(typeof brainUniforms !== 'undefined') brainUniforms.uProgress.value = heatP;
                
                const brainUI = document.getElementById('brain-ui');
                const bTitle = document.getElementById('brain-title');
                const bDesc = document.getElementById('brain-desc');
                const bBar = document.getElementById('brain-progress-bar');
                
                if (brainUI) {
                    if (brainOp > 0.1) {
                        brainUI.style.opacity = '1';
                    } else {
                        brainUI.style.opacity = '0';
                    }
                    
                    if (heatP < 0.33) {
                        bTitle.innerText = "Small Talk";
                        bDesc.innerHTML = "Actividad superficial. Se liberan niveles basales de dopamina. Perfecto para romper el hielo y crear confort inicial.";
                        bTitle.style.color = "#a0d2ff";
                    } else if (heatP < 0.66) {
                        bTitle.innerText = "Profundizando";
                        bDesc.innerHTML = "Aumento de la corteza prefrontal. Comienza la liberacion de oxitocina generando lazos de confianza. El dialogo requiere mas energia.";
                        bTitle.style.color = "#ff9a3d";
                    } else {
                        bTitle.innerText = "Conexion Profunda";
                        bDesc.innerHTML = "Actividad maxima en areas limbicas. Alta oxitocina y serotonina. Emociones a flor de piel, vulnerabilidad y vinculos fuertes creados.";
                        bTitle.style.color = "#ffcc00";
                    }
                    bBar.style.width = (heatP * 100) + '%';
                }
            }
        } else {
            magazineScene.style.transform = `translate(-50%, -50%) scale(0.85)`;
            if (window.brainPivot) window.brainPivot.visible = false;
            const brainUI = document.getElementById('brain-ui');
            if (brainUI) brainUI.style.opacity = '0';
        }
"""

if target in text:
    text = text.replace(target, target + "\n" + scroll_logic)
    print("Injected Scroll logic correctly!")
else:
    print("COULD NOT FIND TARGET EXACT STRING")

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
