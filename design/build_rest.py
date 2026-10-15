"""stack.svg (edge-faded capsule marquee), principles.svg (three opaque cards),
contact.svg (footer card with the one accent action)."""
import kit
from kit import measure, tag

W = 1000
MX = 40


# ============================================================ STACK
def build_stack():
    H = 236
    row1 = [("backend", ".NET 8"), ("language", "C#"), ("database", "PostgreSQL"), ("ui", "React 18"), ("language", "TypeScript"), ("architecture", "Multi-tenant"), ("architecture", "Shared services")]
    row2 = [("implementer", "Claude Code"), ("ide", "JetBrains Rider"), ("planning", "Linear"), ("exploring", "Three.js"), ("ritual", "HANDOFF.md"), ("machine", "macOS")]

    def chips(items, y, cls):
        seq, x = "", 0
        for cat, name in items:
            cw = measure(cat, 11, 500)
            nw = measure(name, 15, 500)
            w = 16 + cw + 8 + nw + 18
            seq += (
                f'<rect x="{x}" y="{y}" width="{w:.1f}" height="42" rx="21" class="surface border" stroke-width="1" filter="url(#cardShadow)"/>'
                f'<text x="{x + 16:.1f}" y="{y + 25.5}" font-size="11" font-weight="500" class="sans tertiary">{cat}</text>'
                f'<text x="{x + 16 + cw + 8:.1f}" y="{y + 26.3}" font-size="15" font-weight="500" class="sans label">{name}</text>'
            )
            x += w + 12
        total = x
        return f'<g class="{cls}" style="--w:{total:.1f}px">{seq}<g transform="translate({total:.1f},0)">{seq}</g></g>', total

    g1, t1 = chips(row1, 98, "marq-l")
    g2, t2 = chips(row2, 154, "marq-r")
    css = kit.TOKENS_CSS + kit.BASE_CSS + f"""
.rise{{opacity:0;animation:rise .7s cubic-bezier(.22,1,.36,1) both}}
@keyframes rise{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
.marq-l{{animation:ml {t1 / 42:.1f}s linear infinite}}
@keyframes ml{{from{{transform:translateX(0)}}to{{transform:translateX({-t1:.1f}px)}}}}
.marq-r{{animation:mr {t2 / 42:.1f}s linear infinite}}
@keyframes mr{{from{{transform:translateX({-t2:.1f}px)}}to{{transform:translateX(0)}}}}
.st-on{{stop-color:#fff;stop-opacity:1}} .st-off{{stop-color:#fff;stop-opacity:0}}
"""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Stack — .NET 8, C#, PostgreSQL, React 18, TypeScript, multi-tenant shared services; tooling: Claude Code, JetBrains Rider, Linear, Three.js (exploring), HANDOFF.md, macOS</title>
<desc id="d">Two rows of capsule chips scrolling in opposite directions with faded edges.</desc>
<style>
/*FONTS*/
{css}
</style>
<defs>
  {kit.defs_common()}
  <linearGradient id="fadeGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0" class="st-off"/><stop offset=".07" class="st-on"/><stop offset=".93" class="st-on"/><stop offset="1" class="st-off"/></linearGradient>
  <mask id="fade"><rect x="{MX}" y="80" width="{W - 2 * MX}" height="130" fill="url(#fadeGrad)"/></mask>
</defs>
<rect width="{W}" height="{H}" rx="28" class="ground"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" class="border" stroke-width="1" opacity=".6"/>
<text x="{MX}" y="46" font-size="13" font-weight="500" class="sans secondary rise" style="animation-delay:.05s">Stack</text>
<text x="{MX}" y="80" font-size="30" font-weight="600" letter-spacing="-.02em" class="sans label rise" style="animation-delay:.1s">What I build with.</text>
<g mask="url(#fade)" class="rise" style="animation-delay:.2s">
  <g transform="translate({MX},0)">{g1}</g>
  <g transform="translate({MX},0)">{g2}</g>
