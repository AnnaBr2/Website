(() => {
  const name = document.querySelector('.anna-hero-name');
  const space = document.querySelector('.anna-name-space');
  const destination = document.querySelector('.anna-brand-destination');
  const header = document.querySelector('.anna-header-home');
  if (!name || !space || !destination || !header) return;

  let docked = false;
  let geometry;
  const enterAt = 12;
  const leaveAt = 2;

  function setDocked(next) {
    if (next === docked) return;
    docked = next;
    name.classList.toggle('anna-name-docked', docked);
    header.classList.toggle('anna-header-name-docked', docked);
  }

  function followScroll() {
    // Scroll only chooses the destination. The compositor completes the whole
    // transition independently of wheel notches or pauses between scroll events.
    const scroll = Math.max(0, window.scrollY);
    setDocked(docked ? scroll > leaveAt : scroll >= enterAt);
  }

  function measure() {
    const style = getComputedStyle(name);
    const height = parseFloat(style.height) || name.offsetHeight;
    if (Math.abs((parseFloat(space.style.height) || 0) - height) > .1) {
      space.style.height = `${height}px`;
    }
    const source = space.getBoundingClientRect();
    const target = destination.getBoundingClientRect();
    const targetFontSize = window.matchMedia('(max-width: 767px)').matches ? 20 : 22;
    const scale = targetFontSize / parseFloat(style.fontSize);
    const next = [source.left, source.top + window.scrollY, target.left,
      target.top + (target.height - height * scale) / 2, scale];
    if (geometry && next.every((value, index) => Math.abs(value - geometry[index]) < .01)) return;
    geometry = next;

    // Reposition instantly only for initial layout, font loading or resizing.
    // Observer callbacks with unchanged geometry cannot interrupt the animation.
    name.classList.add('anna-name-measuring');
    const variables = ['--anna-name-start-x', '--anna-name-start-y',
      '--anna-name-end-x', '--anna-name-end-y', '--anna-name-end-scale'];
    next.forEach((value, index) => name.style.setProperty(variables[index],
      index === 4 ? String(value) : `${value}px`));
    name.classList.add('anna-name-in-motion');
    followScroll();
    name.getBoundingClientRect();
    name.classList.remove('anna-name-measuring');
  }

  window.addEventListener('scroll', followScroll, { passive: true });
  window.addEventListener('resize', measure, { passive: true });
  window.addEventListener('pageshow', measure);
  const observer = new ResizeObserver(measure);
  observer.observe(space);
  observer.observe(destination);
  observer.observe(name);
  measure();
  document.fonts.ready.then(measure);
})();
