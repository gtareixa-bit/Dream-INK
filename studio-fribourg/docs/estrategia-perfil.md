# Estrategia de lanzamiento · Dream Ink Studio

## 1. Panel gigante del perfil (3×2)
Archivos: `social/profile-grid/subir-1…6`. **Orden: sube 1 → 6** (Instagram coloca lo último arriba-izquierda, por eso ya están numerados al revés).
1. Antes: archiva (no borres) los posts antiguos que rompan la estética; o publica el panel y deja pasar.
2. Sube los 6 **el mismo día, seguidos, en 10 minutos** (formato 3:4, 1080×1440, sin recortar, sin filtro). Al 6.º el panel se completa.
3. Mismo día: cambia **foto de perfil** (`brand/logo/dream-ink-avatar-512.png`), **nombre** y **bio**.
4. Si tu cuenta aún muestra la cuadrícula 1:1 antigua, Instagram recorta a 3:4 en el centro: los tiles ya están en ese formato.
5. Fija (pin) los 3 posts de la fila superior solo si quieres que el panel no se mueva con nuevas publicaciones. Los nuevos posts empujarán el panel hacia abajo: publica **en múltiplos de 3** o fija los tiles.
6. Caption igual en los 6 (ver abajo) para no ensuciar el feed; comentarios activados.

## 2. Calendario (historias, ya tienes el teaser “Tout va changer”)
| Día | Historia | Acción |
|---|---|---|
| D-2 | `04-countdown` | Añade sticker **cuenta atrás** en el marco vacío |
| D-1 | `02-symbol` | Revela el símbolo; pregunta/encuesta “¿Lo ves?” |
| D | `01-reveal` → `03-level` → `05-book` | Publica el panel (6 posts) + 3 historias; fija `01-reveal` en destacadas |
| D+1…3 | Reels/fotos del equipo y del nuevo estudio | Etiqueta ubicación Fribourg |
Hora sugerida: 18:00–20:00 (Suiza). Usa el sticker de enlace con la web en `05-book`.

## 3. Textos
**Nombre del perfil:** `Dream Ink Studio` · **Usuario:** `@dreamink.studio` (o el libre más cercano; mantener enlace desde el antiguo).
**Bio (FR):**
`Dream Ink Studio · ex Buda Tattoo`
`Tatouage d'auteur · Fribourg 🇨🇭`
`Même équipe · Autre niveau`
`↓ Réserver`
**Bio (PT):** `Tatuagem de autor · Friburgo · Mesma equipa, outro nível`
**Caption panel (FR):** *Buda Tattoo devient Dream Ink Studio. Même équipe, autre niveau. Bienvenue dans le nouveau chapitre. 🌙 #fribourg #tatouage #dreamink #tattoofribourg #suisse #tatouagesuisse*
**Caption (PT):** *O Buda Tattoo passa a Dream Ink Studio. Mesma equipa, outro nível. Bem-vindos ao novo capítulo. 🌙*
**Historia 05 – sticker:** enlace a la web; **Destacadas:** “Nouveau”, “Projets”, “Contact”, “Infos”.

## 4. Checklist para cambiar la web de Buda
1. Rellena `web/config.js` (teléfono, email, dirección, Instagram, enlace de reservas). Vacío = se oculta.
2. Revisa textos en `web/build.py` (no se han inventado servicios, estilos ni precios; añade los reales).
3. Sube `web/` entero al hosting de Buda (o al servidor de la web) conservando carpetas. Si la web es Wix/WordPress/Squarespace: usa `assets/*` (logo, favicon, og-image, fuentes) y copia los textos de `index.html`.
4. Dominio: mantén el de Buda y añade **redirección 301** del dominio/páginas antiguas → nueva home. Si hay dominio nuevo, 301 del antiguo al nuevo.
5. Google Business Profile: cambia el nombre (“Dream Ink Studio”, categoría Tattoo shop), logo (`avatar-1080`), portada, horarios; avisa en “Novedades”. **Es el cambio SEO más importante**: conserva reseñas.
6. Actualiza: Facebook, TikTok, WhatsApp Business (foto), firma de email, tarjetas, rótulo/escaparate, Doctolib/agenda/reservas.
7. Completa JSON-LD (`<script type="application/ld+json">`) con dirección y teléfono reales; verifica en search.google.com/test/rich-results.
8. Comprueba: Lighthouse móvil, `og-image.jpg` en el depurador de Facebook, favicon.
9. Legal CH: revisa mención legal/privacidad si hay formulario o cookies (no hay tracking incluido).

## 5. Notas y límites
- El logo es un recorte raster del arte original (799 px); está reescalado ×3. Para rótulo/imprenta/bordados **hay que vectorizar o pedir el original** al creador.
- El fondo de estatuas procede de capturas del sitio: resolución suficiente para pantalla, no para impresión.
- No se menciona sedación en nada de Fribourg (era un servicio de Valencia con marco médico distinto); no comuniques servicios médicos en Suiza sin validar normativa.
- Fuentes y datos inventados: ninguno; los 5 años salen de vuestro teaser.
