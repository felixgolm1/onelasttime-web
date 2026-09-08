import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

new_shader = """const polaroidShader = {
        uniforms: {
          tDiffuse: { value: photoTex },
          uProgress: { value: 0.0 } // 0.0 = borrosa/blanca, 1.0 = nitida
        },
        vertexShader: `
          varying vec2 vUv;
          void main() {
            // Zoom out un 20% para que no quede recortado por los lados si el aspecto lo requiere
            float zoom = 1.2;
            vUv = (uv - 0.5) * vec2(1.0, 0.5625) * zoom + vec2(0.5, 0.5);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          uniform sampler2D tDiffuse;
          uniform float uProgress;
          varying vec2 vUv;
          void main() {
            vec3 baseColor = vec3(0.1, 0.15, 0.12);
            vec4 c;
            
            if (vUv.x < 0.0 || vUv.x > 1.0 || vUv.y < 0.0 || vUv.y > 1.0) {
                // Fuera del encuadre del video (mismo color base oscuro de la foto polaroid)
                c = vec4(baseColor, 1.0);
            } else {
                c = texture2D(tDiffuse, vUv);
            }
            
            // Mezclar con la foto usando un curve no lineal para que suba rapido
            float mixAmt = smoothstep(0.0, 0.8, uProgress);
            vec3 finalColor = mix(baseColor, c.rgb, mixAmt);
            
            // Anadir un efecto de "quemado" o "brillo" inicial que se desvanece
            float flash = (1.0 - smoothstep(0.0, 0.3, uProgress)) * 0.8;
            finalColor += vec3(flash);
            
            gl_FragColor = vec4(finalColor, 1.0);
          }
        `
      };"""

pattern = re.compile(r'const polaroidShader = \{.*?fragmentShader: `.*?`\s*\};', re.DOTALL)
text = pattern.sub(new_shader, text)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(text)
