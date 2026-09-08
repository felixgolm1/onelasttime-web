
window.onerror = function(msg, url, line, col, err) {
  let msgStr = String(msg);
  if (msgStr.toLowerCase().indexOf('script error') > -1 || parseInt(line) === 0 || msgStr.indexOf('Extension') > -1) return;
  let d = document.createElement('div');
  d.style.cssText = 'position:fixed;top:0;left:0;z-index:9999999;background:red;color:white;padding:20px;font-size:24px;width:100%;';
  d.innerHTML = '<b>JS ERROR:</b> ' + msgStr + ' <br>Line: ' + line;
  document.body.appendChild(d);
};
