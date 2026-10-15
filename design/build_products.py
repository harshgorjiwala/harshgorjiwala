"""products.svg — four opaque 24px cards on the grouped ground; each card carries a
small live UI motif built from the same kit (inset lists, status tags with word +
icon, glass only on floating controls, one accent)."""
import kit
from kit import glass_capsule, tag, measure

W = 1000
MX, GAP = 40, 16
CW = (W - 2 * MX - GAP) / 2  # 452
CH = 212
TOP = 150
H = TOP + 2 * CH + GAP + MX  # 630

CSS = kit.TOKENS_CSS + kit.BASE_CSS + """
.paper{fill:#FFFFFF} .paper-ink{fill:#101828} .paper-ink-s{stroke:#101828} .paper-mute{fill:#98A2B3}
.card-in{opacity:0;animation:cardin .8s cubic-bezier(.22,1,.36,1) both}
@keyframes cardin{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
.rise{opacity:0;animation:rise .7s cubic-bezier(.22,1,.36,1) both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.spin{transform-box:fill-box;transform-origin:50% 50%;animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* Klinova: queue, 10s loop — rows file one after another */
.kA{animation:kA 10s step-end infinite} .kB{animation:kB 10s step-end infinite}
@keyframes kA{0%,28%{opacity:1}29%,92%{opacity:0}93%,100%{opacity:1}}
@keyframes kB{0%,28%{opacity:0}29%,92%{opacity:1}93%,100%{opacity:0}}
.kA2{animation:kA2 10s step-end infinite} .kB2{animation:kB2 10s step-end infinite}
@keyframes kA2{0%,52%{opacity:1}53%,92%{opacity:0}93%,100%{opacity:1}}
@keyframes kB2{0%,52%{opacity:0}53%,92%{opacity:1}93%,100%{opacity:0}}
.kcount{animation:kcount 10s step-end infinite} .kcount2{animation:kcount2 10s step-end infinite} .kcount3{animation:kcount3 10s step-end infinite}
@keyframes kcount{0%,28%{opacity:1}29%,92%{opacity:0}93%,100%{opacity:1}}
@keyframes kcount2{0%,28%{opacity:0}29%,52%{opacity:1}53%,100%{opacity:0}}
@keyframes kcount3{0%,52%{opacity:0}53%,92%{opacity:1}93%,100%{opacity:0}}

/* SignProof: signature draws, seal springs, glass bar slides up — 9s loop */
.sig{stroke-dasharray:1;stroke-dashoffset:1;animation:sig 9s cubic-bezier(.45,0,.3,1) infinite}
@keyframes sig{0%,6%{stroke-dashoffset:1}34%,94%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
.pen{opacity:0;animation:pen 9s cubic-bezier(.45,0,.3,1) infinite}
@keyframes pen{0%,6%{opacity:0;transform:translate(0,0)}8%{opacity:1}34%{opacity:1;transform:translate(104px,-10px)}38%,100%{opacity:0;transform:translate(104px,-10px)}}
.seal{opacity:0;transform-box:fill-box;transform-origin:50% 50%;animation:seal 9s cubic-bezier(.34,1.56,.64,1) infinite}
@keyframes seal{0%,38%{opacity:0;transform:scale(2) rotate(-20deg)}44%,94%{opacity:1;transform:scale(1) rotate(-8deg)}100%{opacity:0}}
.sbar{opacity:0;animation:sbar 9s cubic-bezier(.22,1,.36,1) infinite}
@keyframes sbar{0%,44%{opacity:0;transform:translateY(14px)}50%,94%{opacity:1;transform:translateY(0)}100%{opacity:0}}

/* PartTrace: sweep + blips (4s) */
.sweep{transform-box:fill-box;transform-origin:0 100%;animation:spin 4s linear infinite}
.blip{transform-box:fill-box;transform-origin:50% 50%;opacity:0;animation:blip 4s ease-out infinite}
@keyframes blip{0%{transform:scale(1);opacity:.8}25%{transform:scale(4);opacity:0}100%{transform:scale(4);opacity:0}}
.pulse{transform-box:fill-box;transform-origin:50% 50%;animation:pulse 2s ease-out infinite}
@keyframes pulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(3);opacity:0}}

/* PolicyPulse: signals stagger in, ring + sparkline draw — 9s loop */
.sigrow{opacity:0;animation:sigrow 9s ease-out infinite}
@keyframes sigrow{0%{opacity:0;transform:translateX(-10px)}6%{opacity:1;transform:translateX(0)}92%{opacity:1}97%,100%{opacity:0}}
.ring{stroke-dasharray:1;stroke-dashoffset:1;animation:ring 9s cubic-bezier(.22,1,.36,1) infinite}
@keyframes ring{0%,14%{stroke-dashoffset:1}48%,92%{stroke-dashoffset:.28}100%{stroke-dashoffset:1}}
.ringtxt{opacity:0;animation:fadeloop 9s infinite}
@keyframes fadeloop{0%,26%{opacity:0}40%,92%{opacity:1}100%{opacity:0}}
.spark{stroke-dasharray:1;stroke-dashoffset:1;animation:spark 9s cubic-bezier(.22,1,.36,1) infinite}
@keyframes spark{0%,10%{stroke-dashoffset:1}55%,92%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
.sparkfill{opacity:0;animation:sparkfill 9s infinite}
@keyframes sparkfill{0%,50%{opacity:0}60%,92%{opacity:1}100%{opacity:0}}
"""


