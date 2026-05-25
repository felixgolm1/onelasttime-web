import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# KEY INSIGHT: To make gyri (worm-like brain folds), we need:
# 1. Domain Warping: distort the noise input space first
# 2. "Voronoi-like" ridged noise: creates elongated cell boundaries
# 3. High displacement with sharper ridge peaks

new_vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vWorldPosition;
      varying float vFold;
      varying float vFoldDepth;

      // Simplex 3D Noise
      vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x, 289.0);}
      vec4 taylorInvSqrt(vec4 r){return 1.79284291400159 - 0.85373472095314 * r;}
      float snoise(vec3 v){ 
        const vec2  C = vec2(1.0/6.0, 1.0/3.0);
        const vec4  D = vec4(0.0, 0.5, 1.0, 2.0);
        vec3 i  = floor(v + dot(v, C.yyy));
        vec3 x0 = v - i + dot(i, C.xxx);
        vec3 g = step(x0.yzx, x0.xyz);
        vec3 l = 1.0 - g;
        vec3 i1 = min(g.xyz, l.zxy);
        vec3 i2 = max(g.xyz, l.zxy);
        vec3 x1 = x0 - i1 + C.xxx;
        vec3 x2 = x0 - i2 + C.yyy;
        vec3 x3 = x0 - D.yyy;
        i = mod(i, 289.0); 
        vec4 p = permute(permute(permute( 
                   i.z + vec4(0.0, i1.z, i2.z, 1.0))
                 + i.y + vec4(0.0, i1.y, i2.y, 1.0)) 
                 + i.x + vec4(0.0, i1.x, i2.x, 1.0));
        float n_ = 1.0/7.0;
        vec3 ns = n_ * D.wyz - D.xzx;
        vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
        vec4 x_ = floor(j * ns.z);
        vec4 y_ = floor(j - 7.0 * x_);
        vec4 x = x_ * ns.x + ns.yyyy;
        vec4 y = y_ * ns.x + ns.yyyy;
        vec4 h = 1.0 - abs(x) - abs(y);
        vec4 b0 = vec4(x.xy, y.xy);
        vec4 b1 = vec4(x.zw, y.zw);
        vec4 s0 = floor(b0) * 2.0 + 1.0;
        vec4 s1 = floor(b1) * 2.0 + 1.0;
        vec4 sh = -step(h, vec4(0.0));
        vec4 a0 = b0.xzyw + s0.xzyw * sh.xxyy;
        vec4 a1 = b1.xzyw + s1.xzyw * sh.zzww;
        vec3 p0 = vec3(a0.xy, h.x);
        vec3 p1 = vec3(a0.zw, h.y);
        vec3 p2 = vec3(a1.xy, h.z);
        vec3 p3 = vec3(a1.zw, h.w);
        vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
        p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
        vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
        m = m * m;
        return 42.0 * dot(m * m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
      }

      // Gyri Pattern: Domain-warped ridged noise to create elongated brain folds
      float gyriNoise(vec3 p) {
        // Domain Warp: first distort the input space for elongated, organic patterns
        vec3 q = vec3(snoise(p + vec3(0.0, 0.0, 0.0)),
                      snoise(p + vec3(5.2, 1.3, 2.1)),
                      snoise(p + vec3(1.7, 9.2, 3.4)));
        vec3 r = vec3(snoise(p + 4.0*q + vec3(1.7, 9.2, 3.4)),
                      snoise(p + 4.0*q + vec3(8.3, 2.8, 1.4)),
                      snoise(p + 4.0*q + vec3(5.1, 7.3, 4.2)));
        
        // The warped position creates elongated streaks (gyri-like)
        float n = snoise(p + 2.0 * r);
        
        // Ridged: convert to 0..1 where 1 = ridge peak (gyrus) and 0 = valley (sulcus)
        return 1.0 - abs(n);
      }

      void main() {
        vUv = uv;
        vec3 pos = position;
        
        // 1. FORMA ANATÓMICA DEL CEREBRO
        // Cerebrum: oval alargado de frente a atrás
        pos.x *= 0.78;
        pos.z *= 1.18;
        pos.y *= 0.82;
        
        // Ensanchar ligeramente los lóbulos parietales
        float latBulge = smoothstep(0.3, 0.8, abs(pos.x)) * smoothstep(-0.5, 0.3, pos.y);
        pos.x += sign(pos.x) * latBulge * 0.08;
        
        // Aplanar la base (no es una esfera perfecta por abajo)
        if (pos.y < 0.0) {
          pos.y *= 0.75;
          // Hundir ligeramente el centro inferior (tronco del encéfalo)
          float trunkFactor = smoothstep(0.4, 0.0, length(pos.xz));
          pos.y -= trunkFactor * 0.15;
        }
        
        // 2. FISURA INTERHEMISFÉRICA (Sulcus central profundo en X=0)
        float distToCenter = abs(pos.x);
        // Suave en los bordes, profunda en el centro
        float fissure = smoothstep(0.0, 0.18, distToCenter);
        pos.y -= (1.0 - fissure) * 0.28;  // Hundir el centro hacia abajo
        pos.z += (1.0 - fissure) * 0.04;  // Ligero empuje hacia atrás en el centro
        
        // 3. SURCO CENTRAL (Sulcus Centralis) - divide frontal del parietal
        float sCenter = exp(-pow((pos.z - 0.1) / 0.12, 2.0)) * exp(-pow(pos.y / 0.7, 2.0));
        sCenter *= fissure; // No aplicar en la fisura central ya existente
        pos.y -= sCenter * 0.08;
        
        // 4. GYRI Y SULCI: Pliegues elongados realistas
        // Usamos frecuencias distintas para gyri grandes (bajos) y mini-pliegues (altos)
        
        // Escalar diferente en cada eje para que los pliegues sean elongados, no redondos
        vec3 gyriPos = pos * vec3(3.0, 4.0, 2.5); // Más frecuencia en Y (giros verticales)
        
        // Multi-octave gyri con bias de elongación
        float gyri1 = gyriNoise(gyriPos * 0.8);
        float gyri2 = gyriNoise(gyriPos * 1.6 + vec3(2.1, 3.7, 1.9)) * 0.5;
        float gyri3 = gyriNoise(gyriPos * 3.2 + vec3(5.3, 1.2, 4.1)) * 0.25;
        
        // Combinar y afilar los picos (para que los gyri tengan cresta definida)
        float gyri = (gyri1 + gyri2 + gyri3) / 1.75;
        // Curva de shaping: aplanar valles, afilar picos
        gyri = smoothstep(0.3, 1.0, gyri);
        gyri = pow(gyri, 0.7); // Ligeramente más planos los picos para mayor realismo
        
        // Reducir pliegues en la fisura central
        gyri *= mix(0.15, 1.0, fissure);
        
        // Desplazamiento
        float displacement = gyri * 0.13;
        
        vec3 finalPos = pos + normalize(pos) * displacement;
        
        vFold = gyri;          // Para AO en el Fragment Shader
        vFoldDepth = fissure;  // Para intensidad de iluminación lateral
        
        vWorldPosition = (modelMatrix * vec4(finalPos, 1.0)).xyz;
        vNormal = normal;
        gl_Position = projectionMatrix * viewMatrix * vec4(vWorldPosition, 1.0);
      }
"""

new_fShader = """
      uniform float uProgress;
      uniform float uTime;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vWorldPosition;
      varying float vFold;
      varying float vFoldDepth;

      // PALETA TÉRMICA TIPO ORYZO (Azul oscuro -> Púrpura -> Magenta -> Naranja -> Amarillo)
      vec3 getThermalColor(float t) {
          // Colores exactos del gradiente de Oryzo
          vec3 c0 = vec3(0.04, 0.01, 0.12); // Frío total: Negro-Púrpura
          vec3 c1 = vec3(0.30, 0.00, 0.50); // Frío: Púrpura
          vec3 c2 = vec3(0.75, 0.05, 0.45); // Templado: Magenta
          vec3 c3 = vec3(1.00, 0.35, 0.00); // Caliente: Naranja
          vec3 c4 = vec3(1.00, 0.88, 0.10); // Muy caliente: Amarillo
          
          t = clamp(t, 0.0, 1.0);
          if (t < 0.25) return mix(c0, c1, t / 0.25);
          if (t < 0.50) return mix(c1, c2, (t - 0.25) / 0.25);
          if (t < 0.75) return mix(c2, c3, (t - 0.50) / 0.25);
          return mix(c3, c4, (t - 0.75) / 0.25);
      }

      void main() {
        vec3 viewDir = normalize(cameraPosition - vWorldPosition);
        
        // Normales en tiempo real (para resaltar los pliegues bajo el heatmap)
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 geoNormal = normalize(cross(dx, dy));
        
        // Iluminación base para que se vea la volumetría 3D aunque no haya calor
        vec3 lightDir = normalize(vec3(1.0, 1.5, 1.0));
        float diff = max(dot(geoNormal, lightDir), 0.0);
        float ambient = 0.25;
        
        // SISTEMA DE CALOR (Heatmap por zonas + scroll progress)
        float heat = 0.0;
        
        // Zona: Prefrontal (lóbulo frontal, hacia +Z)
        float pfZone = smoothstep(-0.1, 1.2, vWorldPosition.z) * smoothstep(-0.5, 0.9, vWorldPosition.y);
        // Zona: Límbico (centro del cerebro)
        float limZone = 1.0 - smoothstep(0.0, 1.1, length(vWorldPosition));
        // Zona: Ínsula / Cortex lateral
        float insZone = smoothstep(0.15, 0.85, abs(vWorldPosition.x));
        
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.5, uProgress);
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.8, uProgress);
        float w3 = smoothstep(0.68, 0.85, uProgress);
        
        heat += pfZone * w1;
        heat += limZone * w2;
        heat += insZone * w3;
        
        // Pulso vivo en las zonas activas
        float pulse = 0.05 * sin(uTime * 5.0) * max(w1, max(w2, w3));
        heat += pulse;
        heat = clamp(heat, 0.0, 1.0);
        
        // Color Térmico
        vec3 thermalColor = getThermalColor(heat);
        
        // Aplicar iluminación SOBRE el color térmico (para preservar profundidad y pliegues)
        float shadingFactor = (diff * 0.6) + ambient;
        
        // Oclusión Ambiental: los surcos se ven más oscuros
        float ao = mix(0.2, 1.0, vFold); // 0 = surco negro, 1 = cresta iluminada
        
        vec3 finalColor = thermalColor * shadingFactor * ao;
        
        // Rim Light (SSS fake): borde brillante con el color de calor o violeta frío
        float fresnel = pow(1.0 - max(dot(viewDir, geoNormal), 0.0), 2.0);
        vec3 rimColor = mix(vec3(0.3, 0.0, 0.6), vec3(1.0, 0.5, 0.0), heat);
        finalColor += rimColor * fresnel * 0.4;
        
        // Brillo especular mínimo en las crestas (no en los sulcos)
        vec3 halfVec = normalize(lightDir + viewDir);
        float spec = pow(max(dot(geoNormal, halfVec), 0.0), 48.0) * 0.25 * vFold;
        finalColor += vec3(spec);

        gl_FragColor = vec4(finalColor, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# Optimize bloom: not too much, just enough glow
bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.7, 0.4, 0.6);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

# Keep resolution at a good level
text = re.sub(r'new THREE\.IcosahedronGeometry\(R,\s*\d+\)', 'new THREE.IcosahedronGeometry(R, 80)', text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied domain-warped gyri shader for realistic brain folds.")
