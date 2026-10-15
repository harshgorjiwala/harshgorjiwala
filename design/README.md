# How this page is built

Everything on the profile is a hand-written SVG rendered by GitHub as an `<img>`. That sandbox allows no JavaScript, no external fonts and no network requests — so each file carries its own CSS keyframes, a few SMIL animations, and a subset of the Geist typeface embedded as a data URI.

## Design system

The visuals follow one small system (a cousin of the Klinova house style):

- **Two layers.** Glass (`rgba(255,255,255,.62)` + hairline + specular highlight) only on the floating layer — the nav capsule, icon rail, toasts, chips. Content sits on opaque surfaces.
- **One accent per section.** Teal means "the primary action". Status colours always come with a word *and* an icon. Selection is neutral (white pill on a grey track), never accent-filled.
- **Concentric corners.** Inner radius = outer radius − padding (cards 24 → panels 12, capsules 999).
- **Semantic tokens, two modes.** Every colour is a CSS custom property with a light and a dark value; `@media (prefers-color-scheme: dark)` swaps them inside the SVG, so the page follows the viewer's system theme.
- **Motion.** Ease-out `cubic-bezier(.22,1,.36,1)` for entrances, a spring `cubic-bezier(.34,1.56,.64,1)` for pills and seals, 40–80 ms stagger, and `prefers-reduced-motion` collapses everything to fades.
- **Type.** Geist (SIL OFL), subset per file to the glyphs actually used and embedded inline. Headlines are tight (−0.04 em), body is 13–17 px.

## Files

| file | builds |
|---|---|
| `kit.py` | tokens, Geist subsetting/embedding, text measurement, glass + tag helpers |
| `build_hero.py` | `assets/hero.svg` — nav, headline reveal, swoosh, seal, console mock |
| `build_products.py` | `assets/products.svg` — four product cards with live UI motifs |
| `build_rest.py` | `assets/stack.svg`, `assets/principles.svg`, `assets/contact.svg` |

```bash
pip install fonttools brotli
cd design
python3 build_hero.py && python3 build_products.py && python3 build_rest.py
```

Geist is © Vercel, licensed under the SIL Open Font License 1.1 (`fonts/LICENSE-Geist.txt`).
