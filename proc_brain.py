with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()
changes=0

# ---- 1. Replace GLTF loader with procedural brain ----
old_loader_start = '  // Cargar brain GLB en la brainScene'
old_loader_end = '  );\n\n\n\n  // brainMat is no longer needed'
s = text.find(old_loader_start)
e = text.find(old_loader_end, s)
print(f'Loader: {s} -> {e}')

PROC_BRAIN = '''  // ============ PROCEDURAL BRAIN (no GLB needed) ============
  (function createProceduralBrain() {
    const R = 1.55, SEG = 96;
    const geo = new THREE.SphereGeometry(R, SEG, SEG/2);
    const pos = geo.attributes.position;
    const cnt = pos.count;

    // Store PRE-DISPLACEMENT original sphere normals for perfect anatomy
    const oNX = new Float32Array(cnt), oNY = new Float32Array(cnt), oNZ = new Float32Array(cnt);
    for (let i=0;i<cnt;i++) {
      const x=pos.getX(i), y=pos.getY(i), z=pos.getZ(i);
      const r=Math.sqrt(x*x+y*y+z*z)||1;
      oNX[i]=x/r; oNY[i]=y/r; oNZ[i]=z/r;
    }

    // Displace: gyri + sulci + brain shape
    for (let i=0;i<cnt;i++) {
      const nx=oNX[i], ny=oNY[i], nz=oNZ[i];
      // Large gyri (low freq)
      const d1 = Math.sin(nx*5.1)*Math.cos(ny*6.3)*Math.sin(nz*4.7) * 0.17;
      // Medium folds
      const d2 = Math.sin(nx*11+1.2)*Math.cos(nz*12+0.9)*Math.sin(ny*10+2.0) * 0.09;
      // Fine sulci detail
      const d3 = Math.sin(nx*22+3)*Math.cos(ny*21+1.5)*Math.sin(nz*23+4) * 0.04;
      // Sagittal fissure along midline
      const sag = Math.exp(-nz*nz * 70) * (-0.09);
      // Flatten inferior pole (brain stem area)
      const inf = Math.max(0, -ny) * 0.28;
      const disp = d1+d2+d3+sag-inf;
      const newR = R + disp;
      // Slight frontal protrusion, flatten posterior
      pos.setXYZ(i, nx*newR*(1+nz*0.08), ny*newR*0.95, nz*newR*0.88);
    }
    geo.computeVertexNormals();

    // Vertex colors (heatmap)
    const colors = new Float32Array(cnt*3);
    // Start navy so brain is immediately visible
    for(let i=0;i<cnt;i++){colors[i*3]=0.04;colors[i*3+1]=0.04;colors[i*3+2]=0.20;}
    geo.setAttribute('color', new THREE.BufferAttribute(colors,3));

    const mat = new THREE.MeshStandardMaterial({
      vertexColors:true, roughness:0.42, metalness:0.04, color:0xffffff
    });
    const brainMesh = new THREE.Mesh(geo, mat);
    brainMesh.frustumCulled = false;

    // Brain stem
    const stemGeo = new THREE.CylinderGeometry(0.15,0.11,0.55,14);
    const stemMat = new THREE.MeshStandardMaterial({color:0x3a2a1a,roughness:0.9});
    const stemMesh = new THREE.Mesh(stemGeo,stemMat);
    stemMesh.position.set(0,-R*0.97,0);

    // Register for heatmap updates (ANATOMY KNOWN via oNX/oNY/oNZ)
    window.brainMeshes = [{
      mesh: brainMesh, colors: colors,
      positions: pos.array,   // displaced coords (for noise)
      oNX: oNX, oNY: oNY, oNZ: oNZ  // original sphere normals = perfect anatomy
    }];

    const brainPivot = new THREE.Group();
    brainPivot.add(brainMesh);
    brainPivot.add(stemMesh);
    brainPivot.position.set(0,0,0);
    brainScene.add(brainPivot);
    window.brainPivot = brainPivot;
    console.log('Procedural brain created, vertices:', cnt);
  })();

'''

text = text[:s] + PROC_BRAIN + '  // brainMat is no longer needed' + text[e+len(old_loader_end):]
changes+=1; print('1. Procedural brain injected')

# ---- 2. Replace updateBrainVertexColors with anatomy-perfect version ----
START = '  // Called every frame to update vertex colors\n  window.updateBrainVertexColors = function(progress, time) {'
END   = '\n  };\n\n\n\n    // brainMat'
s2 = text.find(START)
e2 = text.find(END, s2)
print(f'Update fn: {s2} -> {e2}')

