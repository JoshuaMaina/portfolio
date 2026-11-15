"""Builds index.html from tracks.py, styles.css and fonts.css. Run: python3 build/build.py"""
import html, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from tracks import TRACKS

fontface = (HERE / "fonts.css").read_text()
css = (HERE / "styles.css").read_text()

# Per-track "now playing" rules
np_rules = "\n".join(
    f"body:has(#track-{i}:target) .np-{i} {{ display: inline; }}" for i in range(1, len(TRACKS) + 1)
)

def track_li(i, t):
    side, title, metric, body, stack = t
    return f"""        <li id="track-{i}" class="track">
          <span class="no" aria-hidden="true">{i:02d}</span>
          <h4><a href="#track-{i}">{html.escape(title, quote=False)}</a><span class="eq" aria-hidden="true"><i></i><i></i><i></i></span></h4>
          <span class="metric">{html.escape(metric, quote=False)}</span>
          <div class="notes">
            <p>{html.escape(body, quote=False)}</p>
            <p class="stack">{html.escape(stack, quote=False)}</p>
          </div>
        </li>"""

side_a = "\n".join(track_li(i, t) for i, t in enumerate(TRACKS, 1) if t[0] == "A")
side_b = "\n".join(track_li(i, t) for i, t in enumerate(TRACKS, 1) if t[0] == "B")
b_start = next(i for i, t in enumerate(TRACKS, 1) if t[0] == "B")
np_spans = "\n".join(
    f'        <span class="np np-{i}">Now playing <strong>track {i:02d}, {html.escape(t[1], quote=False)}</strong></span>'
    for i, t in enumerate(TRACKS, 1)
)

def cite(n):
    return f'<a class="cite" href="#track-{n}" aria-label="Play track {n}">{n}</a>'

