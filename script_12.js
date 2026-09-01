
          var textR = "No nos creas a nosotros,<br>escúchales a ellos.";
          var newHtmlR = "";
          for (var i = 0; i < textR.length; i++) {
            if (textR.substring(i, i+4) === "<br>") {
              newHtmlR += "<br>";
              i += 3;
            } else if (textR[i] === ' ') {
              newHtmlR += ' ';
            } else {
              newHtmlR += '<span class="oryzo-char-right" style="opacity:0;">' + textR[i] + '</span>';
            }
          }
          document.getElementById('oryzo-text-right-gradient').innerHTML = newHtmlR;
        