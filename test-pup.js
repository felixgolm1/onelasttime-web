const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://localhost:8000/3d-test.html', {waitUntil: 'networkidle0'});
    // scroll to trigger logic
    await page.evaluate(() => { window.scrollBy(0, 5000); });
    await page.waitForTimeout(1000);
    // expand card
    await page.evaluate(() => {
        const _lt = document.querySelector('.carousel-track-large');
        const _li = _lt.querySelectorAll('.carousel-item');
        _li[4].click();
    });
    await page.waitForTimeout(1000);
    // scrub
    const result = await page.evaluate(() => {
        const range = document.getElementById('envej-range');
        range.value = 5000;
        range.dispatchEvent(new Event('input'));
        const v = window._envejVideoRef;
        return {
            hasVideo: !!v,
            duration: v ? v.duration : null,
            currentTime: v ? v.currentTime : null,
            pct: 5000 / 9999
        };
    });
    console.log(JSON.stringify(result));
    await browser.close();
})();
