
// Ã¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•Â

//  THERMAL CAMERA SYSTEM
// Ã¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•Â

// Ã¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•Â
//  BRAIN 3D THERMAL RENDERER  â€â€ Opción A: dual-model swap
//  Carga human_brain.glb (completo) y human_brain_half.glb.
//  Al inicio muestra el cerebro completo. Durante el scroll, mientras
//  rota sobre Y, hace un crossfade al medio cerebro para revelar
//  las estructuras internas de forma imperceptible.
// Ã¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•Â
(function initBrainRenderer() {
  var _brainRenderer = null, _brainScene = null, _brainCamera = null;
  var _brainFull = null, _brainHalf = null, _brainClock = null;
  var _brainReady = false, _fullLoaded = false, _halfLoaded = false;
  var _brainT = 0;
  var _halfClipPlane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0); // corta por abajo

  function waitForThree(cb) {
    if (typeof THREE !== 'undefined' && THREE.GLTFLoader) { cb(); return; }
    setTimeout(function() { waitForThree(cb); }, 100);
  }

  waitForThree(function() {
    var canvas = document.getElementById('brain-canvas');
    if (!canvas) return;

    // Renderer transparente
    _brainRenderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    _brainRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    _brainRenderer.setSize(window.innerWidth, window.innerHeight);
    _brainRenderer.setClearColor(0x000000, 0);
    _brainRenderer.toneMapping = THREE.ACESFilmicToneMapping;
    _brainRenderer.toneMappingExposure = 1.6;
    _brainRenderer.localClippingEnabled = true; // necesario para clipping por material

    // Escena y camara
    _brainScene = new THREE.Scene();
    _brainCamera = new THREE.PerspectiveCamera(42, window.innerWidth / window.innerHeight, 0.01, 100);
    _brainCamera.position.set(0, 0, 0);

    // ILUMINACION QUE COMPLEMENTA LOS MAPAS BAKED:
    // El normal map ya tiene el relieve, las luces solo deben activarlo.
    // Ambient moderado: permite ver el AO map sin apagarlo completamente
    _brainScene.add(new THREE.AmbientLight(0x180008, 0.55));

    // Key principal: angulo 45 grados â€â€ ni demasiado frontal (aplana) ni demasiado lateral (oscurece)
    var kL = new THREE.DirectionalLight(0xff6600, 5.0);
    kL.position.set(3, 4, 5); _brainScene.add(kL);

    // Fill suave desde el lado opuesto para que los sulcos no sean negros puros
    var fL = new THREE.DirectionalLight(0xff3300, 1.5);
    fL.position.set(-3, 2, 4); _brainScene.add(fL);

    // Top calido: realza las crestas superiores
    var tL = new THREE.DirectionalLight(0xffaa00, 2.0);
    tL.position.set(0, 6, 1); _brainScene.add(tL);

    // Rim frio desde atras: silueta contra el fondo oscuro
    var rL = new THREE.DirectionalLight(0xbb00ee, 1.6);
    rL.position.set(0, -1, -5); _brainScene.add(rL);

    _brainClock = new THREE.Clock();

    // Ã¢â€€Ã¢â€€ Helper: aplica material térmico a todos los meshes de un root Ã¢â€€Ã¢â€€
    function applyThermalMat(root, isHalf) {
      root.traverse(function(c) {
        if (!c.isMesh || !c.material) return;
        var o = Array.isArray(c.material) ? c.material[0] : c.material;

        // Bounding box para normalizar posición en el shader
        if (!c.geometry.boundingBox) c.geometry.computeBoundingBox();
        var _bb = c.geometry.boundingBox;
        var _ctr = new THREE.Vector3(); _bb.getCenter(_ctr);
        var _hsz = new THREE.Vector3(); _bb.getSize(_hsz).multiplyScalar(0.5);
        if (!_hsz.x) _hsz.x = 1; if (!_hsz.y) _hsz.y = 1; if (!_hsz.z) _hsz.z = 1;

        var m = new THREE.MeshStandardMaterial({
          map:             o.map             || null,
          normalMap:       o.normalMap       || null,
          aoMap:           o.aoMap           || null,
          roughnessMap:    o.roughnessMap    || null,
          metalnessMap:    o.metalnessMap    || null,
          displacementMap: o.displacementMap || null,
          alphaMap:        o.alphaMap        || null,
          envMap:          null,
          color:           new THREE.Color(0.75, 0.11, 0.0),
          emissive:        new THREE.Color(0.10, 0.01, 0.0),
          emissiveIntensity: 0.45,
          roughness:    o.roughnessMap ? 1.0 : 0.82,
          metalness:    0.0,
          normalScale:  o.normalMap ? new THREE.Vector2(2.5, 2.5) : new THREE.Vector2(1.0, 1.0),
          aoMapIntensity: 2.2,
          side:         THREE.FrontSide,
          flatShading:  false,
          transparent:  true,
          depthWrite:   false,
          opacity:      1.0
        });

        // Ã¢â€€Ã¢â€€ Shader: zona caliente cingulada â€â€ Three.js r128 Ã¢â€€Ã¢â€€
        m.onBeforeCompile = function(shader) {
          shader.uniforms.uBBCtr = { value: _ctr };
          shader.uniforms.uBBHsz = { value: _hsz };

          // Vertex: pasar posición local al fragment
          shader.vertexShader = 'varying vec3 vLP;\n' + shader.vertexShader;
          shader.vertexShader = shader.vertexShader.replace(
            '#include <begin_vertex>',
            '#include <begin_vertex>\nvLP = position;'
          );

          // Fragment: declaraciones + función cingulate en espacio normalizado
          var fHead = [
            'varying vec3 vLP;',
            'uniform vec3 uBBCtr;',
            'uniform vec3 uBBHsz;',
            'float cingHeat(vec3 lp) {',
            '  vec3 np = (lp - uBBCtr) / uBBHsz;', // -1 a 1
            '  float yZ = smoothstep(-0.05,0.08,np.y)*smoothstep(0.82,0.60,np.y);',
            '  float xZ = smoothstep(0.42,0.10,abs(np.x));', // medial
            '  float zZ = smoothstep(-0.88,-0.70,np.z)*smoothstep(0.48,0.28,np.z);',
            '  return yZ * xZ * zZ;',
            '}'
          ].join('\n');
          shader.fragmentShader = fHead + '\n' + shader.fragmentShader;

          // DIAGNÓSTICO: gradiente naranja→amarillo según posición Y normalizada
          // El cíngulo está ARRIBA del cuerpo calloso, así que aparecerá en la parte amarilla.
          // Dime en qué "nivel" de amarillo aparece el cíngulo para calibrar.
          shader.fragmentShader = shader.fragmentShader.replace(
            'gl_FragColor = vec4( outgoingLight, diffuseColor.a );',
            [
              'gl_FragColor = vec4( outgoingLight, diffuseColor.a );',
              'float _ny = (vLP.y - uBBCtr.y) / uBBHsz.y;', // -1 (abajo) a +1 (arriba)
              'float _h = max(0.0, _ny);', // solo la mitad superior brilla
              'vec3 _hotC = gl_FragColor.rgb * 2.1 + vec3(0.20,0.08,-0.04);',
              'gl_FragColor.rgb = mix(gl_FragColor.rgb, _hotC, _h * 0.85);'
            ].join('\n')
          );
        };

        c.material = m;
        if (o.aoMap && !c.geometry.attributes.uv2 && c.geometry.attributes.uv) {
          c.geometry.setAttribute('uv2', c.geometry.attributes.uv);
        }
      });
    }


    // Ã¢â€€Ã¢â€€ Helper: envuelve un root en un Group centrado y escalado Ã¢â€€Ã¢â€€
    // El Group es lo que se mueve en el render loop.
    // El root interno queda centrado en el origen del Group.
    // Así position.set() en el Group no rompe el centrado.
    function wrapAndCenter(root) {
      var box    = new THREE.Box3().setFromObject(root);
      var size   = box.getSize(new THREE.Vector3());
      var center = box.getCenter(new THREE.Vector3());
      // Centrar el modelo dentro del grupo
      root.position.set(-center.x, -center.y, -center.z);
      var DIST    = 5.0;
      var vH      = 2 * Math.tan((42 * Math.PI / 180) / 2) * DIST;
      var targetH = vH * 0.22;
      var s       = targetH / Math.max(size.x, size.y, size.z);
      var wrapper = new THREE.Group();
      wrapper.scale.setScalar(s);
      wrapper.add(root);
      return wrapper; // mover el wrapper, no el root
    }

    // Ã¢â€€Ã¢â€€ Helper: cambia opacity de todos los meshes de un root Ã¢â€€Ã¢â€€
    function setOpacity(root, opacity) {
      root.traverse(function(c) {
        if (!c.isMesh) return;
        var mats = Array.isArray(c.material) ? c.material : [c.material];
        mats.forEach(function(m) { m.opacity = opacity; });
      });
    }

    // Ã¢â€€Ã¢â€€ Arranca el loop cuando ambos modelos están listos Ã¢â€€Ã¢â€€
    function checkReady() {
      if (!_fullLoaded) return;
      _brainReady = true;
      console.log('[BRAIN] Listo â€â€ swap 2D activo');
      _renderBrainLoop();
    }

    var loader = new THREE.GLTFLoader();

    // Cargar cerebro COMPLETO (visible al inicio)
    loader.load('assets/models/human_brain.glb', function(gltf) {
      var wrapper = wrapAndCenter(gltf.scene);
      wrapper.scale.multiplyScalar(1.1); // 10% más grande que el medio cerebro
      applyThermalMat(wrapper);
      setOpacity(wrapper, 1.0);     // empieza visible
      _brainFull = wrapper;
      _brainScene.add(_brainFull);
      _fullLoaded = true;
      checkReady();
    }, null, function(e) { console.error('[BRAIN] Error full:', e); });

    // El medio cerebro ahora es la imagen 2D â€â€ no se carga el GLB
    _halfLoaded = true; // ya no es necesario

    window.addEventListener('resize', function() {
      if (!_brainRenderer) return;
      _brainRenderer.setSize(window.innerWidth, window.innerHeight);
      _brainCamera.aspect = window.innerWidth / window.innerHeight;
      _brainCamera.updateProjectionMatrix();
    });
  });

  function _renderBrainLoop() {
    requestAnimationFrame(_renderBrainLoop);
    if (!_brainReady || !_brainFull) return;
    _brainT = _brainClock.getElapsedTime();

    // Ã¢â€€Ã¢â€€ FASE 1: Rotación â€â€ bProg 16.3 → 17.0 Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
    // rotEase va de 0 (frontal) a 1 (perfil lateral completo)
    var _bProg = window._brainScrollProg || 0; var _bProgM = _bProg + 0.5;
    var _rotT    = Math.max(0, Math.min(1, (_bProgM - 16.3) / (17.0 - 16.3)));
    var _rotEase = _rotT < 0.5 ? 2 * _rotT * _rotT : 1 - Math.pow(-2 * _rotT + 2, 2) / 2;

    // Ã¢â€€Ã¢â€€ FASE 2: Swap â€â€ bProg 17.0 → 17.8 (DESPUÉS de la rotación completa) Ã¢â€€Ã¢â€€
    var swapT       = Math.max(0, Math.min(1, (_bProgM - 17.0) / (17.8 - 17.0)));
    var fullOpacity = 1.0 - swapT;
    var halfOpacity = swapT;

    // Zoom dramático: la cámara se acerca mientras ocurre el crossfade
    // DIST constante â€â€ el zoom se hace por CSS sobre #thermal-overlay
    var DIST = 5.0;
    var vH   = 2 * Math.tan((42 * Math.PI / 180) / 2) * DIST;
    var vW   = vH * (window.innerWidth / window.innerHeight);
    var posX = -0.008 * vW / 2;
    var posY =  0.312 * vH / 2;

    // Ã¢â€€Ã¢â€€ Zoom CSS sobre el overlay completo Ã¢â€€Ã¢â€€
    var zoomScale = 1.0 + swapT * 0.4225;
    var overlay = document.getElementById('thermal-overlay');
    if (overlay) {
      overlay.style.transformOrigin = '50% 30%';
      var scrollUpVh = window._scrollUpVh || 0;
      overlay.style.transform = 'translateY(-' + scrollUpVh + 'vh) scale(' + zoomScale + ')';
    }

    // Ã¢â€€Ã¢â€€ Mapa de calor 2D: fade-in con swapT Ã¢â€€Ã¢â€€
    if (window._drawHeatMap) window._drawHeatMap(swapT);

    var halfPosX = -0.03 * vW / 2;
    var halfPosY =  0.294 * vH / 2;

    // Cerebro COMPLETO: rota hasta perfil lateral completo (~99Â°)
    _brainFull.rotation.y = _rotEase * (-Math.PI * 0.55);
    _brainFull.position.set(posX, posY, -DIST);

    // Cerebro COMPLETO: fade-out con swapT (la imagen 2D lo reemplaza)
    _brainFull.visible = (fullOpacity > 0.01);
    if (_brainFull.visible) {
      _brainFull.traverse(function(c) {
        if (!c.isMesh) return;
        var mats = Array.isArray(c.material) ? c.material : [c.material];
        mats.forEach(function(m) { m.opacity = fullOpacity; });
      });
    }


    _brainRenderer.render(_brainScene, _brainCamera);
  }

  // Funcion global llamada por smoothScrollLoop para sincronizar el reveal
  window._updateBrainReveal = function(tP, maskValue) {
    var canvas = document.getElementById('brain-canvas');
    if (!canvas) return;
    if (tP <= 0) {
      canvas.style.transition = 'none'; // hide instantaneo, sin flash
      canvas.style.opacity = '0';
      canvas.style.webkitMaskImage = '';
      canvas.style.maskImage = '';
    } else {
      canvas.style.transition = '';
      canvas.style.opacity = '1';
      canvas.style.webkitMaskImage = maskValue;
      canvas.style.maskImage = maskValue;
    }
  };

})();
function buildThermalPalette() {
  const stops = [
    [0,    [10,   0,  40]],
    [0.12, [60,   0, 120]],
    [0.25, [130,  0, 160]],
    [0.38, [200, 20, 120]],
    [0.50, [220, 40,  60]],
    [0.62, [240, 90,   0]],
    [0.75, [255,165,   0]],
    [0.88, [255,230,  40]],
    [1.0,  [255,255, 220]],
  ];
  const palette = new Uint8ClampedArray(256 * 3);
  for (let i = 0; i < 256; i++) {
    const t = i / 255;
    let s = stops[0], e = stops[stops.length - 1];
    for (let j = 0; j < stops.length - 1; j++) {
      if (t >= stops[j][0] && t <= stops[j+1][0]) { s = stops[j]; e = stops[j+1]; break; }
    }
    const f = e[0] === s[0] ? 0 : (t - s[0]) / (e[0] - s[0]);
    palette[i*3]   = Math.round(s[1][0] + (e[1][0] - s[1][0]) * f);
    palette[i*3+1] = Math.round(s[1][1] + (e[1][1] - s[1][1]) * f);
    palette[i*3+2] = Math.round(s[1][2] + (e[1][2] - s[1][2]) * f);
  }
  return palette;
}
const THERMAL_PALETTE = buildThermalPalette();

