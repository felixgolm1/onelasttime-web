import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# THE CORRECT TECHNIQUE: Ridged FBM (used in VFX for all organic folded surfaces)
# 1 - |snoise(p)| = ridge at zero-crossings, valleys between ridges
# This creates CURVED, WINDING, CONNECTED ridges -- exactly brain gyri
# + Double domain warp = organic, non-parallel

new_vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec3 vWorldPosition;
      varying float vFold;
      varying float vFissure;

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

      // RIDGED FBM: The VFX-standard technique for organic folded surfaces
      // 1-|n| creates ridges at zero-crossings (like mountain ranges, brain gyri)
      float ridgedFBM(vec3 p) {
        // Layer 1: Double domain warp for organic, curvy (non-mechanical) paths
        vec3 q = vec3(
          snoise(p * 1.6 + vec3(0.0, 0.0, 0.0)),
          snoise(p * 1.6 + vec3(5.2, 1.3, 2.8)),
          snoise(p * 1.6 + vec3(2.3, 4.7, 1.1))
        );
        vec3 r = vec3(
          snoise(p * 1.6 + 3.5*q + vec3(1.7, 9.2, 3.4)),
          snoise(p * 1.6 + 3.5*q + vec3(8.3, 2.8, 1.4)),
          snoise(p * 1.6 + 3.5*q + vec3(5.1, 7.3, 4.2))
        );
        // Warped position
        vec3 wp = p + 0.45 * r;

        // PRIMARY GYRI: large, ~0.5-1cm equivalent ridges
        // 1 - |snoise| = ridges at zero-crossings = connected winding ridges
        float g1 = 1.0 - abs(snoise(wp * 2.2));
        g1 = pow(g1, 1.6); // Sharpen peaks, deepen valleys (wider sulci)

        // SECONDARY GYRI: half-size secondary folds inside larger ones
        float g2 = 1.0 - abs(snoise(wp * 4.5 + 1.5));
        g2 = pow(g2, 2.0);

        // TERTIARY TEXTURE: fine surface wrinkles
        float g3 = 1.0 - abs(snoise(wp * 9.0 + 3.0));
        g3 = pow(g3, 2.5);

        // Combine: primary folds dominate, secondary add detail
        return g1 * 0.60 + g2 * 0.28 + g3 * 0.12;
      }

      void main() {
        vec3 pos = position;

        // ── ANATOMICAL SHAPE (matches reference image) ─────────────────
        pos.x *= 0.80;   // narrower side-to-side
        pos.z *= 1.22;   // elongated front-to-back (temporal-occipital axis)
        pos.y *= 0.86;   // slightly flattened superior-inferior

        // More pronounced flattening of inferior surface
        if (pos.y < 0.0) {
          float flattenFactor = 1.0 - 0.30 * (-pos.y);
          pos.y *= flattenFactor;
          pos.x *= 1.0 + 0.08 * (-pos.y); // temporal lobes wider below
        }

        // Slight frontal flattening (anterior face of brain is more vertical)
        if (pos.z > 0.5) {
          pos.z = 0.5 + (pos.z - 0.5) * 0.85;
        }

        // ── INTERHEMISPHERIC FISSURE ────────────────────────────────────
        float distCenter = abs(pos.x);
        // The fissure is deep at the top (y > 0), disappearing at base
        float topFactor = smoothstep(-0.1, 0.8, pos.y);
        float fissureDepth = (1.0 - smoothstep(0.0, 0.13, distCenter)) * topFactor;
        vFissure = fissureDepth;

        pos.y -= fissureDepth * 0.28;

        // ── GYRI / SULCI (Ridged FBM) ───────────────────────────────────
        float gyri = ridgedFBM(pos * 1.9);

        // Zero out inside fissure
        gyri *= (1.0 - fissureDepth * 0.9);

        // Displacement (0.12 = 12% of radius = realistic fold depth)
        vec3 finalPos = pos + normalize(pos) * gyri * 0.12;

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

      vec3 thermal(float t) {
        t = clamp(t, 0.0, 1.0);
        // Oryzo palette: dark purple -> purple -> magenta -> orange -> yellow
        vec3 c0 = vec3(0.04, 0.01, 0.12);
        vec3 c1 = vec3(0.30, 0.00, 0.50);
        vec3 c2 = vec3(0.72, 0.06, 0.44);
        vec3 c3 = vec3(1.00, 0.38, 0.00);
        vec3 c4 = vec3(1.00, 0.88, 0.10);
        if (t < 0.25) return mix(c0, c1, t / 0.25);
        if (t < 0.50) return mix(c1, c2, (t - 0.25) / 0.25);
        if (t < 0.75) return mix(c2, c3, (t - 0.50) / 0.25);
        return mix(c3, c4, (t - 0.75) / 0.25);
      }

      void main() {
        // Per-pixel normals from screen derivatives (correctly lights every gyrus)
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 N = normalize(cross(dx, dy));
        vec3 V = normalize(cameraPosition - vWorldPosition);

        // Three-point lighting setup
        vec3 L1 = normalize(vec3(1.0, 2.0, 1.5));   // Key: upper front right
        vec3 L2 = normalize(vec3(-1.5, 0.5, 0.5));  // Fill: left
        vec3 L3 = normalize(vec3(0.0, -1.0, -1.0)); // Back/rim

        float d1 = max(dot(N, L1), 0.0);
        float d2 = max(dot(N, L2), 0.0) * 0.20;
        float d3 = max(dot(N, L3), 0.0) * 0.10;
        float ambient = 0.25;
        float shading = d1 * 0.65 + d2 + d3 + ambient;

        // Soft specular on gyri ridges only
        vec3 H = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 48.0) * 0.20 * vFold;

        // Ambient Occlusion
        // Gyri ridges = bright, sulci valleys = dark
        float ao = mix(0.05, 1.0, pow(vFold, 0.7));
        // Fissure = very dark
        ao *= mix(0.05, 1.0, 1.0 - vFissure);

        // ── HEAT MAP ────────────────────────────────────────────────────
        float heat = 0.0;

        // Phase 1: Prefrontal cortex (front, top)
        float pfZone = smoothstep(-0.05, 1.0, vWorldPosition.z) * smoothstep(-0.2, 0.85, vWorldPosition.y);
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.52, uProgress);

        // Phase 2: Limbic (inner / central mass)
        float limZone = 1.0 - smoothstep(0.0, 1.05, length(vWorldPosition));
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.82, uProgress);

        // Phase 3: Insula / full cortex
        float insZone = smoothstep(0.1, 0.9, abs(vWorldPosition.x)) + 0.4 * smoothstep(0.3, 1.0, vFold);
        float w3 = smoothstep(0.68, 0.85, uProgress);

        heat += pfZone * w1;
        heat += limZone * w2;
        heat += insZone * w3 * 0.85;
        heat += 0.035 * sin(uTime * 5.0) * max(w1, max(w2, w3));
        heat = clamp(heat, 0.0, 1.0);

        // Color
        vec3 col = thermal(heat);
        col = col * shading * ao + vec3(spec);

        // Rim / SSS fake: warm glow on lit edges
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 2.2);
        vec3 rimCol = mix(vec3(0.20, 0.0, 0.50), vec3(1.0, 0.45, 0.0), heat);
        col += rimCol * fresnel * 0.40;

        gl_FragColor = vec4(col, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# Moderate bloom
bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.60, 0.35, 0.60);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Ridged FBM gyri shader applied.")
