import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# KEY FIXES vs previous:
# 1. Lower stripe frequency (4-5 vs 7-8) = FEWER, BIGGER gyri
# 2. Better ridge profile: flat wide tops + narrow sharp sulci
# 3. Less warp amplitude = gyri are more parallel/coherent
# 4. Better brain shape - more elongated

new_vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec3 vWorldPosition;
      varying float vFold;
      varying float vFissure;

      // Simplex noise for domain warping
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

      // GYRUS PROFILE: flat wide top + narrow deep sulcus
      // input t = 0..1 (sine wave normalized)
      // output: 1 = gyrus peak,  0 = sulcus valley
      float gyrusProfile(float t) {
        // t = 0..1 (already positive half of sine)
        // We want: values above 0.45 -> pushed to 1 (gyrus surface = flat)
        //          values below 0.45 -> pushed to 0 (sulcus = narrow & deep)
        return smoothstep(0.35, 0.65, t);
      }

      float computeGyri(vec3 p) {
        // Light domain warp (keep gyri somewhat parallel/coherent)
        vec3 warp = vec3(
          snoise(p * 1.2 + vec3(0.0, 0.0, 0.0)),
          snoise(p * 1.2 + vec3(3.7, 1.5, 2.1)),
          snoise(p * 1.2 + vec3(1.2, 4.3, 3.8))
        ) * 0.22; // reduced warp = more parallel gyri
        vec3 wp = p + warp;

        // LOW frequency stripes = BIG, WIDE gyri like real brain
        // freq 4.5 ≈ about 7-8 gyri visible around the brain
        float s1 = (sin(wp.x * 4.5 + wp.y * 1.5) + 1.0) * 0.5; // 0..1
        float s2 = (sin(wp.y * 5.0 + wp.z * 2.0) + 1.0) * 0.5;
        float s3 = (sin(wp.z * 4.0 + wp.x * 1.0) + 1.0) * 0.5;

        // Apply gyrus profile to each stripe
        float g1 = gyrusProfile(s1);
        float g2 = gyrusProfile(s2);
        float g3 = gyrusProfile(s3);

        // Combine: take the minimum across orientations to create the sulci network
        // (sulci appear where ANY direction says there's a valley)
        float gyri = g1 * 0.6 + g2 * 0.3 + g3 * 0.1;
        // Sharpen the sulci: scale so sulci are well-defined
        gyri = smoothstep(0.2, 1.0, gyri);

        return gyri;
      }

      void main() {
        vec3 pos = position;

        // ── ANATOMICAL SHAPE ──────────────────────────────────────────
        pos.x *= 0.80;  // narrow front-view
        pos.z *= 1.25;  // elongated front-to-back
        pos.y *= 0.85;  // slightly flat

        // Flatten the inferior surface more aggressively
        if (pos.y < 0.0) {
          pos.y *= 0.65;
        }

        // Frontal pole: slightly flattened face
        float frontFlatten = smoothstep(0.0, 0.6, pos.z) * smoothstep(0.7, 0.0, abs(pos.x));
        pos.z += frontFlatten * 0.06;

        // Occipital pole: slightly pointed back
        float occipital = smoothstep(0.0, -0.8, pos.z) * smoothstep(0.5, 0.0, abs(pos.x));
        pos.z -= occipital * 0.05;

        // Widen temporal lobes
        float temporal = smoothstep(0.0, 0.5, -pos.y) * smoothstep(0.3, 0.75, abs(pos.x));
        pos.x += sign(pos.x) * temporal * 0.10;

        // ── INTERHEMISPHERIC FISSURE ──────────────────────────────────
        float distCenter = abs(pos.x);
        float topness = smoothstep(0.0, 0.7, pos.y); // only affects the top dome
        float fissure = smoothstep(0.0, 0.14, distCenter);
        vFissure = (1.0 - fissure) * topness;

        pos.y -= vFissure * 0.25;

        // ── GYRI DISPLACEMENT ─────────────────────────────────────────
        float gyri = computeGyri(pos * 1.8);
        gyri *= smoothstep(0.0, 0.12, distCenter); // zero in fissure

        // Larger displacement for more visible folds
        float disp = gyri * 0.14;
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
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 N = normalize(cross(dx, dy));
        vec3 V = normalize(cameraPosition - vWorldPosition);

        // Lighting
        vec3 L1 = normalize(vec3(1.2, 1.8, 1.0));
        vec3 L2 = normalize(vec3(-1.0, 0.3, -0.5));
        float diff1 = max(dot(N, L1), 0.0);
        float diff2 = max(dot(N, L2), 0.0) * 0.25;
        float ambient = 0.22;

        // Specular on gyri ridges
        vec3 H = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 80.0) * 0.3 * vFold;

        // AO: sulci very dark, gyri bright
        float ao = mix(0.08, 1.0, vFold);
        ao = mix(0.02, ao, 1.0 - vFissure); // fissure = black

        // Heat map zones
        float heat = 0.0;
        float pfZone  = smoothstep(-0.1, 1.2, vWorldPosition.z) * smoothstep(-0.3, 0.9, vWorldPosition.y);
        float limZone = 1.0 - smoothstep(0.0, 1.1, length(vWorldPosition));
        float insZone = smoothstep(0.1, 0.8, abs(vWorldPosition.x));

        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.52, uProgress);
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.82, uProgress);
        float w3 = smoothstep(0.68, 0.85, uProgress);

        heat += pfZone * w1;
        heat += limZone * w2;
        heat += insZone * w3;
        heat += 0.04 * sin(uTime * 5.0) * max(w1, max(w2, w3));
        heat = clamp(heat, 0.0, 1.0);

        vec3 col = thermal(heat);
        col *= (diff1 * 0.65 + diff2 + ambient) * ao;
        col += vec3(spec);

        // Rim light
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 2.5);
        vec3 rim = mix(vec3(0.25, 0.0, 0.55), vec3(1.0, 0.5, 0.0), heat);
        col += rim * fresnel * 0.35;

        gl_FragColor = vec4(col, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

# Moderate bloom
bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.65, 0.4, 0.62);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Big wide gyri shader applied.")
