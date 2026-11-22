#!/usr/bin/env python3
"""Genera el HTML de las historias (FR/PT) y de la cuadrícula de perfil.
Render: node render.js  (Playwright -> PNG 1080x1920 y 3240x2880 + 6 recortes)."""
import random, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "html"; OUT.mkdir(exist_ok=True)
FONTS = "../../../brand/fonts"
LOGO = "../../../web/assets/logo-monogram.png"
PLATE = "../../../web/assets/plate-statues.webp"

BASE_CSS = f"""
@font-face{{font-family:Cinzel;font-weight:400;src:url({FONTS}/cinzel-latin-400-normal.woff2)}}
@font-face{{font-family:Cinzel;font-weight:500;src:url({FONTS}/cinzel-latin-500-normal.woff2)}}
@font-face{{font-family:Cinzel;font-weight:600;src:url({FONTS}/cinzel-latin-600-normal.woff2)}}
@font-face{{font-family:Cormorant;font-weight:400;font-style:italic;src:url({FONTS}/cormorant-garamond-latin-400-italic.woff2)}}
@font-face{{font-family:Cormorant;font-weight:300;font-style:italic;src:url({FONTS}/cormorant-garamond-latin-300-italic.woff2)}}
@font-face{{font-family:Montserrat;font-weight:300;src:url({FONTS}/montserrat-latin-300-normal.woff2)}}
@font-face{{font-family:Montserrat;font-weight:400;src:url({FONTS}/montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:Montserrat;font-weight:500;src:url({FONTS}/montserrat-latin-500-normal.woff2)}}
:root{{--ink:#07090b;--g1:#f5e1ae;--g2:#d4a95a;--g3:#9c6e2e;--turq:#2fd9c4}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:var(--ink)}}
.gold{{background:linear-gradient(180deg,#fbe9b8 0%,#e0b865 48%,#a97a34 100%);-webkit-background-clip:text;background-clip:text;color:transparent!important}}
.grain{{position:absolute;inset:0;opacity:.16;mix-blend-mode:overlay;pointer-events:none;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .9 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
.dust i{{position:absolute;border-radius:50%;background:#f1cf86;box-shadow:0 0 10px 2px rgba(241,207,134,.55)}}
"""

def dust(w, h, n, seed, avoid=None):
    r = random.Random(seed); s = []
    for _ in range(n):
        x, y = r.random()*w, r.random()*h
        d = r.choice([2, 2, 3, 3, 4, 6]); o = r.uniform(.25, .9)
        s.append(f'<i style="left:{x:.0f}px;top:{y:.0f}px;width:{d}px;height:{d}px;opacity:{o:.2f}"></i>')
    return '<div class="dust">' + "".join(s) + "</div>"

# ------------------------------------------------------------------ STORIES
STORY_CSS = BASE_CSS + """
body{width:1080px;height:1920px;overflow:hidden}
.s{position:relative;width:1080px;height:1920px;overflow:hidden;
 background:radial-gradient(ellipse 80% 45% at 50% 38%,#1a1710 0%,var(--ink) 70%)}
.plate{position:absolute;left:0;width:1080px;top:%PLATE_TOP%px;opacity:%PLATE_OP%}
.glow{position:absolute;left:50%;top:%GLOW_Y%px;width:1100px;height:1100px;transform:translate(-50%,-50%);
 background:radial-gradient(circle,rgba(212,169,90,.20),rgba(212,169,90,0) 62%)}
.frame{position:absolute;inset:44px;border:2px solid rgba(212,169,90,.55)}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,9,11,.9) 0%,rgba(7,9,11,0) 22%,rgba(7,9,11,0) 70%,rgba(7,9,11,.95) 100%)}
.c{position:absolute;left:0;right:0;text-align:center;color:#fff}
.kick{font:400 30px Montserrat;letter-spacing:.42em;color:var(--g2);text-transform:uppercase}
.cin{font-family:Cinzel;font-weight:500;text-transform:uppercase}
.it{font-family:Cormorant;font-style:italic;font-weight:400;color:var(--g1)}
.mont{font-family:Montserrat;font-weight:300;letter-spacing:.16em;text-transform:uppercase;color:#ece4d3}
.strike{position:relative;display:inline-block}
.strike:after{content:"";position:absolute;left:-4%;right:-4%;top:52%;height:4px;background:linear-gradient(90deg,transparent,var(--g2),var(--g1),var(--g2),transparent)}
.logo{position:absolute;left:50%;transform:translateX(-50%);filter:drop-shadow(0 0 40px rgba(212,169,90,.35))}
.sticker{position:absolute;left:150px;right:150px;height:150px;border:2px solid rgba(212,169,90,.7)}
.cta{display:inline-block;padding:34px 64px;border:2px solid var(--g2);font:500 34px Montserrat;letter-spacing:.28em;text-transform:uppercase;color:#1a1206;background:linear-gradient(135deg,#f7e3b0,#d4a95a)}
.rule{position:absolute;left:50%;width:150px;height:2px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,var(--g2),transparent)}
"""

