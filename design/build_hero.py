"""hero.svg — Klinova marketing-hero layout: orbs, glass capsule nav, status chip,
line-mask headline with a letter flip, hand-drawn swoosh, springing seal,
one accent CTA, and a console mock (glass rail, neutral segmented, opaque list,
glass toast) with parallax glass chips."""
import kit
from kit import glass_capsule, glass_rect, tag, measure, advances

W, H = 1000, 480
X0 = 60  # left column

# ---------- headline metrics (Geist SemiBold 62, tracking -0.04em)
HS, TR = 62, -0.04
line1 = "One backbone."
word = "Many"
rest = " products."
adv = advances(word, HS, 600, TR)
w_word_space = sum(adv) + advances(" ", HS, 600, TR)[0]
x_rest = X0 + w_word_space
w_rest = measure(rest.strip(), HS, 600, TR)
line1_w = measure(line1, HS, 600, TR)

letters = []
x = X0
for i, ch in enumerate(word):
    letters.append(
        f'<text x="{x:.1f}" y="274" font-size="{HS}" font-weight="600" letter-spacing="{TR}em" '
        f'class="sans label flip" style="animation-delay:{1.05 + i * 0.07:.2f}s">{ch}</text>'
    )
    x += adv[i]

# ---------- nav metrics
name_w = measure("Harsh Gorjiwala", 15, 600)
cta_w = measure("Say hello", 14, 600) + 36
cta_x = 954 - cta_w

# ---------- CTAs
p_text = "See what I'm building"
p_w = measure(p_text, 15, 600) + 44
s_text = "Get in touch"
s_w = measure(s_text, 15, 600) + 44
s_x = X0 + p_w + 12

CSS = kit.TOKENS_CSS + kit.BASE_CSS + kit.ORB_CSS + """
.only-dark{display:none}
@media (prefers-color-scheme: dark){ .only-light{display:none} .only-dark{display:inline} }
.st-sec{stop-color:var(--secondary)} .st-lab{stop-color:var(--label)}

/* entrances */
.rise{opacity:0;animation:rise .8s cubic-bezier(.22,1,.36,1) both}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.mask-line{transform:translateY(84px);animation:maskline .85s cubic-bezier(.22,1,.36,1) both}
@keyframes maskline{to{transform:translateY(0)}}
.flip{opacity:0;transform-box:fill-box;transform-origin:50% 100%;animation:flip .6s cubic-bezier(.34,1.56,.64,1) both}
@keyframes flip{0%{opacity:0;transform:scaleY(0) translateY(-8px)}100%{opacity:1;transform:scaleY(1) translateY(0)}}
.pop{opacity:0;transform-box:fill-box;transform-origin:50% 50%;animation:pop .6s cubic-bezier(.34,1.56,.64,1) both}
@keyframes pop{from{opacity:0;transform:scale(.8)}to{opacity:1;transform:scale(1)}}
.mock-in{opacity:0;animation:mockin 1s cubic-bezier(.22,1,.36,1) .35s both}
@keyframes mockin{from{opacity:0;transform:translate(0,44px) scale(.97)}to{opacity:1;transform:translate(0,0) scale(1)}}

/* swoosh + seal */
.swoosh{stroke-dasharray:1;stroke-dashoffset:1;animation:draw .7s cubic-bezier(.22,1,.36,1) 1.55s forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.seal{opacity:0;transform-box:fill-box;transform-origin:50% 50%;animation:seal .55s cubic-bezier(.34,1.56,.64,1) 2s both}
@keyframes seal{0%{opacity:0;transform:scale(2.1) rotate(-28deg)}100%{opacity:1;transform:scale(1) rotate(-12deg)}}
.seal-ring{transform-box:fill-box;transform-origin:50% 50%;animation:spin 48s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* status chip */
.pulse{transform-box:fill-box;transform-origin:50% 50%;animation:pulse 2.2s ease-out infinite}
@keyframes pulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(3);opacity:0}}

/* nav segmented pill — springs between Work / Stack / Contact */
.segpill{animation:segpill 12s cubic-bezier(.34,1.56,.64,1) 2.5s infinite}
@keyframes segpill{0%,30%{transform:translateX(0)}33.3%,63.3%{transform:translateX(66.7px)}66.6%,96.6%{transform:translateX(133.4px)}100%{transform:translateX(0)}}
.sel1{animation:sel1 12s step-end 2.5s infinite} .sel2{animation:sel2 12s step-end 2.5s infinite} .sel3{animation:sel3 12s step-end 2.5s infinite}
@keyframes sel1{0%,31%{opacity:1}32%,98%{opacity:0}99%,100%{opacity:1}}
@keyframes sel2{0%,32%{opacity:0}33%,64%{opacity:1}65%,100%{opacity:0}}
@keyframes sel3{0%,65%{opacity:0}66%,98%{opacity:1}99%,100%{opacity:0}}
.sheen{animation:sheen 7s ease-in-out 3s infinite}
@keyframes sheen{0%{transform:translateX(-60px) skewX(-20deg)}30%,100%{transform:translateX(160px) skewX(-20deg)}}

/* mock: row 2 processing → filed, toast */
.spin{transform-box:fill-box;transform-origin:50% 50%;animation:spin 1s linear infinite}
.proc{animation:proc 9s step-end infinite} .filed{animation:filed 9s step-end infinite}
@keyframes proc{0%,40%{opacity:1}41%,93%{opacity:0}94%,100%{opacity:1}}
@keyframes filed{0%,40%{opacity:0}41%,93%{opacity:1}94%,100%{opacity:0}}
.toast{opacity:0;animation:toast 9s cubic-bezier(.22,1,.36,1) infinite}
@keyframes toast{0%,40%{opacity:0;transform:translateY(16px)}45%,80%{opacity:1;transform:translateY(0)}86%,100%{opacity:0;transform:translateY(10px)}}
.row{opacity:0;animation:rise .6s cubic-bezier(.22,1,.36,1) both}

/* parallax chips */
.par1{animation:par1 9s ease-in-out infinite} .par2{animation:par2 11s ease-in-out infinite}
@keyframes par1{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
@keyframes par2{0%,100%{transform:translateY(0)}50%{transform:translateY(8px)}}
"""

