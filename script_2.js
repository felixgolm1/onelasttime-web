
    // Guardar un clon puro de la baraja antes de que ningún motor de JS la contamine
    window._pristineMainDeckClone = document.getElementById('mainDeck').cloneNode(true);
    window._pristineMainDeckClone.querySelectorAll('.card-n1, .card-n2, .card-n3, .card-n4').forEach(function(c) { c.style.opacity = '0'; });
  