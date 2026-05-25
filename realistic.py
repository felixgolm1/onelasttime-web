import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Geometry detail to 96 (a sweet spot for high poly without crashing)
text = re.sub(r'new THREE\.IcosahedronGeometry\(R,\s*\d+\)', 'new THREE.IcosahedronGeometry(R, 96)', text)

# 2. Update Shaders for Realistic Fleshy Brain
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
        
        // 1. FORMA ANATÓMICA REALISTA (Cerebrum + Cerebellum hint)
        // Escala base ovalada
        pos.x *= 0.72; // Estrecho de frente
        pos.z *= 1.25; // Alargado de perfil
        pos.y *= 0.85; // Ligeramente achatado arriba
        
        // Ensanchar la parte trasera (Lóbulo parietal/occipital)
        if (pos.z < 0.0) {
            pos.x *= 1.0 + abs(pos.z) * 0.2;
        }
        
        // Hundir la parte inferior frontal y abultar temporal
        if (pos.y < 0.0) {
            pos.y -= 0.15 * smoothstep(0.0, 1.0, abs(pos.x));
        }

        // 2. CISURA INTERHEMISFÉRICA
        float distToCenter = abs(pos.x);
        float fissure = smoothstep(0.01, 0.15, distToCenter);
        // Profundizar la fisura central
        pos.y -= (1.0 - fissure) * 0.35;
        pos.z += (1.0 - fissure) * 0.05;
        
        // 3. CIRCUNVOLUCIONES (Gyri y Sulci realistas)
        // Generamos un patrón tipo 'tubular' o de gusanos usando ruido invertido
        // Alta frecuencia para los pliegues
        vec3 noisePos = pos * 4.5;
        // Distorsionamos el espacio para que los pliegues no sean tan uniformes
        noisePos += vec3(snoise(pos * 2.0), snoise(pos * 2.5 + 1.0), snoise(pos * 2.2 + 2.0)) * 0.5;
        
        float fold1 = 1.0 - abs(snoise(noisePos));
        float fold2 = 1.0 - abs(snoise(noisePos * 2.0));
        
        // Combinamos las frecuencias para darle variabilidad a los pliegues
        float fold = fold1 * 0.75 + fold2 * 0.25;
        
        // Hacemos que los "picos" sean anchos y redondeados, y los valles profundos y estrechos
        fold = smoothstep(0.1, 0.8, fold);
        
        // Suavizar los pliegues cerca de la fisura central para mayor realismo
        fold *= smoothstep(0.0, 0.2, distToCenter);
        
        // Aplicar el desplazamiento
        float displacement = fold * 0.18; // Profundidad de los surcos
        
        vec3 finalPos = pos + normalize(pos) * displacement;
        
        // Guardamos el nivel de pliegue para calcular Ambient Occlusion en el fragment shader
        vFold = fold;
        
        // Fase 3 transicion: contraccion del envoltorio
        float contract = smoothstep(0.6, 1.0, uProgress);
        finalPos = mix(finalPos, finalPos * 0.85, contract);
        
        vWorldPosition = (modelMatrix * vec4(finalPos, 1.0)).xyz;
        vNormal = normal; // Fallback, usaremos dFdx en Fragment
        gl_Position = projectionMatrix * viewMatrix * vec4(vWorldPosition, 1.0);
      }