# ---------- icons (18px grid, our own strokes)
def icon_inbox(cls):
    return f'<path d="M3 10l2.2-6h7.6L15 10v4.5a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z M3 10h3.5l1.2 2.2h2.6l1.2-2.2H15" fill="none" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" class="{cls}"/>'

def icon_doc(cls, s=1.6):
    return f'<path d="M5 2.5h5.5L14.5 6.5V15a1 1 0 0 1-1 1h-8.5a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1z M10.5 2.5v4h4 M6.5 9.5h5 M6.5 12.5h5" fill="none" stroke-width="{s}" stroke-linejoin="round" stroke-linecap="round" class="{cls}"/>'

def icon_pill(cls):
    return f'<g transform="rotate(-35 9 9)"><rect x="2" y="6" width="14" height="6" rx="3" fill="none" stroke-width="1.6" class="{cls}"/><path d="M9 6v6" stroke-width="1.6" class="{cls}"/></g>'

def icon_chart(cls):
    return f'<path d="M3 15h12 M5.5 12V8.5 M9 12V4.5 M12.5 12V7" fill="none" stroke-width="1.6" stroke-linecap="round" class="{cls}"/>'

def icon_sun(cls):
    return f'<circle cx="9" cy="9" r="3.2" fill="none" stroke-width="1.6" class="{cls}"/><path d="M9 2.5v2M9 13.5v2M2.5 9h2M13.5 9h2M4.4 4.4l1.4 1.4M12.2 12.2l1.4 1.4M4.4 13.6l1.4-1.4M12.2 5.8l1.4-1.4" stroke-width="1.6" stroke-linecap="round" class="{cls}"/>'

def icon_moon(cls):
    return f'<path d="M14.5 10.8A6 6 0 0 1 7.2 3.5a6 6 0 1 0 7.3 7.3z" fill="none" stroke-width="1.6" stroke-linejoin="round" class="{cls}"/>'

def icon_plus(cls):
    return f'<path d="M9 4.5v9M4.5 9h9" stroke-width="1.8" stroke-linecap="round" class="{cls}"/>'


