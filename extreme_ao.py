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

      float computeGyri(vec3 p) {
        // Domain warp: single layer, moderate (avoid crystal artifacts from 2 layers)
        vec3 q = vec3(
          snoise(p * 1.5 + vec3(0.0, 0.0, 0.0)),
          snoise(p * 1.5 + vec3(3.7, 1.5, 2.8)),
          snoise(p * 1.5 + vec3(2.3, 4.7, 1.1))
        );
        vec3 wp = p + q * 0.35;

        // PRIMARY GYRI: frequency 2.3 = about 7-8 ridges visible on the brain
        // 1 - |snoise| = ridges at zero-crossings, winding organically
        float g1 = 1.0 - abs(snoise(wp * 2.3));
        // pow(1.1) = gentle sharpening: rounded peaks but DEFINED valleys
        g1 = pow(max(g1, 0.0), 1.15);

        // SECONDARY DETAIL: slightly higher frequency for texture within gyri
        float g2 = 1.0 - abs(snoise(wp * 4.2 + vec3(1.5)));
        g2 = pow(max(g2, 0.0), 1.5);

        // Combined: primary dominant so large folds clearly visible
        float combined = g1 * 0.72 + g2 * 0.28;

        // Critical: return full range 0->1 with clear separation
        // smoothstep with wide range to keep both valleys AND peaks well defined
        return smoothstep(0.0, 0.95, combined);
      }

      void main() {
        vec3 pos = position;

        // SHAPE
        pos.x *= 0.80;
        pos.z *= 1.22;
        pos.y *= 0.86;

        if (pos.y < 0.0) {
          pos.y *= 0.68;
          pos.x *= 1.0 + 0.06 * (-pos.y);
        }
        if (pos.z > 0.6) pos.z = 0.6 + (pos.z - 0.6) * 0.82;

        // Fissure
        float distCenter = abs(pos.x);
        float topFactor = smoothstep(-0.1, 0.7, pos.y);
        float fissureAmt = (1.0 - smoothstep(0.0, 0.13, distCenter)) * topFactor;
        vFissure = fissureAmt;
        pos.y -= fissureAmt * 0.26;

        // Gyri: BIGGER displacement so folds are unmistakably visible
        float gyri = computeGyri(pos * 1.85);
        gyri *= (1.0 - fissureAmt * 0.9);

        // 0.22 = 22% of radius = VERY visible, clear 3D folds
        float disp = gyri * 0.22;
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

      vec3 thermal(float t) {
        t = clamp(t, 0.0, 1.0);
        vec3 c0 = vec3(0.04, 0.01, 0.14);
        vec3 c1 = vec3(0.32, 0.00, 0.52);
        vec3 c2 = vec3(0.70, 0.05, 0.42);
        vec3 c3 = vec3(1.00, 0.36, 0.00);
        vec3 c4 = vec3(1.00, 0.88, 0.12);
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

        // Strong directional light to reveal 3D folds
        vec3 L1 = normalize(vec3(1.0, 2.0, 1.5));
        vec3 L2 = normalize(vec3(-1.0, 0.3, 0.5));
        float d1 = max(dot(N, L1), 0.0);
        float d2 = max(dot(N, L2), 0.0) * 0.18;
        float shading = d1 * 0.75 + d2 + 0.20;

        // Specular: only on gyri peaks, sharp for "wet tissue"
        vec3 H = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 60.0) * 0.22 * vFold;

        // ── CRITICAL: EXTREME AO ─────────────────────────────────────
        // Sulci (vFold~0) = pitch BLACK, gyri (vFold~1) = fully lit
        // This is what makes the folds VISIBLE regardless of color
        float ao = vFold * vFold;  // Quadratic: 0 -> 0, 0.5 -> 0.25, 1 -> 1
        // Fissure: always near black
        ao *= mix(0.0, 1.0, 1.0 - vFissure * 0.95);

        // ── HEAT MAP ─────────────────────────────────────────────────
        float pfZone  = smoothstep(-0.05, 1.0, vWorldPosition.z) * smoothstep(-0.2, 0.9, vWorldPosition.y);
        float limZone = 1.0 - smoothstep(0.0, 1.05, length(vWorldPosition));
        float insZone = smoothstep(0.1, 0.9, abs(vWorldPosition.x));

        float w1 = smoothstep(0.05, 0.25, uProgress) - smoothstep(0.35, 0.52, uProgress);
        float w2 = smoothstep(0.35, 0.55, uProgress) - smoothstep(0.65, 0.82, uProgress);
        float w3 = smoothstep(0.68, 0.85, uProgress);

        float heat = pfZone * w1 + limZone * w2 + insZone * w3 * 0.85;

        // Thermal grain (fMRI pixel noise texture)
        float activeArea = max(w1, max(w2, w3));
        float grain = snoise3(vWorldPosition * 8.0 + uTime * 0.3) * 0.08
                    + snoise3(vWorldPosition * 18.0) * 0.04;
        heat += grain * activeArea;
        heat += 0.035 * sin(uTime * 4.5) * activeArea;
        heat = clamp(heat, 0.0, 1.0);

        // COLOR: thermal tinted by strong AO
        vec3 col = thermal(heat);
        // AO applied MULTIPLICATIVELY so sulci go dark regardless of heat color
        col = col * ao * shading + vec3(spec);

        // Rim/fresnel
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 2.2);
        vec3 rimCol = mix(vec3(0.22, 0.0, 0.50), vec3(1.0, 0.45, 0.0), heat);
        col += rimCol * fresnel * 0.35;

        gl_FragColor = vec4(col, 1.0);
      }
"""

text = re.sub(r'const vShader = `.*?`;', f'const vShader = `{new_vShader}`;', text, flags=re.DOTALL)
text = re.sub(r'const fShader = `.*?`;', f'const fShader = `{new_fShader}`;', text, flags=re.DOTALL)

bloom_fix = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.55, 0.35, 0.58);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom_fix, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Extreme AO + big displacement gyri applied.")
