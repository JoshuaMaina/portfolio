# portfolio

Personal site for Joshua Mwangi Maina, deployed on Vercel from `main`.

## The idea

The career reads as a book. Each project or milestone is a full-height page, newest first, from today back to
2015, and each page lands into place as you scroll to it. A timeline bar is fixed to the bottom of the
screen. It shows which year you're reading, fills up to that year, and lets you jump to any year.
The opening page makes claims with small numbers beside them, and each number links to the page behind
the claim.

## Editing

1. Edit `build/pages.py`. Years are listed oldest first, and the build shows them newest first. Within a year, pages
   show in the order written. The timeline, page numbers
   and year sections are all generated from it.
2. Run `python3 build/build.py` to regenerate `index.html`.
3. Commit and push. Vercel deploys `main` automatically.

## Structure

- `index.html`: the generated page, with CSS inlined.
- `timeline.js`: a small module that mirrors the current year into `aria-current`, plus an
  `IntersectionObserver` fallback for browsers without `scroll-target-group`.
- `build/`: the sources (`pages.py`, `styles.css`, `fonts.css`) and the generator. They aren't deployed.
- `fonts/`: self-hosted Newsreader and Schibsted Grotesk, under the SIL Open Font License.
- Vercel Web Analytics: a deferred `/_vercel/insights/script.js` tag in the page head. Plain HTML doesn't need the
  `@vercel/analytics` npm package, and the script is same-origin, so the CSP allows it.
- `vercel.json`: security headers. The CSP allows only same-origin scripts. Fonts get long-lived caching.

## Built with Chrome's Modern Web Guidance

- **Timeline scrollspy** (`scrollspy` guide): `scroll-target-group: auto` with `:target-current`. Screen
  readers get the current year through `aria-current`, and the active year is shown by size, weight and an
  underline, not colour alone. Browsers without support use the `IntersectionObserver` fallback.
- **Pages landing** (`scroll-entry-exit-effects`): a scroll-driven `view()` animation using individual
  transform properties, wrapped in `prefers-reduced-motion: no-preference` and
  `@supports ((animation-timeline: view()) and (animation-range: entry))`. It's decorative, so there's no
  fallback.
- `scroll-snap-type: y proximity`, so pages settle without trapping long content.
- `light-dark()` colour tokens with `color-scheme`, plus Forced Colors fallbacks.
- rem-based fluid type with `clamp()`, `<meta name="text-scale">` and `font-size-adjust: from-font`.
- Logical properties, native nesting, em-based media queries, and inlined critical CSS with preloaded
  self-hosted fonts.
