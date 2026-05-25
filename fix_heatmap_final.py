dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'
with open(dev_file, 'r', encoding='utf-8') as f:
    text = f.read()

old = "    // DIAGNOSTIC MODE: use progress directly as heat (uniform color across brain)\n    // This proves the vertex color system works before adding spatial blobs\n    const globalHeat = Math.max(0.08, progress);"

# Find the full for loop for vertex colors and replace it
start = text.find("    // DIAGNOSTIC MODE")
# Find end of the }; closing the function
end = text.find("\n  };\n", start) + 6

new_inner = """
    function ss(a, b, x) {
      const t = Math.max(0, Math.min(1, (x - a) / (b - a)));
      return t * t * (3 - 2 * t);
    }

    function heatToRGB(h) {
      const stops = [
        [0.00, 0.04, 0.06, 0.35],
        [0.25, 0.00, 0.28, 0.90],
        [0.45, 0.00, 0.72, 0.88],
        [0.62, 0.08, 0.90, 0.40],
        [0.78, 0.80, 0.97, 0.00],
        [0.90, 1.00, 0.65, 0.00],
        [1.00, 1.00, 0.20, 0.00],
      ];
      for (let i = 0; i < stops.length - 1; i++) {
        const [t0,r0,g0,b0] = stops[i], [t1,r1,g1,b1] = stops[i+1];
        if (h >= t0 && h <= t1) {
          const s = ss(t0, t1, h);
          return [r0+s*(r1-r0), g0+s*(g1-g0), b0+s*(b1-b0)];
        }
      }
      return [1.0, 0.20, 0.0];
    }

    for (const {mesh, colors, positions} of window.brainMeshes) {
      const count = positions.length / 3;
      for (let vi = 0; vi < count; vi++) {
        const px = positions[vi*3], py = positions[vi*3+1], pz = positions[vi*3+2];

        // Y is confirmed working — maps superior(1) to inferior(0)
        const yN = Math.max(0, Math.min(1, (py - bbMin.y) / bbSizeY));

        // Spatial noise using raw positions (no normalization needed)
        const noiseA = Math.sin(px * 2.8 + time * 0.4) * Math.cos(pz * 2.5 + time * 0.3);
        const noiseB = Math.sin(pz * 3.1 + time * 0.5) * Math.cos(px * 2.2 + time * 0.35);
        const noise = (noiseA + noiseB) * 0.12;

        // Phase 1 — Small Talk: language areas = mid-low Y (temporal)
        const lang = ss(0.20, 0.42, yN) * (1 - ss(0.52, 0.68, yN));
        const act1 = Math.min(1, lang * 0.9 + noise);

        // Phase 2 — Profundizando: prefrontal = high Y + anterior cingulate = mid-high Y
        const pfc = ss(0.62, 0.85, yN);
        const cing = ss(0.45, 0.62, yN) * (1 - ss(0.68, 0.82, yN));
        const act2 = Math.min(1, pfc * 0.92 + cing * 0.70 + lang * 0.30 + noise);

        // Phase 3 — Conexión Profunda: limbic = low Y (amygdala/hippocampus) + prefrontal
        const limbic = (1 - ss(0.15, 0.40, yN));
        const act3 = Math.min(1, limbic * 0.92 + pfc * 0.70 + cing * 0.65 + noise);

        const p = progress;
        let activity;
        if      (p <= 0.33) { const s = ss(0,0.33,p);      activity = act1 * s; }
        else if (p <= 0.66) { const s = ss(0.33,0.66,p);   activity = act1*(1-s) + act2*s; }
        else                { const s = ss(0.66,1.0,p);    activity = act2*(1-s) + act3*s; }

        const heat = Math.min(1, Math.max(0, 0.18 + activity * 0.82));
        const [r, g, b] = heatToRGB(heat);
        colors[vi*3] = r; colors[vi*3+1] = g; colors[vi*3+2] = b;
      }
      mesh.geometry.attributes.color.needsUpdate = true;
    }
  };
"""

text = text[:start] + new_inner + text[end:]
with open(dev_file, 'w', encoding='utf-8') as f:
    f.write(text)
print("Done! Y-based anatomical heatmap applied.")
