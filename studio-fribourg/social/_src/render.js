const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{
 const b=await chromium.launch();const dir=path.join(__dirname,'html');
 const out=(...p)=>path.join(__dirname,'..',...p);
 for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.html'))){
  const n=f.replace('.html','');const grid=n.startsWith('profile-grid');const isPost=n.startsWith('post-');
  const pg=await b.newPage({viewport:grid?{width:3240,height:2880}:isPost?{width:1080,height:1440}:{width:1080,height:1920}});
  await pg.goto('file://'+path.join(dir,f));await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(400);
  if(grid){const gl=n.slice(-2);fs.mkdirSync(out('profile-grid',gl),{recursive:true});await pg.screenshot({path:out('profile-grid',gl,'_full.png')});}
  else{const lang=n.slice(-2);const d=isPost?'posts':'stories';fs.mkdirSync(out(d,lang),{recursive:true});await pg.screenshot({path:out(d,lang,n+'.jpg'),type:'jpeg',quality:93});}
  await pg.close();
 }
 await b.close();
})();
