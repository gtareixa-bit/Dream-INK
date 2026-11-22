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
 fq='Buda Tattoo, qu\'est-ce qui change ?',fa='Buda Tattoo est devenu Dream Ink Studio, à Fribourg. Le nom et le symbole changent ; l\'équipe et la passion restent les mêmes. Vous nous avez connus sous le nom de Buda Tattoo : vous êtes au bon endroit.',sp='Comment ça se passe',steps=['Vous nous racontez votre idée.','Nous dessinons ensemble votre projet.','Vous réservez votre séance.','Nous prenons soin de vous, avant, pendant et après.'],
 sc='Réserver',cp='Écrivez-nous pour une première consultation.',
 lab=dict(phone='Téléphone',email='E-mail',address='Adresse',instagram='Instagram',booking='Prendre rendez-vous'),
 foot='Dream Ink Studio · Fribourg · Suisse',alt='pt',altl='Português',altp='pt/'),
'pt':dict(lang='pt',base='../',t='Dream Ink Studio · Tatuagem de autor em Friburgo',
 d='Dream Ink Studio, antigo Buda Tattoo. Tatuagem de autor em Friburgo: mesma equipa, outro nível. Marca a tua consulta.',
 nav='Marcar',k='Friburgo · Suíça',h1='Dream Ink',st='Studio',tag='Mesma equipa · Outro nível',
 old='Antigo Buda Tattoo',cta='Marcar consulta',
 s1='Tudo muda. O talento fica.',p1='O Dream Ink Studio é a nova identidade do Buda Tattoo: a mesma equipa, cinco anos de experiência em Friburgo e uma exigência levada a outro nível.',
 cards=[('Mais cuidado','Cada projeto é pensado contigo, da primeira ideia ao último detalhe.'),('Mais detalhe','Um desenho feito à medida, para uma peça que é só tua.'),('Mais alma','Um estúdio à nossa imagem: sóbrio, acolhedor, exigente.')],
 fq='Buda Tattoo, o que muda?',fa='O Buda Tattoo passou a Dream Ink Studio, em Friburgo. O nome e o símbolo mudam; a equipa e a paixão ficam. Conheceste-nos como Buda Tattoo: estás no sítio certo.',sp='Como funciona',steps=['Contas-nos a tua ideia.','Desenhamos o projeto em conjunto.','Marcas a tua sessão.','Cuidamos de ti antes, durante e depois.'],
 sc='Marcar',cp='Escreve-nos para uma primeira consulta.',
 lab=dict(phone='Telefone',email='E-mail',address='Morada',instagram='Instagram',booking='Marcar online'),
 foot='Dream Ink Studio · Friburgo · Suíça',alt='fr',altl='Français',altp='../'),
}

L['en']=dict(lang='en',t="Dream Ink Studio · Custom tattoo in Fribourg",d="Dream Ink Studio, formerly Buda Tattoo. Custom tattoo studio in Fribourg: same team, next level. Book your consultation.",
 nav='Book',k='Fribourg · Switzerland',h1='Dream Ink',st='Studio',tag='Same team · Next level',old='Formerly Buda Tattoo',cta='Book a consultation',
 s1='Everything changes. The talent stays.',p1='Dream Ink Studio is the new identity of Buda Tattoo: the same team, five years of experience in Fribourg, and a standard taken to the next level.',
 cards=[('More care','Every project is designed with you, from the first idea to the last detail.'),('More detail','A custom drawing, for a piece that belongs only to you.'),('More soul','A studio that reflects us: refined, warm, demanding.')],
 fq='Buda Tattoo: what changes?',fa='Buda Tattoo is now Dream Ink Studio, in Fribourg. The name and the symbol change; the team and the passion stay the same. You knew us as Buda Tattoo: you are in the right place.',
 sp='How it works',steps=['Tell us your idea.','We design your project together.','You book your session.','We take care of you before, during and after.'],
 sc='Book',cp='Write to us for a first consultation.',lab=dict(phone='Phone',email='Email',address='Address',instagram='Instagram',booking='Book online'),foot='Dream Ink Studio · Fribourg · Switzerland')
