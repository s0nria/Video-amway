const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{const d=path.dirname(__dirname), F=d+'/fonts';
 const html=`<!doctype html><html><head><meta charset=utf-8><style>
 @font-face{font-family:Fredoka;font-weight:700;src:url(file://${F}/Fredoka_wght_700.ttf)}
 @font-face{font-family:Fredoka;font-weight:600;src:url(file://${F}/Fredoka_wght_600.ttf)}
 @font-face{font-family:Nunito;font-weight:900;src:url(file://${F}/Nunito_wght_900.ttf)}
 @font-face{font-family:Nunito;font-weight:800;src:url(file://${F}/Nunito_wght_800.ttf)}
 @font-face{font-family:Caveat;font-weight:700;src:url(file://${F}/Caveat_wght_700.ttf)}
 *{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden}
 body{background:#F2EEE5 url(file://${d}/cover/bg.png) center/cover}
 .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(53,54,47,.45) 0%,rgba(53,54,47,.05) 40%,rgba(53,54,47,0) 60%,rgba(53,54,47,.35) 100%)}
 .pill{position:absolute;left:50%;transform:translateX(-50%);top:270px;background:#557F7A;color:#FBF9F4;font:600 36px Fredoka;
  padding:14px 34px;border-radius:999px;letter-spacing:1px;white-space:nowrap;box-shadow:0 6px 18px rgba(0,0,0,.2)}
 .hook{position:absolute;left:70px;width:940px;top:360px;background:#FBF9F4;border-radius:44px;padding:40px 46px 46px;text-align:center;
  box-shadow:0 14px 40px rgba(53,54,47,.35)}
 .hook .q{font:700 108px/1.08 Fredoka;color:#35362F}
 .hook .q b{color:#A3876A;font-weight:700}
 .ring{position:absolute;left:110px;top:1110px;width:320px;height:320px;border-radius:50%;border:8px dashed #FBF9F4;
  box-shadow:0 0 0 4px rgba(53,54,47,.25), inset 0 0 0 4px rgba(53,54,47,.15)}
 .note{position:absolute;left:520px;top:1150px;font:700 70px Caveat;color:#FBF9F4;transform:rotate(-6deg);
  text-shadow:0 2px 6px rgba(53,54,47,.8)}
 .arrow{position:absolute;left:410px;top:1190px}
 .tag{position:absolute;left:50%;transform:translateX(-50%);top:1480px;white-space:nowrap;background:#556A4C;color:#FBF9F4;
  font:700 54px Fredoka;padding:16px 44px;border-radius:999px;box-shadow:0 8px 24px rgba(0,0,0,.25)}
 .wm{position:absolute;left:50%;transform:translateX(-50%);top:1612px;white-space:nowrap;font:24px/1.2 Nunito;font-weight:900;color:#FBF9F4;
  text-shadow:0 1px 2px rgba(53,54,47,.85),0 0 6px rgba(53,54,47,.55)}
 </style></head><body><div class=shade></div>
 <div class=pill>SIRI MIKROPLASTIK · EPISOD 1</div>
 <div class=hook><div class=q>Pernah fikir apa<br>dalam <b>air</b> ni?</div></div>
 <div class=ring></div>
 <div class=note>zarah &lt; 5 mm?</div>
 <svg class=arrow width="120" height="90" viewBox="0 0 120 90"><path d="M110 20 C 80 30, 50 45, 18 70" stroke="#FBF9F4" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M18 70 l22 -4 M18 70 l10 -20" stroke="#FBF9F4" stroke-width="7" stroke-linecap="round"/></svg>
 <div class=tag>Fakta, bukan panik.</div>
 <div class=wm>@empayarbiz_momyizz</div>
 </body></html>`;
 fs.writeFileSync(d+'/cover/cover.html',html);
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 await p.goto('file://'+d+'/cover/cover.html'); await p.evaluate(()=>document.fonts.ready);
 const r=await p.evaluate(()=>[...document.querySelectorAll('.pill,.hook,.ring,.note,.tag,.wm')].map(e=>{const q=e.getBoundingClientRect();return e.className+':'+[q.left,q.top,q.right,q.bottom].map(Math.round).join(',')}));
 console.log(r.join('\n')); await p.screenshot({path:d+'/EP01_cover_hook.png'}); await b.close();})();
