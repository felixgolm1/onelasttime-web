import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the portal logic block to NOT scale magazineScene at all, just fade it.
# And scale the brain up from 0.01 to 1.0 during its fade in.

safe_logic = """
        // --- PORTAL EFFECT & BRAIN ---
        // Se activa solo a partir de 11.62, dejando la revista visible de 10.62 a 11.62
        let portalP = mapRange(prog, 11.62, 12.62, 0, 1);
        if (portalP > 0) {
            let magOpacity = mapRange(portalP, 0.2, 0.8, 1, 0); // Fade out suavemente
            magazineScene.style.opacity = magOpacity;
            // No tocamos transform para no romper el layout!
            magazineScene.style.transform = '';
            
            if (window.brainPivot) {
                window.brainPivot.visible = true;
                let brainOp = mapRange(portalP, 0.5, 1.0, 0, 1);
                
                // Efecto de que el cerebro avanza hacia la camara mientras aparece
                let brainZ = mapRange(portalP, 0.5, 1.0, -80, -15);
                window.brainPivot.position.set(0, 0, brainZ);
                
                let rotY = mapRange(prog, 11.62, 16.0, 0, Math.PI * 2);
                window.brainPivot.rotation.y = rotY;
                window.brainPivot.rotation.x = mapRange(prog, 11.62, 16.0, 0, 0.4);
                
                let heatP = mapRange(prog, 12.62, 16.0, 0, 1);
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
text = re.sub(r"// --- PORTAL EFFECT & BRAIN ---.*?(?=\}\s*\}\s*else)", safe_logic, text, flags=re.DOTALL)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Safe portal logic applied!")
