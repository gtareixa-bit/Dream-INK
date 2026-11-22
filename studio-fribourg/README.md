# Dream Ink Studio · Fribourg  (antes Buda Tattoo)

```
studio-fribourg/
├─ brand/
│  ├─ logo/    monograma ID recortado: gold (PNG transparente 2334×2478), white, on-black, avatar 512/1080 + source-original.jpg
│  └─ fonts/   Cinzel (títulos) · Cormorant Garamond itálica (frases) · Montserrat (texto)  — OFL, libres
├─ web/        sitio listo para subir (FR en /, PT en /pt/). Estático: index.html, config.js, assets/
├─ social/
│  ├─ stories/fr, stories/pt   5 historias 1080×1920 por idioma
│  ├─ profile-grid/            6 recortes 1080×1440 (3:4) + _vista-previa.jpg
│  └─ _src/                    build.py + render.js (regenerar/editar textos)
└─ docs/estrategia-perfil.md   cambio de panel, orden de publicación, captions, bio, checklist web
```
Paleta: negro `#07090b` · oro `#f5e1ae → #d4a95a → #9c6e2e` · acento turquesa `#2fd9c4` (solo detalles).
Regenerar historias/grid: `cd social/_src && python3 build.py && node render.js` (requiere playwright).
Regenerar web: `python3 web/build.py`.
El `index.html` de la raíz del repo (Dream Ink Valencia) **no se ha tocado**.
