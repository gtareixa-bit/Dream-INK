#!/usr/bin/env python3
"""Panel de perfil 3x2 (3240x2880) en 5 idiomas."""
from build import BASE_CSS, dust, LOGO, PLATE, OUT
W,H=3240,2880
G={"fr":("Fribourg · Suisse","Même équipe · Autre niveau","Tatouage d'auteur"),"de":("Freiburg · Schweiz","Gleiches Team · Neues Niveau","Tätowierkunst"),
 "es":("Friburgo · Suiza","Mismo equipo · Otro nivel","Tatuaje de autor"),"pt":("Friburgo · Suíça","Mesma equipa · Outro nível","Tatuagem de autor"),
 "en":("Fribourg · Switzerland","Same team · Next level","Custom tattoo art")}
css=BASE_CSS+f"""
body{{width:{W}px;height:{H}px;overflow:hidden}}
.g{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:var(--ink)}}
.plate{{position:absolute;left:0;top:-150px;width:{W}px}}
.glow{{position:absolute;left:50%;top:1330px;width:2300px;height:2300px;transform:translate(-50%,-50%);background:radial-gradient(circle,rgba(212,169,90,.30),rgba(212,169,90,0) 60%)}}
.logo{{position:absolute;left:50%;top:360px;width:600px;transform:translateX(-50%);filter:drop-shadow(0 0 80px rgba(212,169,90,.45))}}
.c{{position:absolute;left:1080px;width:1080px;text-align:center;color:#fff;white-space:nowrap}}
.cin{{font-family:Cinzel;font-weight:500;text-transform:uppercase}}
.mont{{font-family:Montserrat;font-weight:300;letter-spacing:.2em;text-transform:uppercase;color:#ece4d3}}
.rule{{position:absolute;left:1500px;width:240px;height:3px;background:linear-gradient(90deg,transparent,var(--g2),transparent)}}
.fade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,9,11,.55),rgba(7,9,11,0) 25%,rgba(7,9,11,0) 78%,rgba(7,9,11,.8))}}
"""
FIT="""<script>document.fonts.ready.then(function(){document.querySelectorAll('.c').forEach(function(e){var n=0;function w(){var r=document.createRange();r.selectNodeContents(e);return r.getBoundingClientRect().width}while(w()>940&&n++<40){e.style.fontSize=(parseFloat(getComputedStyle(e).fontSize)*0.96)+'px'}})})</script>"""
for l,(loc,same,sub) in G.items():
    (OUT/f"profile-grid-{l}.html").write_text(f"""<!doctype html><html lang="{l}"><meta charset="utf-8"><style>{css}</style>
<div class="g"><div class="glow"></div><img class="plate" src="{PLATE}">{dust(W,H,260,7)}<div class="fade"></div>
<img class="logo" src="{LOGO}">
<div class="c mont" style="top:150px;font-size:34px">{loc}</div>
<div class="c cin gold" style="top:1450px;font-size:150px;letter-spacing:.1em;line-height:1;left:960px;width:1320px">Dream Ink</div>
<div class="c cin" style="top:1640px;font-size:60px;letter-spacing:.7em;padding-left:.7em;color:var(--g1)">Studio</div>
<div class="rule" style="top:1780px"></div>
<div class="c mont" style="top:1830px;font-size:34px">{same}</div>
<div class="c mont" style="top:2640px;font-size:28px;opacity:.7;color:var(--g2)">{sub}</div>
<div class="grain"></div></div>{FIT}</html>""",encoding="utf-8")
print("grid ok")
