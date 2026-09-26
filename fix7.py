import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the block and replace it
    old_block = """var totalYForBox = slideY + (typeof contentY !== 'undefined' ? contentY : 0);"""
    
    new_block = """var _tCam = clamp01((p - 21.7) / 3.0);
              var _txtY = 130 - (ease(_tCam) * 230);
              var _cntY = Math.min(0, _txtY - slideY);
              var totalYForBox = slideY + _cntY;"""

    content = content.replace(old_block, new_block)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
