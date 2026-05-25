dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find brainVS start and brainMat end
start_line = None
end_line = None

for i, l in enumerate(lines):
    if 'const brainVS = `' in l and start_line is None:
        start_line = i
    if 'blending: THREE.NormalBlending' in l and start_line is not None:
        # The line after the closing }); of brainMat
        end_line = i + 2
        break

if start_line is None or end_line is None:
    # Try alternative end
    for i, l in enumerate(lines):
        if 'const brainVS = `' in l and start_line is None:
            start_line = i
        if 'side: THREE.DoubleSide' in l and start_line is not None:
            end_line = i + 2
            break

print(f"Found block: lines {start_line+1} to {end_line+1}")

new_shader = '''  const brainVS = `
    varying vec3 vNormal;
    varying vec3 vPosition;
    void main() {
      vNormal = normalize(normalMatrix * normal);
      vPosition = position;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `;
  const brainFS = `
    uniform float uProgress;
    uniform float uTime;
    varying vec3 vNormal;
    varying vec3 vPosition;

    vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
    vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
    vec4 permute(vec4 x) { return mod289(((x*34.0)+1.0)*x); }
    vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }
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
      i = mod289(i);
      vec4 p = permute(permute(permute(
                 i.z + vec4(0.0, i1.z, i2.z, 1.0))
               + i.y + vec4(0.0, i1.y, i2.y, 1.0))
               + i.x + vec4(0.0, i1.x, i2.x, 1.0));
      float n_ = 0.142857142857;
      vec3  ns = n_ * D.wyz - D.xzx;
      vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
      vec4 x_ = floor(j * ns.z);
      vec4 y_ = floor(j - 7.0 * x_);
      vec4 x = x_ *ns.x + ns.yyyy;
      vec4 y = y_ *ns.x + ns.yyyy;
      vec4 h = 1.0 - abs(x) - abs(y);
      vec4 b0 = vec4(x.xy, y.xy);
      vec4 b1 = vec4(x.zw, y.zw);
      vec4 s0 = floor(b0)*2.0 + 1.0;
      vec4 s1 = floor(b1)*2.0 + 1.0;
      vec4 sh = -step(h, vec4(0.0));
      vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
      vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
      vec3 p0 = vec3(a0.xy, h.x);
      vec3 p1 = vec3(a0.zw, h.y);
      vec3 p2 = vec3(a1.xy, h.z);
      vec3 p3 = vec3(a1.zw, h.w);
      vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
      p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
      vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
      m = m * m;
      return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
    }

    void main() {
      vec3 N = normalize(vNormal);

      // HEATMAP por region cerebral (frecuencia baja = manchas grandes)
      float noise1 = snoise(vPosition * 0.35 + uTime * 0.08);
      float noise2 = snoise(vPosition * 0.90 + uTime * 0.12);
      float regionNoise = noise1 * 0.7 + noise2 * 0.3;
      float heat = clamp(uProgress + regionNoise * 0.35, 0.0, 1.0);

      // Paleta: azul → violeta → naranja → amarillo
      vec3 cold = vec3(0.08, 0.25, 0.85);
      vec3 mid  = vec3(0.55, 0.10, 0.75);
      vec3 warm = vec3(1.00, 0.42, 0.05);
      vec3 hot  = vec3(1.00, 0.95, 0.20);
      vec3 heatColor = mix(cold, mid,  smoothstep(0.00, 0.35, heat));
      heatColor      = mix(heatColor, warm, smoothstep(0.35, 0.70, heat));
      heatColor      = mix(heatColor, hot,  smoothstep(0.70, 1.00, heat));

      // Phong lighting — revela las arrugas del cerebro
      vec3 L1 = normalize(vec3(0.6, 1.0, 1.0));
      float diff1 = max(dot(N, L1), 0.0);
      vec3 L2 = normalize(vec3(-1.0, 0.3, 0.5));
      float diff2 = max(dot(N, L2), 0.0) * 0.35;
      vec3 L3 = normalize(vec3(0.0, -1.0, 0.2));
      float diff3 = max(dot(N, L3), 0.0) * 0.15;
      vec3 viewDir = normalize(vec3(0.0, 0.0, 1.0));
      vec3 H = normalize(L1 + viewDir);
      float spec = pow(max(dot(N, H), 0.0), 48.0) * 0.35;

      float lighting = 0.25 + diff1 * 0.65 + diff2 + diff3;
      vec3 finalColor = heatColor * lighting + vec3(spec);
      gl_FragColor = vec4(finalColor, 1.0);
    }
  `;

  const brainMat = new THREE.ShaderMaterial({
    vertexShader: brainVS,
    fragmentShader: brainFS,
    uniforms: brainUniforms,
    transparent: false,
    depthWrite: true,
    side: THREE.DoubleSide
  });
'''

lines[start_line:end_line] = [new_shader]

with open(dev_file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Shader replaced! Lines {start_line+1} to {end_line+1}")
