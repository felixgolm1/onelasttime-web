$file = "3d-test.html"
$content = Get-Content $file -Raw -Encoding UTF8

$oldBlock = @'
         // --- INYECCION DE CARTAS VOLANDO ---
         // FASE 1 (tOpen 0→1, prog 28.2→30.2): las cartas aparecen dentro de la caja mientras se abre
         // FASE 2 (prog 30.5+): las cartas salen volando en secuencia
         let c1_peek_end = Math.min(1, tOpen * 1.5);                        // Aparece primero (más rápida)
         let c2_peek_end = Math.min(1, Math.max(0, tOpen - 0.15) * 1.5);   // Ligero delay
         let c3_peek_end = Math.min(1, Math.max(0, tOpen - 0.30) * 1.5);
         let c4_peek_end = Math.min(1, Math.max(0, tOpen - 0.45) * 1.5);
         
         let endCards = [
             { el: deckClone.querySelector('.card-n1'), peek: c1_peek_end, progRange: [30.5, 31.5] },
             { el: deckClone.querySelector('.card-n2'), peek: c2_peek_end, progRange: [30.8, 31.8] },
             { el: deckClone.querySelector('.card-n3'), peek: c3_peek_end, progRange: [31.1, 32.1] },
             { el: deckClone.querySelector('.card-n4'), peek: c4_peek_end, progRange: [31.4, 32.4] }
         ];

         let cardTable = document.getElementById('oryzo-section');
         let isDesktop = window.innerWidth > 768;

         endCards.forEach((cData, idx) => {
             let c = cData.el;
             if (!c) return;
             let peek = cData.peek;
             let progR = cData.progRange;

             if (peek === 0) {
                 if (c.dataset.endState !== 'deck-rest') {
                     c.dataset.endState = 'deck-rest';
                     let interior = deckClone.querySelector('.interior-cards');
                     if (interior && c.parentNode !== interior) interior.insertBefore(c, interior.firstChild);
                     c.style.position = ''; c.style.left = ''; c.style.top = ''; c.style.margin = '';
                     c.classList.remove('card-on-table', 'card-peeking');
                     c.classList.add('card-in-deck');
                     c.style.transition = 'none';
                     c.style.transform = `translate(-50%, calc(-50% + 15px)) translateZ(${c.dataset.zDepth||6}px) rotate(-90deg) scale(0.85)`;
                     c.style.clipPath = 'inset(0 0 0 10px round 16px)';
                 }
             } else if (peek > 0 && p <= progR[0]) {
                 c.dataset.endState = 'extracting';
                 let interior = deckClone.querySelector('.interior-cards');
                 if (interior && c.parentNode !== interior) {
                     interior.insertBefore(c, interior.firstChild);
                     c.style.position = ''; c.style.left = ''; c.style.top = ''; c.style.margin = '';
                 }
                 c.classList.add('card-peeking');
                 c.classList.remove('card-on-table', 'card-in-deck');
                 c.style.transition = 'none';
                 const y = 15 - 345 * peek; 
                 c.style.transform = `translate(-50%, calc(-50% + ${y}px)) translateZ(${c.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;
                 c.style.clipPath = y > 5 ? 'inset(0 0 0 10px round 16px)' : '';
             } else {
                 c.dataset.endState = 'table';
                 if (c.parentNode !== cardTable) {
                     let slotRef = deckClone.querySelector('#slot-reference-end');
                     if (!slotRef) {
                         slotRef = document.createElement('div');
                         slotRef.id = 'slot-reference-end';
                         slotRef.style.cssText = `position:absolute; left:50%; top:50%; width:1px; height:1px; pointer-events:none; opacity:0; transform: translate(-50%, calc(-50% - 330px)) translateZ(${c.dataset.zDepth||6}px) rotate(-90deg) scale(0.9);`;
                         let interior = deckClone.querySelector('.interior-cards');
                         if (interior) interior.appendChild(slotRef);
                     }
                     if (slotRef && cardTable) {
                         const rect = slotRef.getBoundingClientRect();
                         const tableRect = cardTable.getBoundingClientRect();
                         if (rect.width > 0 || rect.left > 0) {
                             c.dataset.boxLeftEnd = (rect.left - tableRect.left).toString();
                             c.dataset.boxTopEnd  = (rect.top - tableRect.top).toString();
                         }
                     }
                     if (cardTable) cardTable.appendChild(c);
                     c.classList.remove('card-in-deck', 'card-peeking');
                     c.classList.add('card-on-table');
                     c.style.position = 'absolute';
                     c.style.clipPath = '';
                     c.style.transition = 'none';
                 }
                 const startX = parseFloat(c.dataset.boxLeftEnd) || (window.innerWidth / 2);
                 const startY = parseFloat(c.dataset.boxTopEnd) || (window.innerHeight / 2 - 114.75);
                 
                 let pRev = mapRange(p, progR[0], progR[1], 0, 1);
                 pRev = ease(pRev);
                 
                 // Distribuir a los lados
                 const targetX = isDesktop ? (idx % 2 === 0 ? window.innerWidth * 0.15 : window.innerWidth * 0.85) : window.innerWidth / 2;
                 const targetY = isDesktop ? window.innerHeight * (0.3 + (idx * 0.1)) : window.innerHeight * 0.2;
                 const targetRot = isDesktop ? (idx % 2 === 0 ? -10 : 10) : 0;
                 const targetScale = isDesktop ? 1.0 : 0.8;

                 const currentX = startX + (targetX - startX) * pRev;
                 const currentY = startY + (targetY - startY) * pRev;
                 const currentRot = -90 + (targetRot + 90) * pRev;
                 const currentScale = 0.9 + (targetScale - 0.9) * pRev;

                 // No need for tExit adjustment because we append to oryzo-section which already moves up!
                 c.style.transform = `translate(-50%, -50%) translate(${currentX}px, ${currentY}px) rotate(${currentRot}deg) scale(${currentScale})`;
                 
                 // Desvanecer cuando aparecen los testimonios HTML
                 let fadeOut = 1 - mapRange(p, 29.2, 29.6, 0, 1);
                 c.style.opacity = fadeOut.toFixed(3);
             }
         });
      }
      
      // 3. Reveal de texto tipo Oryzo (letra a letra con difuminado suave)
'@

$newBlock = @'
         // --- REPLICA EXACTA DE TESTIMONIOS CON localP = p - 26.0 ---
         let localP = p - 26.0;
         let ec1 = deckClone.querySelector('.card-n1');
         let ec2 = deckClone.querySelector('.card-n2');
         let ec3 = deckClone.querySelector('.card-n3');
         let ec4 = deckClone.querySelector('.card-n4');
         let endCardTable = document.getElementById('oryzo-section');

         let ec1_peek = mapRange(localP, 2.5, 3.0, 0, 1);
         let ec2_peek = mapRange(localP, 4.22, 4.72, 0, 1);
         let ec3_peek = mapRange(localP, 6.02, 6.52, 0, 1);
         let ec4_peek = mapRange(localP, 7.82, 8.32, 0, 1);

         if (localP >= 2.2) {
           // --- CARTA 1 ---
           if (ec1) {
             if (ec1_peek === 0) {
               if (ec1.dataset.endState !== 'deck-rest') {
                 ec1.dataset.endState = 'deck-rest';
                 const ei = deckClone.querySelector('.interior-cards');
                 if (ei && ec1.parentNode !== ei) ei.insertBefore(ec1, ei.firstChild);
                 ec1.style.position=''; ec1.style.left=''; ec1.style.top=''; ec1.style.margin='';
                 ec1.classList.remove('card-on-table','card-peeking'); ec1.classList.add('card-in-deck');
                 ec1.style.transition='none';
                 ec1.style.transform=`translate(-50%, calc(-50% + 15px)) translateZ(${ec1.dataset.zDepth||6}px) rotate(-90deg) scale(0.85)`;
                 ec1.style.clipPath='inset(0 0 0 10px round 16px)';
               }
             } else if (ec1_peek > 0 && localP <= 3.0) {
               ec1.dataset.endState='extracting';
               const ei=deckClone.querySelector('.interior-cards');
               if(ei && ec1.parentNode!==ei){ei.insertBefore(ec1,ei.firstChild);ec1.style.position='';ec1.style.left='';ec1.style.top='';ec1.style.margin='';}
               ec1.classList.add('card-peeking'); ec1.classList.remove('card-on-table','card-in-deck');
               ec1.style.transition='none';
               const ey1=15-345*ec1_peek;
               ec1.style.transform=`translate(-50%, calc(-50% + ${ey1}px)) translateZ(${ec1.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;
               ec1.style.clipPath=ey1>5?'inset(0 0 0 10px round 16px)':'';
             } else {
               ec1.dataset.endState='table';
               if(ec1.parentNode!==endCardTable){
                 let sr=deckClone.querySelector('#slot-reference-end');
                 if(!sr){sr=document.createElement('div');sr.id='slot-reference-end';sr.style.cssText=`position:absolute;left:50%;top:50%;width:1px;height:1px;pointer-events:none;opacity:0;transform:translate(-50%,calc(-50% - 330px)) translateZ(${ec1.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;deckClone.querySelector('.interior-cards').appendChild(sr);}
                 const rr=sr.getBoundingClientRect(),tr=endCardTable.getBoundingClientRect();
                 if(rr.width>0&&rr.height>0){ec1.dataset.boxLeftEnd=(rr.left-tr.left).toString();ec1.dataset.boxTopEnd=(rr.top-tr.top).toString();}
                 endCardTable.appendChild(ec1);ec1.classList.remove('card-in-deck','card-peeking');ec1.classList.add('card-on-table');ec1.style.position='absolute';ec1.style.clipPath='';ec1.style.transition='none';
               }
               const sX1=parseFloat(ec1.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY1=parseFloat(ec1.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD=window.innerWidth>768,zS=iD?1.1:0.97,zX=window.innerWidth/2,zY=window.innerHeight/2-(iD?100:150);
               let mi1=0,mo1=0;
               if(localP<=3.4)mi1=mapRange(localP,3.0,3.4,0,0.8);
               else if(localP<=3.8)mi1=mapRange(localP,3.4,3.8,0.8,1.0);
               else if(localP<=4.3){mi1=1.0;mo1=0;}
               else{mi1=1.0;mo1=mapRange(localP,4.3,4.9,0,1);}
               let rp1=0,hp1=0;
               if(localP>3.8&&localP<=4.3)hp1=mapRange(localP,3.8,4.3,0,1);else if(localP>4.3)hp1=1.0;
               if(localP<=3.3)rp1=mapRange(localP,3.0,3.3,0,0.85);
               else if(localP<=3.5)rp1=mapRange(localP,3.3,3.5,0.85,0.95);
               else if(localP<=3.8)rp1=mapRange(localP,3.5,3.8,0.95,1.0);
               else if(localP<=4.9)rp1=mapRange(localP,3.8,4.9,1.0,0.95);
               else rp1=0.95;
               let rz1=-90+(90*rp1),ry1=335+(25*rp1),fp1=mapRange(localP,3.5,4.1,0,1),rx1=fp1*180;
               let cx1,cy1,cs1,sha1;
               if(mo1===0){cx1=sX1+(zX-sX1)*mi1;cy1=sY1+(zY-sY1)*mi1+(60*hp1);cs1=0.9+(zS-0.9)*mi1;sha1=0.16+(0.4-0.16)*mi1;}
               else{cx1=zX-(window.innerWidth*1.5)*mo1;cy1=zY+60+(window.innerHeight*1.5)*mo1;cs1=zS;sha1=0.4-(0.4-0.16)*mo1;rx1+=120*mo1;ry1+=90*mo1;rz1-=60*mo1;}
               if(localP>3.0){ec1.style.transition='none';ec1.style.left=cx1+'px';ec1.style.top=cy1+'px';ec1.style.transform=`translate(-50%,-50%) rotateY(${ry1}deg) rotateX(${rx1}deg) rotateZ(${rz1}deg) scale(${cs1})`;ec1.style.boxShadow=`0 8px 16px rgba(0,0,0,${sha1*0.75}),0 40px 80px rgba(0,0,0,${sha1})`;const ef1=ec1.querySelector('.card-front'),eb1=ec1.querySelector('.card-back');if(ef1&&eb1){if(rx1>90){ef1.style.display='none';eb1.style.display='flex';}else{ef1.style.display='flex';eb1.style.display='none';}}ec1.style.zIndex=(localP>3.0&&localP<4.6)?'500':'2000';}
             }
           }
           // --- CARTA 2 ---
           const efc2=deckClone.querySelector('.interior-cards .interior-card:nth-child(1)');
           if(ec2){
             if(ec2_peek===0){if(efc2)efc2.style.opacity='1';if(ec2.dataset.endState!=='deck-rest'){ec2.dataset.endState='deck-rest';ec2.style.opacity='0';const ei=deckClone.querySelector('.interior-cards');if(ei&&ec2.parentNode!==ei)ei.insertBefore(ec2,ei.firstChild);ec2.style.position='';ec2.style.left='';ec2.style.top='';ec2.style.margin='';ec2.classList.remove('card-on-table','card-peeking');ec2.classList.add('card-in-deck');ec2.style.transition='none';ec2.style.transform=`translate(-50%, calc(-50% - 35px)) translateZ(${ec2.dataset.zDepth||6}px) rotate(-90deg) scale(0.85)`;ec2.style.clipPath='inset(0 0 0 10px round 16px)';}}
             else if(ec2_peek>0&&localP<=4.72){if(efc2)efc2.style.opacity='0';ec2.style.opacity='1';ec2.dataset.endState='extracting';const ei=deckClone.querySelector('.interior-cards');if(ei&&ec2.parentNode!==ei){ei.insertBefore(ec2,ei.firstChild);ec2.style.position='';ec2.style.left='';ec2.style.top='';ec2.style.margin='';}ec2.classList.add('card-peeking');ec2.classList.remove('card-on-table','card-in-deck');ec2.style.transition='none';const ey2=-35-295*ec2_peek;ec2.style.transform=`translate(-50%, calc(-50% + ${ey2}px)) translateZ(${ec2.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;ec2.style.clipPath=ey2>5?'inset(0 0 0 10px round 16px)':'';}
             else{if(efc2)efc2.style.opacity='0';ec2.style.opacity='1';ec2.dataset.endState='table';if(ec2.parentNode!==endCardTable){let sr=deckClone.querySelector('#slot-reference-end');if(!sr){sr=document.createElement('div');sr.id='slot-reference-end';sr.style.cssText=`position:absolute;left:50%;top:50%;width:1px;height:1px;pointer-events:none;opacity:0;transform:translate(-50%,calc(-50% - 330px)) translateZ(${ec2.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;deckClone.querySelector('.interior-cards').appendChild(sr);}const rr=sr.getBoundingClientRect(),tr=endCardTable.getBoundingClientRect();if(rr.width>0&&rr.height>0){ec2.dataset.boxLeftEnd=(rr.left-tr.left).toString();ec2.dataset.boxTopEnd=(rr.top-tr.top).toString();}endCardTable.appendChild(ec2);ec2.classList.remove('card-in-deck','card-peeking');ec2.classList.add('card-on-table');ec2.style.position='absolute';ec2.style.clipPath='';ec2.style.transition='none';}
               const sX2=parseFloat(ec2.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY2=parseFloat(ec2.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD2=window.innerWidth>768,zS2=iD2?1.1:0.97,zX2=window.innerWidth/2,zY2=window.innerHeight/2-(iD2?100:150);
               let mi2=0,mo2=0;if(localP<=5.12)mi2=mapRange(localP,4.72,5.12,0,0.8);else if(localP<=5.52)mi2=mapRange(localP,5.12,5.52,0.8,1.0);else if(localP<=6.02){mi2=1.0;mo2=0;}else{mi2=1.0;mo2=mapRange(localP,6.02,6.62,0,1);}
               let rp2=0,hp2=0;if(localP>5.52&&localP<=6.02)hp2=mapRange(localP,5.52,6.02,0,1);else if(localP>6.02)hp2=1.0;if(localP<=5.02)rp2=mapRange(localP,4.72,5.02,0,0.85);else if(localP<=5.22)rp2=mapRange(localP,5.02,5.22,0.85,0.95);else if(localP<=5.52)rp2=mapRange(localP,5.22,5.52,0.95,1.0);else if(localP<=6.62)rp2=mapRange(localP,5.52,6.62,1.0,0.95);else rp2=0.95;
               let rz2=-90+(90*rp2),ry2=335+(25*rp2),fp2=mapRange(localP,5.22,5.82,0,1),rx2=fp2*180;
               let cx2,cy2,cs2,sha2;if(mo2===0){cx2=sX2+(zX2-sX2)*mi2;cy2=sY2+(zY2-sY2)*mi2+(60*hp2);cs2=0.9+(zS2-0.9)*mi2;sha2=0.16+(0.4-0.16)*mi2;}else{cx2=zX2+(window.innerWidth*1.5)*mo2;cy2=zY2+60+(window.innerHeight*1.5)*mo2;cs2=zS2;sha2=0.4-(0.4-0.16)*mo2;rx2+=120*mo2;ry2-=90*mo2;rz2+=60*mo2;}
               if(localP>4.72){ec2.style.transition='none';ec2.style.left=cx2+'px';ec2.style.top=cy2+'px';ec2.style.transform=`translate(-50%,-50%) rotateY(${ry2}deg) rotateX(${rx2}deg) rotateZ(${rz2}deg) scale(${cs2})`;ec2.style.boxShadow=`0 8px 16px rgba(0,0,0,${sha2*0.75}),0 40px 80px rgba(0,0,0,${sha2})`;const ef2=ec2.querySelector('.card-front'),eb2=ec2.querySelector('.card-back');if(ef2&&eb2){if(rx2>90){ef2.style.display='none';eb2.style.display='flex';}else{ef2.style.display='flex';eb2.style.display='none';}}ec2.style.zIndex=(localP>4.72&&localP<6.32)?'500':'2001';}
             }
           }
           // --- CARTA 3 ---
           const efc3=deckClone.querySelector('.interior-cards .interior-card:nth-child(2)');
           if(ec3){
             if(ec3_peek===0){if(efc3)efc3.style.opacity='1';if(ec3.dataset.endState!=='deck-rest'){ec3.dataset.endState='deck-rest';ec3.style.opacity='0';const ei=deckClone.querySelector('.interior-cards');if(ei&&ec3.parentNode!==ei)ei.insertBefore(ec3,ei.firstChild);ec3.style.position='';ec3.style.left='';ec3.style.top='';ec3.style.margin='';ec3.classList.remove('card-on-table','card-peeking');ec3.classList.add('card-in-deck');ec3.style.transition='none';ec3.style.transform=`translate(-50%, calc(-50% - 35px)) translateZ(${ec3.dataset.zDepth||6}px) rotate(-90deg) scale(0.85)`;ec3.style.clipPath='inset(0 0 0 10px round 16px)';}}
             else if(ec3_peek>0&&localP<=6.52){if(efc3)efc3.style.opacity='0';ec3.style.opacity='1';ec3.dataset.endState='extracting';const ei=deckClone.querySelector('.interior-cards');if(ei&&ec3.parentNode!==ei){ei.insertBefore(ec3,ei.firstChild);ec3.style.position='';ec3.style.left='';ec3.style.top='';ec3.style.margin='';}ec3.classList.add('card-peeking');ec3.classList.remove('card-on-table','card-in-deck');ec3.style.transition='none';const ey3=-35-295*ec3_peek;ec3.style.transform=`translate(-50%, calc(-50% + ${ey3}px)) translateZ(${ec3.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;ec3.style.clipPath=ey3>5?'inset(0 0 0 10px round 16px)':'';}
             else{if(efc3)efc3.style.opacity='0';ec3.style.opacity='1';ec3.dataset.endState='table';if(ec3.parentNode!==endCardTable){let sr=deckClone.querySelector('#slot-reference-end');if(!sr){sr=document.createElement('div');sr.id='slot-reference-end';sr.style.cssText=`position:absolute;left:50%;top:50%;width:1px;height:1px;pointer-events:none;opacity:0;transform:translate(-50%,calc(-50% - 330px)) translateZ(${ec3.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;deckClone.querySelector('.interior-cards').appendChild(sr);}const rr=sr.getBoundingClientRect(),tr=endCardTable.getBoundingClientRect();if(rr.width>0&&rr.height>0){ec3.dataset.boxLeftEnd=(rr.left-tr.left).toString();ec3.dataset.boxTopEnd=(rr.top-tr.top).toString();}endCardTable.appendChild(ec3);ec3.classList.remove('card-in-deck','card-peeking');ec3.classList.add('card-on-table');ec3.style.position='absolute';ec3.style.clipPath='';ec3.style.transition='none';}
               const sX3=parseFloat(ec3.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY3=parseFloat(ec3.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD3=window.innerWidth>768,zS3=iD3?1.1:0.97,zX3=window.innerWidth/2,zY3=window.innerHeight/2-(iD3?100:150);
               let mi3=0,mo3=0;if(localP<=6.92)mi3=mapRange(localP,6.52,6.92,0,0.8);else if(localP<=7.32)mi3=mapRange(localP,6.92,7.32,0.8,1.0);else if(localP<=7.82){mi3=1.0;mo3=0;}else{mi3=1.0;mo3=mapRange(localP,7.82,8.42,0,1);}
               let rp3=0,hp3=0;if(localP>7.32&&localP<=7.82)hp3=mapRange(localP,7.32,7.82,0,1);else if(localP>7.82)hp3=1.0;if(localP<=6.82)rp3=mapRange(localP,6.52,6.82,0,0.85);else if(localP<=7.02)rp3=mapRange(localP,6.82,7.02,0.85,0.95);else if(localP<=7.32)rp3=mapRange(localP,7.02,7.32,0.95,1.0);else if(localP<=8.42)rp3=mapRange(localP,7.32,8.42,1.0,0.95);else rp3=0.95;
               let rz3=-90+(90*rp3),ry3=335+(25*rp3),fp3=mapRange(localP,7.02,7.62,0,1),rx3=fp3*180;
               let cx3,cy3,cs3,sha3;if(mo3===0){cx3=sX3+(zX3-sX3)*mi3;cy3=sY3+(zY3-sY3)*mi3+(60*hp3);cs3=0.9+(zS3-0.9)*mi3;sha3=0.16+(0.4-0.16)*mi3;}else{cx3=zX3;cy3=zY3+60+(window.innerHeight*1.5)*mo3;cs3=zS3;sha3=0.4-(0.4-0.16)*mo3;rx3+=120*mo3;ry3-=90*mo3;rz3+=60*mo3;}
               if(localP>6.52){ec3.style.transition='none';ec3.style.left=cx3+'px';ec3.style.top=cy3+'px';ec3.style.transform=`translate(-50%,-50%) rotateY(${ry3}deg) rotateX(${rx3}deg) rotateZ(${rz3}deg) scale(${cs3})`;ec3.style.boxShadow=`0 8px 16px rgba(0,0,0,${sha3*0.75}),0 40px 80px rgba(0,0,0,${sha3})`;const ef3=ec3.querySelector('.card-front'),eb3=ec3.querySelector('.card-back');if(ef3&&eb3){if(rx3>90){ef3.style.display='none';eb3.style.display='flex';}else{ef3.style.display='flex';eb3.style.display='none';}}ec3.style.zIndex='2001';}
             }
           }
           // --- CARTA 4 ---
           const efc4=deckClone.querySelector('.interior-cards .interior-card:nth-child(3)');
           if(ec4){
             if(ec4_peek===0){if(efc4)efc4.style.opacity='1';if(ec4.dataset.endState!=='deck-rest'){ec4.dataset.endState='deck-rest';ec4.style.opacity='0';const ei=deckClone.querySelector('.interior-cards');if(ei&&ec4.parentNode!==ei)ei.insertBefore(ec4,ei.firstChild);ec4.style.position='';ec4.style.left='';ec4.style.top='';ec4.style.margin='';ec4.classList.remove('card-on-table','card-peeking');ec4.classList.add('card-in-deck');ec4.style.transition='none';ec4.style.transform=`translate(-50%, calc(-50% - 35px)) translateZ(${ec4.dataset.zDepth||6}px) rotate(-90deg) scale(0.85)`;ec4.style.clipPath='inset(0 0 0 10px round 16px)';}}
             else if(ec4_peek>0&&localP<=8.32){if(efc4)efc4.style.opacity='0';ec4.style.opacity='1';ec4.dataset.endState='extracting';const ei=deckClone.querySelector('.interior-cards');if(ei&&ec4.parentNode!==ei){ei.insertBefore(ec4,ei.firstChild);ec4.style.position='';ec4.style.left='';ec4.style.top='';ec4.style.margin='';}ec4.classList.add('card-peeking');ec4.classList.remove('card-on-table','card-in-deck');ec4.style.transition='none';const ey4=-35-295*ec4_peek;ec4.style.transform=`translate(-50%, calc(-50% + ${ey4}px)) translateZ(${ec4.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;ec4.style.clipPath=ey4>5?'inset(0 0 0 10px round 16px)':'';}
             else{if(efc4)efc4.style.opacity='0';ec4.style.opacity='1';ec4.dataset.endState='table';if(ec4.parentNode!==endCardTable){let sr=deckClone.querySelector('#slot-reference-end');if(!sr){sr=document.createElement('div');sr.id='slot-reference-end';sr.style.cssText=`position:absolute;left:50%;top:50%;width:1px;height:1px;pointer-events:none;opacity:0;transform:translate(-50%,calc(-50% - 330px)) translateZ(${ec4.dataset.zDepth||6}px) rotate(-90deg) scale(0.9)`;deckClone.querySelector('.interior-cards').appendChild(sr);}const rr=sr.getBoundingClientRect(),tr=endCardTable.getBoundingClientRect();if(rr.width>0&&rr.height>0){ec4.dataset.boxLeftEnd=(rr.left-tr.left).toString();ec4.dataset.boxTopEnd=(rr.top-tr.top).toString();}endCardTable.appendChild(ec4);ec4.classList.remove('card-in-deck','card-peeking');ec4.classList.add('card-on-table');ec4.style.position='absolute';ec4.style.clipPath='';ec4.style.transition='none';}
               const sX4=parseFloat(ec4.dataset.boxLeftEnd)||(window.innerWidth/2+132.5),sY4=parseFloat(ec4.dataset.boxTopEnd)||(window.innerHeight/2-114.75);
               const iD4=window.innerWidth>768,zS4=iD4?1.1:0.97,zX4=window.innerWidth/2,zY4=window.innerHeight/2-(iD4?100:150);
               let mi4=0,mo4=0;if(localP<=8.72)mi4=mapRange(localP,8.32,8.72,0,0.8);else if(localP<=9.12)mi4=mapRange(localP,8.72,9.12,0.8,1.0);else if(localP<=9.62){mi4=1.0;mo4=0;}else{mi4=1.0;mo4=mapRange(localP,9.62,10.22,0,1);}
               let rp4=0,hp4=0;if(localP>9.12&&localP<=9.62)hp4=mapRange(localP,9.12,9.62,0,1);else if(localP>9.62)hp4=1.0;if(localP<=8.62)rp4=mapRange(localP,8.32,8.62,0,0.85);else if(localP<=8.82)rp4=mapRange(localP,8.62,8.82,0.85,0.95);else if(localP<=9.12)rp4=mapRange(localP,8.82,9.12,0.95,1.0);else if(localP<=10.22)rp4=mapRange(localP,9.12,10.22,1.0,0.95);else rp4=0.95;
               let rz4=-90+(90*rp4),ry4=335+(25*rp4),fp4=mapRange(localP,8.82,9.42,0,1),rx4=fp4*180;
               let cx4,cy4,cs4,sha4;if(mo4===0){cx4=sX4+(zX4-sX4)*mi4;cy4=sY4+(zY4-sY4)*mi4+(60*hp4);cs4=0.9+(zS4-0.9)*mi4;sha4=0.16+(0.4-0.16)*mi4;}else{cx4=zX4;cy4=zY4+60-(window.innerHeight*1.5)*mo4;cs4=zS4;sha4=0.4-(0.4-0.16)*mo4;rx4+=120*mo4;ry4-=90*mo4;rz4+=60*mo4;}
               if(localP>8.32){ec4.style.transition='none';ec4.style.left=cx4+'px';ec4.style.top=cy4+'px';ec4.style.transform=`translate(-50%,-50%) rotateY(${ry4}deg) rotateX(${rx4}deg) rotateZ(${rz4}deg) scale(${cs4})`;ec4.style.boxShadow=`0 8px 16px rgba(0,0,0,${sha4*0.75}),0 40px 80px rgba(0,0,0,${sha4})`;const ef4=ec4.querySelector('.card-front'),eb4=ec4.querySelector('.card-back');if(ef4&&eb4){if(rx4>90){ef4.style.display='none';eb4.style.display='flex';}else{ef4.style.display='flex';eb4.style.display='none';}}ec4.style.zIndex='2001';}
             }
           }
           // --- REVIEWS FINALES (slide-up identico a testimonios) ---
           var eRev1=document.getElementById('end-review-panel-1');
           var eRev2=document.getElementById('end-review-panel-2');
           var eRev3=document.getElementById('end-review-panel-3');
           var eRev4=document.getElementById('end-review-panel-4');
           if(eRev1){if(localP>3.0&&localP<4.6){var eRp1=mapRange(localP,3.0,4.6,0,1);eRev1.style.transform='translateY('+(mapRange(localP,3.0,4.6,window.innerHeight*1.5,-window.innerHeight*1.5))+'px)';eRev1.style.opacity=eRp1>0.85?mapRange(eRp1,0.85,1.0,1,0):1;}else eRev1.style.opacity='0';}
           if(eRev2){if(localP>4.72&&localP<6.32){var eRp2=mapRange(localP,4.72,6.32,0,1);eRev2.style.transform='translateY('+(mapRange(localP,4.72,6.32,window.innerHeight*1.5,-window.innerHeight*1.5))+'px)';eRev2.style.opacity=eRp2>0.85?mapRange(eRp2,0.85,1.0,1,0):1;}else eRev2.style.opacity='0';}
           if(eRev3){if(localP>6.52&&localP<8.12){var eRp3=mapRange(localP,6.52,8.12,0,1);eRev3.style.transform='translateY('+(mapRange(localP,6.52,8.12,window.innerHeight*1.5,-window.innerHeight*1.5))+'px)';eRev3.style.opacity=eRp3>0.85?mapRange(eRp3,0.85,1.0,1,0):1;}else eRev3.style.opacity='0';}
           if(eRev4){if(localP>8.32&&localP<9.92){var eRp4=mapRange(localP,8.32,9.92,0,1);eRev4.style.transform='translateY('+(mapRange(localP,8.32,9.92,window.innerHeight*1.5,-window.innerHeight*1.5))+'px)';eRev4.style.opacity=eRp4>0.85?mapRange(eRp4,0.85,1.0,1,0):1;}else eRev4.style.opacity='0';}
         }
      }
      
      // 3. Reveal de texto tipo Oryzo (letra a letra con difuminado suave)
'@

# Also replace the old endContainer block
$oldEndContainer = @'
      // 4. Testimonios Finales
      var endRev1 = document.getElementById('end-review-panel-1');
      var endRev2 = document.getElementById('end-review-panel-2');
      var endRev3 = document.getElementById('end-review-panel-3');
      var endRev4 = document.getElementById('end-review-panel-4');
      var endContainer = document.getElementById('end-reviews-container');

      if (endContainer) {
          endContainer.style.opacity = (p > 28.6) ? 1 : 0;
          endContainer.style.transform = 'translateY(' + contentY + 'vh)';
          
          if (endRev1) {
              var f1 = ease(clamp01((p - 29.6) / 0.3)) * (1 - ease(clamp01((p - 30.8) / 0.2)));
              endRev1.style.opacity = f1;
              endRev1.style.transform = 'translateY(' + ((1 - f1) * 20) + 'px)';
          }
          if (endRev2) {
              var f2 = ease(clamp01((p - 31.0) / 0.3)) * (1 - ease(clamp01((p - 32.4) / 0.2)));
              endRev2.style.opacity = f2;
              endRev2.style.transform = 'translateY(' + ((1 - f2) * 20) + 'px)';
          }
          if (endRev3) {
              var f3 = ease(clamp01((p - 32.6) / 0.3)) * (1 - ease(clamp01((p - 34.0) / 0.2)));
              endRev3.style.opacity = f3;
              endRev3.style.transform = 'translateY(' + ((1 - f3) * 20) + 'px)';
          }
          if (endRev4) {
              var f4 = ease(clamp01((p - 34.2) / 0.3)) * (1 - ease(clamp01((p - 35.8) / 0.2)));
              endRev4.style.opacity = f4;
              endRev4.style.transform = 'translateY(' + ((1 - f4) * 20) + 'px)';
          }
      }
    }
'@

$newEndContainer = @'
      // 4. Reviews ya manejadas dentro del bloque localP arriba
    }
'@

# Also fix maxProg
$oldMaxProg = "const maxProg = 36.0;"
$newMaxProg = "const maxProg = 37.0;  // Extendido para acomodar el bloque final completo (localP hasta 10.22)"

if ($content.Contains($oldBlock)) {
    $content = $content.Replace($oldBlock, $newBlock)
    Write-Host "OK: bloque principal reemplazado"
} else {
    Write-Host "ERROR: bloque principal no encontrado"
}

if ($content.Contains($oldEndContainer)) {
    $content = $content.Replace($oldEndContainer, $newEndContainer)
    Write-Host "OK: bloque endContainer reemplazado"
} else {
    Write-Host "ERROR: bloque endContainer no encontrado"
}

if ($content.Contains($oldMaxProg)) {
    $content = $content.Replace($oldMaxProg, $newMaxProg)
    Write-Host "OK: maxProg actualizado a 37.0"
} else {
    Write-Host "WARN: maxProg no encontrado o ya actualizado"
}

[System.IO.File]::WriteAllText((Resolve-Path $file), $content, [System.Text.Encoding]::UTF8)
Write-Host "Archivo guardado."
