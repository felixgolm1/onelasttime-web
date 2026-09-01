
// scroll-driven Neural Wiring
(function() {
  var h2 = document.getElementById('oxitocina-title');
  if (!h2) return;
  var TEXT = 'NO ES MAGIA\nES QUÍMICA';
  var GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#*+^~!';
  var PROG_START = 14.85, PROG_END = 15.70;
  var spans = [];
  h2.textContent = ''; h2.style.opacity = '1';
  for (var i = 0; i < TEXT.length; i++) {
    if (TEXT[i] === '\n') { h2.appendChild(document.createElement('br')); continue; }
    var sp = document.createElement('span');
    sp.dataset.ch = TEXT[i];
    sp.textContent = TEXT[i] === ' ' ? '\u00A0' : TEXT[i];
    sp.style.cssText = 'display:inline-block;opacity:0;transition:none;';
    h2.appendChild(sp); spans.push(sp);
  }
  var N = spans.length;
  var sc = document.createElement('canvas');
  sc.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:10000001;';
  document.body.appendChild(sc);
  var sctx = null, sparks = [], sparkRAF = null, scReady = false;
  function initSC() {
    if (scReady) return;
    sc.width = window.innerWidth; sc.height = window.innerHeight;
    sctx = sc.getContext('2d'); scReady = true;
  }
  function fireSpark(r1, r2) {
    if (!r1||!r2||!sctx) return;
    sparks.push({x1:r1.left+r1.width/2,y1:r1.top+r1.height/2,
                 x2:r2.left+r2.width/2,y2:r2.top+r2.height/2,
                 born:performance.now(),life:400});
    if (!sparkRAF) renderSparks();
  }
  function renderSparks() {
    sctx.clearRect(0,0,sc.width,sc.height);
    var now=performance.now(),alive=[];
    sparks.forEach(function(s){
      var t=(now-s.born)/s.life; if(t>=1)return; alive.push(s);
      var a=(1-t)*(1-t)*0.9;
      var mx=(s.x1+s.x2)/2,my=Math.min(s.y1,s.y2)-30*(1-t);
      sctx.beginPath();sctx.moveTo(s.x1,s.y1);
      sctx.quadraticCurveTo(mx,my,s.x2,s.y2);
      sctx.strokeStyle='rgba(180,255,0,'+a+')';
      sctx.lineWidth=1.8*(1-t*0.7);sctx.stroke();
      var ga=sctx.createRadialGradient(s.x2,s.y2,0,s.x2,s.y2,14*(1-t));
      ga.addColorStop(0,'rgba(220,255,80,'+(a*1.3)+')');
      ga.addColorStop(1,'rgba(100,180,0,0)');
      sctx.fillStyle=ga;sctx.beginPath();
      sctx.arc(s.x2,s.y2,14*(1-t),0,Math.PI*2);sctx.fill();
    });
    sparks=alive;
    sparkRAF=sparks.length?requestAnimationFrame(renderSparks):null;
  }
  // N1 = chars line 1 'NO ES MAGIA'=11, N2 = chars line 2 'ES QUIMICA'=10
  var N1=11, N2=10, L2END=spans.length-1;
  var lastActive1=0, lastActive2=0;
  function rnd(g){return g[Math.floor(Math.random()*g.length)];}
  function settleChar(sp, prevSp) {
    var target = sp.dataset.ch===' '?'\u00A0':sp.dataset.ch;
    sp.style.opacity='1'; var f=0;
    (function flick(){
      if(f<3){
        sp.textContent=rnd(GLYPHS);
        sp.style.color='rgba('+(180+Math.random()*40|0)+','+(230+Math.random()*25|0)+',0,0.95)';
        sp.style.textShadow='0 0 14px rgba(180,255,0,0.9)';
        f++;requestAnimationFrame(flick);
      } else {
        sp.textContent=target;
        sp.style.color='#ffffff';
        sp.style.textShadow='0 0 22px rgba(204,255,0,1),0 0 50px rgba(140,220,0,0.55)';
        if(prevSp&&sp.dataset.ch!==' '){
          fireSpark(prevSp.getBoundingClientRect(),sp.getBoundingClientRect());
        }
        setTimeout(function(){
          sp.style.transition='text-shadow 1.2s ease,color 0.7s ease';
          sp.style.color='#f0ecff';
          sp.style.textShadow='0 0 5px rgba(180,255,0,0.22)';
        },320);
      }
    })();
  }
  function resetChar(sp){
    sp.style.cssText='display:inline-block;opacity:0;transition:none;';
    sp.textContent=sp.dataset.ch===' '?'\u00A0':sp.dataset.ch;
  }
  function unsettleChar(sp){
    var f=0; sp.style.transition='none';
    (function flick(){
      if(f<3){
        sp.textContent=rnd(GLYPHS);
        sp.style.opacity='1';
        sp.style.color='rgba('+(180+Math.random()*40|0)+','+(230+Math.random()*25|0)+',0,0.95)';
        sp.style.textShadow='0 0 14px rgba(180,255,0,0.9)';
        f++;requestAnimationFrame(flick);
      } else {
        sp.style.opacity='0';
        sp.textContent=sp.dataset.ch===' '?'\u00A0':sp.dataset.ch;
        sp.style.color='';sp.style.textShadow='';
      }
    })();
  }
  var _origNT = window._updateNeuralText||null;
  window._updateNeuralText = function(prog){
    if(_origNT)_origNT(prog);
    if((prog + 0.5)<15.30){
      if(lastActive1>0||lastActive2>0){
        spans.forEach(resetChar); sparks=[];
        if(sctx)sctx.clearRect(0,0,sc.width,sc.height);
        lastActive1=0; lastActive2=0;
      }
      return;
    }
    initSC();
    var animT=Math.max(0,Math.min(1,(prog-PROG_START)/(PROG_END-PROG_START)));
    // --- Linea 1: izquierda a derecha (indices 0..N1-1) ---
    var na1=Math.min(N1,Math.floor(animT*N1+0.5));
    if(na1>lastActive1){
      for(var i=lastActive1;i<na1;i++)
        settleChar(spans[i],i>0?spans[i-1]:null);
      lastActive1=na1;
    } else if(na1<lastActive1){
      for(var i=na1;i<lastActive1;i++) unsettleChar(spans[i]);
      if(sctx)sctx.clearRect(0,0,sc.width,sc.height); sparks=[];
      lastActive1=na1;
    }
    // --- Linea 2: derecha a izquierda (L2END..N1, en reverso) ---
    var na2=Math.min(N2,Math.floor(animT*N2+0.5));
    if(na2>lastActive2){
      for(var i=lastActive2;i<na2;i++){
        var idx=L2END-i;
        var prevIdx=(i>0)?(L2END-(i-1)):null;
        settleChar(spans[idx],prevIdx!==null?spans[prevIdx]:null);
      }
      lastActive2=na2;
    } else if(na2<lastActive2){
      for(var i=na2;i<lastActive2;i++) unsettleChar(spans[L2END-i]);
      if(sctx)sctx.clearRect(0,0,sc.width,sc.height); sparks=[];
      lastActive2=na2;
    }
  };

    
})();
