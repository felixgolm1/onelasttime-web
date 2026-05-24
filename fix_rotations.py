import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the rotation logic for the flaps in the final animation
# to match EXACTLY the original GSAP logic.
old_logic = """
         // La tapa principal (-92deg es cerrada, 180deg es totalmente abierta hacia atrás)
         var topFlap = deckClone.querySelector('.box-flap');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            topFlap.style.transform = 'translateZ(0px) rotateX(' + (-92 + 272 * ease(tSlide)) + 'deg)';
         }
         // Solapas de polvo (-90deg es cerradas, -180deg es abiertas)
         var dustLeft = deckClone.querySelector('.dust-flap.left');
         var dustRight = deckClone.querySelector('.dust-flap.right');
         if (dustLeft) {
            dustLeft.style.transition = 'none';
            dustLeft.style.transform = 'rotateX(' + (-90 - 90 * ease(tSlide)) + 'deg)';
         }
         if (dustRight) {
            dustRight.style.transition = 'none';
            dustRight.style.transform = 'rotateX(' + (-90 - 90 * ease(tSlide)) + 'deg)';
         }
         // Solapa interior de la tapa principal (tuck-lip)
         var tuckLip = deckClone.querySelector('.tuck-lip');
         if (tuckLip) {
            tuckLip.style.transition = 'none';
            tuckLip.style.transform = 'rotateX(' + (90 - 95 * ease(tSlide)) + 'deg)';
         }
"""

# New logic exactly matching original GSAP mapping ranges:
# flapRot = mapRange(openP, 0.0, 0.5, 90, 180);
# lipRot = mapRange(openP, 0.05, 0.5, -92, -5);
# dustRot = mapRange(openP, 0.4, 0.8, -90, -180);

new_logic = """
         // Helper function for mapping ranges just for the flaps if needed
         function mapFlap(val, inMin, inMax, outMin, outMax) {
             let t = (val - inMin) / (inMax - inMin);
             t = Math.max(0, Math.min(1, t));
             return outMin + t * (outMax - outMin);
         }
         
         let eSlide = ease(tSlide); // Usamos ease para que sea suave

         // La tapa principal (90 a 180)
         var topFlap = deckClone.querySelector('.box-flap');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            let flapRot = mapFlap(eSlide, 0.0, 0.5, 90, 180);
            topFlap.style.transform = 'translateZ(0px) rotateX(' + flapRot + 'deg)';
         }
         // Solapas de polvo (-90 a -180)
         var dustLeft = deckClone.querySelector('.dust-flap.left');
         var dustRight = deckClone.querySelector('.dust-flap.right');
         let dustRot = mapFlap(eSlide, 0.4, 0.8, -90, -180);
         if (dustLeft) {
            dustLeft.style.transition = 'none';
            dustLeft.style.transform = 'rotateX(' + dustRot + 'deg)';
         }
         if (dustRight) {
            dustRight.style.transition = 'none';
            dustRight.style.transform = 'rotateX(' + dustRot + 'deg)';
         }
         // Solapa interior (tuck-lip) (-92 a -5)
         var tuckLip = deckClone.querySelector('.tuck-lip');
         if (tuckLip) {
            tuckLip.style.transition = 'none';
            let lipRot = mapFlap(eSlide, 0.05, 0.5, -92, -5);
            tuckLip.style.transform = 'rotateX(' + lipRot + 'deg)';
         }
"""

if old_logic.strip() in content:
    content = content.replace(old_logic.strip(), new_logic.strip())
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Flap logic updated successfully.")
else:
    print("Could not find the target flap logic!")
    import sys
    sys.exit(1)
