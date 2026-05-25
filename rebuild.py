import re, sys
with open('3d-test-git.html','r',encoding='utf-8') as f: base=f.read()

# 1. ADD BLOOM SCRIPTS after GSAP
base = base.replace(
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>',
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>\n  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>\n  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/LuminosityHighPassShader.js"></script>\n  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>\n  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>\n  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>\n  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"></script>'
)

# 2. ADD brainUniforms + brain vars declaration near start of main script
brain_decls = """
  // ===== BRAIN VARIABLES =====
  let brainCanvasEl = null, brainRenderer = null, brainScene = null, brainCam = null;
  window.brainMeshes = [];
  window.brainPivot = null;
  const brainUniforms = { uProgress: { value: 0.0 }, uTime: { value: 0.0 } };
"""
base = base.replace('  let globalBrainMesh;', '  let globalBrainMesh;\n' + brain_decls)

# 3. ADD brain scroll handler - find the portalP block in git
old_portal = '      if (portalP > 0) {'
new_portal = '''      if (portalP > 0) {
            // ===== BRAIN ACTIVATION =====
            if (window.brainPivot) {
              window.brainPivot.visible = true;
              const brainOp = mapRange(portalP, 0.5, 1.0, 0, 1);
              if (brainCanvasEl) brainCanvasEl.style.opacity = brainOp;
              const heatP = mapRange(prog, 16.0, 20.0, 0, 1);
              brainUniforms.uProgress.value = heatP;
              const hpRot = heatP;
              let tRY, tRX;
              if (hpRot <= 0.33) { const s=Math.pow(hpRot/0.33,2)*(3-2*hpRot/0.33); tRY=s*(-0.40); tRX=s*(-0.12); }
              else if (hpRot <= 0.66) { const s=Math.pow((hpRot-0.33)/0.33,2)*(3-2*(hpRot-0.33)/0.33); tRY=-0.40+s*(-0.60); tRX=-0.12+s*(0.18); }
              else { const s=Math.pow((hpRot-0.66)/0.34,2)*(3-2*(hpRot-0.66)/0.34); tRY=-1.00+s*(-0.15); tRX=0.06+s*(0.08); }
              window.brainPivot.rotation.y += (tRY - window.brainPivot.rotation.y) * 0.08;
              window.brainPivot.rotation.x += (tRX - window.brainPivot.rotation.x) * 0.08;
              const brainUI = document.getElementById('brain-ui');
              const bTitle = document.getElementById('brain-title');
              const bDesc = document.getElementById('brain-desc');
              const bBar = document.getElementById('brain-progress-bar');
              if (brainUI) {
                brainUI.style.opacity = brainOp > 0.1 ? '1' : '0';
                if (heatP < 0.33) { bTitle.innerText='Small Talk'; bTitle.style.color='#a0d2ff'; bDesc.innerHTML='Actividad superficial &mdash; Corteza Prefrontal Dorsolateral. Adrenalina.'; }
                else if (heatP < 0.66) { bTitle.innerText='Conexion'; bTitle.style.color='#ffb347'; bDesc.innerHTML='Nucleo Accumbens activo &mdash; Dopamina. Recompensa cognitiva.'; }
                else { bTitle.innerText='Flow Profundo'; bTitle.style.color='#ffcc00'; bDesc.innerHTML='Insula + Prefrontal Ventral &mdash; Oxitocina. Vinculo inquebrantable.'; }
                if (bBar) bBar.style.width = (heatP*100)+'%';
              }
              if (window.updateBrainAnnotations) window.updateBrainAnnotations(heatP, true);
            }
            // ==========================='''
base = base.replace(old_portal, new_portal, 1)

