import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

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

      // SOFT ridged FBM - organic, NOT crystalline
      // Key: NO extreme pow() sharpening. Soft transitions = organic tissue
      float softRidge(float n) {
        // Soft ridge: wide rounded top, gentle valley
        // Invert and soften: 1-|n| but with smooth shaping
        float r = 1.0 - abs(n);
        // CRITICAL: use sqrt to make ridges ROUNDED not sharp
        return sqrt(max(r, 0.0));
      }

      float computeGyri(vec3 p) {
        // Two-layer domain warp (organic, non-parallel paths)
        vec3 q = vec3(
          snoise(p * 1.4 + vec3(0.0)),
          snoise(p * 1.4 + vec3(3.7, 1.5, 2.8)),
          snoise(p * 1.4 + vec3(2.3, 4.7, 1.1))
        );
        vec3 r = vec3(
          snoise(p * 1.4 + 3.0*q + vec3(1.7, 9.2, 3.4)),
          snoise(p * 1.4 + 3.0*q + vec3(8.3, 2.8, 1.4)),
          snoise(p * 1.4 + 3.0*q + vec3(5.1, 7.3, 4.2))
        );
        vec3 wp = p + 0.4 * r;

        // Primary gyri - large, SOFT ridges
        float g1 = softRidge(snoise(wp * 2.0));

        // Secondary - medium details inside
        float g2 = softRidge(snoise(wp * 3.8 + 1.5)) * 0.45;

        // Combine - primary dominant
        float gyri = g1 * 0.70 + g2 * 0.30;

        // Smooth out to avoid sharp angular artifacts
        // NO extreme power curves!
        return smoothstep(0.05, 1.0, gyri);
      }

      void main() {
        vec3 pos = position;

        // SHAPE
        pos.x *= 0.80;
        pos.z *= 1.22;
        pos.y *= 0.86;

        // Flatten base
        if (pos.y < 0.0) {
          pos.y *= 0.68;
          pos.x *= 1.0 + 0.06 * (-pos.y);
        }

        // Slight frontal flattening
        if (pos.z > 0.6) pos.z = 0.6 + (pos.z - 0.6) * 0.80;

        // Fissure
        float distCenter = abs(pos.x);
        float topFactor = smoothstep(-0.1, 0.7, pos.y);
        float fissureAmt = (1.0 - smoothstep(0.0, 0.13, distCenter)) * topFactor;
        vFissure = fissureAmt;
        pos.y -= fissureAmt * 0.26;

        // Gyri
        float gyri = computeGyri(pos * 1.85);
        gyri *= (1.0 - fissureAmt * 0.9);

        // Larger, softer displacement
        float disp = gyri * 0.13;
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

      // Simplex for thermal grain
      vec4 permute4(vec4 x){return mod(((x*34.0)+1.0)*x,289.0);}
      float snoise3(vec3 v){
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
        vec4 p=permute4(permute4(permute4(
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
        vec4 norm=1.79284291400159-0.85373472095314*sqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
        p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
        vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);
        m=m*m;
        return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
      }

      // Oryzo thermal palette (dark purple -> magenta -> orange -> yellow)
      vec3 thermal(float t) {
        t = clamp(t, 0.0, 1.0);
        vec3 c0 = vec3(0.04, 0.01, 0.14);  // Near black purple
        vec3 c1 = vec3(0.32, 0.00, 0.52);  // Rich purple
        vec3 c2 = vec3(0.70, 0.05, 0.42);  // Magenta
        vec3 c3 = vec3(1.00, 0.36, 0.00);  // Deep orange
        vec3 c4 = vec3(1.00, 0.88, 0.12);  // Warm yellow
        if (t < 0.25) return mix(c0, c1, t / 0.25);
        if (t < 0.50) return mix(c1, c2, (t-0.25)/0.25);
        if (t < 0.75) return mix(c2, c3, (t-0.50)/0.25);
        return mix(c3, c4, (t-0.75)/0.25);
      }

      void main() {
        vec3 dx = dFdx(vWorldPosition);
        vec3 dy = dFdy(vWorldPosition);
        vec3 N = normalize(cross(dx, dy));
        vec3 V = normalize(cameraPosition - vWorldPosition);

        // Soft three-point lighting
        vec3 L1 = normalize(vec3(1.0, 2.0, 1.5));
        vec3 L2 = normalize(vec3(-1.5, 0.3, 0.5));
        float d1 = max(dot(N, L1), 0.0);
        float d2 = max(dot(N, L2), 0.0) * 0.20;
        float shading = d1 * 0.60 + d2 + 0.28;

        // Specular only on gyri peaks
        vec3 H = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 40.0) * 0.15 * vFold;

        // AO: sulci dark, fissure very dark
        float ao = mix(0.10, 1.0, pow(vFold, 0.5));
        ao *= mix(0.03, 1.0, 1.0 - vFissure);

        // ── HEAT MAP with thermal GRANULARITY ────────────────────────────
        // Base zone contributions
        float pfZone  = smoothstep(-0.05, 1.0, vWorldPosition.z) * smoothstep(-0.2, 0.9, vWorldPosition.y);
        float limZone = 1.0 - smoothstep(0.0, 1.05, length(vWorldPosition));
        float insZone = smoothstep(0.1, 0.9, abs(vWorldPosition.x));

        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.52, uProgress);
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.82, uProgress);
        float w3 = smoothstep(0.68, 0.85, uProgress);

        float heat = pfZone * w1 + limZone * w2 + insZone * w3 * 0.85;

        // ── THERMAL GRAIN (key for realistic brain scan look) ─────────────
        // Multi-scale noise on the heat value = granular thermal texture
        // Like the pixel-level variation in a real fMRI / thermal camera
        float grain1 = snoise3(vWorldPosition * 6.0 + uTime * 0.3) * 0.10;
        float grain2 = snoise3(vWorldPosition * 12.0 + uTime * 0.5 + 3.0) * 0.05;
        float grain3 = snoise3(vWorldPosition * 24.0) * 0.025;
        // Only add grain where there's active heat (don't grain the dark zones)
        float activeArea = max(w1, max(w2, w3));
        heat += (grain1 + grain2 + grain3) * activeArea;

        // Organic pulse
        heat += 0.035 * sin(uTime * 4.5) * activeArea;

        heat = clamp(heat, 0.0, 1.0);

        // Color
        vec3 col = thermal(heat);
        col = col * shading * ao + vec3(spec);

        // Rim
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 2.2);
        vec3 rimCol = mix(vec3(0.22, 0.0, 0.50), vec3(1.0, 0.45, 0.0), heat);
        col += rimCol * fresnel * 0.38;

        gl_FragColor = vec4(col, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.55, 0.35, 0.58);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Soft gyri + thermal grain applied.")
