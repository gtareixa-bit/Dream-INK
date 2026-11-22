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