def icon_doc(cls, s=1.5):
    return f'<path d="M5 2.5h5.5L14.5 6.5V15a1 1 0 0 1-1 1h-8.5a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1z M10.5 2.5v4h4 M6.5 9.5h5 M6.5 12.5h5" fill="none" stroke-width="{s}" stroke-linejoin="round" stroke-linecap="round" class="{cls}"/>'


# ---- product marks (22px grid, our own strokes)
MARKS = {
    "klinova": '<path d="M11 4v14M4 11h14" stroke-width="2.4" stroke-linecap="round" class="accent-stroke"/>',
    "signproof": '<path d="M4 16c3-7 6-10 10-11l-2 4c3-1 5 0 4 2-3 2-6 3-9 5z M4.5 18h13" fill="none" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" class="accent-stroke"/>',
    "parttrace": '<circle cx="8" cy="14" r="2" class="accent-fill"/><path d="M11 10.5a5 5 0 0 1 1.5 3.5M14 7.5a9 9 0 0 1 2.6 6.5M17 4.5a13 13 0 0 1 3.8 9.5" fill="none" stroke-width="1.8" stroke-linecap="round" class="accent-stroke"/>',
    "policypulse": '<path d="M3 15l5-6 4 3 6-8" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="accent-stroke"/><path d="M14 4h4v4" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="accent-stroke"/>',
}


def card_shell(x, y, name, category, mark, desc_lines, delay):
    cat, _ = tag(x + 20, y + 118, category, "neutral")
    desc = "".join(
        f'<text x="{x + 20}" y="{y + 154 + i * 19}" font-size="13.5" class="sans secondary">{t}</text>' for i, t in enumerate(desc_lines)
    )
    return f"""
  <g class="card-in" style="animation-delay:{delay}s">
    <rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="24" class="surface border" stroke-width="1" filter="url(#cardShadow)"/>
    <rect x="{x + 20}" y="{y + 20}" width="44" height="44" rx="14" fill="var(--accent-soft)"/>
    <g transform="translate({x + 31},{y + 31})">{MARKS[mark]}</g>
    <text x="{x + 20}" y="{y + 100}" font-size="20" font-weight="600" letter-spacing="-.015em" class="sans label">{name}</text>
    {cat}
    {desc}
  </g>"""


def panel(x, y, w=190, h=184):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="ground"/>'