# 4. ADD brain render call in loop, before card render
old_card_render = '    // Render separado de la carta GLB en su canvas transparente\n    if (cardRenderer2 && cardScene2 && cardCam2 && globalGlbCard && globalGlbCard.visible) {'
new_card_render = '''    // ===== BRAIN RENDER =====
    brainUniforms.uTime.value = t;
    if (brainRenderer && brainScene && brainCam && window.brainPivot && window.brainPivot.visible) {
      const hp = brainUniforms.uProgress.value;
      if (window.updateBrainVertexColors) window.updateBrainVertexColors(hp, t);
      const ss2=(a,b,x)=>{const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t);};
      if (window.rimLight1) window.rimLight1.intensity = ss2(0,.30,hp)*(1-ss2(.45,.65,hp))*1.8;
      if (window.rimLight2) window.rimLight2.intensity = ss2(.25,.58,hp)*(1-ss2(.68,.85,hp))*2.0;
      if (window.rimLight3) window.rimLight3.intensity = ss2(.60,.90,hp)*1.6;
      if (window.brainInteriorLight) window.brainInteriorLight.intensity=ss2(.28,.58,hp)*(1-ss2(.72,.90,hp))*3.5*(0.85+Math.sin(t*2.1)*0.15);
      if (window.insulaSphere) { window.insulaSphere.material.opacity=ss2(.62,.85,hp)*0.85*(0.7+Math.sin(t*1.3)*0.3); window.insulaSphere.scale.setScalar(1+Math.sin(t*1.3)*0.15); }
      if (window.brainComposer) window.brainComposer.render(); else brainRenderer.render(brainScene,brainCam);
    }
    // Render separado de la carta GLB en su canvas transparente
    if (cardRenderer2 && cardScene2 && cardCam2 && globalGlbCard && globalGlbCard.visible) {'''
base = base.replace(old_card_render, new_card_render, 1)

