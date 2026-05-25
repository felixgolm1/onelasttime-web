import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# ── VERTEX SHADER ────────────────────────────────────────────────────────────
vShader = """
      uniform float uTime;
      uniform float uProgress;
      varying vec3 vWorldPos;
      varying float vNoise;
      varying float vFissure;

      // ── SIMPLEX 3D ────────────────────────────────────────────────────────
      vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x,289.0);}
      vec4 tiSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}
      float snoise(vec3 v){
        const vec2 C=vec2(1./6.,1./3.);const vec4 D=vec4(0.,.5,1.,2.);
        vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);
        vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.-g;
        vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);
        vec3 x1=x0-i1+C.x;vec3 x2=x0-i2+C.y;vec3 x3=x0-D.y;
        i=mod(i,289.);
        vec4 p=permute(permute(permute(i.z+vec4(0.,i1.z,i2.z,1.))
          +i.y+vec4(0.,i1.y,i2.y,1.))+i.x+vec4(0.,i1.x,i2.x,1.));
        float n_=1./7.;vec3 ns=n_*D.wyz-D.xzx;
        vec4 j=p-49.*floor(p*ns.z*ns.z);
        vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.*x_);
        vec4 xs=x_*ns.x+ns.yyyy;vec4 ys=y_*ns.x+ns.yyyy;
        vec4 h=1.-abs(xs)-abs(ys);
        vec4 b0=vec4(xs.xy,ys.xy);vec4 b1=vec4(xs.zw,ys.zw);
        vec4 s0=floor(b0)*2.+1.;vec4 s1=floor(b1)*2.+1.;
        vec4 sh=-step(h,vec4(0.));
        vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
        vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);
        vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);
        vec4 norm=tiSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
        p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
        vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.);
        m=m*m;return 42.*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
      }

      // ── RIDGED MULTI-FRACTAL NOISE ────────────────────────────────────────
      // Produces tubular ridge networks (gyri) not random bumps
      float ridgedMF(vec3 p, int octaves) {
        float result  = 0.0;
        float amp     = 0.5;
        float freq    = 1.0;
        float weight  = 1.0;
        // Domain warp to make ridges organic/curvy (not straight lines)
        vec3 q = vec3(snoise(p + vec3(0.0)),
                      snoise(p + vec3(5.2, 1.3, 2.8)),
                      snoise(p + vec3(1.7, 9.2, 3.4)));
        p += q * 0.3;

        for (int i = 0; i < 5; i++) {
          float n = 1.0 - abs(snoise(p * freq));   // Ridge at zero-crossings
          n = n * n;                                // Square = sharper ridges
          n *= weight;
          weight = clamp(n, 0.0, 1.0);             // Weight next octave by current
          result += n * amp;
          freq   *= 2.0;
          amp    *= 0.5;
        }
        return clamp(result, 0.0, 1.0);
      }

      void main() {
        // 1. ELLIPSOID SHAPE
        vec3 baseShape = position * vec3(1.0, 0.80, 1.20);

        // 2. LONGITUDINAL FISSURE (split hemispheres)
        float fissure = smoothstep(0.0, 0.15, abs(baseShape.x));
        // Deepen fissure only on the superior surface (y > 0)
        float topFactor = smoothstep(0.0, 0.6, baseShape.y);
        float fissureDisp = (1.0 - fissure) * topFactor * 0.28;
        vFissure = (1.0 - fissure) * topFactor;

        // 3. RIDGED MULTI-FRACTAL GYRI
        // Scale 2.0 gives ~6-8 primary gyri around the brain (correct anatomical count)
        float ridgeNoise = ridgedMF(baseShape * 2.0, 5);

        // Blend in secondary frequency for sub-folds (gyri within gyri)
        float subFolds   = ridgedMF(baseShape * 4.5, 3) * 0.25;
        float combinedRidge = ridgeNoise * 0.75 + subFolds;

        // Zero ridges inside the fissure
        combinedRidge *= mix(0.2, 1.0, fissure);

        // Pass to fragment for sulci darkening (AO)
        vNoise = combinedRidge;

        // 4. FINAL DISPLACEMENT along vertex normal
        float disp = combinedRidge * 0.18 - fissureDisp;
        vec3 displaced = baseShape + normal * disp;

        // Flatten inferior surface (anatomically more flat)
        if (displaced.y < 0.0) {
          displaced.y *= 0.70;
          displaced.x *= 1.0 + 0.07 * (-displaced.y);
        }

        vWorldPos = (modelMatrix * vec4(displaced, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * vec4(vWorldPos, 1.0);
      }
"""

