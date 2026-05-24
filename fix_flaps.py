import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_js = """
         var topFlap = deckClone.querySelector('.box-flap');
         if (topFlap) {
            topFlap.style.transition = 'none';
            topFlap.style.transformOrigin = 'top center';
            topFlap.style.transform = 'rotateX(' + (110 * ease(tSlide)) + 'deg)';
         }
         var dustLeft = deckClone.querySelector('.dust-flap.left');
         var dustRight = deckClone.querySelector('.dust-flap.right');
         if (dustLeft) {
            dustLeft.style.transition = 'none';
            dustLeft.style.transform = 'rotateY(' + (-80 * ease(tSlide)) + 'deg)';
         }
         if (dustRight) {
            dustRight.style.transition = 'none';
            dustRight.style.transform = 'rotateY(' + (80 * ease(tSlide)) + 'deg)';
         }
"""

new_js = """
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

if old_js.strip() in content:
    content = content.replace(old_js.strip(), new_js.strip())
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed flaps successfully.")
else:
    print("Could not find the flaps block!")
