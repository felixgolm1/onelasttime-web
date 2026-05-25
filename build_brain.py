import re, sys
with open('3d-test.html','r',encoding='utf-8') as f: base=f.read()

# 1. Update maxProg
base = re.sub(r'const maxProg = 16\.0;', r'const maxProg = 20.0;', base)

# 2. Add dependencies
scripts_to_add = """<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/LuminosityHighPassShader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/renderers/CSS2DRenderer.js"></script>
"""
base = base.replace(
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>',
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n  ' + scripts_to_add
)

# 3. Add brain globals
brain_decls = """
  // ===== BRAIN VARIABLES =====
  let brainCanvasEl = null, brainRenderer = null, brainScene = null, brainCam = null;
  let css2DRenderer = null;
  window.brainPivot = null;
  window.brainMeshes = [];
  const brainUniforms = { uProgress: { value: 0.0 }, uTime: { value: 0.0 } };
"""
base = base.replace('  let globalBrainMesh;', '  let globalBrainMesh;\n' + brain_decls)


# 4. Inject Procedural Brain code before the loop
BRAIN_CODE = """
  // =============================================
  // PROCEDURAL BRAIN ENGINE (Icosahedron + Noise + CSS2D)
  // =============================================
  (function initBrainRenderer() {
    // 1. WebGL Renderer
    brainCanvasEl = document.createElement('canvas');
    brainCanvasEl.id = 'brain-canvas';
    brainCanvasEl.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:10008;pointer-events:none;opacity:0;transition:opacity 0.8s ease;';
    document.body.appendChild(brainCanvasEl);
    
    brainRenderer = new THREE.WebGLRenderer({ canvas:brainCanvasEl, antialias:true, alpha:true });
    brainRenderer.setSize(window.innerWidth, window.innerHeight);
    brainRenderer.setPixelRatio(Math.min(devicePixelRatio,2));
    brainRenderer.setClearColor(0x000000, 0);
    
    // 2. Scene & Camera
    brainScene = new THREE.Scene();
    brainCam = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 100);
    brainCam.position.set(0, 0, 5.2);
    brainCam.lookAt(0, 0, 0);
    
    // 3. CSS2DRenderer
    if (typeof THREE.CSS2DRenderer !== 'undefined') {
        css2DRenderer = new THREE.CSS2DRenderer();
        css2DRenderer.setSize(window.innerWidth, window.innerHeight);
        css2DRenderer.domElement.style.position = 'fixed';
        css2DRenderer.domElement.style.top = '0';
        css2DRenderer.domElement.style.left = '0';
        css2DRenderer.domElement.style.pointerEvents = 'none';
        css2DRenderer.domElement.style.zIndex = '10009';
        document.body.appendChild(css2DRenderer.domElement);
    }
    
    // 4. Procedural Geometry (Icosahedron)
    const R = 1.3;
    const geo = new THREE.IcosahedronGeometry(R, 16); // High detail
    
    // Vertex displacement logic in Vertex Shader
    const vShader = `
      uniform float uTime;
      uniform float uProgress;
      varying vec3 vNormal;
      varying vec3 vPosition;
      varying vec2 vUv;
      
      // Simplex noise function
      vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
      vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
      vec4 permute(vec4 x) { return mod289(((x*34.0)+1.0)*x); }
      vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }
      float snoise(vec3 v) {
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
        p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
        vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
        m = m * m; return 42.0 * dot( m*m, vec4( dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3) ) );
      }

      void main() {
        vNormal = normal;
        vUv = uv;
        
        vec3 pos = position;
        
        // Deformacion base (surcos)
        float noise = snoise(pos * 3.5 + uTime * 0.1) * 0.08;
        float noise2 = snoise(pos * 8.0 - uTime * 0.15) * 0.03;
        
        // Fisura interhemisferica
        float fissure = smoothstep(0.05, 0.0, abs(pos.x));
        pos.x += fissure * sign(pos.x) * 0.08;
        
        vec3 newPos = pos + normal * (noise + noise2) * (1.0 - fissure);
        
        // Fase 3 transicion: contraccion del envoltorio exterior
        float contract = smoothstep(0.6, 1.0, uProgress);
        newPos = mix(newPos, newPos * 0.85, contract);
        
        vPosition = newPos;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(newPos, 1.0);
      }
    `;
    
    // Fragment Shader (Heatmap logic)
    const fShader = `
      uniform float uTime;
      uniform float uProgress;
      varying vec3 vNormal;
      varying vec3 vPosition;
      
      void main() {
        vec3 baseColor = vec3(0.02, 0.02, 0.05); // Base muy oscura
        
        // Fase 1: Prefrontal (Frente)
        float f1 = smoothstep(0.2, 1.0, vPosition.z) * smoothstep(0.0, 0.8, vPosition.y);
        float p1 = smoothstep(0.0, 0.33, uProgress) * (1.0 - smoothstep(0.25, 0.5, uProgress));
        vec3 color1 = vec3(0.0, 0.8, 1.0) * f1 * p1 * 2.5; // Cian
        
        // Fase 2: Limbico (Interior / Centro)
        float f2 = smoothstep(1.5, 0.0, length(vPosition)); // Mayor calor en el nucleo
        float p2 = smoothstep(0.3, 0.66, uProgress) * (1.0 - smoothstep(0.6, 0.85, uProgress));
        vec3 color2 = vec3(1.0, 0.4, 0.0) * f2 * p2 * 3.0; // Naranja calido
        
        // Fase 3: Insula (Nucleo denso y exterior transparente)
        float f3 = smoothstep(0.8, 0.0, length(vPosition)); // Muy concentrado en el origen
        float p3 = smoothstep(0.6, 1.0, uProgress);
        vec3 color3 = vec3(0.7, 0.0, 1.0) * f3 * p3 * 5.0; // Violeta neon
        
        vec3 finalColor = baseColor + color1 + color2 + color3;
        
        // Animacion del pulso basada en ruido
        float pulse = sin(uTime * 2.0 + vPosition.y * 5.0) * 0.15 + 0.85;
        finalColor *= pulse;
        
        // Fase 3 Transparencia X-Ray
        float alpha = 1.0;
        float viewFactor = abs(dot(normalize(vNormal), vec3(0.0, 0.0, 1.0)));
        // Hacemos los bordes (Fresnel) invisibles y el nucleo mas opaco en fase 3
        alpha = mix(1.0, f3 + viewFactor * 0.2, p3);
        
        gl_FragColor = vec4(finalColor, alpha);
      }
    `;
    
    const mat = new THREE.ShaderMaterial({
      vertexShader: vShader,
      fragmentShader: fShader,
      uniforms: brainUniforms,
      transparent: true,
      depthWrite: true,
      side: THREE.DoubleSide
    });
    
    const brainMesh = new THREE.Mesh(geo, mat);
    window.brainPivot = new THREE.Group();
    window.brainPivot.add(brainMesh);
    brainScene.add(window.brainPivot);
    
    // 5. CSS2D Labels
    if (css2DRenderer) {
        function createLabel(text, id) {
            const div = document.createElement('div');
            div.id = id;
            div.className = 'brain-label';
            div.innerHTML = text;
            div.style.opacity = '0';
            div.style.transition = 'opacity 0.5s ease';
            const label = new THREE.CSS2DObject(div);
            return label;
        }
        
        // Label 1 (Prefrontal)
        const l1 = createLabel('<b>Fase 1: Prefrontal</b><br>Adrenalina', 'b-label-1');
        l1.position.set(0.5, 0.8, 1.0);
        window.brainPivot.add(l1);
        
        // Label 2 (Limbico)
        const l2 = createLabel('<b>Fase 2: Límbico</b><br>Dopamina', 'b-label-2');
        l2.position.set(-0.8, 0.2, 0.0);
        window.brainPivot.add(l2);
        
        // Label 3 (Insula)
        const l3 = createLabel('<b>Fase 3: Ínsula</b><br>Oxitocina', 'b-label-3');
        l3.position.set(0.0, -0.5, 0.0);
        window.brainPivot.add(l3);
    }
    
    // 6. Post-Processing (Bloom)
    if (typeof THREE.EffectComposer !== 'undefined') {
      window.brainComposer = new THREE.EffectComposer(brainRenderer);
      window.brainComposer.addPass(new THREE.RenderPass(brainScene, brainCam));
      const bloom = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.5, 0.4, 0.1);
      window.brainComposer.addPass(bloom);
    }
    
    window.addEventListener('resize', () => {
      brainCam.aspect = window.innerWidth / window.innerHeight;
      brainCam.updateProjectionMatrix();
      brainRenderer.setSize(window.innerWidth, window.innerHeight);
      if (css2DRenderer) css2DRenderer.setSize(window.innerWidth, window.innerHeight);
      if (window.brainComposer) window.brainComposer.setSize(window.innerWidth, window.innerHeight);
    });
  })();
"""
loop_marker = '  (function loop() {'
base = base.replace(loop_marker, BRAIN_CODE + '\n' + loop_marker)