def nav():
    seg_labels = [("Work", 433.3), ("Stack", 500), ("Contact", 566.7)]
    base = "".join(f'<text x="{cx}" y="56.6" font-size="13" font-weight="500" text-anchor="middle" class="sans secondary">{t}</text>' for t, cx in seg_labels)
    sel = "".join(f'<text x="{cx}" y="56.6" font-size="13" font-weight="600" text-anchor="middle" class="sans label sel{i+1}">{t}</text>' for i, (t, cx) in enumerate(seg_labels))
    founder, _ = tag(84 + name_w + 10, 42, "Founder", "neutral")
    return f"""
  <g class="rise" style="animation-delay:.1s">
    {glass_capsule(30, 24, 940, 56)}
    <!-- mark: a backbone with three products -->
    <rect x="46" y="38" width="28" height="28" rx="8" class="accent-fill"/>
    <path d="M53 46h10M53 52h14M53 58h8" stroke-width="2.6" stroke-linecap="round" class="on-accent" style="stroke:var(--on-accent)"/>
    <text x="84" y="57.2" font-size="15" font-weight="600" class="sans label">Harsh Gorjiwala</text>
    {founder}
    <!-- neutral segmented control -->
    <rect x="400" y="34" width="200" height="36" rx="18" class="track"/>
    <rect x="403.3" y="38" width="60" height="28" rx="14" class="pill segpill" filter="url(#pillShadow)"/>
    {base}{sel}
    <!-- appearance button (sun in light, moon in dark) -->
    <circle cx="828" cy="52" r="18" class="surface border" stroke-width="1"/>
    <g transform="translate(819,43)"><g class="only-light">{icon_sun("ink")}</g><g class="only-dark">{icon_moon("ink")}</g></g>
    <!-- the one accent action in the nav -->
    <clipPath id="ctaClip"><rect x="{cta_x:.1f}" y="34" width="{cta_w:.1f}" height="36" rx="18"/></clipPath>
    <rect x="{cta_x:.1f}" y="34" width="{cta_w:.1f}" height="36" rx="18" class="accent-fill"/>
    <g clip-path="url(#ctaClip)"><rect class="sheen" x="{cta_x:.1f}" y="30" width="28" height="44" fill="#fff" opacity=".22"/></g>
    <text x="{cta_x + cta_w / 2:.1f}" y="57" font-size="14" font-weight="600" text-anchor="middle" class="sans on-accent">Say hello</text>
  </g>"""


def status_chip():
    txt = "Building in Hamilton, Ontario"
    w = measure(txt, 13, 500) + 38
    return f"""
  <g class="rise" style="animation-delay:.3s">
    <rect x="{X0}" y="108" width="{w:.1f}" height="30" rx="15" class="surface border" stroke-width="1"/>
    <circle cx="{X0 + 15}" cy="123" r="4" class="success-fill pulse"/>
    <circle cx="{X0 + 15}" cy="123" r="4" class="success-fill"/>
    <text x="{X0 + 27}" y="127.6" font-size="13" font-weight="500" class="sans" fill="url(#shimmer)">{txt}</text>
  </g>"""


def headline():
    sw_x1 = x_rest + 6
    sw_x2 = x_rest + w_rest - 4
    mid = (sw_x1 + sw_x2) / 2
    seal_cx = X0 + line1_w + 36
    return f"""
  <clipPath id="l1"><rect x="{X0 - 10}" y="150" width="600" height="80"/></clipPath>
  <clipPath id="l2"><rect x="{X0 - 10}" y="212" width="600" height="80"/></clipPath>
  <g clip-path="url(#l1)">
    <text x="{X0}" y="212" font-size="{HS}" font-weight="600" letter-spacing="{TR}em" class="sans label mask-line" style="animation-delay:.45s">{line1}</text>
  </g>
  {''.join(letters)}
  <g clip-path="url(#l2)">
    <text x="{x_rest:.1f}" y="274" font-size="{HS}" font-weight="600" letter-spacing="{TR}em" class="sans label mask-line" style="animation-delay:.7s">{rest.strip()}</text>
  </g>
  <!-- hand-drawn underline swoosh -->
  <path class="swoosh accent-stroke" pathLength="1" d="M{sw_x1:.0f} 290 C {mid - 60:.0f} 300, {mid + 90:.0f} 298, {sw_x2:.0f} 283 C {sw_x2 - 40:.0f} 286, {mid:.0f} 292, {mid - 50:.0f} 291" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" opacity=".95"/>
  <!-- ink seal -->
  <g transform="translate({seal_cx:.0f},186)"><g class="seal">
    <circle r="36" fill="none" stroke-width="2.4" class="ink"/>
    <circle r="27" fill="none" stroke-width="1" stroke-dasharray="2.5 2.5" class="ink"/>
    <g class="seal-ring">
      <defs><path id="sealPath" d="M-31.5 0a31.5 31.5 0 1 1 63 0a31.5 31.5 0 1 1 -63 0"/></defs>
      <text font-size="7.4" font-weight="600" letter-spacing=".16em" class="sans ink-fill"><textPath href="#sealPath" startOffset="0">HAMILTON · ONTARIO · CANADA · FOUNDER ·</textPath></text>
    </g>
    <text y="7" font-size="20" font-weight="600" text-anchor="middle" letter-spacing="-.02em" class="sans ink-fill">HG</text>
  </g></g>"""