</g>
</svg>
"""
    return svg


# ============================================================ PRINCIPLES
def build_principles():
    H = 280
    gap = 16
    cw = (W - 2 * MX - 2 * gap) / 3
    cards = [
        ("Product first", ["I own the product and the architecture", "and direct the build: spec, build, ship,", "measure."], "target"),
        ("Divide and conquer", ["Auth, signing, storage and payments are", "built once as shared services. Each", "product carries only what sets it apart."], "layers"),
        ("AI-native workflow", ["Claude Code is the primary implementer.", "Every major session ends with a", "HANDOFF.md so the next one starts warm."], "terminal"),
    ]
    icons = {
        "target": '<circle cx="11" cy="11" r="8.5" fill="none" stroke-width="1.8" class="accent-stroke ring1"/><circle cx="11" cy="11" r="4.5" fill="none" stroke-width="1.8" class="accent-stroke ring2"/><circle cx="11" cy="11" r="1.6" class="accent-fill"/>',
        "layers": '<path d="M11 3.5l8 4.2-8 4.2-8-4.2z" fill="none" stroke-width="1.8" stroke-linejoin="round" class="accent-stroke"/><path d="M3 11.5l8 4.2 8-4.2" fill="none" stroke-width="1.8" stroke-linejoin="round" class="accent-stroke lay2"/><path d="M3 15.3l8 4.2 8-4.2" fill="none" stroke-width="1.8" stroke-linejoin="round" class="accent-stroke lay3"/>',
        "terminal": '<rect x="2.5" y="4" width="17" height="14" rx="3.5" fill="none" stroke-width="1.8" class="accent-stroke"/><path d="M6.5 9l3 2.5-3 2.5" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="accent-stroke"/><path d="M11.5 14h4" stroke-width="1.8" stroke-linecap="round" class="accent-stroke caret"/>',
    }
    body = ""
    for i, (title, lines, ic) in enumerate(cards):
        x = MX + i * (cw + gap)
        y = 104
        txt = "".join(f'<text x="{x + 20}" y="{y + 100 + j * 19}" font-size="13.5" class="sans secondary">{t}</text>' for j, t in enumerate(lines))
        body += f"""
  <g class="card-in" style="animation-delay:{.2 + i * .12:.2f}s">
    <rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="152" rx="24" class="surface border" stroke-width="1" filter="url(#cardShadow)"/>
    <rect x="{x + 20:.1f}" y="{y + 20}" width="40" height="40" rx="12" fill="var(--accent-soft)"/>
    <g transform="translate({x + 29:.1f},{y + 29})">{icons[ic]}</g>
    <text x="{x + 20:.1f}" y="{y + 80}" font-size="17" font-weight="600" letter-spacing="-.01em" class="sans label">{title}</text>
    {txt}
  </g>"""
    css = kit.TOKENS_CSS + kit.BASE_CSS + """
.rise{opacity:0;animation:rise .7s cubic-bezier(.22,1,.36,1) both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.card-in{opacity:0;animation:cardin .8s cubic-bezier(.22,1,.36,1) both}
@keyframes cardin{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
.ring1{transform-box:fill-box;transform-origin:50% 50%;animation:ring1 3s ease-in-out infinite}
@keyframes ring1{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.12);opacity:.6}}
.ring2{transform-box:fill-box;transform-origin:50% 50%;animation:ring1 3s ease-in-out .3s infinite}
.lay2{animation:lay 4s ease-in-out infinite} .lay3{animation:lay 4s ease-in-out .25s infinite}
@keyframes lay{0%,100%{transform:translateY(0);opacity:1}50%{transform:translateY(1.5px);opacity:.55}}
.caret{animation:blink 1.1s step-end infinite}
@keyframes blink{50%{opacity:0}}
"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">How I work — product first; divide and conquer with shared services; AI-native workflow with Claude Code and HANDOFF.md</title>
<desc id="d">Three cards describing how Harsh works.</desc>
<style>
/*FONTS*/
{css}
</style>
<defs>{kit.defs_common()}</defs>
<rect width="{W}" height="{H}" rx="28" class="ground"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" class="border" stroke-width="1" opacity=".6"/>
<text x="{MX}" y="46" font-size="13" font-weight="500" class="sans secondary rise" style="animation-delay:.05s">How I work</text>
<text x="{MX}" y="80" font-size="30" font-weight="600" letter-spacing="-.02em" class="sans label rise" style="animation-delay:.1s">Own the product. Share the backbone. Ship with AI.</text>
{body}
</svg>
"""


# ============================================================ CONTACT
def build_contact():
    H = 150
    email = "harsh7529gorjiwala@gmail.com"
    p_text, s_text = "Email me", "GitHub"
    p_w = measure(p_text, 15, 600) + 44
    s_w = measure(s_text, 15, 600) + 44
    s_x = W - MX - s_w
    p_x = s_x - 12 - p_w
    loc_w = measure("Hamilton, Ontario", 13, 500) + 44
    css = kit.TOKENS_CSS + kit.BASE_CSS + """
