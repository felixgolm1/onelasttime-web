import sys, re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. SHAPE FIX in vertex shader
old_shape = """        // 1. ELLIPSOID SHAPE
        vec3 baseShape = position * vec3(1.0, 0.80, 1.20);"""

new_shape = """        // 1. ANATOMICAL ELLIPSOID
        // From side view: flatter top-bottom, elongated front-back, moderate width
        vec3 baseShape = position * vec3(1.15, 0.78, 1.30);

        // TEMPORAL LOBE BULGE: widen the sides at mid-inferior level
        // (This creates the distinctive widening seen in the reference image)
        float tempFactor = smoothstep(0.0, -0.8, baseShape.y)   // active below equator
                         * smoothstep(0.8, 1.0, abs(baseShape.x / 1.15)); // at lateral edges
        baseShape.x += sign(baseShape.x) * tempFactor * 0.18;

        // FRONTAL POLE: slightly flatten the anterior face (frontal lobe is more vertical)
        if (baseShape.z > 0.7) baseShape.z = 0.7 + (baseShape.z - 0.7) * 0.65;

        // OCCIPITAL POLE: slightly taper the posterior (back narrows slightly at top)
        if (baseShape.z < -0.6 && baseShape.y > 0.2) {
          baseShape.x *= 1.0 - 0.15 * smoothstep(-0.6, -1.3, baseShape.z);
        }"""

old_inferior = """        // Flatten inferior surface (anatomically more flat)
        if (displaced.y < 0.0) {
          displaced.y *= 0.70;
          displaced.x *= 1.0 + 0.07 * (-displaced.y);
        }"""

new_inferior = """        // FLATTEN INFERIOR: brain base is almost flat (rests on skull base)
        if (displaced.y < 0.0) {
          float flattenT = -displaced.y; // 0 at equator, 1 at bottom pole
          displaced.y *= mix(1.0, 0.45, flattenT);
          // Temporal lobes widen more at inferior
          displaced.x *= 1.0 + 0.09 * flattenT;
        }"""

text = text.replace(old_shape, new_shape)
text = text.replace(old_inferior, new_inferior)

# 2. CAMERA: move closer and tilt for 3/4 view like reference image
old_cam = "window.brainCam.position.set(0, 0, 5.2);\n    window.brainCam.lookAt(0, 0, 0);"
new_cam = """window.brainCam.position.set(-1.0, 0.6, 4.2); // 3/4 view like reference
    window.brainCam.lookAt(0.0, -0.1, 0.0);"""

text = text.replace(old_cam, new_cam)

# 3. Make the brain bigger: increase R
text = text.replace('const R = 1.0;', 'const R = 1.35;')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Shape fixes applied: temporal bulge, flat base, 3/4 camera.")
