
    document.addEventListener('DOMContentLoaded', () => {
      const nextBtn = document.getElementById('dial-next-btn');
      const phase1 = document.getElementById('dial-phase-1');
      const phase2 = document.getElementById('dial-phase-2');
      const title = document.getElementById('dial-title');
      const slider = document.getElementById('depth-slider');
      const question = document.getElementById('dial-question');
      const nameInput = document.getElementById('neon-html-input');

      const questions = [
        '\u00bfCu\u00e1l es tu pel\u00edcula favorita?',
        '\u00bfQu\u00e9 talento in\u00fatil tienes?',
        '\u00bfCu\u00e1ndo fue la \u00faltima vez que re\u00edste a carcajadas?',
        '\u00bfQu\u00e9 es lo que m\u00e1s te gusta de tu vida ahora mismo?',
        '\u00bfQu\u00e9 te daba miedo de peque\u00f1o y ahora no?',
        'Si pudieras revivir un solo d\u00eda, \u00bfcu\u00e1l ser\u00eda?',
        '\u00bfQu\u00e9 sue\u00f1o has abandonado por miedo?',
        '\u00bfCu\u00e1ndo fue la \u00faltima vez que te sentiste muy solo?',
        '\u00bfQu\u00e9 es lo que nunca le has perdonado a tus padres?',
        'Si hoy fuera tu \u00faltimo d\u00eda, \u00a1a qui\u00e9n llamar\u00edas?'
      ];

      if(nextBtn && phase1 && phase2 && title && slider && question && nameInput) {
        nextBtn.addEventListener('click', () => {
          let name = nameInput.value.trim() || 'Desconocido';
          title.innerHTML = `<b>${name}</b>, \u00bfhasta d\u00f3nde quieres llegar?`;
          
          phase1.style.transform = 'translateY(-20px)';
          phase1.style.opacity = '0';
          
          setTimeout(() => {
            phase1.style.pointerEvents = 'none';
            phase2.style.pointerEvents = 'auto';
            phase2.style.transform = 'translateY(0)';
            phase2.style.opacity = '1';
          }, 500);
        });

        slider.addEventListener('input', (e) => {
          let val = parseInt(e.target.value);
          let index = Math.floor((val / 100) * (questions.length - 1));
          question.textContent = questions[index];
          
          let glow = (val / 100) * 30;
          document.getElementById('visible-input-group').style.boxShadow = `inset 0 0 0 1.5px #ccff00, 0 10px 30px rgba(0,0,0,0.8), 0 0 ${glow}px rgba(204,255,0,0.6)`;
          
          if (val === 100) {
            window.isDialLocked = false;
            question.style.textShadow = '0 0 10px #ccff00';
            slider.style.pointerEvents = 'none';
            setTimeout(() => {
              question.textContent = '\u00a1Sigue haciendo scroll!';
              question.style.color = '#fff';
              question.style.textShadow = 'none';
            }, 1500);
          }
        });
        
        nameInput.addEventListener('keypress', (e) => {
          if (e.key === 'Enter') {
            nextBtn.click();
          }
        });
        
        nameInput.addEventListener('input', (e) => {
          if(e.target.value.trim().length > 0) {
            nextBtn.style.opacity = '1';
          } else {
            nextBtn.style.opacity = '0.5';
          }
        });
      }
    });
  