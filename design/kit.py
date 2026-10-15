"""Shared design kit for the profile README SVGs — Klinova house style.

Tokens are semantic (light + dark via prefers-color-scheme), type is Geist
(SIL OFL, subset + embedded per file), glass only on the floating layer,
content on opaque surfaces, one accent-filled action per section.
"""
import base64
import io
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

GEIST_DIR = Path(__file__).resolve().parent / "fonts"
WEIGHTS = {400: "Geist-Regular.woff2", 500: "Geist-Medium.woff2", 600: "Geist-SemiBold.woff2"}
MONO = "GeistMono-Regular.woff2"

FONT_STACK = "'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO_STACK = "'Geist Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace"

# ---------------------------------------------------------------- tokens
TOKENS_CSS = """
:root{
  --bg:#FBFBFD; --ground:#F2F4F7; --surface:#FFFFFF; --elevated:#FFFFFF; --paper:#FFFFFF;
  --label:#101828; --secondary:#475467; --tertiary:#667085; --separator:#E4E7EC;
  --accent:#0B7A69; --accent-hover:#096B5C; --on-accent:#FFFFFF; --accent-soft:rgba(11,122,105,.12);
  --success:#067647; --warning:#B54708; --info:#5925DC; --destructive:#B42318;
  --tag-success:#ECFDF3; --tag-warning:#FFFAEB; --tag-info:#F4F3FF; --tag-neutral:#F2F4F7; --tag-neutral-text:#344054;
  --glass:rgba(255,255,255,.62); --glass-border:rgba(16,24,40,.08); --glass-highlight:rgba(255,255,255,.9);
  --track:rgba(16,24,40,.06); --pill:#FFFFFF; --pill-neutral:rgba(16,24,40,.07); --border:rgba(16,24,40,.12);
  --orb-blue:#C3DDF5; --orb-mint:#CBEDE4; --orb-lilac:#DEDAF6; --orb-opacity:1;
  --ink:#101828; --mock-ground:#F2F4F7;
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#0B0D12; --ground:#0B0D12; --surface:#161A22; --elevated:#1E232D;
    --label:#F5F7FA; --secondary:#A6AFBD; --tertiary:#8A94A6; --separator:#2A303B;
    --accent:#34C6AE; --accent-hover:#5EE0C9; --on-accent:#04201B; --accent-soft:rgba(52,198,174,.16);
    --success:#47CD89; --warning:#FDB022; --info:#A48AFB; --destructive:#F97066;
    --tag-success:rgba(71,205,137,.14); --tag-warning:rgba(253,176,34,.14); --tag-info:rgba(164,138,251,.14); --tag-neutral:rgba(255,255,255,.12); --tag-neutral-text:#D0D5DD;
    --glass:rgba(38,44,56,.74); --glass-border:rgba(255,255,255,.16); --glass-highlight:rgba(255,255,255,.18);
    --track:rgba(255,255,255,.08); --pill:#2E3440; --pill-neutral:rgba(255,255,255,.10); --border:rgba(255,255,255,.12);
    --orb-blue:#1F3A5F; --orb-mint:#16463C; --orb-lilac:#332C5C; --orb-opacity:.9;
    --ink:#F5F7FA; --mock-ground:#0F1219;
  }
}
@media (prefers-reduced-motion: reduce){
  *{animation-duration:.01ms !important; animation-delay:0s !important; animation-iteration-count:1 !important;}
}
"""

BASE_CSS = """
.sans{font-family:%s}
.mono{font-family:%s}
.label{fill:var(--label)} .secondary{fill:var(--secondary)} .tertiary{fill:var(--tertiary)}
.on-accent{fill:var(--on-accent)} .accent-text{fill:var(--accent)}
.surface{fill:var(--surface)} .ground{fill:var(--ground)} .bg{fill:var(--bg)}
.sep{stroke:var(--separator)} .border{stroke:var(--border)}
.accent-fill{fill:var(--accent)} .accent-stroke{stroke:var(--accent)}
.ink{stroke:var(--label)} .ink-fill{fill:var(--label)} .ink2{stroke:var(--secondary)}
.glass{fill:var(--glass);stroke:var(--glass-border)} .glass-hl{stroke:var(--glass-highlight)}
.track{fill:var(--track)} .pill{fill:var(--pill)} .pill-neutral{fill:var(--pill-neutral)}
.tag-success{fill:var(--tag-success)} .tag-success-text{fill:var(--success)} .success-stroke{stroke:var(--success)} .success-fill{fill:var(--success)}
.tag-warning{fill:var(--tag-warning)} .tag-warning-text{fill:var(--warning)} .warning-stroke{stroke:var(--warning)} .warning-fill{fill:var(--warning)}
.tag-info{fill:var(--tag-info)} .tag-info-text{fill:var(--info)} .info-stroke{stroke:var(--info)} .info-fill{fill:var(--info)}
.tag-neutral{fill:var(--tag-neutral)} .tag-neutral-text{fill:var(--tag-neutral-text)}
.orb-blue{fill:var(--orb-blue);opacity:var(--orb-opacity)} .orb-mint{fill:var(--orb-mint);opacity:var(--orb-opacity)} .orb-lilac{fill:var(--orb-lilac);opacity:var(--orb-opacity)}
.ease{animation-timing-function:cubic-bezier(.22,1,.36,1)}
""" % (FONT_STACK, MONO_STACK)

