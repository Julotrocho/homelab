// Carrousel simple, sans dépendance — un par bloc .carousel présent sur la page
document.querySelectorAll('[data-carousel]').forEach((root) => {
  const track = root.querySelector('.carousel-track');
  const slides = Array.from(track.children);
  const dotsWrap = root.querySelector('.carousel-dots');
  const prevBtn = root.querySelector('.prev');
  const nextBtn = root.querySelector('.next');
  let index = 0;

  slides.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.setAttribute('aria-label', `Aller à l'image ${i + 1}`);
    if (i === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goTo(i));
    dotsWrap.appendChild(dot);
  });
  const dots = Array.from(dotsWrap.children);

  function goTo(i) {
    index = (i + slides.length) % slides.length;
    track.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach((d, di) => d.classList.toggle('active', di === index));
  }

  prevBtn.addEventListener('click', () => goTo(index - 1));
  nextBtn.addEventListener('click', () => goTo(index + 1));

  root.setAttribute('tabindex', '0');
  root.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') goTo(index - 1);
    if (e.key === 'ArrowRight') goTo(index + 1);
  });
});
