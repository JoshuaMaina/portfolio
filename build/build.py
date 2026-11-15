"""Builds index.html from pages.py, styles.css and fonts.css. Run: python3 build/build.py"""
import html
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from pages import YEARS as YEARS_OLDEST_FIRST

# Newest first: readers care most about recent work
YEARS = list(reversed(YEARS_OLDEST_FIRST))

FIRST, LAST = YEARS[-1]["year"], YEARS[0]["year"]  # oldest, newest
SPAN = LAST - FIRST
N = len(YEARS)


def esc(s):
    return html.escape(s, quote=False)


fontface = (HERE / "fonts.css").read_text()
css = (HERE / "styles.css").read_text()

# The fill grows to whichever year is current (one rule per year)
fill_rules = "\n".join(
    f".timeline:has(li:nth-child({i}) a:is(:target-current, .target-current)) .fill "
    f"{{ inline-size: {((LAST - y['year']) / SPAN) * 100:.2f}%; }}"
    for i, y in enumerate(YEARS, 1)
)
fill_rules += "\n@media (width < 40em) {\n" + "\n".join(
    f"  .timeline:has(li:nth-child({i}) a:is(:target-current, .target-current)) .fill "
    f"{{ inline-size: {((i - 1) / (N - 1)) * 100:.2f}%; }}"
    for i in range(1, N + 1)
) + "\n}"

# Number every page in order
total = sum(len(y["pages"]) for y in YEARS) + 1  # +1 for the intro page
folio = 1
sections = []
for y in YEARS:
    pages_html = []
    for p in y["pages"]:
        folio += 1
        stack = f'\n            <p class="stack">{esc(p["stack"])}</p>' if p["stack"] else ""
        pages_html.append(f"""      <article id="{p['id']}" class="page entry" aria-labelledby="{p['id']}-title">
        <div class="sheet">
          <span class="year" aria-hidden="true">{y['year']}</span>
          <p class="where">{esc(p['where'])}</p>
          <h3 id="{p['id']}-title">{esc(p['title'])}</h3>
          <span class="metric">{esc(p['metric'])}</span>
          <p class="body">{esc(p['body'])}</p>{stack}
          <span class="folio" aria-hidden="true">{folio} / {total}</span>
        </div>
      </article>""")
    sections.append(f"""    <section id="y{y['year']}" class="year-group" tabindex="-1" aria-labelledby="y{y['year']}-title">
      <h2 id="y{y['year']}-title" class="visually-hidden">{y['year']}</h2>
{chr(10).join(pages_html)}
    </section>""")

timeline_items = "\n".join(
    f'        <li style="--t: {(LAST - y["year"]) / SPAN:.4f}; --i: {i}; --n: {N - 1}">'
    f'<a href="#y{y["year"]}"><span class="full">{y["year"]}</span>'
    f'<span class="short" aria-hidden="true">’{str(y["year"])[2:]}</span></a></li>'
    for i, y in enumerate(YEARS)
)

page_no = {p["id"]: None for y in YEARS for p in y["pages"]}


def cite(page_id, n):
    assert page_id in page_no, page_id
    return f'<a class="cite" href="#{page_id}" aria-label="Go to {n}">{n}</a>'


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
  <meta property="og:description" content="Pricing infrastructure and LLM systems that have to be right, one page at a time.">
  <meta property="og:type" content="profile">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/fonts/schibsted-grotesk-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
  <style>
{fontface}{css}
/* Timeline fill, one rule per year */
{fill_rules}
  </style>
  <script type="module" src="/timeline.js"></script>
  <!-- Vercel Web Analytics: same-origin script, allowed by the CSP. No npm package needed for plain HTML. -->
  <script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="site-header">
    <a class="name" href="/">Joshua Mwangi Maina</a>
    <nav aria-label="Primary">
      <ul>
        <li><a href="#y{LAST}">The story</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main id="main">
    <section class="page intro" aria-labelledby="intro-title">
      <div class="sheet">
        <p class="award">Finalist, Black Developer of the Year, Black Tech Awards</p>
        <h1 id="intro-title">Josh builds systems where a wrong number costs money.</h1>
        <p class="lede">
          At Goldman Sachs that has meant pricing infrastructure. I built a clustered cache that made
          cross-asset pricing more than ten times faster{cite("cache", 1)},
          a load balancer that lets us deploy to pricing systems mid-session with zero downtime{cite("load-balancer", 2)},
          and a new way to ship a core library that cut service start-up time by 90%{cite("start-up", 3)}.
          Lately it means LLM agents: a platform where every user gets an isolated agent runtime{cite("agent-platform", 4)},
          and a trading chat that can’t make up a figure{cite("grounded-chat", 5)}.
        </p>
        <p class="sub">
          Vice President and software engineer in London, working in Java and Python. I trained as an
          actuary, so I still think in failure modes and evidence. Each small number links to the page
          behind the claim. Scroll to read it from {LAST} back to {FIRST}, or jump to a year on the timeline.
        </p>
        <span class="folio" aria-hidden="true">1 / {total}</span>
      </div>
    </section>

{chr(10).join(sections)}

    <section id="contact" class="page contact" tabindex="-1" aria-labelledby="contact-title">
      <div class="sheet">
        <h2 id="contact-title">Contact</h2>
        <p>For roles, collaborations or a chat about any page here, message me on LinkedIn. I also mentor
          students moving into finance and technology.</p>
        <ul class="links">
          <li><a href="https://www.linkedin.com/in/joshua-mwangi-32ab9879/" rel="me">LinkedIn</a></li>
          <li><a href="https://github.com/JoshuaMaina" rel="me">GitHub</a></li>
        </ul>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>Joshua Mwangi Maina, London.</p>
  </footer>

  <nav class="timeline" aria-label="Timeline">
    <div class="track">
      <span class="axis" aria-hidden="true"></span>
      <span class="fill" aria-hidden="true"></span>
      <ol>
{timeline_items}
      </ol>
    </div>
  </nav>
</body>
</html>
"""
(HERE.parent / "index.html").write_text(page)
print("ok", len(page), "pages:", total)
