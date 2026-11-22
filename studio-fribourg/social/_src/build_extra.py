#!/usr/bin/env python3
"""Historias extra (teasers, merci, mismo compte, cambia/queda, sondeo, preguntas) + publicaciones de feed 1080x1440."""
from build_stories import CSS, WAVES, G, H, T, page, dust, LOGO, OUT
import random
POST_WAVES = WAVES.replace('preserveAspectRatio="none"', 'preserveAspectRatio="xMidYMid slice"')
def post(name, lang, body, seed):
    css = CSS.replace("{}", "100") + "body{width:1080px;height:1440px}.s{height:1440px}"
    (OUT/f"{name}.html").write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><style>{css}</style><div class="s">{POST_WAVES}{dust(1080,1440,50,seed)}<div class="frame"></div>{body}<div class="grain"></div></div></html>',encoding="utf-8")
def c(top, txt, cls="sub", extra=""): return f'<div class="c {cls}" style="top:{top}px;{extra}">{txt}</div>'
def logo(top, w): return f'<img class="logo" src="{LOGO}" style="top:{top}px;width:{w}px">'
def box(top, h=230): return f'<div class="box" style="top:{top}px;height:{h}px"></div>'
X = {
 "fr": dict(j3=("Quelque chose","se prépare."),j2=("Un nouveau","symbole arrive."),j1=("Demain,","tout change."),cd="Activez le compte à rebours",
  merci=("Merci.","5 ans à Fribourg","Cette nouvelle étape,<br>c'est grâce à vous."),
  same=("Même compte.","Nouveau nom.","Vous êtes déjà au bon endroit.<br>Pas besoin de nous chercher."),
  chg="Ce qui change",chg_l=("Le nom","Le symbole","L'identité du studio"),stay="Ce qui reste",stay_l=("L'équipe","La passion","Fribourg"),
  poll=("Vous l'aviez","deviné ?"),polls="Sondage",q=("Une question ?","Posez-la ici — on répond."),
  p2=("5 ans. Une équipe.","Une envie :","aller plus loin."),p5="Un nouveau symbole.",p5s="I + D · la lune, l'encre, le rêve",
  p7=("Votre prochain","tatouage","commence ici."),share="Partagez à un ami fribourgeois",save="Enregistrez ce post",
  swapk="Nouveau nom · Même équipe",swap2="Autre niveau.",
  pm=("Merci,","Fribourg."),pms="5 ans de confiance.<br>Le prochain chapitre commence maintenant.",ex="Anciennement Buda Tattoo"),
 "pt": dict(j3=("Algo está","a chegar."),j2=("Um novo","símbolo chega."),j1=("Amanhã,","tudo muda."),cd="Ativa a contagem decrescente",
  merci=("Obrigado.","5 anos em Friburgo","Esta nova etapa<br>é graças a vocês."),
  same=("Mesma conta.","Novo nome.","Já estás no sítio certo.<br>Não precisas de nos procurar."),
  chg="O que muda",chg_l=("O nome","O símbolo","A identidade do estúdio"),stay="O que fica",stay_l=("A equipa","A paixão","Friburgo"),
  poll=("Já tinhas","adivinhado?"),polls="Sondagem",q=("Tens uma dúvida?","Pergunta aqui — respondemos."),
  p2=("5 anos. Uma equipa.","Uma vontade:","ir mais longe."),p5="Um novo símbolo.",p5s="I + D · a lua, a tinta, o sonho",
  p7=("A tua próxima","tatuagem","começa aqui."),share="Partilha com um amigo de Friburgo",save="Guarda este post",
  swapk="Novo nome · Mesma equipa",swap2="Outro nível.",
  pm=("Obrigado,","Friburgo."),pms="5 anos de confiança.<br>O próximo capítulo começa agora.",ex="Antigo Buda Tattoo")}
