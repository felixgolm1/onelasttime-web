import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

sidebar_html = """
<!-- Mobile Sidebar -->
<div id="sidebar-overlay"></div>
<div id="mobile-sidebar">
  <div class="sidebar-header">
    <div id="sidebar-close-pill">+ CLOSE</div>
  </div>
  <div class="sidebar-links">
    <a href="#" data-scroll="0.00">INTRO</a>
    <a href="#" data-scroll="0.91">COMO FUNCIONA</a>
    <a href="#" data-scroll="2.18">LA EXPERIENCIA</a>
    <a href="#" data-scroll="41.87">ONE LAST TIME</a>
  </div>
</div>
<script>
  document.addEventListener('DOMContentLoaded', () => {
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
  });
</script>
</html>
"""

content = content.replace("</html>", sidebar_html)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done injecting HTML.")
