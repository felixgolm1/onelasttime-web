# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Replace the hardcoded 1.25 with the dynamic perspective compensation
old_code = '''globalGlbCard.scale.setScalar(lc.scale * boardScale * 1.25);'''

new_code = '''// Compensacion de perspectiva: al alejarse del centro, la camara 3D lo hace ver mas pequeno.
                  // Calculamos la distancia real a la lente y escalamos proporcionalmente para mantener tamano visual 2D constante.
                  const currentDist = Math.sqrt(
                      Math.pow(globalGlbCard.position.x, 2) + 
                      Math.pow(globalGlbCard.position.y, 2) + 
                      Math.pow(DIST, 2)
                  );
                  const perspectiveComp = currentDist / DIST;
                  
                  globalGlbCard.scale.setScalar(lc.scale * boardScale * perspectiveComp);'''

content = content.replace(old_code, new_code)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