# ---------------------------------------------------------------- motifs
def motif_klinova(x, y):
    """Inset grouped list of incoming faxes; rows file one by one; glass header floats over it."""
    rows = [("Rx renewal", "2 pages · 09:12"), ("Lab order", "1 page · 09:15"), ("Referral", "3 pages · 09:21")]
    out = []
    for i, (t, m) in enumerate(rows):
        ry = y + 48 + i * 44
        if i == 0:
            tg, w = tag(0, ry + 12, "Filed", "success", icon="check", size=11, h=20)
            tags = f'<g transform="translate({x + 180 - w:.1f},0)">{tg}</g>'
        elif i == 1:
            a, wa = tag(0, ry + 12, "Parsing", "neutral", icon="spinner", size=11, h=20)
            b, wb = tag(0, ry + 12, "Filed", "success", icon="check", size=11, h=20)
            tags = f'<g class="kA" transform="translate({x + 180 - wa:.1f},0)">{a}</g><g class="kB" transform="translate({x + 180 - wb:.1f},0)">{b}</g>'
        else:
            a, wa = tag(0, ry + 12, "Queued", "neutral", icon="clock", size=11, h=20)
            b, wb = tag(0, ry + 12, "Filed", "success", icon="check", size=11, h=20)
            tags = f'<g class="kA2" transform="translate({x + 180 - wa:.1f},0)">{a}</g><g class="kB2" transform="translate({x + 180 - wb:.1f},0)">{b}</g>'
        sep = f'<path d="M{x + 44} {ry} H{x + 180}" class="sep" stroke-width="1"/>' if i else ""
        out.append(f"""
      {sep}
      <rect x="{x + 10}" y="{ry + 9}" width="26" height="26" rx="7" class="tag-neutral"/>
      <g transform="translate({x + 14},{ry + 13})">{icon_doc("ink2", 1.4)}</g>
      <text x="{x + 44}" y="{ry + 19}" font-size="11.5" font-weight="500" class="sans label">{t}</text>
      <text x="{x + 44}" y="{ry + 32}" font-size="9.5" class="sans secondary">{m}</text>
      {tags}""")
    counts = (
        f'<text x="{x + 172}" y="{y + 25}" font-size="10" font-weight="600" text-anchor="end" class="sans secondary kcount">2 pending</text>'
        f'<text x="{x + 172}" y="{y + 25}" font-size="10" font-weight="600" text-anchor="end" class="sans secondary kcount2">1 pending</text>'
        f'<text x="{x + 172}" y="{y + 25}" font-size="10" font-weight="600" text-anchor="end" class="sans tag-success-text kcount3">All filed</text>'
    )
    return f"""
    <rect x="{x}" y="{y}" width="190" height="184" rx="12" class="surface border" stroke-width="1"/>
    {''.join(out)}
    <!-- floating glass header -->
    {glass_capsule(x + 8, y + 8, 174, 30)}
    <text x="{x + 20}" y="{y + 27}" font-size="11.5" font-weight="600" class="sans label">Fax intake</text>
    {counts}"""


def motif_signproof(x, y):
    """Signing paper (always light), self-drawing signature, teal seal, glass bar."""
    return f"""
    {panel(x, y)}
    <rect x="{x + 22}" y="{y + 12}" width="146" height="172" rx="8" class="paper" filter="url(#cardShadow)"/>
    <rect x="{x + 36}" y="{y + 26}" width="60" height="5" rx="2.5" fill="#667085"/>
    <rect x="{x + 36}" y="{y + 40}" width="116" height="4" rx="2" fill="#E4E7EC"/>
    <rect x="{x + 36}" y="{y + 50}" width="100" height="4" rx="2" fill="#E4E7EC"/>
    <rect x="{x + 36}" y="{y + 60}" width="110" height="4" rx="2" fill="#E4E7EC"/>
    <rect x="{x + 36}" y="{y + 70}" width="74" height="4" rx="2" fill="#E4E7EC"/>
    <path d="M{x + 36} {y + 126} H{x + 154}" stroke="#98A2B3" stroke-width="1" stroke-dasharray="3 2"/>
    <text x="{x + 36}" y="{y + 138}" font-size="7" font-weight="500" letter-spacing=".08em" class="sans paper-mute">SIGNATURE</text>
    <path class="sig" pathLength="1" d="M{x + 40} {y + 120}c4-16 9-24 13-12 3 9-3 17-7 14-4-4 6-18 15-20 7-2 2 14 9 12 6-2 8-14 14-10 5 4-1 14 7 10 7-4 9-14 17-8 5 4 0 12 8 8 7-4 10-9 18-6 4 2 6 5 10 4" fill="none" stroke="#1B2A4A" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/>
    <g class="pen"><path d="M{x + 42} {y + 116}l6-6 3 3-6 6-4 1z" fill="#F2F4F7" stroke="#101828" stroke-width="1"/></g>
    <g transform="translate({x + 142},{y + 36})"><g class="seal">
      <circle r="20" class="accent-fill"/>
      <circle r="15.5" fill="none" stroke="var(--on-accent)" stroke-width="1" stroke-dasharray="2.5 2" opacity=".8"/>
      <path d="M-7 0l5 5 9-10" fill="none" stroke="var(--on-accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
    </g></g>
    <g class="sbar">
      {glass_capsule(x + 14, y + 146, 162, 30)}
      <g transform="translate({x + 26},{y + 155})">{kit.ICONS["check"]("success")}</g>
      <text x="{x + 44}" y="{y + 165}" font-size="10.5" font-weight="500" class="sans label">Sealed</text>
      <text x="{x + 164}" y="{y + 165}" font-size="9.5" text-anchor="end" class="mono secondary">9f3a…c21e</text>
    </g>"""


