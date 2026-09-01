
window.addEventListener('error', function(e) {
    let errBox = document.getElementById('js-err-box');
    if (!errBox) {
        errBox = document.createElement('div');
        errBox.id = 'js-err-box';
        errBox.style = 'position:fixed; top:0; left:0; width:100%; background:red; color:white; z-index:99999999; padding:20px; font-size:20px; font-weight:bold; pointer-events: none;';
        document.documentElement.appendChild(errBox);
    }
    errBox.innerHTML += "JS ERROR: " + e.message + "<br>Line: " + e.lineno + "<br>";
});

document.addEventListener('mouseover', e => {
    const logger = document.getElementById('hover-logger');
    if (logger) {
        let path = [];
        let el = e.target;
        while(el && el.tagName) {
            path.push(el.tagName + (el.id ? '#' + el.id : '') + (el.className ? '.' + el.className.split(' ').join('.') : ''));
            el = el.parentElement;
        }
        logger.innerHTML = 'Hovered: ' + path[0] + '<br>Path: ' + path.slice(0, 4).join(' -> ');
    }
});
