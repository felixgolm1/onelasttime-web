import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update z-index of #mobile-menu-pill
content = re.sub(
    r'<div id="mobile-menu-pill" style="display: none; position: fixed; z-index: 10000020;">\+ MENU</div>',
    r'<div id="mobile-menu-pill" style="display: none; position: fixed; z-index: 1000000000; transition: all 0.3s ease;">+ MENU</div>',
    content
)

# 2. Hide or remove sidebar-close-pill
content = re.sub(
    r'<div id="sidebar-close-pill">\+\s*CLOSE</div>',
    r'<!-- removed close pill -->',
    content
)

# 3. Update the Javascript logic
old_js = """    document.addEventListener('DOMContentLoaded', () => {
      const pill = document.getElementById('mobile-menu-pill');
      const sidebar = document.getElementById('mobile-sidebar');
      const overlay = document.getElementById('sidebar-overlay');
      const closeBtn = document.getElementById('sidebar-close-pill');
      
      if(pill) {
        pill.style.cursor = 'pointer';
        pill.style.pointerEvents = 'auto'; // ensure clickability
        pill.addEventListener('click', () => {
          sidebar.classList.add('open');
          overlay.classList.add('open');
        });
      }
      
      if(closeBtn) {
        closeBtn.addEventListener('click', () => {
          sidebar.classList.remove('open');
          overlay.classList.remove('open');
        });
      }
      
      if(overlay) {
        overlay.addEventListener('click', () => {
          sidebar.classList.remove('open');
          overlay.classList.remove('open');
        });
      }
      
      document.querySelectorAll('.sidebar-links a').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const scrollVal = parseFloat(link.getAttribute('data-scroll'));
          if (!isNaN(scrollVal) && window.jumpToProg) {
            window.jumpToProg(scrollVal);
            sidebar.classList.remove('open');
            overlay.classList.remove('open');
          }
        });
      });
    });"""

new_js = """    document.addEventListener('DOMContentLoaded', () => {
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
    });"""

if old_js in content:
    content = content.replace(old_js, new_js)
    print("Replaced JS successfully")
else:
    print("Could not find old JS snippet")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
