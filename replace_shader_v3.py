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
        end_line = i + 2
        break

print(f"Replacing lines {start_line+1} to {end_line}")

# This completely replaces the shader+material block with a vertex-color approach
# brainMat is now just a reference; real material comes from the model
new_block = '''  // ---- BRAIN VERTEX-COLOR HEATMAP ----
  // Strategy: keep original GLB material (preserves wrinkles/anatomy detail),
  // but add vertex colors driven by anatomical region activation.
  // Each frame we recompute vertex colors based on uProgress.

  // Helper: Gaussian blob activation
  function brainBlob(normPos, cx, cy, cz, sigma) {
    const dx = normPos.x - cx, dy = normPos.y - cy, dz = normPos.z - cz;
    const d2 = dx*dx + dy*dy + dz*dz;
    return Math.exp(-d2 / (2.0 * sigma * sigma));
  }

  // fMRI palette: blue-cyan-green-yellow-orange-red
  function heatToRGB(heat) {
    const stops = [
      [0.00, 0.00, 0.00, 0.22],
      [0.16, 0.00, 0.30, 0.90],
      [0.33, 0.00, 0.78, 0.85],
      [0.50, 0.10, 0.88, 0.30],
      [0.66, 0.95, 0.92, 0.00],
      [0.83, 1.00, 0.45, 0.00],
      [1.00, 1.00, 0.05, 0.05],
    ];
    let r=stops[0][1], g=stops[0][2], b=stops[0][3];
    for (let i=0; i<stops.length-1; i++) {
      const [t0,r0,g0,b0] = stops[i];
      const [t1,r1,g1,b1] = stops[i+1];
      if (heat >= t0 && heat <= t1) {
        const t = (heat-t0)/(t1-t0);
        // smoothstep
        const s = t*t*(3-2*t);
        r = r0 + s*(r1-r0);
        g = g0 + s*(g1-g0);
        b = b0 + s*(b1-b0);
        break;
      }
    }
    return {r, g, b};
  }

  // Keeps track of all meshes + their geometry for vertex color updates
  window.brainMeshes = [];

  // Called every frame to update vertex colors
  window.updateBrainVertexColors = function(progress, time) {
    if (!window.brainMeshes.length) return;

    const bbMin = brainUniforms.uBrainMin.value;
    const bbMax = brainUniforms.uBrainMax.value;
    const bbSize = new THREE.Vector3().subVectors(bbMax, bbMin);

    for (const {mesh, colors, positions} of window.brainMeshes) {
      const count = positions.length / 3;

      for (let vi = 0; vi < count; vi++) {
        const px = positions[vi*3];
        const py = positions[vi*3+1];
        const pz = positions[vi*3+2];

        // Normalized position in [0,1] bounding box
        const nx = bbSize.x > 0 ? (px - bbMin.x) / bbSize.x : 0.5;
        const ny = bbSize.y > 0 ? (py - bbMin.y) / bbSize.y : 0.5;
        const nz = bbSize.z > 0 ? (pz - bbMin.z) / bbSize.z : 0.5;
        const norm = {x: nx, y: ny, z: nz};

        // ---- ANATOMICAL REGIONS (normalized brain space) ----
        // Assumes: Z=anterior(1)/posterior(0), Y=superior(1)/inferior(0)

        // Phase 1 - Small Talk: Broca's + Wernicke's + Temporal
        const broca     = brainBlob(norm, 0.50, 0.35, 0.80, 0.14);
        const wernicke  = brainBlob(norm, 0.50, 0.38, 0.38, 0.13);
        const temporal  = brainBlob(norm, 0.50, 0.12, 0.50, 0.16);
        const temporal2 = brainBlob(norm, 0.50, 0.18, 0.65, 0.12);
        const act1 = broca*0.9 + wernicke*0.7 + temporal*0.55 + temporal2*0.45;

        // Phase 2 - Profundizando: Prefrontal + Motor + sustained temporal
        const prefrontal  = brainBlob(norm, 0.50, 0.75, 0.88, 0.18);
        const prefrontal2 = brainBlob(norm, 0.50, 0.60, 0.92, 0.12);
        const motor       = brainBlob(norm, 0.50, 0.85, 0.58, 0.14);
        const insula      = brainBlob(norm, 0.50, 0.45, 0.65, 0.10);
        const act2 = prefrontal*0.85 + prefrontal2*0.65 + motor*0.55 + insula*0.50 + temporal*0.35 + broca*0.25;

        // Phase 3 - Conexion Profunda: Limbic + Hippocampus + Amygdala + all
        const limbic      = brainBlob(norm, 0.50, 0.28, 0.52, 0.14);
        const hippocampus = brainBlob(norm, 0.50, 0.20, 0.48, 0.10);
        const amygdala    = brainBlob(norm, 0.50, 0.22, 0.58, 0.09);
        const parietal    = brainBlob(norm, 0.50, 0.78, 0.38, 0.16);
        const cingulate   = brainBlob(norm, 0.50, 0.55, 0.58, 0.12);
        const act3 = limbic*0.9 + hippocampus*0.85 + amygdala*0.80 + prefrontal*0.70 + parietal*0.55 + cingulate*0.65 + temporal*0.50;

        // Blend between phases
        const p = progress;
        let regionActivity;
        if (p < 0.33) {
          regionActivity = act1 * (p / 0.33);
        } else if (p < 0.66) {
          const t = (p - 0.33) / 0.33;
          const s = t*t*(3-2*t); // smoothstep
          regionActivity = act1 * (1-s) + act2 * s;
        } else {
          const t = (p - 0.66) / 0.34;
          const s = t*t*(3-2*t);
          regionActivity = act2 * (1-s) + act3 * s;
        }

        // Small pulsing noise based on position + time (simulates neural firing)
        const noiseX = Math.sin(px*3.1 + time*0.8) * Math.cos(py*2.7 + time*0.6);
        const noiseY = Math.sin(pz*2.9 + time*0.7) * Math.cos(px*3.3 + time*0.5);
        const pulse = (noiseX + noiseY) * 0.06;

        const heat = Math.min(1.0, Math.max(0.0, regionActivity + pulse));

        const {r, g, b} = heatToRGB(heat);
        colors[vi*3]   = r;
        colors[vi*3+1] = g;
        colors[vi*3+2] = b;
      }
      mesh.geometry.attributes.color.needsUpdate = true;
    }
  };

  // brainMat is no longer needed as a shader — we use vertex colors on original material
  const brainMat = null; // placeholder to avoid undefined errors below
'''

lines[start_line:end_line] = [new_block]

with open(dev_file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Replaced shader block with vertex-color approach. Lines {start_line+1} to {end_line}")
