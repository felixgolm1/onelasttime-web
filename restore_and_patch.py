import os

prod_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web-produccion/3d-test.html'
dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(prod_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Variables
vars_inject = """
  let globalBrainMesh;
  const brainUniforms = {
    uProgress: { value: 0.0 },
    uTime: { value: 0.0 }
  };
"""
text = text.replace("let cardRenderer2, cardScene2, cardCam2;", "let cardRenderer2, cardScene2, cardCam2;" + vars_inject)

# 2. Shader & Loader
shader_inject = """
  const brainVS = `
    varying vec3 vNormal;
    varying vec3 vPosition;
    void main() {
      vNormal = normalize(normalMatrix * normal);
      vPosition = position;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `;
  const brainFS = `
    uniform float uProgress;
    uniform float uTime;
    varying vec3 vNormal;
    varying vec3 vPosition;

    vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
    vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
    vec4 permute(vec4 x) { return mod289(((x*34.0)+1.0)*x); }
    vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }
    float snoise(vec3 v){
      const vec2  C = vec2(1.0/6.0, 1.0/3.0) ;
      const vec4  D = vec4(0.0, 0.5, 1.0, 2.0);
      vec3 i  = floor(v + dot(v, C.yyy) );
      vec3 x0 = v - i + dot(i, C.xxx) ;
      vec3 g = step(x0.yzx, x0.xyz);
      vec3 l = 1.0 - g;
      vec3 i1 = min( g.xyz, l.zxy );
      vec3 i2 = max( g.xyz, l.zxy );
      vec3 x1 = x0 - i1 + C.xxx;
      vec3 x2 = x0 - i2 + C.yyy;
      vec3 x3 = x0 - D.yyy;
      i = mod289(i);
      vec4 p = permute( permute( permute(
                 i.z + vec4(0.0, i1.z, i2.z, 1.0 ))
               + i.y + vec4(0.0, i1.y, i2.y, 1.0 ))
               + i.x + vec4(0.0, i1.x, i2.x, 1.0 ));
      float n_ = 0.142857142857;
      vec3  ns = n_ * D.wyz - D.xzx;
      vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
      vec4 x_ = floor(j * ns.z);
      vec4 y_ = floor(j - 7.0 * x_ );
      vec4 x = x_ *ns.x + ns.yyyy;
      vec4 y = y_ *ns.x + ns.yyyy;
      vec4 h = 1.0 - abs(x) - abs(y);
      vec4 b0 = vec4( x.xy, y.xy );
      vec4 b1 = vec4( x.zw, y.zw );
      vec4 s0 = floor(b0)*2.0 + 1.0;
      vec4 s1 = floor(b1)*2.0 + 1.0;
      vec4 sh = -step(h, vec4(0.0));
      vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy ;
      vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww ;
      vec3 p0 = vec3(a0.xy,h.x);
      vec3 p1 = vec3(a0.zw,h.y);
      vec3 p2 = vec3(a1.xy,h.z);
      vec3 p3 = vec3(a1.zw,h.w);
      vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2, p2), dot(p3,p3)));
      p0 *= norm.x;
      p1 *= norm.y;
      p2 *= norm.z;
      p3 *= norm.w;
      vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
      m = m * m;
      return 42.0 * dot( m*m, vec4( dot(p0,x0), dot(p1,x1),
                                    dot(p2,x2), dot(p3,x3) ) );
    }

    void main() {
      float noiseVal = snoise(vPosition * 2.0 + uTime * 0.5);
      float heat = clamp(uProgress + noiseVal * 0.4, 0.0, 1.0);

      vec3 cold = vec3(0.2, 0.5, 1.0); 
      vec3 warm = vec3(0.6, 0.0, 0.6);
      vec3 hot  = vec3(1.0, 0.8, 0.2);
      vec3 white = vec3(1.0, 1.0, 1.0);

      vec3 color = mix(cold, warm, smoothstep(0.0, 0.5, heat));
      color = mix(color, hot, smoothstep(0.5, 0.8, heat));
      color = mix(color, white, smoothstep(0.8, 1.0, heat));

      vec3 viewDir = normalize(cameraPosition - vPosition);
      float fresnel = pow(1.0 - max(dot(viewDir, vNormal), 0.0), 2.5);
      
      float alpha = mix(0.8, 1.0, heat + fresnel*0.5);
      gl_FragColor = vec4(color, alpha);
    }
  `;

  const brainMat = new THREE.ShaderMaterial({
    vertexShader: brainVS,
    fragmentShader: brainFS,
    uniforms: brainUniforms,
    transparent: true,
    depthWrite: false,
    blending: THREE.NormalBlending
  });

  const gltfLoader = new THREE.GLTFLoader();
  
  // NEW LOAD FOR BRAIN
  gltfLoader.load('assets/models/human_brain.glb', (gltf) => {
        globalBrainMesh = gltf.scene;
        
        const box = new THREE.Box3().setFromObject(globalBrainMesh);
        const size = box.getSize(new THREE.Vector3());
        const center = box.getCenter(new THREE.Vector3());
        const maxDim = Math.max(size.x, size.y, size.z);
        
        const uiText = document.getElementById('brain-ui').querySelector('div');
        if (maxDim === 0) {
            uiText.innerText = "ERROR: TAMAÑO CERO";
            return;
        }
        
        const targetW = 20.0;
        const scale = targetW / maxDim;
        globalBrainMesh.scale.setScalar(scale);
        globalBrainMesh.position.set(-center.x * scale, -center.y * scale, -center.z * scale);
        
        const brainPivot = new THREE.Group();
        brainPivot.add(globalBrainMesh);
        
        globalBrainMesh.traverse(child => {
          if (child.isMesh) {
            child.material = brainMat;
            child.frustumCulled = false;
          }
        });
        
        uiText.innerText = "ACTIVIDAD CEREBRAL";
        brainPivot.visible = false;
        brainPivot.position.set(0, 0, -15);
        scene.add(brainPivot);
        window.brainPivot = brainPivot;
  });
"""

# Find `const gltfLoader = new THREE.GLTFLoader();` and replace it
text = text.replace("const gltfLoader = new THREE.GLTFLoader();", shader_inject)

# 3. maxProg
text = text.replace("const maxProg = 16.0;", "const maxProg = 20.0;")

# 4. Render loop
text = text.replace("renderer.render(scene, camera);", "if(typeof brainUniforms !== 'undefined') { brainUniforms.uTime.value += 0.01; }\n    renderer.render(scene, camera);")

# 5. UI HTML
ui_html = """
<div id="brain-ui" style="position:fixed; right:5vw; top:50%; transform:translateY(-50%); opacity:0; pointer-events:none; z-index:10010; color:white; font-family:'Inter', sans-serif; transition: opacity 0.5s ease; background: rgba(10,15,10,0.85); backdrop-filter: blur(10px); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 320px; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
    <div style="font-size: 10px; letter-spacing: 2px; color: #a3ff00; font-weight: 700; margin-bottom: 10px;">ACTIVIDAD CEREBRAL</div>
    <div id="brain-title" style="font-size: 32px; font-weight: 700; margin-bottom: 15px; font-family: 'Playfair Display', serif; color: #a0d2ff; transition: color 0.5s ease;">Small Talk</div>
    <div style="width: 100%; height: 2px; background: rgba(255,255,255,0.1); margin-bottom: 15px; position: relative;">
        <div id="brain-progress-bar" style="position: absolute; left: 0; top: 0; height: 100%; width: 0%; background: #a3ff00; transition: width 0.3s ease;"></div>
    </div>
    <div id="brain-desc" style="font-size: 13px; line-height: 1.6; color: #e0e0e0;">Actividad superficial. Se liberan niveles basales de dopamina. Perfecto para romper el hielo y crear confort inicial.</div>
</div>
"""
text = text.replace("<!-- --- UI OVERLAYS --- -->", "<!-- --- UI OVERLAYS --- -->\n" + ui_html)

# 6. Portal Logic
portal_logic = """
        // --- PORTAL EFFECT & BRAIN ---
        let portalP = mapRange(prog, 14.62, 16.0, 0, 1);
        if (portalP > 0) {
            let magScale = 0.85 * (1 + (portalP * 12));
            let magOpacity = mapRange(portalP, 0.4, 1.0, 1, 0);
            
            magazineScene.style.transform = `translate(-50%, -50%) scale(${magScale})`;
            magazineScene.style.opacity = magOpacity;
            
            if (window.brainPivot) {
                window.brainPivot.visible = true;
                let brainOp = mapRange(portalP, 0.5, 1.0, 0, 1);
                
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
                    brainUI.style.opacity = brainOp > 0.1 ? '1' : '0';
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
target = "lineR.setAttribute('y1', '100%'); lineR.setAttribute('y2', `${100 - (100 * dashP)}%`);\n        }"
text = text.replace(target, target + "\n" + portal_logic)

with open(dev_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Restore and Patch Completed!")