"""

new_fShader = """
      // Enable Standard Derivatives to compute perfect normals from displaced geometry
      #extension GL_OES_standard_derivatives : enable
      
      uniform float uProgress;
      uniform float uTime;
      varying vec2 vUv;
      varying vec3 vNormal;
      varying vec3 vWorldPosition;
      varying float vFold;

      void main() {
        // Calcular Normales Reales del modelo desplazado proceduralmente
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 normal = normalize(cross(dx, dy));
        
        // Suavizar un poco las normales para un look mas orgánico
        // (Mezclando la normal geométrica con la normal calculada)
        // vec3 finalNormal = normalize(mix(normal, vNormal, 0.2));
        vec3 finalNormal = normal;

        vec3 viewDir = normalize(cameraPosition - vWorldPosition);
        
        // 1. ILUMINACIÓN Y MATERIAL (Carne realista)
        // Colores base basados en referencias médicas (Rosa carne, Rojo oscuro)
        vec3 fleshColor = vec3(0.85, 0.55, 0.50);
        vec3 creviceColor = vec3(0.20, 0.05, 0.05); // Sombras de los surcos (Sulci)
        
        // Oclusión Ambiental (Ambient Occlusion) basada en la profundidad del pliegue
        float ao = smoothstep(0.0, 0.7, vFold);
        vec3 baseColor = mix(creviceColor, fleshColor, ao);
        
        // Iluminación Direccional (Luz principal y luz de relleno)
        vec3 lightDir1 = normalize(vec3(1.0, 1.0, 1.0));
        vec3 lightDir2 = normalize(vec3(-1.0, 0.5, -0.5));
        
        float diff1 = max(dot(finalNormal, lightDir1), 0.0);
        float diff2 = max(dot(finalNormal, lightDir2), 0.0) * 0.5;
        
        // Iluminación ambiental base
        float ambient = 0.3;
        
        // Reflejos especulares (Look húmedo/orgánico)
        vec3 halfVector = normalize(lightDir1 + viewDir);
        float spec = pow(max(dot(finalNormal, halfVector), 0.0), 64.0) * 0.4 * ao; // Solo brilla en la cima de los giros
        
        vec3 shading = baseColor * (diff1 + diff2 + ambient) + vec3(spec);
        
        // Rim light suave (Subsurface scattering fake)
        float fresnel = pow(1.0 - max(dot(viewDir, finalNormal), 0.0), 3.0);
        shading += vec3(0.9, 0.3, 0.3) * fresnel * 0.3 * ao;

        vec3 finalColor = shading;

        // 2. HEATMAPS (Colores superpuestos por uProgress)
        // En lugar de sustituir, añadimos un resplandor "energético"
        
        // Fase 1: Prefrontal (Cian)
        float pfZone = smoothstep(0.5, 1.5, vWorldPosition.z) * smoothstep(0.0, 0.8, vWorldPosition.y);
        vec3 pfColor = vec3(0.0, 0.9, 1.0) * pfZone * 2.0;
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.5, uProgress);

        // Fase 2: Límbico (Naranja/Amarillo brillante interno)
        float limZone = smoothstep(1.0, 0.0, length(vWorldPosition - vec3(0.0, -0.2, 0.0)));
        vec3 limColor = vec3(1.0, 0.6, 0.0) * limZone * 3.0;
        limColor *= 0.8 + 0.2 * sin(uTime * 6.0); // Pulso rápido
        float w2 = smoothstep(0.35, 0.5, uProgress) - smoothstep(0.65, 0.8, uProgress);

        // Fase 3: Ínsula / Cerebro Completo (Violeta radiante)
        float insZone = smoothstep(0.2, 1.2, abs(vWorldPosition.x)) * smoothstep(-0.5, 0.5, vWorldPosition.y);
        vec3 insColor = vec3(0.7, 0.0, 1.0) * insZone * 2.5;
        float w3 = smoothstep(0.68, 0.85, uProgress);

        // Aplicamos el heatmap como capa de luz (Additive blending)
        vec3 glowLayer = (pfColor * w1) + (limColor * w2) + (insColor * w3);
        finalColor += glowLayer;
        
        // Oscurecer ligeramente la carne cuando el glow está activo para mayor contraste
        float totalGlow = min(1.0, (pfZone * w1) + (limZone * w2) + (insZone * w3));
        finalColor = mix(finalColor, finalColor * 0.5 + glowLayer * 1.5, totalGlow);

        gl_FragColor = vec4(finalColor, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# Tweak Bloom settings so the flesh doesn't blow out, only the neon glow
bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.8, 0.3, 0.8);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

# Remove the red tint background
text = text.replace('background-color: rgba(255, 0, 0, 0.1);', 'background-color: transparent;')
text = text.replace('background-color: #0b0c10;', 'background-color: transparent;')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated shaders for ultra-realistic procedural brain.")