def story(name, lang, body, plate_top=640, plate_op=1, glow_y=760, seed=1):
    css = STORY_CSS.replace("%PLATE_TOP%", str(plate_top)).replace("%PLATE_OP%", str(plate_op)).replace("%GLOW_Y%", str(glow_y))
    html = f"""<!doctype html><html lang="{lang}"><meta charset="utf-8"><style>{css}</style>
<div class="s"><div class="glow"></div><img class="plate" src="{PLATE}">{dust(1080,1920,70,seed)}<div class="fade"></div><div class="frame"></div>
{body}<div class="grain"></div></div></html>"""
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")

T = {
 "fr": dict(
  k1="Fribourg · 5 ans", same="Même équipe · Autre niveau", studio="Studio",
  s2a="Un nouveau", s2b="symbole.", s2c="La lune, l'encre, le rêve.",
  s3a="Plus de soin.", s3b="Plus de détail.", s3c="Plus d'âme.", s3d="Tatouage d'auteur · Fribourg",
  s4a="C'est pour", s4b="bientôt.", s4c="Activez le compte à rebours",
  s5a="Votre prochain", s5b="tatouage", s5c="commence ici.", cta="Réserver une consultation", bio="Lien en bio",
  new="Nouveau nom", loc="Fribourg · Suisse"),
 "pt": dict(
  k1="Friburgo · 5 anos", same="Mesma equipa · Outro nível", studio="Studio",
  s2a="Um novo", s2b="símbolo.", s2c="A lua, a tinta, o sonho.",
  s3a="Mais cuidado.", s3b="Mais detalhe.", s3c="Mais alma.", s3d="Tatuagem de autor · Friburgo",
  s4a="É já em", s4b="breve.", s4c="Ativa a contagem decrescente",
  s5a="A tua próxima", s5b="tatuagem", s5c="começa aqui.", cta="Marcar consulta", bio="Link na bio",
  new="Novo nome", loc="Friburgo · Suíça"),
}