def motif_parttrace(x, y):
    cx, cy = x + 95, y + 84
    blips = [(0.5, 26, -32), (1.7, 32, 44), (2.6, -28, 22), (3.4, -46, -24)]
    b = "".join(
        f'<circle class="blip accent-stroke" style="animation-delay:{d}s" cx="{cx + dx}" cy="{cy + dy}" r="3" fill="none" stroke-width="1"/>'
        f'<circle cx="{cx + dx}" cy="{cy + dy}" r="3" class="accent-fill"/>'
        for d, dx, dy in blips
    )
    live, lw = tag(0, y + 10, "Live", "success", icon="dot", size=10.5, h=18)
    tg, tw = tag(0, y + 150, "PT-0418 · Bay 3", "neutral", size=10.5, h=20)
    return f"""
    {panel(x, y)}
    <circle cx="{cx}" cy="{cy}" r="68" fill="none" class="sep" stroke-width="1"/>
    <circle cx="{cx}" cy="{cy}" r="46" fill="none" class="sep" stroke-width="1"/>
    <circle cx="{cx}" cy="{cy}" r="24" fill="none" class="sep" stroke-width="1"/>
    <path d="M{cx - 68} {cy}H{cx + 68}M{cx} {cy - 68}V{cy + 68}" class="sep" stroke-width="1" opacity=".7"/>
    <g class="sweep"><path d="M{cx} {cy}L{cx} {cy - 68}A68 68 0 0 1 {cx + 48.1} {cy - 48.1}Z" fill="url(#sweepGrad)"/><path d="M{cx} {cy}L{cx} {cy - 68}" class="accent-stroke" stroke-width="1.4" opacity=".9"/></g>
    <circle cx="{cx}" cy="{cy}" r="3" class="accent-fill"/>
    {b}
    <g transform="translate({x + 180 - lw:.1f},0)">{live}</g>
    <g transform="translate({x + 10},0)">{tg}</g>"""


