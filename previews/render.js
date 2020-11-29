const puppeteer = require('puppeteer');
const path = require("path");

const args = process.argv;

const configFile = args[2];
const config = require('./' + configFile);

console.log("config:", config);

const { title, subtitle, output } = config;

// const title = "CRISP-DM";
// const subtitle = "Machine Learning Process";

(async () => {
  const browser = await puppeteer.launch({
    defaultViewport: {
      width: 940,
      height: 550,
      isLandscape: true
    }
  });

  const page = await browser.newPage();

  const fileName = path.resolve("./template.html");
  await page.goto('file://' + fileName);
  await page.waitForSelector('#title');

  await page.evaluate(({title, subtitle}) => {
    document.getElementById('title').textContent = title;
    document.getElementById('subtitle').textContent = subtitle;
  }, { title, subtitle });

  await page.screenshot({ 
    path: output,
    quality: 85
  });
 
  await browser.close();
})();