page = f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="text-scale" content="scale">
  <title>Joshua Mwangi Maina, software engineer</title>
  <meta name="description" content="Joshua Mwangi Maina is a software engineer and Vice President at Goldman Sachs in London, building pricing infrastructure and LLM systems that have to be right.">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#F1F3F2" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#121920" media="(prefers-color-scheme: dark)">
  <meta property="og:title" content="Joshua Mwangi Maina, software engineer">
  <meta property="og:description" content="Systems that have to be right, pressed to vinyl.">
  <meta property="og:type" content="profile">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/fonts/schibsted-grotesk-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
  <style>
{fontface}{css}
/* Now playing captions, one per track */
{np_rules}
  </style>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="site-header">
    <a class="name" href="/">Joshua Mwangi Maina</a>
    <nav aria-label="Primary">
      <ul>
        <li><a href="#tracklist">Tracklist</a></li>
        <li><a href="#credits">Credits</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <div class="layout">
    <div class="deck-col">
      <div class="deck" aria-hidden="true">
        <div class="sleeve">
          <span class="sleeve-title">Systems that have to be right</span>
          <span class="sleeve-sub">Joshua Mwangi Maina<br>Side A pricing, side B AI</span>
        </div>
        <div class="record-slot">
          <div class="record">
            <div class="label">
              <span class="label-top">JMM</span>
              <span class="label-bottom">33⅓</span>
            </div>
          </div>
        </div>
        <svg class="tonearm" viewBox="0 0 100 220" fill="none">
          <circle cx="72" cy="20" r="14"/>
          <path d="M72 20 L60 150 L40 186" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
          <rect x="26" y="180" width="22" height="30" rx="4" transform="rotate(30 37 195)"/>
        </svg>
      </div>
      <p class="now-playing">
        <span class="np-idle">Pick a track to drop the needle.</span>
{np_spans}
        <a class="stop" href="#tracklist">Lift the needle</a>
      </p>
    </div>

    <main id="main">
      <section class="statement" aria-labelledby="statement-title">
        <h1 id="statement-title">Joshua Mwangi Maina builds systems where a wrong number costs money.</h1>
        <p class="lede">
          At Goldman Sachs that has meant pricing infrastructure. I built a clustered cache that made
          cross-asset pricing more than ten times faster{cite(1)},
          a load balancer that lets us deploy to pricing systems mid-session with zero downtime{cite(2)},
          and a new way to ship a core library that cut service start-up time by 90%{cite(3)}.
          Lately it means LLM agents: a platform where every user gets an isolated agent runtime{cite(b_start)},
          and a trading chat that can’t make up a figure{cite(b_start + 1)}.
        </p>
        <p class="sub">
          Vice President and software engineer in London, working in Java and Python. I trained as an
          actuary, so I still think in failure modes and evidence. The small numbers are track numbers:
          press one to play the work behind the claim.
        </p>
        <a class="play-cta" href="#track-1">Play side A</a>
      </section>

      <section id="tracklist" aria-labelledby="tracklist-title">
        <h2 id="tracklist-title">Tracklist</h2>

        <h3 class="side">Side A: pricing and trading infrastructure</h3>
        <ol>
{side_a}
        </ol>

        <h3 class="side">Side B: AI and agents</h3>
        <ol>
{side_b}
        </ol>
        <p class="hint">Press a track title to put it on the turntable.</p>
      </section>

      <section id="credits" aria-labelledby="credits-title">
        <h2 id="credits-title">Credits</h2>
        <ol class="steps">
          <li>
            <h3><time datetime="2015">2015</time>, Starehe Boys’ Centre</h3>
            <p>Kenya Certificate of Secondary Education, grade A.</p>
          </li>
          <li>
            <h3><time datetime="2016-06">2016</time>, front-end intern, Archangel Interactive</h3>
            <p>My first job building websites, and where programming started for me.</p>
          </li>
          <li>
            <h3><time datetime="2016">2016</time> to <time datetime="2020">2020</time>, BSc Actuarial Science, University of Nairobi</h3>
            <p>First-class honours, and best student in second and final year. Passed the Institute and Faculty of Actuaries papers CM1, CS1 and CB1. Vice-chair of the Nairobi Actuarial Students’ Association.</p>
          </li>
          <li>
            <h3><time datetime="2019-05">2019</time>, actuarial intern, Liberty Life Kenya</h3>
            <p>Audited actuarial models and wrote their audit trails. Built a Group Life quotation tool with another intern, first in Excel and R Shiny, then automated it with macros. Ran investigations into annuity payments and unit fund values, and helped value unit-linked products.</p>
          </li>
          <li>
            <h3><time datetime="2019-08">2019</time>, data analyst, IBM student start-up programme</h3>
            <p>Part of a small university start-up team, analysing data in R and Watson Studio.</p>
          </li>
          <li>
            <h3><time datetime="2020-07">2020</time>, summer analyst, Goldman Sachs</h3>
            <p>Built a back-testing tool that compared new pricing models with the old ones across historical data.</p>
          </li>
          <li>
            <h3><time datetime="2021-06">2021</time>, analyst</h3>
            <p>gRPC tooling, pricing-flow monitoring and the zero-downtime load balancer.</p>
          </li>
          <li>
            <h3><time datetime="2024-01">2024</time>, associate</h3>
            <p>The pricing cache, the start-up work, the tracing migration, worker pools and the shared platform.</p>
          </li>
          <li>
            <h3><time datetime="2026-01">2026</time>, vice president</h3>
            <p>Agent platforms, grounded AI for traders and Bloomberg chat bots.</p>
          </li>
        </ol>
        <p class="aside">
          Finalist, Black Developer of the Year, Black Tech Awards. I also mentor students moving into
          finance and technology.
        </p>
      </section>

      <section id="contact" class="contact" aria-labelledby="contact-title">
        <h2 id="contact-title">Contact</h2>
        <p>For roles, collaborations or a chat about any track, message me on LinkedIn.</p>
        <ul class="links">
          <li><a href="https://www.linkedin.com/in/joshua-mwangi-32ab9879/" rel="me">LinkedIn</a></li>
          <li><a href="https://github.com/JoshuaMaina" rel="me">GitHub</a></li>
        </ul>
      </section>
    </main>
  </div>

  <footer class="site-footer">
    <p>Joshua Mwangi Maina, London. Pressed in plain HTML and CSS.</p>
  </footer>
</body>
</html>
"""
(HERE.parent / "index.html").write_text(page)
print("ok", len(page))