EASE_OUT = "cubic-bezier(.22,1,.36,1)"
SPRING = "cubic-bezier(.34,1.56,.64,1)"

# ---------------------------------------------------------------- fonts
_font_cache = {}


def _font(weight):
    if weight not in _font_cache:
        _font_cache[weight] = TTFont(GEIST_DIR / WEIGHTS[weight])
    return _font_cache[weight]


def measure(text, size, weight=600, tracking_em=0.0):
    """Approximate advance width (no kerning) of text at size px."""
    f = _font(weight)
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    upem = f["head"].unitsPerEm
    total = 0.0
    for ch in text:
        gid = cmap.get(ord(ch)) or cmap.get(ord("?"))
        total += hmtx[gid][0] / upem * size
    total += tracking_em * size * max(len(text) - 1, 0)
    return total


def advances(text, size, weight=600, tracking_em=0.0):
    f = _font(weight)
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    upem = f["head"].unitsPerEm
    out = []
    for ch in text:
        gid = cmap.get(ord(ch)) or cmap.get(ord("?"))
        out.append(hmtx[gid][0] / upem * size + tracking_em * size)
    return out


def _subset_b64(path, text):
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga", "calt"]
    opts.hinting = False
    opts.desubroutinize = True
    opts.notdef_outline = True
    opts.name_IDs = ["*"]
    font = subset.load_font(str(path), opts)
    s = subset.Subsetter(opts)
    s.populate(text=text)
    s.subset(font)
    buf = io.BytesIO()
    subset.save_font(font, buf, opts)
    return base64.b64encode(buf.getvalue()).decode()


def _collect_text(svg):
    """All text-node characters inside <text>/<tspan> (for font subsetting)."""
    root = ET.fromstring(svg)
    chars = set()
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag in ("text", "tspan"):
            if el.text:
                chars.update(el.text)
            if el.tail and tag == "tspan":
                chars.update(el.tail)
    chars.update("0123456789 ")
    return "".join(sorted(chars))


def embed_fonts(svg, weights=(400, 500, 600), mono=False):
    text = _collect_text(svg)
    faces = []
    for w in weights:
        b64 = _subset_b64(GEIST_DIR / WEIGHTS[w], text)
        faces.append(f"@font-face{{font-family:'Geist';font-style:normal;font-weight:{w};src:url(data:font/woff2;base64,{b64}) format('woff2')}}")
    if mono:
        b64 = _subset_b64(GEIST_DIR / MONO, text)
        faces.append(f"@font-face{{font-family:'Geist Mono';font-style:normal;font-weight:400;src:url(data:font/woff2;base64,{b64}) format('woff2')}}")
    return svg.replace("/*FONTS*/", "\n".join(faces), 1)


# ---------------------------------------------------------------- helpers
def glass_capsule(x, y, w, h, extra_class="", shadow="url(#glassShadow)"):
    """Floating glass capsule: fill + hairline border + specular top highlight."""
    r = min(w, h) / 2
    hl_y = y + 1.5
    hl_inset = r * 0.45
    return (
        f'<g class="glass-wrap {extra_class}">'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="glass" stroke-width="1" filter="{shadow}"/>'
        f'<path d="M{x + hl_inset} {hl_y} H{x + w - hl_inset}" class="glass-hl" stroke-width="1" stroke-linecap="round" opacity=".9"/>'
        f"</g>"
    )


def glass_rect(x, y, w, h, r, extra_class="", shadow="url(#glassShadow)"):
    hl_y = y + 1.5
    return (
        f'<g class="glass-wrap {extra_class}">'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="glass" stroke-width="1" filter="{shadow}"/>'
        f'<path d="M{x + r} {hl_y} H{x + w - r}" class="glass-hl" stroke-width="1" stroke-linecap="round" opacity=".9"/>'
        f"</g>"
    )


