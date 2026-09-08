import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
mobile_css_additions = """
  #nav-menu > a { display: none !important; }
  
  #subheadline {
    max-width: 95% !important;
  }
  
  #mobile-sidebar {
    position: fixed;
    top: 0; right: -100%;
    width: 75vw; height: 100vh;
    background: #0e0e0e;
    z-index: 99999999;
    display: flex;
    flex-direction: column;
    padding: 1rem 1rem;
    transition: right 0.4s cubic-bezier(0.85, 0, 0.15, 1);
    box-shadow: -10px 0 30px rgba(0,0,0,0.5);
  }
  #mobile-sidebar.open {
    right: 0;
  }
  #sidebar-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(4px);
    z-index: 99999998;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
  }
  #sidebar-overlay.open {
    opacity: 1;
    pointer-events: auto;
  }
  .sidebar-header {
    display: flex;
    justify-content: flex-end;
    margin-top: 1.5rem;
    margin-right: 1.5rem;
  }
  #sidebar-close-pill {
    background: #fff;
    color: #000;
    border-radius: 20px;
    padding: 6px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.5px;
    cursor: pointer;
    text-transform: uppercase;
  }
  .sidebar-links {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding-left: 10%;
    gap: 1.8rem;
  }
  .sidebar-links a {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 1.8rem;
    color: #fff;
    text-decoration: none;
    letter-spacing: 0.02em;
    text-transform: uppercase;
  }
"""

# Find the end of #subheadline p rule inside the mobile media query
target_str = """#subheadline p {
    text-align: center !important;
    margin: 0 !important;
  }"""

if target_str in content:
    content = content.replace(target_str, target_str + "\n" + mobile_css_additions)
else:
    print("WARNING: Could not find target CSS string to append to.")

# 2. Append HTML and JS before </body>
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
</body>
"""

content = content.replace("</body>", sidebar_html)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done building sidebar.")
