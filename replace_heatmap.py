dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the updateBrainVertexColors function with the calibrated version
old_func_start = "  // Called every frame to update vertex colors\n  window.updateBrainVertexColors = function(progress, time) {"
old_func_end = "  // brainMat is no longer needed as a shader"

start_idx = text.find(old_func_start)
end_idx = text.find(old_func_end)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Could not find function block")
    print("start:", start_idx, "end:", end_idx)
else:
    new_func = """  // Called every frame to update vertex colors
  window.updateBrainVertexColors = function(progress, time) {
    if (!window.brainMeshes || !window.brainMeshes.length) return;
    if (!window.brainBBMin || !window.brainBBMax) return;

    const bbMin = window.brainBBMin;
    const bbMax = window.brainBBMax;
    const bbSizeX = (bbMax.x - bbMin.x) || 1;
    const bbSizeY = (bbMax.y - bbMin.y) || 1;
    const bbSizeZ = (bbMax.z - bbMin.z) || 1;

    // ==========================================
    // PREMIUM fMRI PALETTE (Oryzo-style)
    // Dark navy baseline → Electric blue → Cyan → Green-lime → Yellow-gold → Orange
    // Inactive regions are ALWAYS visible (dark blue, never black)
    // ==========================================
    function heatToRGB(heat) {
      // 6 color stops with smooth hermite interpolation (smoothstep between each pair)
      const stops = [
        [0.00,  0.01, 0.03, 0.22],  // deep navy (resting state)
        [0.20,  0.00, 0.18, 0.75],  // deep blue
        [0.42,  0.00, 0.55, 0.95],  // electric blue-cyan
        [0.62,  0.00, 0.88, 0.62],  // cyan-green
        [0.78,  0.72, 0.96, 0.00],  // yellow-green
        [0.90,  1.00, 0.72, 0.00],  // yellow-orange
        [1.00,  1.00, 0.28, 0.00],  // warm orange
      ];
      for (let i = 0; i < stops.length - 1; i++) {
        const [t0,r0,g0,b0] = stops[i];
        const [t1,r1,g1,b1] = stops[i+1];
        if (heat >= t0 && heat <= t1) {
          // Hermite smoothstep for ultra-smooth transition
          const t = (heat - t0) / (t1 - t0);
          const s = t * t * (3 - 2 * t); // smoothstep
          return [r0 + s*(r1-r0), g0 + s*(g1-g0), b0 + s*(b1-b0)];
        }
      }
      return [1.0, 0.28, 0.0]; // fallback orange
    }

    // Gaussian activation blob
    function blob(nx, ny, nz, cx, cy, cz, sigma) {
      const dx = nx-cx, dy = ny-cy, dz = nz-cz;
      return Math.exp(-(dx*dx + dy*dy + dz*dz) / (2*sigma*sigma));
    }

    for (const {mesh, colors, positions} of window.brainMeshes) {
      const count = positions.length / 3;

      for (let vi = 0; vi < count; vi++) {
        const px = positions[vi*3];
        const py = positions[vi*3+1];
        const pz = positions[vi*3+2];

        // Normalized [0..1] in brain bounding box
        // Z=1 → anterior/frontal, Z=0 → posterior/occipital
        // Y=1 → superior/dorsal, Y=0 → inferior/basal
        const nx = (px - bbMin.x) / bbSizeX;
        const ny = (py - bbMin.y) / bbSizeY;
        const nz = (pz - bbMin.z) / bbSizeZ;

        // ==============================================
        // PHASE 1 — SMALL TALK
        // Dominant: language areas (Broca + Wernicke + auditory cortex)
        // ==============================================
        const broca    = blob(nx,ny,nz, 0.48, 0.30, 0.80, 0.13) * 0.85; // frontal-inferior
        const wernicke = blob(nx,ny,nz, 0.50, 0.42, 0.33, 0.12) * 0.80; // posterior-temporal
        const auditory = blob(nx,ny,nz, 0.50, 0.30, 0.45, 0.11) * 0.65; // temporal superior
        const motor    = blob(nx,ny,nz, 0.50, 0.85, 0.58, 0.10) * 0.45; // motor mouth area
        const act1 = Math.min(1.0, broca + wernicke + auditory + motor);

        // ==============================================
        // PHASE 2 — PROFUNDIZANDO
        // Growing: prefrontal cortex + ACC + insula + TPJ
        // Fading: language areas
        // ==============================================
        const dlpfc    = blob(nx,ny,nz, 0.50, 0.72, 0.86, 0.16) * 0.90; // dorsolateral prefrontal
        const vlpfc    = blob(nx,ny,nz, 0.50, 0.48, 0.90, 0.12) * 0.70; // ventrolateral prefrontal
        const acc      = blob(nx,ny,nz, 0.50, 0.62, 0.62, 0.11) * 0.75; // anterior cingulate
        const insula   = blob(nx,ny,nz, 0.50, 0.48, 0.58, 0.10) * 0.65; // insula
        const tpj      = blob(nx,ny,nz, 0.50, 0.58, 0.32, 0.13) * 0.70; // temporoparietal junction
        const act2 = Math.min(1.0, dlpfc + vlpfc + acc * 0.7 + insula * 0.6 + tpj * 0.6
                               + wernicke * 0.35 + broca * 0.25);

        // ==============================================
        // PHASE 3 — CONEXION PROFUNDA
        // Peak: limbic system + hippocampus + amygdala + insula + orbitofrontal
        // All social-emotional brain on fire
        // ==============================================
        const amygdala   = blob(nx,ny,nz, 0.50, 0.25, 0.56, 0.10) * 0.92; // amygdala
        const hippocampus= blob(nx,ny,nz, 0.50, 0.22, 0.50, 0.09) * 0.88; // hippocampus
        const pcc        = blob(nx,ny,nz, 0.50, 0.60, 0.28, 0.13) * 0.80; // posterior cingulate
        const ofc        = blob(nx,ny,nz, 0.50, 0.32, 0.88, 0.11) * 0.78; // orbitofrontal
        const cingulate2 = blob(nx,ny,nz, 0.50, 0.70, 0.55, 0.12) * 0.75; // mid cingulate
        const act3 = Math.min(1.0, amygdala + hippocampus + pcc + dlpfc * 0.8
                               + insula * 0.9 + tpj * 0.8 + ofc * 0.7 + cingulate2 * 0.65);

        // ==============================================
        // BLEND BETWEEN PHASES (smooth hermite interpolation)
        // ==============================================
        const p = progress;
        let regionActivity;

        if (p <= 0.33) {
          // Pure small talk growing from nothing
          const t = p / 0.33;
          const s = t*t*(3-2*t);
          regionActivity = act1 * s;
        } else if (p <= 0.66) {
          // Transition from small talk to profundizando
          const t = (p - 0.33) / 0.33;
          const s = t*t*(3-2*t);
          regionActivity = act1 * (1-s) + act2 * s;
        } else {
          // Transition from profundizando to conexion profunda
          const t = (p - 0.66) / 0.34;
          const s = t*t*(3-2*t);
          regionActivity = act2 * (1-s) + act3 * s;
        }

        // BASE ACTIVITY: All regions have a slight baseline (dark blue resting state)
        // This ensures the brain never goes completely black — always shows anatomy
        const BASE_HEAT = 0.08;
        
        // Subtle pulsing "neural noise" — simulates ongoing brain activity
        const pulse = (Math.sin(px*2.3 + time*0.9) * Math.cos(py*2.7 + time*0.7)
                     + Math.sin(pz*2.1 + time*0.8) * 0.5) * 0.04;

        const heat = Math.min(1.0, Math.max(0.0, BASE_HEAT + regionActivity * 0.92 + pulse));

        const [r, g, b] = heatToRGB(heat);
        colors[vi*3]   = r;
        colors[vi*3+1] = g;
        colors[vi*3+2] = b;
      }
      mesh.geometry.attributes.color.needsUpdate = true;
    }
  };

  """

    # Build new text
    text = text[:start_idx] + new_func + text[end_idx:]
    with open(dev_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Calibrated neuroscientific heatmap applied!")
