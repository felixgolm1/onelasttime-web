import re

def main():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove the old polaroid HTML
    start_tag = '<div id="olt-final-text"'
    end_tag = '</div>\n  </div>\n</div>'
    
    start_idx = html.find(start_tag)
    if start_idx != -1:
        # Find the end of this div manually or use regex
        # It's inside a structure. Let's use regex to find the block.
        # Looking at the code, it ends right before `<a href="arbol.html" id="olt-final-cta"`
        end_idx = html.find('<a href="arbol.html" id="olt-final-cta"')
        if end_idx != -1:
            html = html[:start_idx] + html[end_idx:]

    # 2. Add camera lerp logic in updateGlobalScenes()
    lerp_logic = """
              // Camera flies back to top
              if (typeof camera !== 'undefined' && typeof THREE !== 'undefined' && typeof CAM_LOOK !== 'undefined') {
                  let targetCamPos = new THREE.Vector3(-0.3, 12, 3);
                  let targetCamLook = new THREE.Vector3(0, 0, 0);
                  camera.position.lerp(targetCamPos, polProg);
                  CAM_LOOK.lerp(targetCamLook, polProg);
              }
              
              // Shadow becomes smaller and sharper as it lands
"""
    html = html.replace('// Shadow becomes smaller and sharper as it lands\n', lerp_logic)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
