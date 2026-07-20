import re

def main():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Make the table huge so it never cuts off
    html = html.replace('new THREE.PlaneGeometry(60,60)', 'new THREE.PlaneGeometry(300,300)')

    # Fix the camera target and polaroid transform
    old_code = """              // Camera flies back to top
              if (typeof CAM_BASE !== 'undefined' && typeof CAM_LOOK !== 'undefined') {
                  CAM_BASE.x += (-0.3 - CAM_BASE.x) * polProg;
                  CAM_BASE.y += (12 - CAM_BASE.y) * polProg;
                  CAM_BASE.z += (3 - CAM_BASE.z) * polProg;
                  
                  CAM_LOOK.x += (0 - CAM_LOOK.x) * polProg;
                  CAM_LOOK.y += (0 - CAM_LOOK.y) * polProg;
                  CAM_LOOK.z += (0 - CAM_LOOK.z) * polProg;
              }
              
              // Shadow becomes smaller and sharper as it lands
              let shadowY = 50 * (1 - polProg);
              let shadowBlur = 80 * (1 - polProg) + 10;
              let shadowOp = 0.8 * (1 - polProg) + 0.2;
              
              polCont.style.transform = `translate3d(${swayX}px, ${yPos}vh, 0px) rotateX(${rotX}deg) rotateY(${rotY}deg) rotateZ(${rotZ}deg)`;
              polCont.style.zIndex = '999999';
              polCont.style.display = 'block';
              polCont.style.boxShadow = `0px ${shadowY}px ${shadowBlur}px rgba(0,0,0,${shadowOp})`;"""

    new_code = """              // Camera flies back to top (straight down view)
              if (typeof CAM_BASE !== 'undefined' && typeof CAM_LOOK !== 'undefined') {
                  CAM_BASE.x += (0 - CAM_BASE.x) * polProg;
                  CAM_BASE.y += (16 - CAM_BASE.y) * polProg;
                  CAM_BASE.z += (0 - CAM_BASE.z) * polProg;
                  
                  CAM_LOOK.x += (0 - CAM_LOOK.x) * polProg;
                  CAM_LOOK.y += (0 - CAM_LOOK.y) * polProg;
                  CAM_LOOK.z += (0 - CAM_LOOK.z) * polProg;
              }
              
              // Shadow becomes smaller and sharper as it lands
              let shadowY = 50 * (1 - polProg);
              let shadowBlur = 80 * (1 - polProg) + 10;
              let shadowOp = 0.8 * (1 - polProg) + 0.2;
              
              // Simple, foolproof positioning. Start 100vh ABOVE center, land in center.
              let yOffset = (1 - polProg) * -100;
              
              polCont.style.top = '50%';
              polCont.style.left = '50%';
              polCont.style.transform = `translate(calc(-50% + ${swayX}px), calc(-50% + ${yOffset}vh)) rotateX(${rotX}deg) rotateY(${rotY}deg) rotateZ(${rotZ}deg)`;
              polCont.style.zIndex = '999999';
              polCont.style.display = 'block';
              polCont.style.boxShadow = `0px ${shadowY}px ${shadowBlur}px rgba(0,0,0,${shadowOp})`;"""

    html = html.replace(old_code, new_code)

    # Make sure we don't accidentally hide the polaroid by resetting top/left in CSS
    old_css = """    #polaroid-falling-container {
      position: fixed;
      top: -100vh;
      left: 50%;
      width: 320px;
      margin-left: -160px;
      background: #fcfcfc;"""

    new_css = """    #polaroid-falling-container {
      position: fixed;
      top: 50%;
      left: 50%;
      width: 320px;
      background: #fcfcfc;"""

    html = html.replace(old_css, new_css)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
