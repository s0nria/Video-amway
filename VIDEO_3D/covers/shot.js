// Jana PNG cover 1 saat: node VIDEO_3D/covers/shot.js cover-hari08.html
const {chromium}=require('playwright');const path=require('path');
(async()=>{const f=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const out=path.join(__dirname,f.replace('.html','.png'));await p.screenshot({path:out});await b.close();console.log(out);})();
