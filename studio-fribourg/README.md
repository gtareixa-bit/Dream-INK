# Dream Ink Studio · Fribourg  (antes Buda Tattoo)

```
studio-fribourg/
├─ brand/
│  ├─ logo/    monograma ID fino (último logo enviado) recortado: gold (PNG transparente 1545×2166), white, on-black, avatar 512/1080 + source-original.jpg
│  └─ fonts/   Cinzel (títulos) · Cormorant Garamond itálica (frases) · Montserrat (texto)  — OFL, libres
├─ web/        sitio listo para subir (FR en /, PT en /pt/). Estático: index.html, config.js, assets/
├─ social/
│  ├─ stories/fr, stories/pt   13 historias 1080×1920 por idioma (teasers J-3/2/1, reveal, símbolo, nivel, cuenta atrás, reservar, merci, mismo compte, cambia/queda, sondeo, preguntas)
│  ├─ posts/fr, posts/pt       feed 1080×1440: carrusel de 7 (c1…c7) + post-swap + post-merci
│  ├─ profile-grid/            6 recortes 1080×1440 (3:4) + _vista-previa.jpg
│  └─ _src/                    build.py + render.js (regenerar/editar textos)
└─ docs/  plan-transicion.md (calendario D-14→D+30, SEO de 5 años, plantillas) · captions.md · estrategia-perfil.md (panel 3×2, bio, checklist web)
```
Paleta: negro `#07090b` · oro `#f5e1ae → #d4a95a → #9c6e2e` · acento turquesa `#2fd9c4` (solo detalles).
Regenerar historias/grid: `cd social/_src && python3 build.py && python3 build_stories.py && python3 build_extra.py && node render.js` (requiere playwright). Historias con la estética del teaser «Tout va changer» (negro, ondas doradas, Playfair + Montserrat); panel de perfil con estatuas + logo ID.
Regenerar web: `python3 web/build.py`.
El `index.html` de la raíz del repo (Dream Ink Valencia) **no se ha tocado**.
