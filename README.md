# portfolio

Personal site for Joshua Mwangi Maina, pressed as a record. It's a single static page with no JavaScript,
deployed on Vercel from `main`.

## The idea

My career is laid out as an album. Side A is pricing and trading infrastructure, and Side B is AI and agents.
Each project is a track. The opening statement makes claims, and the small numbers beside them are track
numbers. Press one, or any track title, and the tonearm drops, the record spins at 33⅓ rpm and the track
lights up. "Lift the needle" stops it.

It's all CSS. Choosing a track sets the URL fragment (`#track-3`), and `body:has(.track:target)` drives the
turntable.

## Editing

1. Edit `build/tracks.py` for tracks, `build/styles.css` for styles, or `build/build.py` for the page copy.
2. Run `python3 build/build.py` to regenerate `index.html`.
3. Commit and push. Vercel deploys `main` automatically.

## Structure

- `index.html`: the generated page, with CSS inlined.
- `build/`: the sources and the generator, which aren't deployed.
- `fonts/`: self-hosted Newsreader and Schibsted Grotesk, under the SIL Open Font License.
- `favicon.svg`: adapts to light and dark mode.
- `vercel.json`: security headers, with no scripts allowed, and long-lived caching for fonts.

## Built with Chrome's Modern Web Guidance

- **Motion is opt-in.** The record only spins after a visitor picks a track, and there's a visible control to
  stop it. The slide-out entrance and the spin only run under `prefers-reduced-motion: no-preference`. With
  reduced motion, the tonearm still moves but nothing spins.
- Animations use only `rotate` and `translate`, as individual transform properties, so they stay on the
  compositor.
- `light-dark()` colour tokens with `color-scheme`, plus Forced Colors fallbacks.
- rem-based fluid type with `clamp()`, `<meta name="text-scale">` and container query units on the sleeve
  and label.
- `font-size-adjust: from-font`, `text-wrap: balance` and `pretty`, logical properties and native nesting.
- Inlined critical CSS, preloaded self-hosted fonts and no third-party requests.