def tag(x, y, text, kind="neutral", icon=None, size=11.5, weight=500, h=20, pad=8):
    """Status tag — 4px radius, word + icon, status colours only."""
    w = measure(text, size, weight) + pad * 2 + (14 if icon else 0)
    icon_svg = ""
    tx = x + pad
    if icon:
        icon_svg = f'<g transform="translate({x + pad},{y + h / 2 - 6})">{ICONS[icon](kind)}</g>'
        tx += 14
    return (
        f'<g class="tag">'
        f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="4" class="tag-{kind}"/>'
        f"{icon_svg}"
        f'<text x="{tx:.1f}" y="{y + h / 2 + size * 0.36:.1f}" font-size="{size}" font-weight="{weight}" class="sans tag-{kind}-text">{text}</text>'
        f"</g>",
        w,
    )


def _stroke_class(kind):
    return {"success": "success-stroke", "warning": "warning-stroke", "info": "info-stroke", "neutral": "ink2"}[kind]


# 12px icon grid, stroke icons of our own
ICONS = {
    "check": lambda k: f'<path d="M2.5 6.5l2.5 2.5 4.5-5" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="{_stroke_class(k)}"/>',
    "alert": lambda k: f'<path d="M6 1.8l4.6 8.2H1.4z" fill="none" stroke-width="1.5" stroke-linejoin="round" class="{_stroke_class(k)}"/><path d="M6 5v2.4M6 8.6v.1" stroke-width="1.5" stroke-linecap="round" class="{_stroke_class(k)}"/>',
    "clock": lambda k: f'<circle cx="6" cy="6" r="4.6" fill="none" stroke-width="1.5" class="{_stroke_class(k)}"/><path d="M6 3.6V6l1.8 1.2" fill="none" stroke-width="1.5" stroke-linecap="round" class="{_stroke_class(k)}"/>',
    "dot": lambda k: f'<circle cx="6" cy="6" r="2.6" class="{ {"success":"success-fill","warning":"warning-fill","info":"info-fill","neutral":"ink-fill"}[k] }"/>',
    "spinner": lambda k: f'<circle cx="6" cy="6" r="4.4" fill="none" stroke-width="1.6" stroke-dasharray="14 9" stroke-linecap="round" class="{_stroke_class(k)} spin"/>',
}


def defs_common():
    return """
  <filter id="glassShadow" x="-20%" y="-40%" width="140%" height="200%">
    <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#101828" flood-opacity=".10"/>
  </filter>
  <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#101828" flood-opacity=".06"/>
  </filter>
  <filter id="mockShadow" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="24" stdDeviation="22" flood-color="#101828" flood-opacity=".16"/>
  </filter>
  <filter id="pillShadow" x="-20%" y="-40%" width="140%" height="200%">
    <feDropShadow dx="0" dy="1" stdDeviation="1.4" flood-color="#101828" flood-opacity=".14"/>
  </filter>
  <filter id="orbBlur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
"""


def orbs(cx1, cy1, r1, cx2, cy2, r2, cx3, cy3, r3):
    return f"""
  <g filter="url(#orbBlur)">
    <circle class="orb-blue drift1" cx="{cx1}" cy="{cy1}" r="{r1}"/>
    <circle class="orb-mint drift2" cx="{cx2}" cy="{cy2}" r="{r2}"/>
    <circle class="orb-lilac drift3" cx="{cx3}" cy="{cy3}" r="{r3}"/>
  </g>"""


ORB_CSS = """
.drift1{animation:drift1 26s ease-in-out infinite}
.drift2{animation:drift2 30s ease-in-out infinite}
.drift3{animation:drift3 22s ease-in-out infinite}
@keyframes drift1{0%,100%{transform:translate(0,0)}50%{transform:translate(60px,30px)}}
@keyframes drift2{0%,100%{transform:translate(0,0)}50%{transform:translate(-50px,-40px)}}
@keyframes drift3{0%,100%{transform:translate(0,0)}50%{transform:translate(30px,50px)}}
"""


def finish(svg, out_path, weights=(400, 500, 600), mono=False):
    svg = embed_fonts(svg, weights, mono)
    # collapse runs of blank lines
    svg = re.sub(r"\n{3,}", "\n\n", svg)
    Path(out_path).write_text(svg)
    return len(svg.encode())