NEW_UPDATE = '''  // Called every frame to update vertex colors
  window.updateBrainVertexColors = function(progress, time) {
    if (!window.brainMeshes || !window.brainMeshes.length) return;
    const {mesh, colors, positions, oNX, oNY, oNZ} = window.brainMeshes[0];
    if (!oNX) return;
    const cnt = oNX.length;

    function ss(a,b,x){const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t);}
    function thermal(t) {
      t=Math.max(0,Math.min(1,t));
      const S=[[0,.04,.04,.32],[.18,0,.18,.72],[.36,0,.55,.90],[.50,0,.82,.62],
               [.64,.45,.96,.08],[.78,.96,.68,0],[.90,1,.24,0],[1,1,.88,.75]];
      for(let i=0;i<S.length-1;i++){
        const[t0,r0,g0,b0]=S[i],[t1,r1,g1,b1]=S[i+1];
        if(t<=t1){const f=(t-t0)/(t1-t0),s=f*f*(3-2*f);return[r0+s*(r1-r0),g0+s*(g1-g0),b0+s*(b1-b0)];}
      }
      return[1,.88,.75];
    }

    const p=progress, tt=time;
    // Cumulative ramps — never go backwards
    const r1=ss(0,.28,p), r2=ss(.28,.58,p), r3=ss(.58,.90,p);
    const r1f=1-ss(.50,.80,p)*.5;
    const base=0.08+p*0.30;

    for(let vi=0;vi<cnt;vi++){
      // PERFECT anatomical coordinates from original sphere normals
      const nx=oNX[vi], ny=oNY[vi], nz=oNZ[vi];
      // ny: +1=superior(top), -1=inferior(bottom)
      // nz: +1=anterior(frontal), -1=posterior(occipital)
      // nx: +1=right, -1=left
      const yN=(ny+1)/2;    // 0=inferior, 1=superior
      const zN=(nz+1)/2;    // 0=posterior, 1=anterior

      // ---- ANATOMICAL REGIONS (precise, no guesswork) ----
      const dlpfc  = ss(.65,1.0,yN)*ss(.55,.95,zN);              // prefrontal dorsolateral top-front
      const lang   = ss(.30,.62,yN)*(1-ss(.62,.78,yN))*ss(.50,.85,zN); // language: mid-front
      const amyg   = ss(.04,.28,1-yN)*ss(.42,.72,zN);            // amygdala: inferior-anterior
      const acc    = ss(.60,.88,yN)*ss(.40,.68,zN);               // ant cingulate: mid-high front
      const insula = ss(.35,.65,yN)*(1-ss(.55,.78,yN))*(1-ss(.18,.65,Math.abs(nz))); // lateral mid
      const vmpfc  = ss(.30,.58,yN)*ss(.72,.98,zN)*(1-Math.abs(nx)*.6);  // ventromedial front
      const hippo  = ss(.04,.26,1-yN)*ss(.32,.62,zN);             // hippocampus: inferior

      // Spatial noise from displaced geometry for organic blobs
      const px=positions[vi*3], py=positions[vi*3+1], pz=positions[vi*3+2];
      const n1=Math.sin(px*3.8*Math.PI+tt*.32)*Math.cos(pz*3.5*Math.PI+tt*.27);
      const n2=Math.sin(py*4.2*Math.PI+tt*.21)*Math.cos(px*4.8*Math.PI+tt*.29);
      const n3=Math.sin(pz*5.5*Math.PI+tt*.18)*Math.cos(py*6.0*Math.PI+tt*.22);
      const noise=n1*.45+n2*.35+n3*.20;
      const nM=1.0+noise*.26;

      // Sulci darkening: valleys appear darker (more realistic)
      const sulci = (n1*n2 < -0.18) ? 0.78 : 1.0;

      const flash=Math.abs(Math.sin(nx*10+tt*3.2)*Math.cos(nz*8+tt*2.7))*r1*.18;
      const h1=(dlpfc*.85+lang*.72+flash)*r1*r1f;
      const h2=(amyg*.90+acc*.78+hippo*.70)*r2;
      const h3=(vmpfc*.90+insula*.85+amyg*.60+dlpfc*.50)*r3;

      let heat=base+(h1+h2+h3)*nM;
      heat=Math.max(0,Math.min(1,heat))*sulci;
      const[r,g,b]=thermal(heat);
      colors[vi*3]=r;colors[vi*3+1]=g;colors[vi*3+2]=b;
    }
    mesh.geometry.attributes.color.needsUpdate=true;
  }'''

text = text[:s2] + NEW_UPDATE + text[e2:]
changes+=1; print('2. updateBrainVertexColors updated for procedural anatomy')

with open('3d-test.html','w',encoding='utf-8') as f: f.write(text)
print(f'Done: {changes}/2 changes applied')