# 5. ADD initBrainRenderer + PROC_BRAIN + updateBrainVertexColors before loop
BRAIN_CODE = '''
  // =============================================
  // INIT BRAIN RENDERER
  // =============================================
  (function initBrainRenderer() {
    brainCanvasEl = document.createElement('canvas');
    brainCanvasEl.id = 'brain-canvas';
    brainCanvasEl.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:10008;pointer-events:none;opacity:0;transition:opacity 0.8s ease;';
    document.body.appendChild(brainCanvasEl);
    brainRenderer = new THREE.WebGLRenderer({ canvas:brainCanvasEl, antialias:true, alpha:true });
    brainRenderer.setSize(window.innerWidth, window.innerHeight);
    brainRenderer.setPixelRatio(Math.min(devicePixelRatio,2));
    brainRenderer.setClearColor(0x000000,0);
    brainRenderer.toneMapping = THREE.ACESFilmicToneMapping;
    brainScene = new THREE.Scene();
    brainCam = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 100);
    brainCam.position.set(0,0.3,5.2);
    brainCam.lookAt(0,0,0);
    brainScene.add(new THREE.AmbientLight(0x0a0a18, 0.6));
    const key = new THREE.DirectionalLight(0xfff5e0,1.8); key.position.set(2,5,5); brainScene.add(key);
    window.rimLight1 = new THREE.DirectionalLight(0x00cfff,0); window.rimLight1.position.set(-4,1,-3); brainScene.add(window.rimLight1);
    window.rimLight2 = new THREE.DirectionalLight(0xff6a00,0); window.rimLight2.position.set(4,-1,-4); brainScene.add(window.rimLight2);
    window.rimLight3 = new THREE.DirectionalLight(0xaa00ff,0); window.rimLight3.position.set(0,-4,-3); brainScene.add(window.rimLight3);
    window.brainInteriorLight = new THREE.PointLight(0xff5500,0,6,2); brainScene.add(window.brainInteriorLight);
    const iGeo=new THREE.SphereGeometry(0.18,16,12);
    const iMat=new THREE.MeshBasicMaterial({color:0xcc44ff,transparent:true,opacity:0,blending:THREE.AdditiveBlending,depthWrite:false});
    window.insulaSphere=new THREE.Mesh(iGeo,iMat); window.insulaSphere.position.set(-0.4,-0.3,0.2); brainScene.add(window.insulaSphere);
    if (typeof THREE.EffectComposer!=='undefined') {
      window.brainComposer=new THREE.EffectComposer(brainRenderer);
      window.brainComposer.addPass(new THREE.RenderPass(brainScene,brainCam));
      window.brainComposer.addPass(new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth,window.innerHeight),0.65,0.38,0.60));
    }
    window.addEventListener('resize',()=>{
      brainCam.aspect=window.innerWidth/window.innerHeight; brainCam.updateProjectionMatrix();
      brainRenderer.setSize(window.innerWidth,window.innerHeight);
      if(window.brainComposer) window.brainComposer.setSize(window.innerWidth,window.innerHeight);
    });
  })();

  // =============================================
  // PROCEDURAL BRAIN
  // =============================================
  (function createProceduralBrain() {
    const R=1.55, SEG=96;
    const geo=new THREE.SphereGeometry(R,SEG,SEG/2);
    const pos=geo.attributes.position; const cnt=pos.count;
    const oNX=new Float32Array(cnt),oNY=new Float32Array(cnt),oNZ=new Float32Array(cnt);
    for(let i=0;i<cnt;i++){const x=pos.getX(i),y=pos.getY(i),z=pos.getZ(i);const r=Math.sqrt(x*x+y*y+z*z)||1;oNX[i]=x/r;oNY[i]=y/r;oNZ[i]=z/r;}
    for(let i=0;i<cnt;i++){
      const nx=oNX[i],ny=oNY[i],nz=oNZ[i];
      const d1=Math.sin(nx*5.1)*Math.cos(ny*6.3)*Math.sin(nz*4.7)*0.17;
      const d2=Math.sin(nx*11+1.2)*Math.cos(nz*12+0.9)*Math.sin(ny*10+2.0)*0.09;
      const d3=Math.sin(nx*22+3)*Math.cos(ny*21+1.5)*Math.sin(nz*23+4)*0.04;
      const sag=Math.exp(-nz*nz*70)*(-0.09);
      const inf=Math.max(0,-ny)*0.28;
      const disp=d1+d2+d3+sag-inf; const newR=R+disp;
      pos.setXYZ(i,nx*newR*(1+nz*0.08),ny*newR*0.95,nz*newR*0.88);
    }
    geo.computeVertexNormals();
    const colors=new Float32Array(cnt*3);
    for(let i=0;i<cnt;i++){colors[i*3]=0.04;colors[i*3+1]=0.04;colors[i*3+2]=0.20;}
    geo.setAttribute('color',new THREE.BufferAttribute(colors,3));
    const mat=new THREE.MeshStandardMaterial({vertexColors:true,roughness:0.42,metalness:0.04,color:0xffffff});
    const brainMesh=new THREE.Mesh(geo,mat); brainMesh.frustumCulled=false;
    const stemGeo=new THREE.CylinderGeometry(0.15,0.11,0.55,14);
    const stemMesh=new THREE.Mesh(stemGeo,new THREE.MeshStandardMaterial({color:0x3a2a1a,roughness:0.9}));
    stemMesh.position.set(0,-R*0.97,0);
    window.brainMeshes=[{mesh:brainMesh,colors,positions:pos.array,oNX,oNY,oNZ}];
    const pivot=new THREE.Group(); pivot.add(brainMesh); pivot.add(stemMesh);
    brainScene.add(pivot); window.brainPivot=pivot;
  })();

  // =============================================
  // VERTEX COLOR HEATMAP
  // =============================================
  window.updateBrainVertexColors=function(progress,time){
    if(!window.brainMeshes||!window.brainMeshes.length)return;
    const{mesh,colors,positions,oNX,oNY,oNZ}=window.brainMeshes[0]; if(!oNX)return;
    const cnt=oNX.length;
    function ss(a,b,x){const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t);}
    function thermal(t){
      t=Math.max(0,Math.min(1,t));
      const S=[[0,.04,.04,.32],[.18,0,.18,.72],[.36,0,.55,.90],[.50,0,.82,.62],[.64,.45,.96,.08],[.78,.96,.68,0],[.90,1,.24,0],[1,1,.88,.75]];
      for(let i=0;i<S.length-1;i++){const[t0,r0,g0,b0]=S[i],[t1,r1,g1,b1]=S[i+1];if(t<=t1){const f=(t-t0)/(t1-t0),s=f*f*(3-2*f);return[r0+s*(r1-r0),g0+s*(g1-g0),b0+s*(b1-b0)];}}
      return[1,.88,.75];
    }
    const p=progress,tt=time;
    const r1=ss(0,.28,p),r2=ss(.28,.58,p),r3=ss(.58,.90,p),r1f=1-ss(.50,.80,p)*.5,base=0.08+p*0.30;
    for(let vi=0;vi<cnt;vi++){
      const nx=oNX[vi],ny=oNY[vi],nz=oNZ[vi];
      const yN=(ny+1)/2,zN=(nz+1)/2;
      const dlpfc=ss(.65,1,yN)*ss(.55,.95,zN);
      const lang=ss(.30,.62,yN)*(1-ss(.62,.78,yN))*ss(.50,.85,zN);
      const amyg=ss(.04,.28,1-yN)*ss(.42,.72,zN);
      const acc=ss(.60,.88,yN)*ss(.40,.68,zN);
      const insula=ss(.35,.65,yN)*(1-ss(.55,.78,yN))*(1-ss(.18,.65,Math.abs(nz)));
      const vmpfc=ss(.30,.58,yN)*ss(.72,.98,zN)*(1-Math.abs(nx)*.6);
      const hippo=ss(.04,.26,1-yN)*ss(.32,.62,zN);
      const px=positions[vi*3],py=positions[vi*3+1],pz=positions[vi*3+2];
      const n1=Math.sin(px*3.8*Math.PI+tt*.32)*Math.cos(pz*3.5*Math.PI+tt*.27);
      const n2=Math.sin(py*4.2*Math.PI+tt*.21)*Math.cos(px*4.8*Math.PI+tt*.29);
      const n3=Math.sin(pz*5.5*Math.PI+tt*.18)*Math.cos(py*6.0*Math.PI+tt*.22);
      const nM=1+( n1*.45+n2*.35+n3*.20)*0.26;
      const sulci=(n1*n2<-0.18)?0.78:1.0;
      const flash=Math.abs(Math.sin(nx*10+tt*3.2)*Math.cos(nz*8+tt*2.7))*r1*.18;
      const h1=(dlpfc*.85+lang*.72+flash)*r1*r1f;
      const h2=(amyg*.90+acc*.78+hippo*.70)*r2;
      const h3=(vmpfc*.90+insula*.85+amyg*.60+dlpfc*.50)*r3;
      let heat=Math.max(0,Math.min(1,base+(h1+h2+h3)*nM))*sulci;
      const[r,g,b]=thermal(heat);
      colors[vi*3]=r;colors[vi*3+1]=g;colors[vi*3+2]=b;
    }
    mesh.geometry.attributes.color.needsUpdate=true;
  };

'''

