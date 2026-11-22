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

# ------------------------------------------------------------------ PROFILE GRID 3x2 (cada tile 1080x1440, 3:4)
W, H = 3240, 2880
grid = BASE_CSS + f"""
body{{width:{W}px;height:{H}px;overflow:hidden}}
.g{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:var(--ink)}}
.plate{{position:absolute;left:0;top:-150px;width:{W}px}}
.glow{{position:absolute;left:50%;top:1330px;width:2300px;height:2300px;transform:translate(-50%,-50%);background:radial-gradient(circle,rgba(212,169,90,.30),rgba(212,169,90,0) 60%)}}
.logo{{position:absolute;left:50%;top:360px;width:600px;transform:translateX(-50%);filter:drop-shadow(0 0 80px rgba(212,169,90,.45))}}
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
