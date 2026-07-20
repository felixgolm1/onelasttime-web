import re

def main():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix the camera lerp to use CAM_BASE instead of camera.position
    old_camera_code = """              // Camera flies back to top
              if (typeof camera !== 'undefined' && typeof THREE !== 'undefined' && typeof CAM_LOOK !== 'undefined') {
                  let targetCamPos = new THREE.Vector3(-0.3, 12, 3);
                  camera.position.lerp(targetCamPos, polProg);
                  
                  CAM_LOOK.x += (0 - CAM_LOOK.x) * polProg;
                  CAM_LOOK.y += (0 - CAM_LOOK.y) * polProg;
                  CAM_LOOK.z += (0 - CAM_LOOK.z) * polProg;
              }"""
              
    new_camera_code = """              // Camera flies back to top
              if (typeof CAM_BASE !== 'undefined' && typeof CAM_LOOK !== 'undefined') {
                  CAM_BASE.x += (-0.3 - CAM_BASE.x) * polProg;
                  CAM_BASE.y += (12 - CAM_BASE.y) * polProg;
                  CAM_BASE.z += (3 - CAM_BASE.z) * polProg;
                  
                  CAM_LOOK.x += (0 - CAM_LOOK.x) * polProg;
                  CAM_LOOK.y += (0 - CAM_LOOK.y) * polProg;
                  CAM_LOOK.z += (0 - CAM_LOOK.z) * polProg;
              }"""
              
    html = html.replace(old_camera_code, new_camera_code)

    # Force the polaroid to be ultra visible
    old_transform = "polCont.style.transform = `translate3d(${swayX}px, ${yPos}vh, 0px) rotateX(${rotX}deg) rotateY(${rotY}deg) rotateZ(${rotZ}deg)`;"
    new_transform = "polCont.style.transform = `translate3d(${swayX}px, ${yPos}vh, 0px) rotateX(${rotX}deg) rotateY(${rotY}deg) rotateZ(${rotZ}deg)`;\n              polCont.style.zIndex = '999999';\n              polCont.style.display = 'block';"
    
    html = html.replace(old_transform, new_transform)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
