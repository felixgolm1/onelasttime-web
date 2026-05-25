import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the ENTIRE fragment color section
old_color_section = """        // ── BASE AMBIENT HEAT: cold areas = rich purple, NOT black ──────
        // Like Oryzo: even "cold" zones show saturated purple/indigo
        float baseHeat = 0.32; // Minimum heat so surface is always colorful
        heat = baseHeat + heat * (1.0 - baseHeat); // Remap: 0->0.32, 1->1.0

        // ── COLOR RAMP ────────────────────────────────────────────────────
        vec3 col = petColor(heat);

        // ── SULCI DARKENING ───────────────────────────────────────────────
        // GENTLE AO: sulci are DARKER purple, not black
        // Oryzo style: everything stays colored, just different brightness
        float sulciAO = mix(0.22, 1.0, vNoise);          // min 0.22 = dark but colored
        sulciAO *= mix(0.15, 1.0, 1.0 - vFissure * 0.8); // fissure: darkest

        // Much brighter ambient so the whole brain surface is visible
        float brightDiff = diff * 0.7 + 0.45; // bumped ambient from 0.22 to 0.45

        col = col * sulciAO * brightDiff;

        // Specular on gyri ridges - adds bright white highlights
        vec3 H    = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 45.0) * 0.28 * vNoise;
        col += vec3(spec * 0.6, spec * 0.3, spec * 0.8); // Purple-tinted specular

        // Rim glow: Oryzo-style edge light
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 1.8);
        vec3 rimCol = mix(vec3(0.50, 0.0, 0.80), vec3(1.0, 0.50, 0.0), heat);
        col += rimCol * fresnel * 0.50;

        gl_FragColor = vec4(col, 1.0);"""

new_color_section = """        // ══════════════════════════════════════════════════════════════
        // ORYZO-STYLE THERMAL MAP: Multiple activity clusters at varying temps
        // ══════════════════════════════════════════════════════════════

        // ── RESTING STATE ACTIVITY (always on, baseline brain) ─────────────
        // Simulates the brain's constant background metabolic activity
        // Different clusters = different functional regions at rest
        float bgHeat = 0.0;

        // Default Mode Network (high baseline): medial prefrontal + posterior cingulate
        bgHeat += petZone(vWorldPos, vec3( 0.0,  0.35,  0.60), 0.55) * 0.30; // medial PFC
        bgHeat += petZone(vWorldPos, vec3( 0.0,  0.10, -0.50), 0.50) * 0.25; // posterior cingulate

        // Sensorimotor cortex (moderate): bilateral, central band
        bgHeat += petZone(vWorldPos, vec3( 0.55, 0.30,  0.10), 0.45) * 0.22; // right motor
        bgHeat += petZone(vWorldPos, vec3(-0.55, 0.30,  0.10), 0.45) * 0.20; // left motor

        // Visual cortex (low-moderate): posterior
        bgHeat += petZone(vWorldPos, vec3( 0.30, 0.05, -0.65), 0.40) * 0.18; // right V1
        bgHeat += petZone(vWorldPos, vec3(-0.30, 0.05, -0.65), 0.40) * 0.18; // left V1

        // Temporal lobe language areas (low)
        bgHeat += petZone(vWorldPos, vec3( 0.65, 0.05,  0.20), 0.35) * 0.14; // Wernicke R
        bgHeat += petZone(vWorldPos, vec3(-0.65, 0.05,  0.20), 0.35) * 0.12; // Wernicke L

        // Cerebellum-ish: inferior regions
        bgHeat += petZone(vWorldPos, vec3( 0.30,-0.45,  0.15), 0.35) * 0.12;
        bgHeat += petZone(vWorldPos, vec3(-0.30,-0.45,  0.15), 0.35) * 0.10;

        // FBM noise over the background = organic granular texture (PET scan look)
        float organicNoise = fbm(vWorldPos * 5.0 + uTime * 0.12) * 0.10
                           + fbm(vWorldPos * 10.0) * 0.04;
        bgHeat += organicNoise;

        bgHeat = clamp(bgHeat, 0.0, 0.55); // bg max = warm (never hot)

        // ── PHASE-SPECIFIC HOT ZONES (very hot when active) ────────────────
        float phaseHeat = heat1 * w1 + heat2 * w2 + heat3 * w3;
        phaseHeat += 0.04 * sin(uTime * 4.5) * max(w1, max(w2, w3));
        phaseHeat = clamp(phaseHeat, 0.0, 1.0);

        // Merge: base indigo (0.05) + background activity + phase heat
        // Phase heat dominates when active
        float totalHeat = 0.05 + bgHeat + phaseHeat * (1.0 - bgHeat * 0.4);
        totalHeat = clamp(totalHeat, 0.0, 1.0);

        // ── 6-STOP COLOR RAMP (Oryzo palette) ─────────────────────────────
        // cold: deep indigo → purple → magenta → red → orange → yellow-white: hot
        vec3 col;
        {
          float t = totalHeat;
          vec3 k0 = vec3(0.04, 0.01, 0.22);  // deep indigo (Oryzo cold bg)
          vec3 k1 = vec3(0.32, 0.02, 0.52);  // rich purple
          vec3 k2 = vec3(0.78, 0.08, 0.48);  // hot magenta
          vec3 k3 = vec3(0.95, 0.25, 0.05);  // red-orange
          vec3 k4 = vec3(1.00, 0.58, 0.00);  // orange
          vec3 k5 = vec3(1.00, 0.92, 0.20);  // yellow-white
          if      (t < 0.20) col = mix(k0, k1, t / 0.20);
          else if (t < 0.40) col = mix(k1, k2, (t-0.20)/0.20);
          else if (t < 0.60) col = mix(k2, k3, (t-0.40)/0.20);
          else if (t < 0.80) col = mix(k3, k4, (t-0.60)/0.20);
          else               col = mix(k4, k5, (t-0.80)/0.20);
        }

        // ── SULCI DARKENING ────────────────────────────────────────────────
        // Sulci are darker version of same hue (not black) so gyri are visible
        float sulciAO = mix(0.28, 1.0, vNoise);
        sulciAO *= mix(0.18, 1.0, 1.0 - vFissure * 0.85);

        // Lighting
        col = col * sulciAO * (diff * 0.65 + 0.45);

        // Specular: cool purple highlight on gyri ridges
        vec3 H    = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 45.0) * 0.22 * vNoise;
        col += mix(vec3(0.3,0.0,0.7), vec3(1.0,0.7,0.3), totalHeat) * spec;

        // Rim glow: strong purple-to-orange like Oryzo
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 1.8);
        vec3 rimCol   = mix(vec3(0.45, 0.0, 0.85), vec3(1.0, 0.50, 0.0), totalHeat);
        col += rimCol * fresnel * 0.55;

        gl_FragColor = vec4(col, 1.0);"""

if old_color_section in text:
    text = text.replace(old_color_section, new_color_section)
    print("Full thermal map with resting state networks injected.")
else:
    print("WARNING: Could not find exact match. Trying to locate and replace...")
    # Find between the heat calculation and gl_FragColor
    idx = text.find("// ── BASE AMBIENT HEAT")
    idx2 = text.find("gl_FragColor = vec4(col, 1.0);", idx) + len("gl_FragColor = vec4(col, 1.0);")
    if idx > 0 and idx2 > idx:
        text = text[:idx] + new_color_section + text[idx2:]
        print("Range replacement done.")
    else:
        print("ERROR: Could not find replacement range.")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done.")