let _thermalModelCanvas = null;
function getThermalModelCanvas(srcImg, w, h) {
  if (_thermalModelCanvas) return _thermalModelCanvas;
  const oc = document.createElement('canvas');
  oc.width = w; oc.height = h;
  const ctx = oc.getContext('2d');
  ctx.drawImage(srcImg, 0, 0, w, h);
  const id = ctx.getImageData(0, 0, w, h);
  const d  = id.data;
  for (let i = 0; i < d.length; i += 4) {
    if (d[i+3] < 10) continue;
    const r = d[i], g = d[i+1], b = d[i+2];
    const skinBoost = (r > g + 25 && r > b + 15) ? 22 : 0;
    const lum = Math.min(255, Math.round(0.299*r + 0.587*g + 0.114*b) + skinBoost);
    const pi  = lum * 3;
    d[i]   = THERMAL_PALETTE[pi];
    d[i+1] = THERMAL_PALETTE[pi+1];
    d[i+2] = THERMAL_PALETTE[pi+2];
  }
  ctx.putImageData(id, 0, 0);
  _thermalModelCanvas = oc;
  return oc;
}

// Ruido pequeño 256Ã—256 escalado
let _bgNoiseCanvas = null;
function getBgNoiseCanvas() {
  if (_bgNoiseCanvas) return _bgNoiseCanvas;
  const S = 256;
  const oc = document.createElement('canvas');
  oc.width = S; oc.height = S;
  const ctx = oc.getContext('2d');
  const id  = ctx.createImageData(S, S);
  const d   = id.data;
  for (let y = 0; y < S; y++) {
    for (let x = 0; x < S; x++) {
      // valor noise rápido con Math.sin hash
      const n1 = (Math.sin(x * 0.07 + y * 0.11) * 0.5 + 0.5);
      const n2 = (Math.sin(x * 0.19 + y * 0.03 + 5.0) * 0.5 + 0.5);
      const n3 = (Math.sin(x * 0.04 - y * 0.17 + 2.7) * 0.5 + 0.5);
      const v  = n1 * 0.5 + n2 * 0.3 + n3 * 0.2;
      const t  = Math.max(0, Math.min(0.52, v * 0.52));
      const pi = Math.round(t * 255) * 3;
      const idx = (y * S + x) * 4;
      d[idx]   = THERMAL_PALETTE[pi];
      d[idx+1] = THERMAL_PALETTE[pi+1];
      d[idx+2] = THERMAL_PALETTE[pi+2];
      d[idx+3] = 255;
    }
  }
  ctx.putImageData(id, 0, 0);
  _bgNoiseCanvas = oc;
  return oc;
}
// Pre-generar en idle para que no bloquee al primer uso
if (typeof requestIdleCallback !== 'undefined') {
  requestIdleCallback(() => getBgNoiseCanvas());
} else {
  setTimeout(() => getBgNoiseCanvas(), 200);
}