L['es']=dict(lang='es',t="Dream Ink Studio · Tatuaje de autor en Friburgo",d="Dream Ink Studio, antes Buda Tattoo. Tatuaje de autor en Friburgo: mismo equipo, otro nivel. Reserva tu consulta.",
 nav='Reservar',k='Friburgo · Suiza',h1='Dream Ink',st='Studio',tag='Mismo equipo · Otro nivel',old='Antes Buda Tattoo',cta='Reservar consulta',
 s1='Todo cambia. El talento se queda.',p1='Dream Ink Studio es la nueva identidad de Buda Tattoo: el mismo equipo, cinco años de experiencia en Friburgo y una exigencia llevada a otro nivel.',
 cards=[('Más cuidado','Cada proyecto se piensa contigo, desde la primera idea hasta el último detalle.'),('Más detalle','Un dibujo a medida, para una pieza que solo es tuya.'),('Más alma','Un estudio a nuestra imagen: sobrio, cálido, exigente.')],
 fq='Buda Tattoo: ¿qué cambia?',fa='Buda Tattoo ahora es Dream Ink Studio, en Friburgo. Cambian el nombre y el símbolo; el equipo y la pasión siguen siendo los mismos. Nos conocías como Buda Tattoo: estás en el sitio correcto.',
 sp='Cómo funciona',steps=['Nos cuentas tu idea.','Diseñamos juntos tu proyecto.','Reservas tu sesión.','Cuidamos de ti antes, durante y después.'],
 sc='Reservar',cp='Escríbenos para una primera consulta.',lab=dict(phone='Teléfono',email='Email',address='Dirección',instagram='Instagram',booking='Reservar online'),foot='Dream Ink Studio · Friburgo · Suiza')
L['de']=dict(lang='de',t="Dream Ink Studio · Tattoo-Kunst in Freiburg",d="Dream Ink Studio, früher Buda Tattoo. Tattoo-Studio in Freiburg: gleiches Team, neues Niveau. Buche deine Beratung.",
 nav='Buchen',k='Freiburg · Schweiz',h1='Dream Ink',st='Studio',tag='Gleiches Team · Neues Niveau',old='Früher Buda Tattoo',cta='Beratung buchen',
 s1='Alles ändert sich. Das Talent bleibt.',p1='Dream Ink Studio ist die neue Identität von Buda Tattoo: dasselbe Team, fünf Jahre Erfahrung in Freiburg und ein Anspruch auf neuem Niveau.',
 cards=[('Mehr Sorgfalt','Jedes Projekt entsteht mit dir, von der ersten Idee bis zum letzten Detail.'),('Mehr Detail','Eine massgeschneiderte Zeichnung für ein Stück, das nur dir gehört.'),('Mehr Seele','Ein Studio, das zu uns passt: schlicht, warm, anspruchsvoll.')],
 fq='Buda Tattoo: was ändert sich?',fa='Aus Buda Tattoo wird Dream Ink Studio in Freiburg. Name und Symbol ändern sich; Team und Leidenschaft bleiben dieselben. Du kanntest uns als Buda Tattoo: du bist am richtigen Ort.',
 sp='So läuft es ab',steps=['Du erzählst uns deine Idee.','Wir entwerfen dein Projekt gemeinsam.','Du buchst deine Sitzung.','Wir kümmern uns um dich: davor, währenddessen und danach.'],
 sc='Buchen',cp='Schreib uns für eine erste Beratung.',lab=dict(phone='Telefon',email='E-Mail',address='Adresse',instagram='Instagram',booking='Online buchen'),foot='Dream Ink Studio · Freiburg · Schweiz')