def subhead():
    lines = [
        "Founder in Hamilton, Ontario. I build vertical SaaS —",
        "Klinova, SignProof, PartTrace and PolicyPulse — on one",
        "shared backbone for auth, signing, storage and payments.",
    ]
    return "".join(
        f'<text x="{X0}" y="{316 + i * 24}" font-size="17" class="sans secondary rise" style="animation-delay:{1.25 + i * 0.08:.2f}s">{t}</text>'
        for i, t in enumerate(lines)
    )


def ctas():
    return f"""
  <g class="rise" style="animation-delay:1.55s">
    <rect x="{X0}" y="394" width="{p_w:.1f}" height="44" rx="22" class="accent-fill"/>
    <text x="{X0 + p_w / 2:.1f}" y="421.4" font-size="15" font-weight="600" text-anchor="middle" class="sans on-accent">{p_text}</text>
  </g>
  <g class="rise" style="animation-delay:1.65s">
    <rect x="{s_x:.1f}" y="394" width="{s_w:.1f}" height="44" rx="22" class="surface border" stroke-width="1"/>
    <text x="{s_x + s_w / 2:.1f}" y="421.4" font-size="15" font-weight="600" text-anchor="middle" class="sans label">{s_text}</text>
  </g>"""


def mock():
    rows = [
        ("Rx renewal", "Fax · 09:12 · 2 pages", "filed"),
        ("Lab requisition", "Fax · 09:15 · 1 page", "flip"),
        ("Referral letter", "Fax · 09:21 · 3 pages", "review"),
    ]
    out = []
    for i, (title, meta, state) in enumerate(rows):
        y = 112 + i * 52
        tags = ""
        if state == "filed":
            t, w = tag(0, y + 16, "Filed", "success", icon="check")
            tags = f'<g transform="translate({346 - w:.1f},0)">{t}</g>'
        elif state == "review":
            t, w = tag(0, y + 16, "Needs review", "warning", icon="alert")
            tags = f'<g transform="translate({346 - w:.1f},0)">{t}</g>'
        else:
            t1, w1 = tag(0, y + 16, "Processing", "neutral", icon="spinner")
            t2, w2 = tag(0, y + 16, "Filed", "success", icon="check")
            tags = f'<g class="proc" transform="translate({346 - w1:.1f},0)">{t1}</g><g class="filed" transform="translate({346 - w2:.1f},0)">{t2}</g>'
        sep = f'<path d="M124 {y} H346" class="sep" stroke-width="1"/>' if i else ""
        out.append(f"""
      <g class="row" style="animation-delay:{.9 + i * .1:.1f}s">
        {sep}
        <rect x="84" y="{y + 12}" width="28" height="28" rx="7" class="tag-neutral"/>
        <g transform="translate(89,{y + 17})">{icon_doc("ink2", 1.5)}</g>
        <text x="122" y="{y + 23}" font-size="12.5" font-weight="500" class="sans label">{title}</text>
        <text x="122" y="{y + 38}" font-size="10.5" class="sans secondary">{meta}</text>
        {tags}
      </g>""")
    rows_svg = "".join(out)
    rail_icons = [icon_inbox("ink"), icon_doc("ink2"), icon_pill("ink2"), icon_chart("ink2")]
    rail = "".join(f'<g transform="translate(27,{35 + i * 40})">{ic}</g>' for i, ic in enumerate(rail_icons))
    seg = "".join(f'<text x="{cx}" y="91.3" font-size="11.5" font-weight="{"600" if i == 0 else "500"}" text-anchor="middle" class="sans {"label" if i == 0 else "secondary"}">{t}</text>' for i, (t, cx) in enumerate([("All", 100), ("Faxes", 156), ("Rx", 212)]))
    new_w = 66
    return f"""
  <g class="mock-in">
    <g transform="translate(600,104)">
      <rect width="370" height="336" rx="24" fill="var(--mock-ground)" class="border" stroke-width="1" filter="url(#mockShadow)"/>
      <!-- floating glass icon rail -->
      {glass_capsule(12, 12, 48, 312)}
      <circle cx="36" cy="44" r="17" class="pill-neutral"/>
      {rail}
      <circle cx="36" cy="296" r="13" fill="var(--accent-soft)"/>
      <text x="36" y="299.5" font-size="9" font-weight="600" text-anchor="middle" class="sans accent-text">HG</text>
      <!-- page header: large title + the one accent action -->
      <text x="72" y="44" font-size="22" font-weight="600" letter-spacing="-.02em" class="sans label">Inbox</text>
      <text x="72" y="60" font-size="11" class="sans secondary">3 new · 1 needs review</text>
      <rect x="{358 - new_w}" y="26" width="{new_w}" height="32" rx="16" class="accent-fill"/>
      <g transform="translate({358 - new_w + 8},33)">{icon_plus("on-accent")}</g>
      <text x="{358 - new_w + 29}" y="46" font-size="12" font-weight="600" class="sans on-accent">New</text>
      <!-- neutral segmented control -->
      <rect x="72" y="72" width="168" height="30" rx="15" class="track"/>
      <rect x="75" y="75" width="50" height="24" rx="12" class="pill" filter="url(#pillShadow)"/>
      {seg}
      <!-- opaque content card: inset grouped list -->
      <rect x="72" y="112" width="286" height="156" rx="14" class="surface border" stroke-width="1" filter="url(#cardShadow)"/>
      {rows_svg}
      <!-- glass toast (floating layer) -->
      <g class="toast">
        {glass_capsule(96, 284, 208, 36)}
        <g transform="translate(110,296)">{kit.ICONS["check"]("success")}</g>
        <text x="130" y="306.5" font-size="12" font-weight="500" class="sans label">Filed to chart</text>
        <text x="290" y="306.5" font-size="12" font-weight="600" text-anchor="end" class="sans accent-text">Undo</text>
      </g>
    </g>
  </g>
  <!-- parallax glass chips from the other products -->
  <g class="pop" style="animation-delay:1.3s"><g class="par1">
    {glass_capsule(846, 86, 128, 34)}
    <g transform="translate(860,97)">{kit.ICONS["check"]("success")}</g>
    <text x="878" y="107.5" font-size="12" font-weight="500" class="sans label">Sealed · SignProof</text>
  </g></g>
  <g class="pop" style="animation-delay:1.45s"><g class="par2">
    {glass_capsule(556, 404, 150, 34)}
    <circle cx="573" cy="421" r="4" class="accent-fill"/>
    <circle cx="573" cy="421" r="4" class="accent-fill pulse"/>
    <text x="586" y="425.5" font-size="12" font-weight="500" class="sans label">PT-0418 · Bay 3 · live</text>
  </g></g>"""


def build():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Harsh Gorjiwala — founder building vertical SaaS products in Hamilton, Ontario</title>
<desc id="d">Light hero with soft colour orbs, a floating glass navigation capsule, the headline “One backbone. Many products.”, and a mock of a pharmacy inbox console with a glass icon rail, neutral segmented control, opaque list and a toast.</desc>
<style>
/*FONTS*/
{CSS}
.on-accent{{stroke:var(--on-accent)}}
</style>
<defs>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="28"/></clipPath>
  <linearGradient id="shimmer" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" class="st-sec"/><stop offset=".5" class="st-lab"/><stop offset="1" class="st-sec"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="-1 0" to="1 0" dur="3.2s" repeatCount="indefinite"/>
  </linearGradient>
  {kit.defs_common()}
</defs>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" class="bg"/>
  {kit.orbs(190, 110, 230, 820, 430, 250, 600, 40, 190)}
</g>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" class="border" stroke-width="1" opacity=".6"/>
{nav()}
{status_chip()}
{headline()}
{subhead()}
{ctas()}
{mock()}
</svg>
"""
    return svg


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "../assets/hero.svg"
    n = kit.finish(build(), out)
    print(f"hero.svg {n/1024:.1f} KB")
