import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Geometry detail
text = re.sub(r'new THREE\.IcosahedronGeometry\(R,\s*\d+\)', 'new THREE.IcosahedronGeometry(R, 64)', text)

# 2. Update Shaders
new_vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vPosition;

      // Simplex 3D Noise
      vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x, 289.0);}
      vec4 taylorInvSqrt(vec4 r){return 1.79284291400159 - 0.85373472095314 * r;}
      float snoise(vec3 v){ 
        const vec2  C = vec2(1.0/6.0, 1.0/3.0) ;
        const vec4  D = vec4(0.0, 0.5, 1.0, 2.0);
        vec3 i  = floor(v + dot(v, C.yyy) );
        vec3 x0 = v - i + dot(i, C.xxx) ;
        vec3 g = step(x0.yzx, x0.xyz);
        vec3 l = 1.0 - g;
        vec3 i1 = min( g.xyz, l.zxy );
        vec3 i2 = max( g.xyz, l.zxy );
        vec3 x1 = x0 - i1 + 1.0 * C.xxx;
        vec3 x2 = x0 - i2 + 2.0 * C.xxx;
        vec3 x3 = x0 - 1.0 + 3.0 * C.xxx;
        i = mod(i, 289.0 ); 
        vec4 p = permute( permute( permute( 
                   i.z + vec4(0.0, i1.z, i2.z, 1.0 ))
                 + i.y + vec4(0.0, i1.y, i2.y, 1.0 )) 
                 + i.x + vec4(0.0, i1.x, i2.x, 1.0 ));
        float n_ = 1.0/7.0;
        vec3  ns = n_ * D.wyz - D.xzx;
        vec4 j = p - 49.0 * floor(p * ns.z *ns.z);
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
        vUv = uv;
        vec3 pos = position;
        
        // 1. Dar forma ovalada
        pos.x *= 0.8;
        pos.z *= 1.15;
        pos.y *= 0.9;
        
        // 2. Cisura interhemisférica (hundir el centro)
        float distToCenter = abs(pos.x);
        float fissure = smoothstep(0.0, 0.4, distToCenter);
        pos.y -= (1.0 - fissure) * 0.4;
        pos.z += (1.0 - fissure) * 0.1;
        
        // 3. Circunvoluciones (Surcos y giros) usando ruido en múltiples frecuencias
        // Ridged noise
        float n1 = 1.0 - abs(snoise(pos * 3.0));
        float n2 = snoise(pos * 6.0 + uTime * 0.1);
        float n3 = snoise(pos * 12.0);
        
        // Combinación orgánica
        float displacement = (n1 * 0.15) + (n2 * 0.05) + (n3 * 0.02);
        
        // Reducir ruido en la cisura
        displacement *= fissure;
        
        // Fase 3 transicion: contraccion del envoltorio
        float contract = smoothstep(0.6, 1.0, uProgress);
        vec3 finalPos = pos + normal * displacement;
        finalPos = mix(finalPos, finalPos * 0.85, contract);
        
        vPosition = finalPos;
        
        // Calcular normales aproximadas (idealmente deberia ser derivado, pero aproximo)
        vNormal = normalize(normal + vec3(n2*0.1, n1*0.1, n3*0.1));
        
        gl_Position = projectionMatrix * modelViewMatrix * vec4(finalPos, 1.0);
      }
"""

new_fShader = """
      uniform float uProgress;
      uniform float uTime;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vPosition;

      void main() {
        // Fresnel (Rim light) para el borde del cerebro
        vec3 viewDir = normalize(cameraPosition - vPosition);
        float fresnel = pow(1.0 - max(dot(viewDir, vNormal), 0.0), 1.5);
        
        // Base Color: Holographic dark blue
        vec3 baseColor = vec3(0.02, 0.05, 0.15);
        vec3 rimColor = vec3(0.0, 0.5, 1.0) * fresnel * 0.8;
        
        vec3 finalColor = baseColor + rimColor;

        // Fases del Heatmap
        // Fase 1: Prefrontal (Cian)
        float pfZone = smoothstep(0.5, 1.5, vPosition.z) * smoothstep(0.0, 0.8, vPosition.y);
        vec3 pfColor = vec3(0.0, 0.8, 1.0) * pfZone * 2.0;
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.5, uProgress);

        // Fase 2: Límbico (Naranja/Rojo central)
        float limZone = smoothstep(1.0, 0.0, length(vPosition - vec3(0.0, -0.2, 0.0)));
        vec3 limColor = vec3(1.0, 0.3, 0.0) * limZone * 2.5;
        // Pulso
        limColor *= 0.8 + 0.2 * sin(uTime * 5.0);
        float w2 = smoothstep(0.35, 0.5, uProgress) - smoothstep(0.65, 0.8, uProgress);

        // Fase 3: Ínsula / Global (Violeta energético)
        float insZone = smoothstep(0.2, 1.2, abs(vPosition.x)) * smoothstep(-0.5, 0.5, vPosition.y);
        vec3 insColor = vec3(0.6, 0.0, 1.0) * insZone * 2.0;
        float w3 = smoothstep(0.68, 0.85, uProgress);

        finalColor += (pfColor * w1) + (limColor * w2) + (insColor * w3);
        
        // Aumentar la intensidad global con uProgress para el climax
        finalColor *= 1.0 + (w3 * 0.5);

        gl_FragColor = vec4(finalColor, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# 3. Restore EffectComposer for Bloom and set background color to black
text = text.replace('background-color: rgba(255, 0, 0, 0.1);', 'background-color: #0b0c10;')
text = text.replace('background-color: transparent;', 'background-color: #0b0c10;')

old_render = """        // Force direct render to avoid EffectComposer transparency issues
        window.brainRenderer.render(window.brainScene, window.brainCam);"""
new_render = """        if (window.brainComposer) {
            window.brainComposer.render();
        } else {
            window.brainRenderer.render(window.brainScene, window.brainCam);
        }"""
text = text.replace(old_render, new_render)

# Make sure the EffectComposer code is initialized correctly
bloom_init = """      const renderScene = new THREE.RenderPass(window.brainScene, window.brainCam);
      const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.2, 0.4, 0.2);
      window.brainComposer.addPass(renderScene);
      window.brainComposer.addPass(bloomPass);"""

if 'bloomPass' not in text:
    old_init = "window.brainComposer = new THREE.EffectComposer(window.brainRenderer);"
    new_init = "window.brainComposer = new THREE.EffectComposer(window.brainRenderer);\n" + bloom_init
    text = text.replace(old_init, new_init)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Shaders and enabled Bloom with solid background.")