for l,x in X.items():
    t=T[l]; K=f'<div class="c kick" style="top:150px">%s</div>'
    # ---- historias
    for n,key,s,top in (("00a-teaser-j3","j3",1,"J-3"),("00b-teaser-j2","j2",2,"J-2"),("00c-teaser-j1","j1",3,"J-1")):
        a,b=x[key]
        page(f"{n}-{l}",l,K%"Dream Ink · Studio"+f'<div class="c h gold" style="top:380px;font-size:300px">{top}</div>'+H(112,a,800)+H(112,G%b,930)+c(1230,x["cd"],"small")+box(1310),70+s)
    page(f"06-merci-{l}",l,K%x["merci"][1]+H(210,G%x["merci"][0],560)+c(900,x["merci"][2],"sub","font-size:48px;line-height:1.4")+logo(1230,200),61)
    page(f"07-same-account-{l}",l,K%"Dream Ink · Studio"+H(110,x["same"][0],620)+H(110,G%x["same"][1],750)+c(1010,x["same"][2],"sub","font-size:42px;line-height:1.45;letter-spacing:.01em")+logo(1260,220),62)
    page(f"08-stays-{l}",l,K%t["same"]+c(430,x["chg"],"small")+"".join(c(500+i*85,v,"sub","font-size:54px") for i,v in enumerate(x["chg_l"]))
      +'<div class="rule" style="position:absolute;left:50%;top:850px;width:160px;height:2px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,#d4a95a,transparent)"></div>'
      +c(910,x["stay"],"small")+"".join(c(980+i*85,v,"sub","font-size:54px") for i,v in enumerate(x["stay_l"]))+logo(1290,180),63)
    page(f"09-poll-{l}",l,K%x["polls"]+logo(260,220)+H(112,x["poll"][0],640)+H(112,G%x["poll"][1],765)+box(1010,260),64)
    page(f"10-questions-{l}",l,K%"Dream Ink · Studio"+logo(260,220)+H(94,x["q"][0],660)+c(840,x["q"][1],"small")+box(940,230),65)
    # ---- publicaciones feed 1080x1440 (carrusel de 7 + 2 sueltas)
    P=lambda i:f"post-c{i}-{l}"
    post(P(1),l,c(130,t["k"],"kick")+logo(200,230)+c(640,'<span class="strike">Buda Tattoo</span>',"mt")+H(150,"Dream Ink",720)+H(150,G%"Studio.",870)+c(1090,t["same"])+c(1280,"→","small","font-size:60px"),101)
    post(P(2),l,c(130,"Dream Ink · Studio","kick")+H(96,x["p2"][0],430)+H(96,x["p2"][1],560)+H(110,G%x["p2"][2],690)+logo(930,230),102)
    post(P(3),l,c(130,t["same"],"kick")+c(330,x["chg"],"small","font-size:44px")+"".join(c(470+i*150,G%v,"h","font-size:80px;font-family:Playfair") for i,v in enumerate(x["chg_l"])),103)
    post(P(4),l,c(130,t["same"],"kick")+c(330,x["stay"],"small","font-size:44px")+"".join(c(470+i*150,v,"h","font-size:80px;font-family:Playfair") for i,v in enumerate(x["stay_l"]))+logo(1010,180),104)
    post(P(5),l,c(130,"Dream Ink · Studio","kick")+logo(210,520)+H(84,x["p5"],900)+c(1130,x["p5s"],"small","font-size:30px"),105)
    post(P(6),l,c(130,t["same"],"kick")+H(112,t["s3"][0],400)+H(112,t["s3"][1],550)+H(112,G%t["s3g"],700)+logo(960,260),106)
    post(P(7),l,c(130,t["loc"],"kick")+logo(190,210)+H(100,x["p7"][0],560)+H(100,G%x["p7"][1],680)+H(100,x["p7"][2],800)+f'<div class="c" style="top:1010px"><span class="cta">{t["cta"]}</span></div>'+c(1150,"↑ "+t["bio"],"small")+c(1260,x["share"],"small","font-size:26px;opacity:.8"),107)
    post(f"post-swap-{l}",l,c(150,x["swapk"],"kick")+c(330,'<span class="strike">Buda Tattoo</span>',"mt","font-size:80px")+c(480,"↓","small","font-size:90px")+H(150,"Dream Ink",640)+H(150,G%"Studio.",790)+c(1030,x["swap2"],"sub")+c(1230,t["loc"],"small"),110)
    post(f"post-merci-{l}",l,c(150,t["k"],"kick")+H(150,x["pm"][0],420)+H(150,G%x["pm"][1],580)+c(860,x["pms"],"sub","font-size:44px;line-height:1.45;letter-spacing:.01em")+logo(1090,170),111)
print("extra ok")
