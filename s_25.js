
  // Magnetic Effect for Final CTA (Medium Heavy)
  const finalCtaMagnetic = document.getElementById('olt-final-cta');
  if (finalCtaMagnetic) {
    finalCtaMagnetic.style.transition = 'transform 0.6s cubic-bezier(0.34, 1.1, 0.64, 1), opacity 0.3s ease';
    
    finalCtaMagnetic.addEventListener('mousemove', function(e) {
      if (!window._isFinalCtaCentered) return;
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      
      this.style.setProperty('--mx', (x * 0.1) + 'px');
      this.style.setProperty('--my', (y * 0.2) + 'px');
    });

    finalCtaMagnetic.addEventListener('mouseleave', function(e) {
      this.style.setProperty('--mx', '0px');
      this.style.setProperty('--my', '0px');
      this.style.transition = 'transform 0.6s cubic-bezier(0.34, 1.1, 0.64, 1), opacity 0.3s ease';
    });
    
    finalCtaMagnetic.addEventListener('mouseenter', function(e) {
      if (!window._isFinalCtaCentered) return;
      this.style.transition = 'transform 0.1s ease-out, opacity 0.3s ease';
    });
  }
