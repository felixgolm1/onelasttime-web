with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()
changes = 0

# ============================================================
# 1. Add Bloom/EffectComposer CDN scripts after three.js
# ============================================================
old_scripts = '  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/renderers/CSS3DRenderer.js"></script>'
new_scripts = old_scripts + """
  <!-- Postprocessing: Bloom for brain cinematic effect -->
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/LuminosityHighPassShader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"></script>"""

if old_scripts in text:
    text = text.replace(old_scripts, new_scripts)
    changes += 1; print('1. Bloom scripts added')
else:
    print('ERROR: script tag not found')

# ============================================================
# 2. Upgrade initBrainRenderer: PBR renderer, rim lights,
#    interior point light, insula sphere, bloom composer
# ============================================================
old_init = """    brainRenderer = new THREE.WebGLRenderer({ canvas: brainCanvasEl, antialias: true, alpha: true, preserveDrawingBuffer: false });
    brainRenderer.setSize(window.innerWidth, window.innerHeight);
    brainRenderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    brainRenderer.setClearColor(0x000000, 0);
    brainRenderer.toneMapping = THREE.NoToneMapping;

    brainScene = new THREE.Scene();

    // Camara frontal simple: mira directamente al frente
    brainCam = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    brainCam.position.set(0, 0, 5);
    brainCam.lookAt(0, 0, 0);

    // Iluminacion del cerebro
    const ambBrain = new THREE.AmbientLight(0xffffff, 0.3);
    brainScene.add(ambBrain);
    const keyBrain = new THREE.DirectionalLight(0xffffff, 1.5);
    keyBrain.position.set(3, 5, 5);
    brainScene.add(keyBrain);

    window.addEventListener('resize', () => {
      brainCam.aspect = window.innerWidth / window.innerHeight;
      brainCam.updateProjectionMatrix();
      brainRenderer.setSize(window.innerWidth, window.innerHeight);
    });
  })();"""

new_init = """    brainRenderer = new THREE.WebGLRenderer({ canvas: brainCanvasEl, antialias: true, alpha: true, preserveDrawingBuffer: false });
    brainRenderer.setSize(window.innerWidth, window.innerHeight);
    brainRenderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    brainRenderer.setClearColor(0x000000, 0);
    brainRenderer.toneMapping = THREE.ACESFilmicToneMapping;
    brainRenderer.toneMappingExposure = 1.0;
    brainRenderer.shadowMap.enabled = false;

    brainScene = new THREE.Scene();

    // Cinematic camera — will be moved per phase
    brainCam = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    brainCam.position.set(0, 0.5, 5.5);
    brainCam.lookAt(0, 0, 0);

    // === LIGHTING RIG ===
    // Ambient: very subtle — most light comes from key + rim
    const ambBrain = new THREE.AmbientLight(0x0a0a18, 0.6);
    brainScene.add(ambBrain);

    // Key light: warm white top-front
    const keyBrain = new THREE.DirectionalLight(0xfff5e0, 1.8);
    keyBrain.position.set(2, 5, 5);
    brainScene.add(keyBrain);

    // Rim Light 1 — Phase 1: electric cyan (back-right)
    window.rimLight1 = new THREE.DirectionalLight(0x00cfff, 0.0);
    window.rimLight1.position.set(-4, 1, -3);
    brainScene.add(window.rimLight1);

    // Rim Light 2 — Phase 2: amber orange (back-left)
    window.rimLight2 = new THREE.DirectionalLight(0xff6a00, 0.0);
    window.rimLight2.position.set(4, -1, -4);
    brainScene.add(window.rimLight2);

    // Rim Light 3 — Phase 3: deep violet (bottom)
    window.rimLight3 = new THREE.DirectionalLight(0xaa00ff, 0.0);
    window.rimLight3.position.set(0, -4, -3);
    brainScene.add(window.rimLight3);

    // Interior Point Light — orange, simulates neural glow escaping fissures
    window.brainInteriorLight = new THREE.PointLight(0xff5500, 0.0, 6.0, 2.0);
    window.brainInteriorLight.position.set(0, 0, 0);
    brainScene.add(window.brainInteriorLight);

    // Insula sphere — violet pulsing sphere for Phase 3
    const insulaGeo = new THREE.SphereGeometry(0.18, 16, 12);
    const insulaMat = new THREE.MeshBasicMaterial({
      color: 0xcc44ff, transparent: true, opacity: 0.0,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    window.insulaSphere = new THREE.Mesh(insulaGeo, insulaMat);
    window.insulaSphere.position.set(-0.4, -0.3, 0.2); // insula: lateral, inferior
    brainScene.add(window.insulaSphere);

    // === BLOOM COMPOSER ===
    if (typeof THREE.EffectComposer !== 'undefined') {
      window.brainComposer = new THREE.EffectComposer(brainRenderer);
      const renderPass = new THREE.RenderPass(brainScene, brainCam);
      window.brainComposer.addPass(renderPass);
      const bloomPass = new THREE.UnrealBloomPass(
        new THREE.Vector2(window.innerWidth, window.innerHeight),
        0.65,   // strength
        0.38,   // radius
        0.60    // threshold (only bright areas glow)
      );
      window.brainBloomPass = bloomPass;
      window.brainComposer.addPass(bloomPass);
    }

    window.addEventListener('resize', () => {
      brainCam.aspect = window.innerWidth / window.innerHeight;
      brainCam.updateProjectionMatrix();
      brainRenderer.setSize(window.innerWidth, window.innerHeight);
      if (window.brainComposer) window.brainComposer.setSize(window.innerWidth, window.innerHeight);
    });
  })();"""

