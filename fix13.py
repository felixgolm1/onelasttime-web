import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_js = """var boxEnterY = 0;
          if (isMob) {
              var _tCam = clamp01((p - 21.7) / 3.0);
              var _txtY = 130 - (ease(_tCam) * 230);
              var _cntY = Math.min(0, _txtY - slideY);
              var totalYForBox = slideY + _cntY;
              var boxDelayProg = clamp01(((-5) - totalYForBox) / 30); 
              boxEnterY = (1 - boxDelayProg) * 70;
          }
          var boxTotalY = boxEnterY + (tExitBox * 80);"""
          
    new_js = """if (isMob) {
              var _tCam = clamp01((p - 21.7) / 3.0);
              var _txtY = 130 - (ease(_tCam) * 230);
              var _cntY = Math.min(0, _txtY - slideY);
          }
          var boxTotalY = (tExitBox * 80);"""

    content = content.replace(old_js, new_js)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