def motif_policypulse(x, y):
    sigs = [("Rate decision · hold", "success", 0.2), ("Carbon levy · draft", "warning", 0.9), ("Filing · 10-K", "info", 1.6)]
    rows = ""
    for i, (t, k, d) in enumerate(sigs):
        ry = y + 12 + i * 26
        rows += f"""
      <g class="sigrow" style="animation-delay:{d}s">
        <rect x="{x + 10}" y="{ry}" width="112" height="22" rx="6" class="surface border" stroke-width="1"/>
        <g transform="translate({x + 15},{ry + 5})">{kit.ICONS["dot"](k)}</g>
        <text x="{x + 32}" y="{ry + 15}" font-size="9.5" font-weight="500" class="sans label">{t}</text>
      </g>"""
    rcx, rcy = x + 158, y + 40
    return f"""
    {panel(x, y)}
    {rows}
    <circle cx="{rcx}" cy="{rcy}" r="22" fill="none" class="sep" stroke-width="5"/>
    <circle class="ring accent-stroke" pathLength="1" cx="{rcx}" cy="{rcy}" r="22" fill="none" stroke-width="5" stroke-linecap="round" transform="rotate(-90 {rcx} {rcy})"/>
    <text class="ringtxt sans label" x="{rcx}" y="{rcy + 4.5}" font-size="13" font-weight="600" text-anchor="middle">72</text>
    <text class="ringtxt sans secondary" x="{rcx}" y="{rcy + 36}" font-size="8.5" font-weight="500" text-anchor="middle" letter-spacing=".06em">IMPACT</text>
    <text x="{x + 12}" y="{y + 106}" font-size="9.5" font-weight="500" class="sans secondary">Thesis confidence</text>
    <path d="M{x + 12} {y + 170}H{x + 178}" class="sep" stroke-width="1"/>
    <path class="sparkfill" d="M{x + 14} {y + 156}L{x + 36} {y + 148}L{x + 58} {y + 152}L{x + 80} {y + 136}L{x + 102} {y + 142}L{x + 124} {y + 126}L{x + 146} {y + 130}L{x + 176} {y + 114}L{x + 176} {y + 170}L{x + 14} {y + 170}Z" fill="url(#sparkGrad)"/>
    <path class="spark accent-stroke" pathLength="1" d="M{x + 14} {y + 156}L{x + 36} {y + 148}L{x + 58} {y + 152}L{x + 80} {y + 136}L{x + 102} {y + 142}L{x + 124} {y + 126}L{x + 146} {y + 130}L{x + 176} {y + 114}" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="{x + 176}" cy="{y + 114}" r="3" class="accent-fill ringtxt"/>"""


def build():
    cards = [
        ("Klinova", "Healthcare", "klinova", ["Multi-tenant platform for", "pharmacies: fax intake, clinical", "workflows and billing."], motif_klinova),
        ("SignProof", "e-Signature", "signproof", ["Canadian e-signature with", "tamper-evident audit trails,", "hosted in Canada."], motif_signproof),
        ("PartTrace", "Manufacturing", "parttrace", ["Standalone, in-facility RFID", "parts tracking for small and", "midsize manufacturers."], motif_parttrace),
        ("PolicyPulse", "Research", "policypulse", ["An engine that turns policy and", "regulatory signals into", "investment research."], motif_policypulse),
    ]
    body = ""
    for i, (name, cat, mark, desc, motif) in enumerate(cards):
        col, row = i % 2, i // 2
        x = MX + col * (CW + GAP)
        y = TOP + row * (CH + GAP)
        mx, my = x + CW - 12 - 190, y + 14
        body += card_shell(x, y, name, cat, mark, desc, 0.15 + i * 0.12)
        body += f'<g class="card-in" style="animation-delay:{0.25 + i * 0.12:.2f}s">{motif(mx, my)}</g>'

    sub = "Each product carries only what makes it different — auth, signing, storage and payments are shared services."
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">What I'm building — Klinova, SignProof, PartTrace, PolicyPulse</title>
<desc id="d">Four product cards: Klinova (pharmacy and healthcare, fax intake list), SignProof (Canadian e-signature, a signature being drawn and sealed), PartTrace (RFID parts tracking radar), PolicyPulse (policy signals, impact score and confidence sparkline).</desc>
<style>
/*FONTS*/
{CSS}
</style>
<defs>
  {kit.defs_common()}
  <linearGradient id="sweepGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="var(--accent)" stop-opacity="0"/><stop offset="1" stop-color="var(--accent)" stop-opacity=".35"/></linearGradient>
  <linearGradient id="sparkGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--accent)" stop-opacity=".28"/><stop offset="1" stop-color="var(--accent)" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" rx="28" class="ground"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" class="border" stroke-width="1" opacity=".6"/>
<text x="{MX}" y="54" font-size="13" font-weight="500" class="sans secondary rise" style="animation-delay:.05s">What I'm building</text>
<text x="{MX}" y="92" font-size="34" font-weight="600" letter-spacing="-.02em" class="sans label rise" style="animation-delay:.1s">Four products, one backbone.</text>
<text x="{MX}" y="120" font-size="16" class="sans secondary rise" style="animation-delay:.15s">{sub}</text>
{body}
</svg>
"""


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "../assets/products.svg"
    n = kit.finish(build(), out, mono=True)
    print(f"products.svg {n/1024:.1f} KB")
