


document.addEventListener('mouseover', e => {
    const logger = document.getElementById('hover-logger');
    if (logger) {
        let path = [];
        let el = e.target;
        while(el && el.tagName) {
            path.push(el.tagName + (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className ? '.' + el.className.split(' ').join('.') : ''));
            el = el.parentElement;
        }
        logger.innerHTML = 'Hovered: ' + path[0] + '<br>Path: ' + path.slice(0, 4).join(' -> ');
    }
});
