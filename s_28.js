
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
