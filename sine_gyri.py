import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# THE CORRECT TECHNIQUE FOR GYRI:
# Brain folds = sinusoidal stripe patterns + domain warping
# sin(freq * warpedPosition) creates parallel worm-like bands -> REAL GYRI
# NOT random noise bumps

new_vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec3 vWorldPosition;
      varying float vFold;
      varying float vFissure;

      // Simplex 3D for domain warping only
      vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x,289.0);}
      vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}
      float snoise(vec3 v){
        const vec2 C=vec2(1.0/6.0,1.0/3.0);
        const vec4 D=vec4(0.0,0.5,1.0,2.0);
        vec3 i=floor(v+dot(v,C.yyy));
        vec3 x0=v-i+dot(i,C.xxx);
        vec3 g=step(x0.yzx,x0.xyz);
        vec3 l=1.0-g;
        vec3 i1=min(g.xyz,l.zxy);
        vec3 i2=max(g.xyz,l.zxy);
        vec3 x1=x0-i1+C.xxx;
        vec3 x2=x0-i2+C.yyy;
        vec3 x3=x0-D.yyy;
        i=mod(i,289.0);
        vec4 p=permute(permute(permute(
          i.z+vec4(0.0,i1.z,i2.z,1.0))
          +i.y+vec4(0.0,i1.y,i2.y,1.0))
          +i.x+vec4(0.0,i1.x,i2.x,1.0));
        float n_=1.0/7.0;
        vec3 ns=n_*D.wyz-D.xzx;
        vec4 j=p-49.0*floor(p*ns.z*ns.z);
        vec4 x_=floor(j*ns.z);
        vec4 y_=floor(j-7.0*x_);
        vec4 x=x_*ns.x+ns.yyyy;
        vec4 y=y_*ns.x+ns.yyyy;
        vec4 h=1.0-abs(x)-abs(y);
        vec4 b0=vec4(x.xy,y.xy);
        vec4 b1=vec4(x.zw,y.zw);
        vec4 s0=floor(b0)*2.0+1.0;
        vec4 s1=floor(b1)*2.0+1.0;
        vec4 sh=-step(h,vec4(0.0));
        vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;
        vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
        vec3 p0=vec3(a0.xy,h.x);
        vec3 p1=vec3(a0.zw,h.y);
        vec3 p2=vec3(a1.xy,h.z);
        vec3 p3=vec3(a1.zw,h.w);
        vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
        p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
        vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);
        m=m*m;
        return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
      }

      // GYRI FUNCTION: Sinusoidal stripes + domain warping = brain folds
      float computeGyri(vec3 p) {
        // STEP 1: Domain warp - distort space so stripes become organic/curvy
        vec3 warp1 = vec3(
          snoise(p * 1.8 + vec3(0.0, 0.0, 0.0)),
          snoise(p * 1.8 + vec3(3.7, 1.5, 2.1)),
          snoise(p * 1.8 + vec3(1.2, 4.3, 3.8))
        );
        // Apply warp to create curvilinear bands
        vec3 wp = p + warp1 * 0.35;
        
        // STEP 2: Sinusoidal stripe patterns in multiple orientations
        // These create the worm-like parallel ridges (gyri)
        // Freq ~7-9 = number of gyri around the brain
        float stripe1 = sin(wp.x * 7.5 + wp.y * 2.0 + wp.z * 1.0);
        float stripe2 = sin(wp.y * 8.0 + wp.z * 3.0 + wp.x * 1.5);
        float stripe3 = sin(wp.z * 6.5 + wp.x * 2.5 + wp.y * 2.0);
        
        // Combine stripes: use abs to turn sine waves into ridges
        // Each abs(sin) = V-shaped valley between each pair of ridges
        float gyri = (abs(stripe1) + abs(stripe2) * 0.5 + abs(stripe3) * 0.3) / 1.8;
        
        // STEP 3: Sharpen the ridges (smooth flat tops, narrow sharp valleys)
        // pow < 1 = rounder peaks; pow > 1 = sharper peaks
        gyri = pow(gyri, 1.4);
        
        // Invert: 1 = RIDGE (gyrus), 0 = VALLEY (sulcus)
        return gyri;
      }

      void main() {
        vec3 pos = position;
        
        // ── ANATOMICAL SHAPE ──────────────────────────────
        // Stretch to bean/oval shape (side profile like reference image)
        pos.x *= 0.78;   // Narrow from front
        pos.z *= 1.22;   // Elongate front-to-back
        pos.y *= 0.84;   // Slightly flat top-bottom
        
        // Flatten the base (inferior surface is flatter than superior)
        if (pos.y < 0.0) {
          pos.y *= 0.70;
          // Create the frontal and occipital poles (slight pinching)
          float poleShape = 1.0 - 0.15 * exp(-pow(abs(pos.z) - 0.9, 2.0) * 8.0);
          pos.x *= poleShape;
        }
        
        // Widen temporal lobes (middle lateral areas)
        float tempBulge = smoothstep(0.0, 0.6, -pos.y) * smoothstep(0.2, 0.7, abs(pos.x));
        pos.x += sign(pos.x) * tempBulge * 0.12;
        
        // ── INTERHEMISPHERIC FISSURE (deep central split) ──
        float distCenter = abs(pos.x);
        float fissure = smoothstep(0.0, 0.16, distCenter);
        vFissure = 1.0 - fissure;
        
        // Deep longitudinal fissure along the top
        float topFactor = smoothstep(0.0, 0.8, pos.y); // Only affects the top
        pos.y -= (1.0 - fissure) * 0.30 * topFactor;
        
        // ── GYRI / SULCI DISPLACEMENT ────────────────────
        float gyri = computeGyri(pos * 2.0); // Scale controls density
        
        // Zero out gyri inside the fissure
        gyri *= fissure;
        
        // Displacement along vertex normal
        float disp = gyri * 0.10;
        
        vec3 finalPos = pos + normalize(pos) * disp;
        
        vFold = gyri;
        
        vWorldPosition = (modelMatrix * vec4(finalPos, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * vec4(vWorldPosition, 1.0);
      }
"""

new_fShader = """
      uniform float uProgress;
      uniform float uTime;
      varying vec3 vWorldPosition;
      varying float vFold;
      varying float vFissure;

      // Oryzo Thermal Palette
      vec3 thermal(float t) {
        t = clamp(t, 0.0, 1.0);
        vec3 c0 = vec3(0.03, 0.01, 0.10);
        vec3 c1 = vec3(0.28, 0.00, 0.48);
        vec3 c2 = vec3(0.72, 0.05, 0.42);
        vec3 c3 = vec3(1.00, 0.38, 0.00);
        vec3 c4 = vec3(1.00, 0.90, 0.10);
        if (t < 0.25) return mix(c0, c1, t / 0.25);
        if (t < 0.50) return mix(c1, c2, (t - 0.25) / 0.25);
        if (t < 0.75) return mix(c2, c3, (t - 0.50) / 0.25);
        return mix(c3, c4, (t - 0.75) / 0.25);
      }

      void main() {
        // Per-pixel normals from screen-space derivatives (correct lighting on gyri)
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 N = normalize(cross(dx, dy));
        
        vec3 viewDir = normalize(cameraPosition - vWorldPosition);
        
        // Key light from upper-front-right
        vec3 L1 = normalize(vec3(1.2, 1.5, 1.0));
        // Fill light from left
        vec3 L2 = normalize(vec3(-1.0, 0.5, 0.0));
        
        float diff1 = max(dot(N, L1), 0.0);
        float diff2 = max(dot(N, L2), 0.0) * 0.3;
        float ambient = 0.20;
        float shading = diff1 * 0.65 + diff2 + ambient;
        
        // Specular (wet organic tissue)
        vec3 H = normalize(L1 + viewDir);
        float spec = pow(max(dot(N, H), 0.0), 60.0) * 0.25 * vFold;
        
        // AO: sulci darker, gyri brighter
        float ao = mix(0.15, 1.0, vFold);
        // Fissure is always dark
        ao = mix(0.05, ao, 1.0 - vFissure);
        
        // HEATMAP
        float heat = 0.0;
        // Phase 1: Prefrontal
        float pfZ  = smoothstep(-0.2, 1.1, vWorldPosition.z);
        float pfY  = smoothstep(-0.4, 0.9, vWorldPosition.y);
        float pfZone  = pfZ * pfY;
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.52, uProgress);
        heat += pfZone * w1;
        
        // Phase 2: Limbic (center mass)
        float limZone = 1.0 - smoothstep(0.0, 1.2, length(vWorldPosition));
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.82, uProgress);
        heat += limZone * w2;
        
        // Phase 3: Insula / lateral cortex
        float insZone = smoothstep(0.1, 0.8, abs(vWorldPosition.x));
        float w3 = smoothstep(0.68, 0.85, uProgress);
        heat += insZone * w3;
        
        // Alive pulse
        float pulse = 0.04 * sin(uTime * 5.0) * max(w1, max(w2, w3));
        heat = clamp(heat + pulse, 0.0, 1.0);
        
        // Base color: cool dark purple when no heat
        vec3 col = thermal(heat);
        col *= shading * ao;
        col += vec3(spec);
        
        // Rim light — warm edge on hot zones, cool on cold
        float fresnel = pow(1.0 - max(dot(viewDir, N), 0.0), 2.5);
        vec3 rim = mix(vec3(0.25, 0.0, 0.55), vec3(1.0, 0.5, 0.0), heat);
        col += rim * fresnel * 0.35;

        gl_FragColor = vec4(col, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# Bloom: subtle, just enough for warmth
bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.6, 0.4, 0.65);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Sinusoidal gyri shader applied.")
