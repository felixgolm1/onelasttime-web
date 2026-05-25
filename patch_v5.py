import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extend maxProg from 16.0 to 20.0
text = text.replace("const maxProg = 16.0;", "const maxProg = 20.0;")

# 2. Re-implement the Portal Effect but starting at 14.62 (after carousel finishes)
# Remove the old safe portal logic
text = re.sub(r"// --- PORTAL EFFECT & BRAIN ---.*?(?=\}\s*\}\s*else)", "", text, flags=re.DOTALL)

# Insert new logic exactly before "} else {" of the if (prog > 9.62) block
# Wait, let's use the lineR.setAttribute again to be safe.
target = "lineR.setAttribute('y1', '100%'); lineR.setAttribute('y2', `${100 - (100 * dashP)}%`);\n        }"

portal_logic = """
        // --- PORTAL EFFECT & BRAIN ---
        // Ocurre DESPUES de la revista (el carrusel termina en 14.62)
        let portalP = mapRange(prog, 14.62, 16.0, 0, 1);
        if (portalP > 0) {
            let magScale = 1 + (portalP * 12);
            let magOpacity = mapRange(portalP, 0.4, 1.0, 1, 0);
            
            // Hacemos el Zoom-in (Dive-in) escalando la escena completa.
            // Como el carrusel esta en la ultima imagen centrada, el zoom ira hacia esa imagen!
            magazineScene.style.transform = `scale(${magScale})`;
            magazineScene.style.opacity = magOpacity;
            
            if (window.brainPivot) {
                window.brainPivot.visible = true;
                let brainOp = mapRange(portalP, 0.5, 1.0, 0, 1);
                
                window.brainPivot.position.set(0, 0, -15);
                
                let rotY = mapRange(prog, 14.62, 20.0, 0, Math.PI * 2);
                window.brainPivot.rotation.y = rotY;
                window.brainPivot.rotation.x = mapRange(prog, 14.62, 20.0, 0, 0.4);
                
                let heatP = mapRange(prog, 16.0, 20.0, 0, 1);
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
                        bDesc.innerHTML = "Aumento de la corteza prefrontal. Comienza la liberación de oxitocina generando lazos de confianza. El diálogo requiere más energía.";
                        bTitle.style.color = "#ff9a3d";
                    } else {
                        bTitle.innerText = "Conexión Profunda";
                        bDesc.innerHTML = "Actividad máxima en áreas límbicas. Alta oxitocina y serotonina. Emociones a flor de piel, vulnerabilidad y vínculos fuertes creados.";
                        bTitle.style.color = "#ffcc00";
                    }
                    bBar.style.width = (heatP * 100) + '%';
                }
            }
        } else {
            magazineScene.style.transform = '';
            if (window.brainPivot) window.brainPivot.visible = false;
            const brainUI = document.getElementById('brain-ui');
            if (brainUI) brainUI.style.opacity = '0';
        }
"""
text = text.replace(target, target + "\n" + portal_logic)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch v5 applied!")
