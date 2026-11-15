# portfolio

Personal site for Joshua Mwangi Maina. It is a single static page, deployed on Vercel from `main`.

## The idea

My trading-chat work is about never showing a number without its source, and the page works the same way.
Each claim in the opening statement has a citation mark. The mark links to the project behind the claim,
and the project is highlighted when you land on it.

## Structure

- `index.html`: the whole page. The CSS is inlined in `<style>`, and there is no JavaScript.
- `fonts/`: self-hosted Newsreader and Schibsted Grotesk, under the SIL Open Font License.
- `favicon.svg`: adapts to light and dark mode.
- `vercel.json`: security headers and long-lived caching for fonts.

## Editing

Projects are `<li class="ref" id="ref-N">` entries. Numbering comes from a CSS counter that runs across both
groups. If you add or reorder projects, update the `href="#ref-N"` citations in the opening statement to match.

## Built with Chrome's Modern Web Guidance

- `light-dark()` colour tokens with `color-scheme`, plus Forced Colors fallbacks
- rem-based fluid type with `clamp()`, `<meta name="text-scale">` and no root font-size override
- `font-size-adjust: from-font` to keep layout stable while fonts swap
- `text-wrap: balance` on headings and `pretty` on paragraphs
- logical properties, native CSS nesting and em-based media queries
- inlined critical CSS and preloaded self-hosted fonts, with no third-party requests
- smooth scrolling and transitions only when the user hasn't asked for reduced motion

## Run locally

```sh
npx serve .
```