for lang, t in T.items():
    # 01 REVEAL: Buda Tattoo -> Dream Ink Studio
    story(f"01-reveal-{lang}", lang, f"""
<div class="c kick" style="top:250px">{t['k1']}</div>
<div class="c cin" style="top:330px;font-size:66px;letter-spacing:.06em"><span class="strike">Buda Tattoo</span></div>
<img class="logo" src="{LOGO}" style="top:440px;width:470px">
<div class="c cin gold" style="top:1000px;font-size:128px;letter-spacing:.12em;line-height:1">Dream Ink</div>
<div class="c cin" style="top:1150px;font-size:54px;letter-spacing:.7em;padding-left:.7em;color:var(--g1)">{t['studio']}</div>
<div class="rule" style="top:1250px"></div>
<div class="c mont" style="top:1290px;font-size:36px">{t['same']}</div>""", plate_top=760, plate_op=.7, glow_y=760, seed=11)
    # 02 NUEVO SIMBOLO
    story(f"02-symbol-{lang}", lang, f"""
<div class="c kick" style="top:250px">{t['new']}</div>
<img class="logo" src="{LOGO}" style="top:380px;width:640px">
<div class="c it" style="top:1160px;font-size:104px;line-height:1.02">{t['s2a']}<br>{t['s2b']}</div>
<div class="rule" style="top:1440px"></div>
<div class="c mont" style="top:1480px;font-size:30px;letter-spacing:.2em">{t['s2c']}</div>""", plate_top=720, plate_op=.55, glow_y=640, seed=22)
    # 03 FILOSOFIA
    story(f"03-level-{lang}", lang, f"""
<div class="c kick" style="top:250px">{t['same']}</div>
<div class="c cin gold" style="top:560px;font-size:108px;line-height:1.18;letter-spacing:.04em">{t['s3a']}<br>{t['s3b']}<br>{t['s3c']}</div>
<div class="rule" style="top:1010px"></div>
<div class="c it" style="top:1060px;font-size:62px">{t['s3d']}</div>
<img class="logo" src="{LOGO}" style="top:1250px;width:240px;opacity:.95">""", plate_top=900, plate_op=.55, glow_y=800, seed=33)
    # 04 CUENTA ATRAS
    story(f"04-countdown-{lang}", lang, f"""
<div class="c kick" style="top:250px">Dream Ink · {t['studio']}</div>
<img class="logo" src="{LOGO}" style="top:360px;width:330px">
<div class="c it" style="top:830px;font-size:150px;line-height:1">{t['s4a']}<br>{t['s4b']}</div>
<div class="c mont" style="top:1230px;font-size:30px;letter-spacing:.24em;color:var(--g2)">{t['s4c']}</div>
<div class="sticker" style="top:1300px"></div>""", plate_top=700, plate_op=.5, glow_y=700, seed=44)
    # 05 CTA
    story(f"05-book-{lang}", lang, f"""
<div class="c kick" style="top:250px">{t['loc']}</div>
<img class="logo" src="{LOGO}" style="top:350px;width:380px">
<div class="c it" style="top:860px;font-size:112px;line-height:1.04">{t['s5a']}<br><span class="gold" style="font-family:Cormorant;font-style:italic">{t['s5b']}</span><br>{t['s5c']}</div>
<div class="c" style="top:1330px"><span class="cta">{t['cta']}</span></div>
<div class="c mont" style="top:1470px;font-size:30px;letter-spacing:.3em;color:var(--g2)">↑ {t['bio']}</div>""", plate_top=820, plate_op=.45, glow_y=650, seed=55)

# ------------------------------------------------------------------ PROFILE GRID 3x2 (cada tile 1080x1440, 3:4)
W, H = 3240, 2880
grid = BASE_CSS + f"""
body{{width:{W}px;height:{H}px;overflow:hidden}}
.g{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:var(--ink)}}
.plate{{position:absolute;left:0;top:-150px;width:{W}px}}
.glow{{position:absolute;left:50%;top:1330px;width:2300px;height:2300px;transform:translate(-50%,-50%);background:radial-gradient(circle,rgba(212,169,90,.30),rgba(212,169,90,0) 60%)}}
.logo{{position:absolute;left:50%;top:430px;width:900px;transform:translateX(-50%);filter:drop-shadow(0 0 80px rgba(212,169,90,.45))}}
.c{{position:absolute;left:1080px;width:1080px;text-align:center;color:#fff}}
.cin{{font-family:Cinzel;font-weight:500;text-transform:uppercase}}
.mont{{font-family:Montserrat;font-weight:300;letter-spacing:.2em;text-transform:uppercase;color:#ece4d3}}
.rule{{position:absolute;left:1500px;width:240px;height:3px;background:linear-gradient(90deg,transparent,var(--g2),transparent)}}
.fade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,9,11,.55),rgba(7,9,11,0) 25%,rgba(7,9,11,0) 78%,rgba(7,9,11,.8))}}
"""
(OUT / "profile-grid.html").write_text(f"""<!doctype html><html><meta charset="utf-8"><style>{grid}</style>
<div class="g"><div class="glow"></div><img class="plate" src="{PLATE}">{dust(W,H,260,7)}<div class="fade"></div>
<img class="logo" src="{LOGO}">
<div class="c mont" style="top:150px;font-size:34px"><span class="strike" style="position:relative">Fribourg · Suisse</span></div>
<div class="c cin gold" style="top:1450px;font-size:150px;letter-spacing:.1em;line-height:1;left:960px;width:1320px">Dream Ink</div>
<div class="c cin" style="top:1640px;font-size:60px;letter-spacing:.7em;padding-left:.7em;color:var(--g1)">Studio</div>
<div class="rule" style="top:1780px"></div>
<div class="c mont" style="top:1830px;font-size:34px">Même équipe · Autre niveau</div>
<div class="c mont" style="top:2640px;font-size:28px;opacity:.7;color:var(--g2)">Tatouage d'auteur</div>
<div class="grain"></div></div></html>""", encoding="utf-8")
print("html ok:", sorted(p.name for p in OUT.glob("*.html")))
