const fs = require('fs');
const path = require("path");


const fm = require('front-matter');
const puppeteer = require('puppeteer');

const args = process.argv;
const input = args[2];
const output = args[3];


const render = async (config, output) => {
  const browser = await puppeteer.launch({
    defaultViewport: {
      width: 940,
      height: 550,
      isLandscape: true
    },
    executablePath: 'google-chrome-stable',
    args: ['--no-sandbox'],
  });

  const page = await browser.newPage();

  const fileName = path.resolve("./template_podcast.html");
  await page.goto('file://' + fileName);
  await page.waitForSelector('#title');

  const title = config.short;
  
  const authors = config.guests.map(author => {
    const dataPath = `../_people/${author}.md`;

    const data = fs.readFileSync(dataPath, 'utf8');
    const attributes = fm(data).attributes;

    const name = attributes.title;

    const image = 'file://' + path.resolve(`../images/authors/${author}.jpg`);

    return { name, image };
  });

  console.log('authors', authors);

  await page.evaluate(({title, authors}) => {
    document.getElementById('title').textContent = title;

    const author = authors[0];
    document.getElementById('image').setAttribute('src', author.image);
    document.getElementById('author-name').textContent = author.name;
  }, { title, authors });

  await page.screenshot({ 
    path: output,
    quality: 85
  });
 
  await browser.close();
};

const data = fs.readFileSync(input, 'utf8');
const content = fm(data);
const config = content.attributes;


render(config, output);