import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# find the script that contains the menu logic
pattern = re.compile(
    r"<script>\s*document\.addEventListener\('DOMContentLoaded', \(\) => \{\s*const pill = document\.getElementById\('mobile-menu-pill'\);.*?\}\);\s*</script>",
    re.DOTALL
)

new_js = """<script>
    document.addEventListener('DOMContentLoaded', () => {
      const pill = document.getElementById('mobile-menu-pill');
      const sidebar = document.getElementById('mobile-sidebar');
      const overlay = document.getElementById('sidebar-overlay');
      
      function closeMenu() {
          sidebar.classList.remove('open');
          overlay.classList.remove('open');
          if (pill) {
              pill.innerHTML = '+ MENU';
              pill.style.background = 'rgba(255,255,255,0.1)';
              pill.style.color = '#fff';
          }
      }

      function openMenu() {
          sidebar.classList.add('open');
          overlay.classList.add('open');
          if (pill) {
              pill.innerHTML = 'CERRAR';
              pill.style.background = '#fff';
              pill.style.color = '#000';
          }
      }

      if(pill) {
        pill.style.cursor = 'pointer';
        pill.style.pointerEvents = 'auto'; // ensure clickability
        pill.addEventListener('click', () => {
          if (sidebar.classList.contains('open')) {
              closeMenu();
          } else {
              openMenu();
          }
        });
      }
      
      if(overlay) {
        overlay.addEventListener('click', closeMenu);
      }
      
      document.querySelectorAll('.sidebar-links a').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const scrollVal = parseFloat(link.getAttribute('data-scroll'));
          if (!isNaN(scrollVal) && window.jumpToProg) {
            window.jumpToProg(scrollVal);
            closeMenu();
          }
        });
      });
    });
  </script>"""

if pattern.search(content):
    content = pattern.sub(new_js, content)
    print("Replaced with regex correctly!")
else:
    print("Regex still failed to find the block.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
