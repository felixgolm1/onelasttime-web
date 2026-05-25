import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace ONLY the fragment shader color/lighting section
old_frag_end = """        // ── COLOR RAMP ────────────────────────────────────────────────────
        vec3 col = petColor(heat);

        // ── SULCI DARKENING (vNoise used as AO) ───────────────────────────
        // Spec: "multiply final color by vNoise so cracks are darker"
        float sulciAO = vNoise * vNoise;                  // quadratic: sulci = black
        sulciAO *= mix(0.02, 1.0, 1.0 - vFissure * 0.9); // fissure very dark

        col = col * sulciAO * diff;

        // Specular on gyri ridges
        vec3 H    = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 55.0) * 0.20 * vNoise;
        col += vec3(spec);

        // Rim glow (edge subsurface scattering)
        float fresnel = pow(1.0 - max(dot(V, N), 0.0), 2.2);
        vec3 rimCol   = mix(vec3(0.20, 0.0, 0.50), vec3(1.0, 0.45, 0.0), heat);
        col += rimCol * fresnel * 0.35;

        gl_FragColor = vec4(col, 1.0);"""

new_frag_end = """        // ── BASE AMBIENT HEAT: cold areas = rich purple, NOT black ──────
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

if old_frag_end in text:
    text = text.replace(old_frag_end, new_frag_end)
    print("Fragment shader lighting/color fixed.")
else:
    print("ERROR: Could not find target. Trying regex...")
    text = re.sub(
        r'// ── COLOR RAMP.*?gl_FragColor = vec4\(col, 1\.0\);',
        new_frag_end,
        text,
        flags=re.DOTALL
    )
    print("Regex replacement applied.")

# Also boost Bloom slightly for the Oryzo glow feel
bloom = "const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.2, 0.6, 0.40);"
text = re.sub(r'const bloomPass = new THREE\.UnrealBloomPass\(.*?\);', bloom, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done.")
