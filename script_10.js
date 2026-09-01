
          (function(){
            var el = document.getElementById('oryzo-text-gradient');
            if(!el) return;
            var text = "COMO MUCHAS<br>PAREJAS YA<br>HAN HECHO";
            var newHtml = '';
            for(var i=0; i<text.length; i++){
               if(text.substring(i, i+4) === '<br>'){
                  newHtml += '<br>';
                  i += 3;
               } else if(text[i] === ' ') {
                  newHtml += ' ';
               } else {
                  newHtml += '<span class="oryzo-char" style="opacity:0;">' + text[i] + '</span>';
               }
            }
            el.innerHTML = newHtml;
          })();
        