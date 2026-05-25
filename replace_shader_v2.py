dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find brainVS start and the end of brainMat block
start_line = None
end_line = None

for i, l in enumerate(lines):
    if 'const brainVS = `' in l and start_line is None:
        start_line = i
    if start_line is not None and 'side: THREE.DoubleSide' in l:
        end_line = i + 2  # include the }); line
        break

print(f"Replacing lines {start_line+1} to {end_line}")

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
    uniform vec3  uBrainMin;
    uniform vec3  uBrainMax;
    varying vec3 vNormal;
    varying vec3 vPosition;

    // Simplex Noise 3D
    vec3 mod289(vec3 x){return x-floor(x*(1./289.))*289.;}
    vec4 mod289(vec4 x){return x-floor(x*(1./289.))*289.;}
    vec4 permute(vec4 x){return mod289(((x*34.)+1.)*x);}
    vec4 tInvSqrt(vec4 r){return 1.79284291-0.85373472*r;}
    float snoise(vec3 v){
      const vec2 C=vec2(1./6.,1./3.);const vec4 D=vec4(0.,.5,1.,2.);
      vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);
      vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.-g;
      vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);
      vec3 x1=x0-i1+C.xxx;vec3 x2=x0-i2+C.yyy;vec3 x3=x0-D.yyy;
      i=mod289(i);
      vec4 p=permute(permute(permute(i.z+vec4(0.,i1.z,i2.z,1.))+i.y+vec4(0.,i1.y,i2.y,1.))+i.x+vec4(0.,i1.x,i2.x,1.));
      float n_=.142857142857;vec3 ns=n_*D.wyz-D.xzx;
      vec4 j=p-49.*floor(p*ns.z*ns.z);vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.*x_);
      vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.-abs(x)-abs(y);
      vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);
      vec4 s0=floor(b0)*2.+1.;vec4 s1=floor(b1)*2.+1.;vec4 sh=-step(h,vec4(0.));
      vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
      vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);
      vec4 norm=tInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
      p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
      vec4 m=max(.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.);m=m*m;
      return 42.*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
    }

    void main() {
      vec3 N = normalize(vNormal);

      // Normalizar posicion [0..1] dentro del bounding box del cerebro
      vec3 normPos = (vPosition - uBrainMin) / (uBrainMax - uBrainMin);

      // ==== REGIONES ANATOMICAS ====
      // NOTA: En la vista lateral estandar, asumimos Z = anterior-posterior,
      // Y = superior-inferior, X = medial-lateral.
      // normPos.z alto = frontal, bajo = occipital
      // normPos.y alto = superior (corteza dorsal), bajo = inferior (temporal/limbico)

      // Corteza Prefrontal: zona frontal-superior
      float prefrontal = normPos.z * 0.6 + normPos.y * 0.4;
      prefrontal = smoothstep(0.3, 0.95, prefrontal);

      // Lobulo Temporal: zona inferior-media
      float temporal = (1.0 - normPos.y) * 0.5 + (1.0 - abs(normPos.z - 0.4)) * 0.5;
      temporal = smoothstep(0.2, 0.85, temporal);

      // Sistema Limbico: zona central-inferior (profunda)
      float limbic = (1.0 - abs(normPos.z - 0.45)) * 0.5 + (1.0 - normPos.y) * 0.5;
      limbic = smoothstep(0.35, 0.9, limbic);

      // Corteza Motor/Parietal: zona superior-media
      float parietal = normPos.y * 0.6 + (1.0 - abs(normPos.z - 0.5)) * 0.4;
      parietal = smoothstep(0.3, 0.9, parietal);

      // ==== ACTIVIDAD POR FASE ====
      // Fase 0-0.33: Small Talk — motor/temporal activo, prefrontal bajo
      float heat_small = temporal * 0.7 + parietal * 0.3;

      // Fase 0.33-0.66: Profundizando — prefrontal crece, temporal sostenido
      float heat_deep = prefrontal * 0.65 + temporal * 0.35;

      // Fase 0.66-1.0: Conexion Profunda — limbico + prefrontal full
      float heat_max = limbic * 0.6 + prefrontal * 0.4;

      // Mezcla suave entre fases segun uProgress
      float t1 = smoothstep(0.0, 0.33, uProgress);
      float t2 = smoothstep(0.33, 0.66, uProgress);
      float regionBase = mix(heat_small, mix(heat_small, heat_deep, t2), t1);
      regionBase       = mix(regionBase, heat_max, smoothstep(0.66, 1.0, uProgress));

      // Pulso vivo: pequeno ruido animado que simula actividad neural
      float pulse = snoise(vPosition * 1.2 + uTime * 0.15) * 0.12;
      float heat = clamp(regionBase + pulse, 0.0, 1.0);

      // ==== PALETA DE COLORES ====
      vec3 cold = vec3(0.05, 0.10, 0.55);  // Azul profundo (inactivo)
      vec3 mid  = vec3(0.60, 0.05, 0.70);  // Violeta (activacion inicial)
      vec3 warm = vec3(1.00, 0.35, 0.00);  // Naranja vivo (activo)
      vec3 hot  = vec3(1.00, 0.92, 0.10);  // Amarillo brillante (maxima activacion)

      vec3 heatColor = mix(cold, mid,  smoothstep(0.15, 0.45, heat));
      heatColor      = mix(heatColor, warm, smoothstep(0.45, 0.72, heat));
      heatColor      = mix(heatColor, hot,  smoothstep(0.72, 1.00, heat));

      // ==== ILUMINACION PARA VER LOS PLIEGUES ====
      // Luz principal fuerte — contraste maximo entre giros iluminados y surcos en sombra
      vec3 L1 = normalize(vec3(0.5, 0.8, 1.0));
      float diff1 = max(dot(N, L1), 0.0);

      // Luz de relleno lateral muy debil (no aplana las sombras)
      vec3 L2 = normalize(vec3(-1.0, 0.2, 0.4));
      float diff2 = max(dot(N, L2), 0.0) * 0.18;

      // Rim light trasero para definir el contorno del cerebro
      vec3 L3 = normalize(vec3(0.0, 0.3, -1.0));
      float diff3 = max(dot(N, L3), 0.0) * 0.12;

      // Especular concentrado — los giros brillan como tejido humedo
      vec3 viewDir = normalize(vec3(0.0, 0.0, 1.0));
      vec3 H = normalize(L1 + viewDir);
      float spec = pow(max(dot(N, H), 0.0), 80.0) * 0.5;

      // Ambient MUY bajo para maximo contraste en los surcos
      float ambient = 0.08;
      float lighting = ambient + diff1 * 0.82 + diff2 + diff3;

      // Color final: heatColor modulado por la luz
      vec3 finalColor = heatColor * lighting + vec3(spec * 0.8);

      gl_FragColor = vec4(finalColor, 1.0);
    }
  `;

  // Uniforms del cerebro — ahora incluyen bounding box para regiones anatomicas
  // (brainUniforms ya declarado globalmente arriba, solo anhadimos los nuevos)
  brainUniforms.uBrainMin = { value: new THREE.Vector3() };
  brainUniforms.uBrainMax = { value: new THREE.Vector3() };

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

print(f"Anatomical shader applied! Replaced lines {start_line+1} to {end_line}")