.rise{opacity:0;animation:rise .7s cubic-bezier(.22,1,.36,1) both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.sheen{animation:sheen 6s ease-in-out 2s infinite}
@keyframes sheen{0%{transform:translateX(-70px) skewX(-20deg)}35%,100%{transform:translateX(170px) skewX(-20deg)}}
.pulse{transform-box:fill-box;transform-origin:50% 50%;animation:pulse 2.2s ease-out infinite}
@keyframes pulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(3);opacity:0}}
"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Say hello — {email} · Hamilton, Ontario · github.com/harshgorjiwala</title>
<desc id="d">Footer card with an email button and a GitHub button.</desc>
<style>
/*FONTS*/
{css}
</style>
<defs>{kit.defs_common()}
  <clipPath id="pclip"><rect x="{p_x:.1f}" y="53" width="{p_w:.1f}" height="44" rx="22"/></clipPath>
</defs>
<rect width="{W}" height="{H}" rx="28" class="ground"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" class="border" stroke-width="1" opacity=".6"/>
<g class="rise" style="animation-delay:.05s">
  <text x="{MX}" y="68" font-size="28" font-weight="600" letter-spacing="-.02em" class="sans label">Say hello.</text>
  <text x="{MX}" y="96" font-size="15" class="sans secondary">{email}</text>
</g>
<g class="rise" style="animation-delay:.15s">
  <rect x="{W - MX - s_w - 12 - p_w - 12 - loc_w:.1f}" y="57" width="{loc_w:.1f}" height="36" rx="18" class="surface border" stroke-width="1"/>
  <g transform="translate({W - MX - s_w - 12 - p_w - 12 - loc_w + 14:.1f},66)">
    <path d="M9 2.5a5.5 5.5 0 0 1 5.5 5.5c0 4-5.5 9-5.5 9S3.5 12 3.5 8A5.5 5.5 0 0 1 9 2.5z" fill="none" stroke-width="1.6" class="ink2"/><circle cx="9" cy="8" r="1.8" class="ink-fill"/>
  </g>
  <text x="{W - MX - s_w - 12 - p_w - 12 - loc_w + 36:.1f}" y="79.5" font-size="13" font-weight="500" class="sans label">Hamilton, Ontario</text>
</g>
<g class="rise" style="animation-delay:.25s">
  <rect x="{p_x:.1f}" y="53" width="{p_w:.1f}" height="44" rx="22" class="accent-fill"/>
  <g clip-path="url(#pclip)"><rect class="sheen" x="{p_x:.1f}" y="49" width="30" height="52" fill="#fff" opacity=".22"/></g>
  <text x="{p_x + p_w / 2:.1f}" y="80.4" font-size="15" font-weight="600" text-anchor="middle" class="sans on-accent">{p_text}</text>
</g>
<g class="rise" style="animation-delay:.35s">
  <rect x="{s_x:.1f}" y="53" width="{s_w:.1f}" height="44" rx="22" class="surface border" stroke-width="1"/>
  <text x="{s_x + s_w / 2:.1f}" y="80.4" font-size="15" font-weight="600" text-anchor="middle" class="sans label">{s_text}</text>
</g>
<text x="{MX}" y="128" font-size="11.5" class="sans tertiary rise" style="animation-delay:.4s">Every graphic on this page is a hand-written SVG with CSS keyframes — no JavaScript, no external requests. Type is Geist (OFL), subset and embedded.</text>
</svg>
"""


if __name__ == "__main__":
    import sys
    base = sys.argv[1] if len(sys.argv) > 1 else "../assets"
    for name, fn in [("stack", build_stack), ("principles", build_principles), ("contact", build_contact)]:
        n = kit.finish(fn(), f"{base}/{name}.svg")
        print(f"{name}.svg {n/1024:.1f} KB")
