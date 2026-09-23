with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_guarantee_code = """                      // Guarantee Phase
                      var guaranteeRow = document.getElementById('p2-guarantee');
                      if (guaranteeRow) {
                          guaranteeRow.style.opacity = _p1ReverseP.toFixed(2);
                          
                          if (localP >= 28.5) {
                              guaranteeRow.style.opacity = 0;
                          }
                      }"""

# Actually, I need to check the exact lines.