ORDER=['fr','de','es','pt','en']
CSS=(R/'assets'/'style.css').read_text()
for k,t in L.items():
    b='' if k=='fr' else '../'
    cards=''.join(f'<article class="card"><h3>{a}</h3><p>{c}</p></article>' for a,c in t['cards'])
    steps=''.join(f'<li><span>{i+1:02d}</span>{s}</li>' for i,s in enumerate(t['steps']))
    contact=''.join(f'<li data-cfg="{f}"><b>{l}</b><a></a></li>' for f,l in t['lab'].items())
    path=lambda x:('' if x=='fr' else x+'/')
    rel=lambda x:('../' if k!='fr' else '')+path(x)
    HREF=''.join(f'<link rel="alternate" hreflang="{x}" href="{rel(x)}">' for x in ORDER)
    LANGNAV=''.join(f'<a href="{rel(x)}" hreflang="{x}"'+(' class="cur"' if x==k else '')+f'>{x}</a>' for x in ORDER)
    html=f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['t']}</title><meta name="description" content="{t['d']}">
<meta name="theme-color" content="#07090b">
<link rel="icon" href="{b}assets/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="192x192" href="{b}assets/favicon-192.png"><link rel="apple-touch-icon" href="{b}assets/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:title" content="{t['t']}"><meta property="og:description" content="{t['d']}"><meta property="og:image" content="{b}assets/og-image.jpg"><meta property="og:locale" content="{t['lang']}_CH">
<meta name="twitter:card" content="summary_large_image">
{HREF}
<link rel="preload" href="{b}assets/fonts/cinzel-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS.replace('url(fonts/','url('+b+'assets/fonts/').replace('url(plate-statues','url('+b+'assets/plate-statues')}</style>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"TattooParlor","name":"Dream Ink Studio","alternateName":"Buda Tattoo","image":"/assets/og-image.jpg","address":{{"@type":"PostalAddress","addressLocality":"Fribourg","addressCountry":"CH"}}}}</script>
</head><body>
<header class="nav"><a class="mk" href="#top"><img src="{b}assets/favicon-192.png" alt="" width="34" height="34"><span>Dream Ink</span></a><nav>{LANGNAV}<a class="btn sm" href="#contact">{t['nav']}</a></nav></header>
<main id="top">
<section class="hero"><div class="plate"></div><div class="in">
<p class="kick">{t['k']}</p><img class="logo" src="{b}assets/logo-monogram.png" alt="Dream Ink Studio" width="260" height="364">
<h1 class="gold">{t['h1']}</h1><p class="studio">{t['st']}</p><p class="tag">{t['tag']}</p><p class="old">{t['old']}</p>
<a class="btn" href="#contact">{t['cta']}</a></div></section>
<section class="wrap"><h2>{t['s1']}</h2><p class="lead">{t['p1']}</p><div class="cards">{cards}</div></section>
<section class="wrap"><h2>{t['fq']}</h2><p class="lead">{t['fa']}</p></section>
<section class="wrap proc"><h2>{t['sp']}</h2><ol>{steps}</ol></section>
<section class="wrap" id="contact"><h2>{t['sc']}</h2><p class="lead">{t['cp']}</p><ul class="contact">{contact}</ul></section>
</main><footer><img src="{b}assets/logo-monogram.png" alt="" width="56" height="60"><p>{t['foot']}</p></footer>
<script src="{b}config.js"></script><script>
(function(c){{c=window.DI_CONFIG||{{}};document.querySelectorAll('[data-cfg]').forEach(function(li){{var v=c[li.dataset.cfg],a=li.querySelector('a');
if(!v){{li.hidden=true;return}}a.textContent=v.replace(/^(mailto:|tel:|https?:\\/\\/)/,'').replace(/\\/$/,'');
a.href=li.dataset.cfg==='email'?'mailto:'+v:li.dataset.cfg==='phone'?'tel:'+v.replace(/\\s/g,''):/^http/.test(v)?v:'#';if(li.dataset.cfg==='address')a.removeAttribute('href')}});
if(c.booking)document.querySelectorAll('a.btn').forEach(function(a){{a.href=c.booking}});}})();
</script></body></html>'''
    out=R/('index.html' if k=='fr' else k+'/index.html'); out.parent.mkdir(exist_ok=True); out.write_text(html,encoding='utf-8')
print('ok')
