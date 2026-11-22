#!/usr/bin/env python3
"""Genera web/index.html (FR) y web/pt/index.html (PT)."""
import pathlib
R=pathlib.Path(__file__).resolve().parent
L={
'fr':dict(lang='fr',base='',t='Dream Ink Studio · Tatouage d\'auteur à Fribourg',
 d='Dream Ink Studio, anciennement Buda Tattoo. Tatouage d\'auteur à Fribourg : même équipe, autre niveau. Réservez votre consultation.',
 nav='Réserver',k='Fribourg · Suisse',h1='Dream Ink',st='Studio',tag='Même équipe · Autre niveau',
 old='Anciennement Buda Tattoo',cta='Réserver une consultation',
 s1='Tout change. Le talent reste.',p1='Dream Ink Studio est la nouvelle identité de Buda Tattoo : la même équipe, cinq ans d\'expérience à Fribourg, et une exigence portée à un autre niveau.',
 cards=[('Plus de soin','Chaque projet est pensé avec vous, de la première idée au dernier détail.'),('Plus de détail','Un dessin créé sur mesure, pour une pièce qui n\'appartient qu\'à vous.'),('Plus d\'âme','Un studio à notre image : sobre, chaleureux, exigeant.')],
 sp='Comment ça se passe',steps=['Vous nous racontez votre idée.','Nous dessinons ensemble votre projet.','Vous réservez votre séance.','Nous prenons soin de vous, avant, pendant et après.'],
 sc='Réserver',cp='Écrivez-nous pour une première consultation.',
 lab=dict(phone='Téléphone',email='E-mail',address='Adresse',instagram='Instagram',booking='Prendre rendez-vous'),
 foot='Dream Ink Studio · Fribourg · Suisse',alt='pt',altl='Português',altp='pt/'),
'pt':dict(lang='pt',base='../',t='Dream Ink Studio · Tatuagem de autor em Friburgo',
 d='Dream Ink Studio, antigo Buda Tattoo. Tatuagem de autor em Friburgo: mesma equipa, outro nível. Marca a tua consulta.',
 nav='Marcar',k='Friburgo · Suíça',h1='Dream Ink',st='Studio',tag='Mesma equipa · Outro nível',
 old='Antigo Buda Tattoo',cta='Marcar consulta',
 s1='Tudo muda. O talento fica.',p1='O Dream Ink Studio é a nova identidade do Buda Tattoo: a mesma equipa, cinco anos de experiência em Friburgo e uma exigência levada a outro nível.',
 cards=[('Mais cuidado','Cada projeto é pensado contigo, da primeira ideia ao último detalhe.'),('Mais detalhe','Um desenho feito à medida, para uma peça que é só tua.'),('Mais alma','Um estúdio à nossa imagem: sóbrio, acolhedor, exigente.')],
 sp='Como funciona',steps=['Contas-nos a tua ideia.','Desenhamos o projeto em conjunto.','Marcas a tua sessão.','Cuidamos de ti antes, durante e depois.'],
 sc='Marcar',cp='Escreve-nos para uma primeira consulta.',
 lab=dict(phone='Telefone',email='E-mail',address='Morada',instagram='Instagram',booking='Marcar online'),
 foot='Dream Ink Studio · Friburgo · Suíça',alt='fr',altl='Français',altp='../'),
}
CSS=(R/'assets'/'style.css').read_text()
for k,t in L.items():
    b=t['base']
    cards=''.join(f'<article class="card"><h3>{a}</h3><p>{c}</p></article>' for a,c in t['cards'])
    steps=''.join(f'<li><span>{i+1:02d}</span>{s}</li>' for i,s in enumerate(t['steps']))
    contact=''.join(f'<li data-cfg="{f}"><b>{l}</b><a></a></li>' for f,l in t['lab'].items())
    html=f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['t']}</title><meta name="description" content="{t['d']}">
<meta name="theme-color" content="#07090b">
<link rel="icon" href="{b}assets/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="192x192" href="{b}assets/favicon-192.png"><link rel="apple-touch-icon" href="{b}assets/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:title" content="{t['t']}"><meta property="og:description" content="{t['d']}"><meta property="og:image" content="{b}assets/og-image.jpg"><meta property="og:locale" content="{t['lang']}_CH">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="fr" href="{'' if k=='fr' else '../'}"><link rel="alternate" hreflang="pt" href="{'pt/' if k=='fr' else ''}">
<link rel="preload" href="{b}assets/fonts/cinzel-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS.replace('url(fonts/','url('+b+'assets/fonts/').replace('url(plate-statues','url('+b+'assets/plate-statues')}</style>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"TattooParlor","name":"Dream Ink Studio","alternateName":"Buda Tattoo","image":"/assets/og-image.jpg","address":{{"@type":"PostalAddress","addressLocality":"Fribourg","addressCountry":"CH"}}}}</script>
</head><body>
<header class="nav"><a class="mk" href="#top"><img src="{b}assets/favicon-192.png" alt="" width="34" height="34"><span>Dream Ink</span></a><nav><a href="{t['altp']}" hreflang="{t['alt']}">{t['altl']}</a><a class="btn sm" href="#contact">{t['nav']}</a></nav></header>
<main id="top">
<section class="hero"><div class="plate"></div><div class="in">
<p class="kick">{t['k']}</p><img class="logo" src="{b}assets/logo-monogram.png" alt="Dream Ink Studio" width="360" height="382">
<h1 class="gold">{t['h1']}</h1><p class="studio">{t['st']}</p><p class="tag">{t['tag']}</p><p class="old">{t['old']}</p>
<a class="btn" href="#contact">{t['cta']}</a></div></section>
<section class="wrap"><h2>{t['s1']}</h2><p class="lead">{t['p1']}</p><div class="cards">{cards}</div></section>
<section class="wrap proc"><h2>{t['sp']}</h2><ol>{steps}</ol></section>
<section class="wrap" id="contact"><h2>{t['sc']}</h2><p class="lead">{t['cp']}</p><ul class="contact">{contact}</ul></section>
</main><footer><img src="{b}assets/logo-monogram.png" alt="" width="56" height="60"><p>{t['foot']}</p></footer>
<script src="{b}config.js"></script><script>
(function(c){{c=window.DI_CONFIG||{{}};document.querySelectorAll('[data-cfg]').forEach(function(li){{var v=c[li.dataset.cfg],a=li.querySelector('a');
if(!v){{li.hidden=true;return}}a.textContent=v.replace(/^(mailto:|tel:|https?:\\/\\/)/,'').replace(/\\/$/,'');
a.href=li.dataset.cfg==='email'?'mailto:'+v:li.dataset.cfg==='phone'?'tel:'+v.replace(/\\s/g,''):/^http/.test(v)?v:'#';if(li.dataset.cfg==='address')a.removeAttribute('href')}});
if(c.booking)document.querySelectorAll('a.btn').forEach(function(a){{a.href=c.booking}});}})();
</script></body></html>'''
    out=R/('index.html' if k=='fr' else 'pt/index.html'); out.parent.mkdir(exist_ok=True); out.write_text(html,encoding='utf-8')
print('ok')
