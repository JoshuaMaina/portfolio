// Keeps the timeline's current year in sync for assistive tech, and provides
// the scrollspy for browsers without `scroll-target-group` (per Chrome's
// Modern Web Guidance scrollspy guide).
const links = [...document.querySelectorAll('.timeline a')];

const mark = (current) => {
  for (const link of links) {
    const on = link === current;
    link.classList.toggle('target-current', on && !CSS.supports('scroll-target-group: auto'));
    if (on) link.setAttribute('aria-current', 'true');
    else link.removeAttribute('aria-current');
  }
};

if (CSS.supports('scroll-target-group: auto')) {
  const sync = () => mark(document.querySelector('.timeline a:target-current'));
  sync();
  // :target-current settles a frame after scrolling ends
  document.addEventListener('scrollend', () => requestAnimationFrame(() => requestAnimationFrame(sync)));
} else {
  const byId = new Map(links.map((a) => [a.hash.slice(1), a]));
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) mark(byId.get(entry.target.id));
    }
  }, { rootMargin: '-50% 0px -50% 0px', threshold: 0 });
  for (const id of byId.keys()) observer.observe(document.getElementById(id));
}