if old_init in text:
    text = text.replace(old_init, new_init)
    changes += 1; print('2. Renderer upgraded with lights + bloom')
else:
    print('ERROR: init block not found')

# ============================================================
# 3. Upgrade material setup: PBR roughness + metalness
# ============================================================
old_mat = """            child.material = child.material.clone();
            child.material.vertexColors = true;
            // CRITICAL: set material.color to white so vertex colors display pure
            // Without this, vertex colors are multiplied by the original material color (dark brown)
            child.material.color.setRGB(1, 1, 1);
            child.material.needsUpdate = true;"""

new_mat = """            child.material = child.material.clone();
            child.material.vertexColors = true;
            // White base so vertex colors render pure
            child.material.color.setRGB(1, 1, 1);
            // PBR: organic hydrated tissue look
            if (child.material.roughness !== undefined) {
              child.material.roughness = 0.42;
              child.material.metalness = 0.04;
            }
            child.material.needsUpdate = true;"""

if old_mat in text:
    text = text.replace(old_mat, new_mat)
    changes += 1; print('3. PBR material set')
else:
    print('ERROR: material block not found')

# ============================================================
# 4. Upgrade render loop: lights per phase + camera + bloom
# ============================================================
old_render = """    // Render del cerebro en su canvas dedicado
    if (brainRenderer && brainScene && brainCam && window.brainPivot && window.brainPivot.visible) {
      // Actualizar vertex colors del mapa de actividad cerebral
      if (window.updateBrainVertexColors) {
        window.updateBrainVertexColors(
          brainUniforms.uProgress.value,
          brainUniforms.uTime.value
        );
      }
      brainRenderer.render(brainScene, brainCam);
    }"""

new_render = """    // Render del cerebro en su canvas dedicado
    if (brainRenderer && brainScene && brainCam && window.brainPivot && window.brainPivot.visible) {
      const hp = brainUniforms.uProgress.value;
      const tt = brainUniforms.uTime.value;

      // --- Update vertex heatmap ---
      if (window.updateBrainVertexColors) {
        window.updateBrainVertexColors(hp, tt);
      }

      // --- Cinematic camera path per phase ---
      // Phase 1: slight upper-right (front lobe view) -> Phase 2: center -> Phase 3: frontal
      const camP1 = Math.max(0, Math.min(1, hp / 0.33));
      const camP2 = Math.max(0, Math.min(1, (hp-0.33) / 0.33));
      const camP3 = Math.max(0, Math.min(1, (hp-0.66) / 0.34));
      const cx = 0 + camP1*1.2 - camP2*1.2 + camP3*(-0.4);
      const cy = 0.5 - camP2*0.5;
      const cz = 5.5 - camP1*0.5 + camP3*0.2;
      brainCam.position.x += (cx - brainCam.position.x) * 0.05;
      brainCam.position.y += (cy - brainCam.position.y) * 0.05;
      brainCam.position.z += (cz - brainCam.position.z) * 0.05;
      brainCam.lookAt(0, 0, 0);

      // --- Phase-based lighting ---
      const ss = function(a,b,x){const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t);};
      if (window.rimLight1) window.rimLight1.intensity = ss(0.0, 0.30, hp) * (1-ss(0.45,0.65,hp)) * 1.8;
      if (window.rimLight2) window.rimLight2.intensity = ss(0.25, 0.58, hp) * (1-ss(0.68,0.85,hp)) * 2.0;
      if (window.rimLight3) window.rimLight3.intensity = ss(0.60, 0.90, hp) * 1.6;

      // Interior point light: orange glow escaping through fissures (Phase 2 peak)
      if (window.brainInteriorLight) {
        const intI = ss(0.28, 0.58, hp) * (1-ss(0.72,0.90,hp)) * 3.5;
        window.brainInteriorLight.intensity = intI;
        // Slow pulse for organic feel
        window.brainInteriorLight.intensity *= 0.85 + Math.sin(tt*2.1)*0.15;
      }

      // Insula sphere: violet pulse for Phase 3
      if (window.insulaSphere) {
        const insOp = ss(0.62, 0.85, hp) * 0.85;
        window.insulaSphere.material.opacity = insOp * (0.7 + Math.sin(tt*1.3)*0.3);
        window.insulaSphere.scale.setScalar(1.0 + Math.sin(tt*1.3)*0.15);
      }

      // --- Render (bloom if available, fallback to direct) ---
      if (window.brainComposer) {
        window.brainComposer.render();
      } else {
        brainRenderer.render(brainScene, brainCam);
      }
    }"""

if old_render in text:
    text = text.replace(old_render, new_render)
    changes += 1; print('4. Render loop upgraded')
else:
    print('ERROR: render loop not found')

with open('3d-test.html','w',encoding='utf-8') as f: f.write(text)
print(f'Done. {changes}/4 changes applied.')