# 5. Inject Render update inside the loop
old_render = '    renderer.render(scene, camera);'
new_render = """    renderer.render(scene, camera);
    
    // ==== BRAIN RENDER ====
    brainUniforms.uTime.value = t;
    if (brainRenderer && brainScene && window.brainPivot && window.brainPivot.visible) {
        if (window.brainComposer) {
            window.brainComposer.render();
        } else {
            brainRenderer.render(brainScene, brainCam);
        }
        if (css2DRenderer) css2DRenderer.render(brainScene, brainCam);
    }
"""
base = base.replace(old_render, new_render)

# 6. Inject logic in smoothScrollLoop for prog > 16.0
old_scroll_update = '        scrollTl.progress(Math.min(1, prog / 2.2));'
new_scroll_update = """        scrollTl.progress(Math.min(1, prog / 2.2));
        
        // ==== BRAIN PROGRESS LOGIC ====
        if (prog >= 16.0) {
            if (brainCanvasEl) brainCanvasEl.style.opacity = '1';
            if (window.brainPivot) window.brainPivot.visible = true;
            
            // Map scroll prog (16.0 -> 20.0) to uProgress (0.0 -> 1.0)
            const bProg = Math.max(0, Math.min(1, (prog - 16.0) / 4.0));
            brainUniforms.uProgress.value = bProg;
            
            // Camera / Object Rotation logic
            // Fase 1: 3/4
            // Fase 2: Zenital
            // Fase 3: Frontal
            let tRY, tRX;
            if (bProg <= 0.33) { 
                tRY = -0.6; tRX = 0.2; 
            } else if (bProg <= 0.66) { 
                tRY = 0.0; tRX = 1.0; 
            } else { 
                tRY = 0.0; tRX = 0.0; 
            }
            if (window.brainPivot) {
                window.brainPivot.rotation.y += (tRY - window.brainPivot.rotation.y) * 0.05;
                window.brainPivot.rotation.x += (tRX - window.brainPivot.rotation.x) * 0.05;
            }
            
            // Labels
            const l1 = document.getElementById('b-label-1');
            const l2 = document.getElementById('b-label-2');
            const l3 = document.getElementById('b-label-3');
            if (l1) l1.style.opacity = (bProg > 0.05 && bProg < 0.4) ? '1' : '0';
            if (l2) l2.style.opacity = (bProg > 0.35 && bProg < 0.7) ? '1' : '0';
            if (l3) l3.style.opacity = (bProg > 0.68) ? '1' : '0';
            
        } else {
            if (brainCanvasEl) brainCanvasEl.style.opacity = '0';
        }
"""
base = base.replace(old_scroll_update, new_scroll_update)

# 7. Add CSS for labels
CSS = """
<style>
  .brain-label {
    background: rgba(10, 15, 10, 0.75);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 10px 15px;
    border-radius: 8px;
    color: white;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    line-height: 1.4;
    box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    pointer-events: none;
    text-align: left;
  }
  .brain-label b { font-weight: 700; font-size: 14px; letter-spacing: 0.5px; }
  #b-label-1 b { color: #00d2ff; }
  #b-label-2 b { color: #ff8c00; }
  #b-label-3 b { color: #b700ff; }
</style>
"""
base = base.replace('</head>', CSS + '\n</head>')

with open('3d-test.html','w',encoding='utf-8') as f: f.write(base)
print("Build successful.")
