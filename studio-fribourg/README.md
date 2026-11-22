# Dream Ink Studio · Fribourg  (antes Buda Tattoo)

```
studio-fribourg/
├─ brand/
│  ├─ logo/    monograma ID fino (último logo enviado) recortado: gold (PNG transparente 1545×2166), white, on-black, avatar 512/1080 + source-original.jpg
│  └─ fonts/   Cinzel (títulos) · Cormorant Garamond itálica (frases) · Montserrat (texto)  — OFL, libres
├─ web/        sitio listo para subir en 5 idiomas (FR en /, DE /de/, ES /es/, PT /pt/, EN /en/) con hreflang. Estático: index.html, config.js, assets/
├─ social/
│  ├─ stories/{fr,de,es,pt,en}   14 historias 1080×1920 por idioma (incl. `00d-date`: miércoles 25.11) (JPG) (teasers J-3/2/1, reveal, símbolo, nivel, cuenta atrás, reservar, merci, mismo compte, cambia/queda, sondeo, preguntas)
│  ├─ posts/{fr,de,es,pt,en}       feed 1080×1440: carrusel de 7 (c1…c7) + post-swap + post-merci
│  ├─ profile-grid/{fr,de,es,pt,en}/  6 recortes 1080×1440 (3:4) + _vista-previa.jpg por idioma
│  └─ _src/                    build.py + render.js (regenerar/editar textos)
└─ docs/  plan-transicion.md (calendario D-14→D+30, SEO de 5 años, plantillas) · captions.md · estrategia-perfil.md (panel 3×2, bio, checklist web)
```
Paleta: negro `#07090b` · oro `#f5e1ae → #d4a95a → #9c6e2e` · acento turquesa `#2fd9c4` (solo detalles).
Regenerar historias/grid: `cd social/_src && python3 build.py && ./build_all.sh` (requiere playwright). Historias con la estética del teaser «Tout va changer» (negro, ondas doradas, Playfair + Montserrat); panel de perfil con estatuas + logo ID.
Regenerar web: `python3 web/build.py`.
El `index.html` de la raíz del repo (Dream Ink Valencia) **no se ha tocado**.

Idiomas: Français · Deutsch · Español · Português · English — todo el material (historias, posts, panel, web, captions, plantillas) existe en los 5.
