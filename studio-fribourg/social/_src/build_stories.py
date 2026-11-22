#!/usr/bin/env python3
"""Historias 1080x1920 FR/PT con la estética del teaser 'Tout va changer' + logo ID luna."""
import pathlib, random
from build import BASE_CSS, dust, LOGO, FONTS, OUT
CSS = BASE_CSS + f"""
@font-face{{font-family:Playfair;font-weight:500;src:url({FONTS}/playfair-display-latin-500-normal.woff2)}}
@font-face{{font-family:Playfair;font-weight:700;src:url({FONTS}/playfair-display-latin-700-normal.woff2)}}
body{{width:1080px;height:1920px;overflow:hidden}}
.s{{position:relative;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(ellipse 90% 50% at 70% 35%,#171310,#09090a 65%)}}
.waves{{position:absolute;inset:0}}
.frame{{position:absolute;inset:52px;border:2px solid rgba(212,169,90,.6)}}
.c{{position:absolute;left:0;right:0;text-align:center;color:#fff}}
.kick{{font:400 32px Montserrat;letter-spacing:.34em;color:#d9b36a;text-transform:uppercase}}
.mt{{font:500 62px Montserrat;letter-spacing:.02em;text-transform:uppercase}}
.strike{{position:relative;display:inline-block}}.strike:after{{content:"";position:absolute;left:-5%;right:-5%;top:50%;height:5px;background:linear-gradient(90deg,transparent,#e0b865,#f5e1ae,#e0b865,transparent)}}
.h{{white-space:nowrap;font:500 {{}}px/1.0 Playfair;text-transform:uppercase;letter-spacing:-.01em}}
.sub{{font:500 44px Montserrat;letter-spacing:.02em;text-transform:uppercase}}
.small{{font:400 34px Montserrat;letter-spacing:.04em;text-transform:uppercase;color:#d9b36a}}
.logo{{position:absolute;left:50%;transform:translateX(-50%);filter:drop-shadow(0 0 40px rgba(212,169,90,.4))}}
.box{{position:absolute;left:150px;right:150px;height:230px;border:2px solid rgba(212,169,90,.8)}}
.cta{{display:inline-block;padding:36px 70px;font:500 36px Montserrat;letter-spacing:.2em;text-transform:uppercase;color:#1a1206;background:linear-gradient(135deg,#f7e3b0,#d4a95a)}}
"""
WAVES = """<svg class="waves" viewBox="0 0 1080 1920" preserveAspectRatio="none"><defs>
<linearGradient id="g" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#6e4a1c" stop-opacity="0"/><stop offset=".45" stop-color="#d4a95a"/><stop offset=".7" stop-color="#fbe9b8"/><stop offset="1" stop-color="#a97a34" stop-opacity="0"/></linearGradient>
<linearGradient id="k" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050506"/><stop offset="1" stop-color="#1b1b1e"/></linearGradient>
<filter id="b"><feGaussianBlur stdDeviation="6"/></filter><filter id="b2"><feGaussianBlur stdDeviation="22"/></filter></defs>
<path d="M-60 980 C 200 760 380 900 560 640 C 720 420 880 300 1180 60 L1180 330 C 900 520 780 640 640 860 C 480 1100 260 1020 -60 1260Z" fill="url(#k)" opacity=".95"/>
<path d="M-60 1000 C 220 800 400 930 590 690 C 760 470 900 360 1180 150" fill="none" stroke="url(#g)" stroke-width="38" filter="url(#b2)" opacity=".55"/>
<path d="M-60 1000 C 220 800 400 930 590 690 C 760 470 900 360 1180 150" fill="none" stroke="url(#g)" stroke-width="16" filter="url(#b)"/>
<path d="M-60 1070 C 240 880 420 1000 620 760 C 800 540 930 430 1180 250" fill="none" stroke="url(#g)" stroke-width="5" opacity=".8"/>
<path d="M-60 120 C 200 260 330 160 520 330 C 700 490 860 440 1180 640" fill="none" stroke="url(#g)" stroke-width="8" filter="url(#b)" opacity=".6"/></svg>"""
T = {
 "fr": dict(k="Fribourg · 5 ans", same="Même équipe · Autre niveau", s2=("Un nouveau","symbole."), s2s="La lune · l'encre · le rêve",
   s3=("Plus de soin.","Plus de détail."),s3g="Plus d'âme.",s4=("C'est pour","bientôt."),s4s="Activez le compte à rebours",
   s5=("Votre prochain","tatouage","commence ici."),cta="Réserver",bio="Lien en bio",loc="Fribourg · Suisse"),
 "pt": dict(k="Friburgo · 5 anos", same="Mesma equipa · Outro nível", s2=("Um novo","símbolo."), s2s="A lua · a tinta · o sonho",
   s3=("Mais cuidado.","Mais detalhe."),s3g="Mais alma.",s4=("É já em","breve."),s4s="Ativa a contagem decrescente",
   s5=("A tua próxima","tatuagem","começa aqui."),cta="Marcar consulta",bio="Link na bio",loc="Friburgo · Suíça")}
G='<span class="gold">%s</span>'
def page(name, lang, body, seed):
    (OUT/f"{name}.html").write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><style>{CSS.replace("{}","100")}</style><div class="s">{WAVES}{dust(1080,1920,60,seed)}<div class="frame"></div><div style="position:absolute;inset:0;transform:translateY(130px)">{body}</div><div class="grain"></div></div></html>',encoding="utf-8")
def H(size,txt,top,extra=""): return f'<div class="c h" style="top:{top}px;font-size:{size}px;{extra}">{txt}</div>'
for l,t in T.items():
    page(f"01-reveal-{l}",l,f'<div class="c kick" style="top:150px">{t["k"]}</div><img class="logo" src="{LOGO}" style="top:240px;width:400px">'
     f'<div class="c mt" style="top:760px"><span class="strike">Buda Tattoo</span></div>'+H(170,"Dream Ink",840)+H(170,G%"Studio.",1010)+f'<div class="c sub" style="top:1260px">{t["same"]}</div>',11)
    page(f"02-symbol-{l}",l,f'<div class="c kick" style="top:150px">Dream Ink · Studio</div><img class="logo" src="{LOGO}" style="top:260px;width:660px">'
     +H(130,t["s2"][0],1000)+H(130,G%t["s2"][1],1130)+f'<div class="c small" style="top:1380px">{t["s2s"]}</div>',22)
    page(f"03-level-{l}",l,f'<div class="c kick" style="top:150px">{t["same"]}</div>'+H(104,t["s3"][0],560)+H(104,t["s3"][1],690)+H(104,G%t["s3g"],820)
     +f'<img class="logo" src="{LOGO}" style="top:1180px;width:300px">',33)
    page(f"04-countdown-{l}",l,f'<div class="c kick" style="top:150px">Dream Ink · Studio</div><img class="logo" src="{LOGO}" style="top:250px;width:330px">'
     +H(150,t["s4"][0],760)+H(150,G%t["s4"][1],910)+f'<div class="c small" style="top:1230px">{t["s4s"]}</div><div class="box" style="top:1310px"></div>',44)
    page(f"05-book-{l}",l,f'<div class="c kick" style="top:150px">{t["loc"]}</div><img class="logo" src="{LOGO}" style="top:240px;width:380px">'
     +H(96,t["s5"][0],760)+H(96,G%t["s5"][1],880)+H(96,t["s5"][2],1000)+f'<div class="c" style="top:1280px"><span class="cta">{t["cta"]}</span></div><div class="c small" style="top:1440px">↑ {t["bio"]}</div>',55)
print("stories ok")