# ── FRAGMENT SHADER ───────────────────────────────────────────────────────────
fShader = """
      uniform float uProgress;
      uniform float uTime;
      varying vec3  vWorldPos;
      varying float vNoise;
      varying float vFissure;

      // Simplex for PET organic blobs
      vec4 permute4(vec4 x){return mod(((x*34.0)+1.0)*x,289.0);}
      float snoise3(vec3 v){
        const vec2 C=vec2(1./6.,1./3.);const vec4 D=vec4(0.,.5,1.,2.);
        vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);
        vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.-g;
        vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);
        vec3 x1=x0-i1+C.x;vec3 x2=x0-i2+C.y;vec3 x3=x0-D.y;
        i=mod(i,289.);
        vec4 p=permute4(permute4(permute4(i.z+vec4(0.,i1.z,i2.z,1.))
          +i.y+vec4(0.,i1.y,i2.y,1.))+i.x+vec4(0.,i1.x,i2.x,1.));
        float n_=1./7.;vec3 ns=n_*D.wyz-D.xzx;
        vec4 j=p-49.*floor(p*ns.z*ns.z);
        vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.*x_);
        vec4 xs=x_*ns.x+ns.yyyy;vec4 ys=y_*ns.x+ns.yyyy;
        vec4 h=1.-abs(xs)-abs(ys);
        vec4 b0=vec4(xs.xy,ys.xy);vec4 b1=vec4(xs.zw,ys.zw);
        vec4 s0=floor(b0)*2.+1.;vec4 s1=floor(b1)*2.+1.;
        vec4 sh=-step(h,vec4(0.));
        vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
        vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);
        vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);
        vec4 norm=1.79284291400159-0.85373472095314*sqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
        p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
        vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.);
        m=m*m;return 42.*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
      }

      // FBM for organic PET blob edges
      float fbm(vec3 p) {
        float v = 0.0; float a = 0.5;
        for (int i = 0; i < 4; i++) {
          v += a * snoise3(p);
          p *= 2.1; a *= 0.5;
        }
        return v;
      }

      // PET SCAN heat zone: organic blob (not a perfect sphere)
      float petZone(vec3 wp, vec3 center, float radius) {
        float dist = length(wp - center);
        // FBM warps the edges to create organic "splotch" shapes
        float organicEdge = fbm(wp * 3.5 + uTime * 0.2) * 0.25;
        return smoothstep(radius, 0.0, dist - organicEdge);
      }

      // EXACT COLOR RAMP from specification
      vec3 petColor(float t) {
        t = clamp(t, 0.0, 1.0);
        vec3 c0 = vec3(0.05, 0.00, 0.15);  // 0.0 - Indigo oscuro
        vec3 c1 = vec3(0.80, 0.00, 0.50);  // 0.3 - Magenta vibrante
        vec3 c2 = vec3(1.00, 0.30, 0.00);  // 0.6 - Naranja fuego
        vec3 c3 = vec3(1.00, 0.90, 0.20);  // 0.9-1.0 - Amarillo neón

        if (t < 0.3) return mix(c0, c1, t / 0.3);
        if (t < 0.6) return mix(c1, c2, (t - 0.3) / 0.3);
        return mix(c2, c3, (t - 0.6) / 0.4);
      }

      void main() {
        // Pixel normals for correct lighting on gyri
        vec3 dx = dFdx(vWorldPos);
        vec3 dy = dFdy(vWorldPos);
        vec3 N  = normalize(cross(dx, dy));
        vec3 V  = normalize(cameraPosition - vWorldPos);

        // Lighting — strong key to reveal 3D folds
        vec3 L1 = normalize(vec3(1.0, 2.0, 1.5));
        vec3 L2 = normalize(vec3(-1.0, 0.3, 0.5));
        float diff = max(dot(N, L1), 0.0) * 0.65
                   + max(dot(N, L2), 0.0) * 0.15
                   + 0.22; // ambient

        // ── HEAT (PET Scan zones) ─────────────────────────────────────────
        // Phase 1: Prefrontal cortex (front-top zone)
        vec3  zone1 = vec3(0.0,  0.3,  0.9);   // anterior top
        float heat1 = petZone(vWorldPos, zone1, 0.85);
        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.50, uProgress);

        // Phase 2: Limbic system (central / inferior)
        vec3  zone2 = vec3(0.0, -0.1,  0.0);   // center mass
        float heat2 = petZone(vWorldPos, zone2, 0.95);
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.82, uProgress);

        // Phase 3: Insula / deep core (lateral)
        vec3  zone3 = vec3(0.0,  0.1, -0.3);   // posterior-central
        float heat3 = petZone(vWorldPos, zone3, 1.1);
        float w3 = smoothstep(0.68, 0.85, uProgress);

        float heat = heat1 * w1 + heat2 * w2 + heat3 * w3;

        // Organic pulse (biological rhythm)
        heat += 0.04 * sin(uTime * 4.5) * max(w1, max(w2, w3));
        heat  = clamp(heat, 0.0, 1.0);

        // ── COLOR RAMP ────────────────────────────────────────────────────
        vec3 col = petColor(heat);

        // ── SULCI DARKENING (vNoise used as AO) ───────────────────────────
        // Spec: "multiply final color by vNoise so cracks are darker"
        float sulciAO = vNoise * vNoise;                  // quadratic: sulci = black
        sulciAO *= mix(0.02, 1.0, 1.0 - vFissure * 0.9); // fissure very dark

        col = col * sulciAO * diff;

        // Specular on gyri ridges
        vec3 H    = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 55.0) * 0.20 * vNoise;
        col += vec3(spec);

        // Rim glow (edge subsurface scattering)
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 2.2);
        vec3 rimCol   = mix(vec3(0.20, 0.0, 0.50), vec3(1.0, 0.45, 0.0), heat);
        col += rimCol * fresnel * 0.35;

        gl_FragColor = vec4(col, 1.0);
      }
"""

# Inject shaders
text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{fShader}`;', text, flags=re.DOTALL)

# Update geometry to 128 detail as specified
text = re.sub(r'new THREE\.IcosahedronGeometry\(R,\s*\d+\)', 'new THREE.IcosahedronGeometry(R, 128)', text)

# Update R radius
text = text.replace('const R = 1.3;', 'const R = 1.0;')

# Stronger Bloom for the magenta/yellow glow
bloom = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.0, 0.5, 0.50);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom, text)

# Also update varyings in shader material to include vWorldPos instead of vWorldPosition
# (already done via vShader replacement)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Master rewrite applied: Ridged MF + PET Scan organic zones.")
