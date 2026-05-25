import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# TARGETED FIX: Make gyri wider/thicker
# 1. Lower primary frequency: 2.3 -> 1.6 (fewer, bigger folds)
# 2. Adjust smoothstep range to push more area to "gyrus" side (wide tops)
# 3. Keep secondary freq but reduce its weight

old_gyri = """      float computeGyri(vec3 p) {
        // Domain warp: single layer, moderate (avoid crystal artifacts from 2 layers)
        vec3 q = vec3(
          snoise(p * 1.5 + vec3(0.0, 0.0, 0.0)),
          snoise(p * 1.5 + vec3(3.7, 1.5, 2.8)),
          snoise(p * 1.5 + vec3(2.3, 4.7, 1.1))
        );
        vec3 wp = p + q * 0.35;

        // PRIMARY GYRI: frequency 2.3 = about 7-8 ridges visible on the brain
        // 1 - |snoise| = ridges at zero-crossings, winding organically
        float g1 = 1.0 - abs(snoise(wp * 2.3));
        // pow(1.1) = gentle sharpening: rounded peaks but DEFINED valleys
        g1 = pow(max(g1, 0.0), 1.15);

        // SECONDARY DETAIL: slightly higher frequency for texture within gyri
        float g2 = 1.0 - abs(snoise(wp * 4.2 + vec3(1.5)));
        g2 = pow(max(g2, 0.0), 1.5);

        // Combined: primary dominant so large folds clearly visible
        float combined = g1 * 0.72 + g2 * 0.28;

        // Critical: return full range 0->1 with clear separation
        // smoothstep with wide range to keep both valleys AND peaks well defined
        return smoothstep(0.0, 0.95, combined);
      }"""

new_gyri = """      float computeGyri(vec3 p) {
        // Domain warp
        vec3 q = vec3(
          snoise(p * 1.5 + vec3(0.0, 0.0, 0.0)),
          snoise(p * 1.5 + vec3(3.7, 1.5, 2.8)),
          snoise(p * 1.5 + vec3(2.3, 4.7, 1.1))
        );
        vec3 wp = p + q * 0.35;

        // PRIMARY GYRI: frequency 1.6 = FEWER, THICKER folds (closer to real brain)
        float g1 = 1.0 - abs(snoise(wp * 1.6));
        g1 = pow(max(g1, 0.0), 1.1);

        // SECONDARY DETAIL: medium frequency for sub-folds
        float g2 = 1.0 - abs(snoise(wp * 3.5 + vec3(1.5)));
        g2 = pow(max(g2, 0.0), 1.4);

        // Combined: primary strongly dominant
        float combined = g1 * 0.78 + g2 * 0.22;

        // smoothstep: push more area to gyrus-side (0.15..1.0 range)
        // Values > 0.15 become gyri, only lowest ~15% become sulci
        // This means gyri are WIDE and sulci are NARROW - like real brain
        return smoothstep(0.15, 1.0, combined);
      }"""

if old_gyri in text:
    text = text.replace(old_gyri, new_gyri)
    print("computeGyri updated successfully")
else:
    print("Could not find computeGyri to replace - doing regex fallback")
    text = re.sub(
        r'float computeGyri\(vec3 p\) \{.*?return smoothstep\(0\.0, 0\.95, combined\);\s*\}',
        new_gyri,
        text,
        flags=re.DOTALL
    )

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done: Thicker gyri applied.")