function updateThermalCurtain(progress) {
  const canvas = document.getElementById('thermal-canvas');
  if (!canvas) { console.warn('[THERMAL] canvas not found'); return; }
  if (progress <= 0) { canvas.style.display = 'none'; return; }

  console.log('[THERMAL] progress=', progress.toFixed(3));

  const vw = window.innerWidth, vh = window.innerHeight;
  canvas.width  = vw;
  canvas.height = vh;
  canvas.style.display  = 'block';
  canvas.style.zIndex   = '999990'; // override: más alto que todo

  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, vw, vh);

  const curtainH = Math.round(vh * progress);
  const curtainY = vh - curtainH;

  // Diagnóstico: relleno rojo-lila sólido para verificar visibilidad
  ctx.save();
  ctx.beginPath();
  ctx.rect(0, curtainY, vw, curtainH);
  ctx.clip();
  ctx.fillStyle = 'rgba(180, 0, 120, 0.92)';
  ctx.fillRect(0, 0, vw, vh);
  ctx.restore();
}

// Ã¢â€€Ã¢â€€ Driver independiente: lee prog de sessionStorage cada 50ms Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
setInterval(function() {
  var p  = parseFloat(sessionStorage.getItem('dev_prog') || '0');
    var pM = p + 0.5;
  var tP = Math.min(1, Math.max(0, (pM - 16.27) / (17.2 - 16.27)));
  var tc = document.getElementById('thermal-canvas');
  if (!tc) return;
  if (tP <= 0) { tc.style.display = 'none'; return; }
  var vw = window.innerWidth, vh = window.innerHeight;
  var extendedVh = vh * 1.30; // 30vh extra para bajar el corte
  tc.width = vw; tc.height = extendedVh;
  tc.style.position = 'fixed'; tc.style.top = '0'; tc.style.left = '0';
  tc.style.width = '100%'; tc.style.height = '130vh';
  tc.style.zIndex = '9999999'; tc.style.display = 'block'; tc.style.pointerEvents = 'none';
  tc.style.transform = 'translateY(-' + (window._scrollUpVh || 0) + 'vh)';
  var ctx = tc.getContext('2d');
  ctx.clearRect(0, 0, vw, extendedVh);
  ctx.fillStyle = 'rgba(200,0,130,0.95)';
  // Dibujar el fondo púrpura hasta abajo
  ctx.fillRect(0, extendedVh - Math.round(extendedVh * tP), vw, Math.round(extendedVh * tP));
}, 50);


