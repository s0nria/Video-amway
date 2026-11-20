// Render video 3D Momyizz ke MP4 (1080x1920, 30 fps, H.264, audio senyap AAC).
// Guna: node VIDEO_3D/render.js <fail.html> <saat> <output.mp4>
// Contoh: node VIDEO_3D/render.js hari07-span.html 57 hari07-span.mp4
// Pelayan web dimulakan sendiri pada akar repo (port 8765).
const {chromium}=require('playwright');const {spawn}=require('child_process');const path=require('path');
const [file='hari07-span.html',dur='57',out='out.mp4']=process.argv.slice(2);
const ROOT=path.resolve(__dirname,'..');
(async()=>{const FPS=30,N=Math.round(FPS*Number(dur));
const srv=spawn('python3',['-m','http.server','8765'],{cwd:ROOT,stdio:'ignore'});await new Promise(r=>setTimeout(r,1000));
const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto(`http://localhost:8765/VIDEO_3D/${file}`);await p.waitForFunction(()=>window.READY===true,null,{timeout:60000});
if(process.env.SNAP){for(const t of process.env.SNAP.split(',')){await p.evaluate(t=>renderAt(t),Number(t));await p.screenshot({path:path.join(__dirname,`snap_${t}.png`)});}
  await b.close();srv.kill();return;}
const ff=spawn('ffmpeg',['-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-shortest',
 '-c:v','libx264','-preset','medium','-b:v',process.env.BITRATE||'14M','-maxrate',process.env.MAXRATE||'16M','-bufsize','24M','-pix_fmt','yuv420p','-r',String(FPS),'-c:a','aac','-b:a','320k','-movflags','+faststart',path.resolve(out)],{stdio:['pipe','ignore','ignore']});
for(let i=0;i<N;i++){await p.evaluate(t=>renderAt(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:94});
 if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r)); if(i%150===0)console.log(`bingkai ${i}/${N}`);}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();srv.kill();console.log('siap:',path.resolve(out));})();
