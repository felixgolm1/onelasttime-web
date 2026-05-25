import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Shaders
new_vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vWorldPosition;
      varying float vFold;

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
        
        // 1. FORMA BASE DEL CEREBRO (Bean shape)
        pos.x *= 0.75;
        pos.z *= 1.2;
        pos.y *= 0.85;
        
        // Lóbulo Temporal (Ensanchar ligeramente abajo a los lados)
        float tempLobe = smoothstep(0.4, 0.0, abs(pos.y + 0.2)) * smoothstep(0.0, 0.6, abs(pos.x));
        pos.x += sign(pos.x) * tempLobe * 0.15;
        
        // Fisura Interhemisférica (Corte central)
        float distToCenter = abs(pos.x);
        float fissure = smoothstep(0.0, 0.12, distToCenter);
        pos.y -= (1.0 - fissure) * 0.3;
        pos.z += (1.0 - fissure) * 0.05;
        
        // 2. PLIEGUES (Gyri / Sulci)
        // Usamos alta frecuencia pero menor desplazamiento para mantener la forma
        vec3 noisePos = pos * 8.0;
        float fold = 1.0 - abs(snoise(noisePos));
        // Afilar los surcos
        fold = smoothstep(0.2, 0.9, fold);
        
        // Suavizar cerca de la fisura
        fold *= smoothstep(0.0, 0.1, distToCenter);
        
        float displacement = fold * 0.07;
        
        vec3 finalPos = pos + normalize(pos) * displacement;
        
        vFold = fold; // Para Ambient Occlusion
        
        // Fase 3 transicion: pequeña contracción al final
        float contract = smoothstep(0.6, 1.0, uProgress);
        finalPos = mix(finalPos, finalPos * 0.9, contract);
        
        vWorldPosition = (modelMatrix * vec4(finalPos, 1.0)).xyz;
        vNormal = normal; 
        gl_Position = projectionMatrix * viewMatrix * vec4(vWorldPosition, 1.0);
      }
"""

new_fShader = """
      #extension GL_OES_standard_derivatives : enable
      
      uniform float uProgress;
      uniform float uTime;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vWorldPosition;
      varying float vFold;

      // PALETA TÉRMICA TIPO ORYZO
      vec3 getThermalColor(float t) {
          vec3 c0 = vec3(0.05, 0.02, 0.15); // Fondo: Azul oscuro / Púrpura muy oscuro
          vec3 c1 = vec3(0.35, 0.0, 0.40);  // Frío: Púrpura brillante
          vec3 c2 = vec3(0.80, 0.1, 0.30);  // Templado: Magenta / Rojo
          vec3 c3 = vec3(1.00, 0.5, 0.00);  // Caliente: Naranja
          vec3 c4 = vec3(1.00, 0.9, 0.20);  // Muy caliente: Amarillo brillante
          vec3 c5 = vec3(1.00, 1.0, 1.00);  // Extremo: Blanco
          
          if (t < 0.2) return mix(c0, c1, t / 0.2);
          if (t < 0.4) return mix(c1, c2, (t - 0.2) / 0.2);
          if (t < 0.6) return mix(c2, c3, (t - 0.4) / 0.2);
          if (t < 0.8) return mix(c3, c4, (t - 0.6) / 0.2);
          return mix(c4, c5, (t - 0.8) / 0.2);
      }

      void main() {
        // Normales por derivadas para sombreado exacto de los pliegues
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 finalNormal = normalize(cross(dx, dy));
        
        // SISTEMA DE CALOR (Heatmap)
        float heat = 0.0;
        
        // Fase 1: Prefrontal (Frente)
        float pfZone = smoothstep(0.2, 1.2, vWorldPosition.z) * smoothstep(-0.2, 0.8, vWorldPosition.y);
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.5, uProgress);
        heat += pfZone * w1 * 0.9;
        
        // Fase 2: Límbico (Centro interno)
        float limZone = smoothstep(0.9, 0.0, length(vWorldPosition - vec3(0.0, -0.1, 0.0)));
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.8, uProgress);
        heat += limZone * w2 * 1.0;
        
        // Fase 3: Ínsula (Global / Laterales)
        float insZone = smoothstep(0.2, 0.9, abs(vWorldPosition.x));
        float w3 = smoothstep(0.68, 0.85, uProgress);
        heat += insZone * w3 * 0.85;
        
        // Pulso orgánico en el calor
        heat += (sin(uTime * 4.0) * 0.05 + 0.05) * max(w1, max(w2, w3));
        
        // El calor no debe exceder 1.0
        heat = clamp(heat, 0.0, 1.0);
        
        // Convertir calor a color térmico
        vec3 baseColor = getThermalColor(heat);
        
        // Oclusión ambiental para los surcos
        float ao = smoothstep(0.1, 0.8, vFold);
        baseColor *= mix(0.4, 1.0, ao); // Oscurecer los surcos profundos
        
        // Iluminación volumétrica suave
        vec3 viewDir = normalize(cameraPosition - vWorldPosition);
        float fresnel = pow(1.0 - max(dot(viewDir, finalNormal), 0.0), 2.5);
        
        // Especular (brillo de tejido húmedo)
        vec3 lightDir = normalize(vec3(1.0, 1.0, 1.0));
        vec3 halfVector = normalize(lightDir + viewDir);
        float spec = pow(max(dot(finalNormal, halfVector), 0.0), 32.0) * 0.3 * ao;
        
        // Añadir brillo de borde (Rim) cálido basado en el calor
        vec3 rimColor = mix(vec3(0.2, 0.0, 0.5), vec3(1.0, 0.5, 0.0), heat);
        
        vec3 finalColor = baseColor + (rimColor * fresnel * 0.5) + vec3(spec);

        gl_FragColor = vec4(finalColor, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# Re-adjust Bloom Settings to ensure it glows like Oryzo but doesn't white out
bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.2, 0.6, 0.5);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

# Set base geometry back to a stable high poly 
text = re.sub(r'new THREE\.IcosahedronGeometry\(R,\s*\d+\)', 'new THREE.IcosahedronGeometry(R, 80)', text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied Oryzo Thermal Heatmap style to the procedural brain.")
