function makeCardBackTex(data = '4 PASOS') {
    const W = 760, H = 468;
    const ctx = globalBackCtx;
    ctx.fillStyle = '#0d0d0d';
    ctx.fillRect(0, 0, W, H);
    ctx.textBaseline = 'middle';
    
    if (typeof data === 'object' && data.type === 'name_input') {
      return globalBackCanvas;

      return globalBackCanvas;

      const val = data.val;
      const cursorAlpha = data.cursorAlpha;
      const focused = data.focused;
      const selS = data.selS || 0;
      const selE = data.selE || 0;
      
      ctx.font = '600 64px "Poppins", sans-serif';
      
      if (val.length === 0) {
        // Siempre mostrar placeholder gris: "Hola tu nombre"
        const t1 = "Hola ";
        const t2 = "tu nombre";
        const w1 = ctx.measureText(t1).width;
        const w2 = ctx.measureText(t2).width;
        const totalW = w1 + w2;
        const startX = W / 2 - totalW / 2;
        
        ctx.textAlign = 'left';
        ctx.fillStyle = '#ffffff';
        ctx.fillText(t1, startX, H / 2);
        
        ctx.fillStyle = 'rgba(255, 255, 255, 0.25)'; // Gris elegante
        ctx.fillText(t2, startX + w1, H / 2);
        
        // Si está en focus, dibujar el cursor justo antes de "Nombre"
        if (focused && cursorAlpha > 0 && selS === selE) {
          const cursorX = startX + w1;
          ctx.fillStyle = `rgba(204, 255, 0, ${cursorAlpha})`;
          ctx.save(); ctx.translate(cursorX, H / 2); ctx.scale(0.7, 1.0); ctx.fillText('|', 0, 0); ctx.restore();
        }
      } else if (val.length > 8) {
        // MODO MULTILINEA: Hola arriba, Nombre abajo
        const y1 = H / 2 - 42;
        const y2 = H / 2 + 42;
        
        ctx.textAlign = 'center';
        
        // Dibujar Selección si existe
        if (focused && selS !== selE) {
          ctx.save();
          const textBefore = val.substring(0, Math.min(selS, selE));
          const selectedText = val.substring(Math.min(selS, selE), Math.max(selS, selE));
          const fullW = ctx.measureText(val).width;
          const startX = (W / 2 - fullW / 2) + ctx.measureText(textBefore).width;
          const selW = ctx.measureText(selectedText).width;
          ctx.fillStyle = 'rgba(193, 255, 0, 0.4)';
          ctx.fillRect(startX, y2 - 40, selW, 80);
          ctx.restore();
        }

        ctx.fillStyle = '#ffffff';
        ctx.fillText("Hola", W / 2, y1);
        ctx.fillText(val, W / 2, y2);
        
        if (focused && cursorAlpha > 0 && selS === selE) {
          const textBeforeCursor = val.substring(0, selS);
          const fullTextWidth = ctx.measureText(val).width;
          const textBeforeWidth = ctx.measureText(textBeforeCursor).width;
          const cursorX = (W / 2 - fullTextWidth / 2) + textBeforeWidth + 2;
          
          ctx.fillStyle = `rgba(193, 255, 0, ${cursorAlpha})`;
          ctx.textAlign = 'left';
          ctx.save(); ctx.translate(cursorX, y2); ctx.scale(0.7, 1.0); ctx.fillText('|', 0, 0); ctx.restore();
        }
      } else {
        // MODO UNA LINEA
        const baseText = "Hola " + val;
        ctx.textAlign = 'center';

        // 1. Dibujar texto base blanco
        ctx.fillStyle = '#ffffff';
        ctx.fillText(baseText, W / 2, H / 2);
        
        // 2. Si hay selección, dibujar bloque sólido + texto negro clipeado
        if (focused && selS !== selE) {
          const tS = Math.min(selS, selE);
          const tE = Math.max(selS, selE);
          const textBefore = "Hola " + val.substring(0, tS);
          const selectedText = val.substring(tS, tE);
          const fullW = ctx.measureText(baseText).width;
          const startX = (W / 2 - fullW / 2) + ctx.measureText(textBefore).width;
          const selW = ctx.measureText(selectedText).width;
          
          ctx.save();
          // Bloque verde sólido
          ctx.fillStyle = '#c1ff00';
          ctx.fillRect(startX, H / 2 - 40, selW, 80);
          
          // Clipear para dibujar el texto negro SOLO dentro del bloque verde
          ctx.beginPath();
          ctx.rect(startX, H / 2 - 40, selW, 80);
          ctx.clip();
          
          ctx.fillStyle = '#000000';
          ctx.fillText(baseText, W / 2, H / 2);
          ctx.restore();
        }

        if (focused && cursorAlpha > 0 && selS === selE) {
          const textBeforeCursor = "Hola " + val.substring(0, selS);
          const fullTextWidth = ctx.measureText(baseText).width;
          const textBeforeWidth = ctx.measureText(textBeforeCursor).width;
          const cursorX = (W / 2 - fullTextWidth / 2) + textBeforeWidth + 2;
          
          ctx.fillStyle = '#c1ff00';
          ctx.textAlign = 'left';
          ctx.save(); ctx.translate(cursorX, H / 2); ctx.scale(0.7, 1.0); ctx.fillText('|', 0, 0); ctx.restore();
        }
      }
    } else {
      // String estandar (ej. "4 PASOS", "3. DISFRUTA...")
      const text = typeof data === 'string' ? data : '';
      ctx.fillStyle = '#ffffff';
      ctx.textAlign = 'center';
      ctx.font = 'bold 100px "Bebas Neue", Impact, sans-serif';
      ctx.fillText(text, W / 2, H / 2);
    }
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, 1); ctx.lineTo(W, 1); ctx.stroke();
    
    globalBackTex.needsUpdate = true;
    return globalBackTex;
  }