# Insert brain code before the loop
loop_marker = '\n\n  (function loop() {'
base = base.replace(loop_marker, BRAIN_CODE + '\n\n  (function loop() {', 1)

# 6. ADD brain HTML before </body>
BRAIN_HTML = '''
  <div id="brain-ui" style="position:fixed;right:5vw;top:50%;transform:translateY(-50%);opacity:0;pointer-events:none;z-index:10010;color:white;font-family:'Inter',sans-serif;transition:opacity 0.5s;background:rgba(10,15,10,0.85);backdrop-filter:blur(10px);padding:30px;border-radius:12px;border:1px solid rgba(255,255,255,0.1);width:300px;">
    <div style="font-size:10px;letter-spacing:2px;color:#a3ff00;font-weight:700;margin-bottom:10px;">ACTIVIDAD CEREBRAL</div>
    <div id="brain-title" style="font-size:28px;font-weight:700;margin-bottom:12px;font-family:'Playfair Display',serif;color:#a0d2ff;transition:color 0.5s;">Small Talk</div>
    <div style="width:100%;height:2px;background:rgba(255,255,255,0.1);margin-bottom:12px;position:relative;">
      <div id="brain-progress-bar" style="position:absolute;left:0;top:0;height:100%;width:0%;background:#a3ff00;transition:width 0.3s;"></div>
    </div>
    <div id="brain-desc" style="font-size:12px;line-height:1.6;color:#e0e0e0;"></div>
  </div>

<style>
  #brain-annotations{position:fixed;top:0;left:0;width:100%;height:100%;z-index:10009;pointer-events:none;font-family:'Inter',sans-serif;}
  .bann{position:absolute;width:100%;height:100%;opacity:0;transition:opacity 0.7s;}
  .bann.active{opacity:1;}
  .bann-dot{position:absolute;width:8px;height:8px;border-radius:50%;transform:translate(-50%,-50%);animation:ann-pulse 2s ease-out infinite;}
  @keyframes ann-pulse{0%{box-shadow:0 0 0 0 currentColor;}70%{box-shadow:0 0 0 10px transparent;}100%{box-shadow:0 0 0 0 transparent;}}
  .bann-label{position:absolute;transform:translateY(-50%);text-align:right;}
  .bann-phase{font-size:8px;letter-spacing:2px;font-weight:700;text-transform:uppercase;opacity:0.6;margin-bottom:2px;}
  .bann-name{font-size:12px;font-weight:700;color:#fff;line-height:1.25;margin-bottom:3px;}
  .bann-chem{font-size:10px;font-weight:600;}
  .bann-emo{font-size:10px;color:rgba(255,255,255,0.5);margin-top:1px;}
  .bann-line{transition:opacity 0.7s;}
</style>
<div id="brain-annotations">
  <svg style="position:absolute;top:0;left:0;width:100%;height:100%;overflow:visible;" pointer-events="none">
    <line class="bann-line" id="bl1" x1="38%" y1="28%" x2="28%" y2="34%" stroke="#a0d2ff" stroke-width="1" stroke-dasharray="3 5" opacity="0"/>
    <line class="bann-line" id="bl2" x1="36%" y1="47%" x2="24%" y2="47%" stroke="#ffb347" stroke-width="1" stroke-dasharray="3 5" opacity="0"/>
    <line class="bann-line" id="bl3" x1="34%" y1="59%" x2="22%" y2="58%" stroke="#ffcc00" stroke-width="1" stroke-dasharray="3 5" opacity="0"/>
  </svg>
  <div class="bann" id="bann-1">
    <div class="bann-dot" style="left:38%;top:28%;background:#a0d2ff;color:#a0d2ff;"></div>
    <div class="bann-label" style="left:3%;top:34%;">
      <div class="bann-phase" style="color:#a0d2ff;">Fase 1 · Hielo</div>
      <div class="bann-name">Corteza Prefrontal<br>Dorsolateral</div>
      <div class="bann-chem" style="color:#a0d2ff;">Adrenalina</div>
      <div class="bann-emo">Filtrado de seguridad</div>
    </div>
  </div>
  <div class="bann" id="bann-2">
    <div class="bann-dot" style="left:36%;top:47%;background:#ffb347;color:#ffb347;"></div>
    <div class="bann-label" style="left:3%;top:47%;">
      <div class="bann-phase" style="color:#ffb347;">Fase 2 · Conexion</div>
      <div class="bann-name">Nucleo Accumbens<br>/ C. Cingulada</div>
      <div class="bann-chem" style="color:#ffb347;">Dopamina</div>
      <div class="bann-emo">Recompensa cognitiva</div>
    </div>
  </div>
  <div class="bann" id="bann-3">
    <div class="bann-dot" style="left:34%;top:59%;background:#ffcc00;color:#ffcc00;"></div>
    <div class="bann-label" style="left:3%;top:58%;">
      <div class="bann-phase" style="color:#ffcc00;">Fase 3 · Flow</div>
      <div class="bann-name">Insula + Prefrontal<br>Ventromedial</div>
      <div class="bann-chem" style="color:#ffcc00;">Oxitocina</div>
      <div class="bann-emo">Vinculo inquebrantable</div>
    </div>
  </div>
</div>
<script>
  function updateBrainAnnotations(heatP,vis){
    const a1=document.getElementById('bann-1'),a2=document.getElementById('bann-2'),a3=document.getElementById('bann-3');
    if(!a1)return;
    const show=vis&&heatP>0.02;
    const s1=show&&heatP<0.40,s2=show&&heatP>=0.30&&heatP<0.72,s3=show&&heatP>=0.62;
    a1.classList.toggle('active',s1);a2.classList.toggle('active',s2);a3.classList.toggle('active',s3);
    const op=(id,v)=>{const el=document.getElementById(id);if(el)el.style.opacity=v;};
    op('bl1',s1?'0.7':'0');op('bl2',s2?'0.7':'0');op('bl3',s3?'0.7':'0');
  }
  window.updateBrainAnnotations=updateBrainAnnotations;
</script>
'''
base = base.replace('\n</body>\n</html>', BRAIN_HTML + '\n</body>\n</html>')

with open('3d-test.html','w',encoding='utf-8') as f: f.write(base)
print('Done. Size:', len(base))
