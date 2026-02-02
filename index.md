---
layout: default
title: Home
---

<section class="hero">
  <p class="hero-tagline">From <em>lipids</em> to <em>life</em></p>
  <h1>Laboratory of Synthetic Membrane Biology</h1>
</section>

<section class="intro-row">
  <div class="intro-text">
    <h2>Research outlook</h2>
    <div class="intro-media">
      <video autoplay loop muted playsinline class="membrane-video">
        <source src="{{ '/assets/img/membrane.mp4' | relative_url }}" type="video/mp4">
        <source src="{{ '/assets/img/membrane.mov' | relative_url }}" type="video/quicktime">
      </video>
      <span class="media-caption">Animation by Julia Eichhorn, MPI-CBG Graphics</span>
    </div>
    <p>
      Our laboratory studies the design principles of living membranes. We combine
      lipid biochemistry, membrane biophysics, and synthetic genomics to understand
      how lipid composition gives rise to membrane physical properties that shape
      cellular function — from synthetic protocells to minimal organisms. A central
      aim is to identify the minimal set of components required to build a robust
      and responsive synthetic cell membrane.
    </p>
  </div>
  <div class="intro-feed">
    <h2>Posts from Bluesky</h2>
    <bsky-embed
      username="jamessaenz.bsky.social"
      limit="3"
      mode="light">
    </bsky-embed>
    <script type="module" src="https://cdn.jsdelivr.net/npm/bsky-embed/dist/bsky-embed.es.js" async></script>
  </div>
</section>

<section class="carousel-section">
  <div class="carousel" id="labCarousel">
    <div class="carousel-slide active">
      <div class="carousel-placeholder">Lab photo 1 — add images to assets/img/</div>
    </div>
    <div class="carousel-slide">
      <div class="carousel-placeholder">Lab photo 2</div>
    </div>
    <div class="carousel-slide">
      <div class="carousel-placeholder">Lab photo 3</div>
    </div>
    <div class="carousel-slide">
      <div class="carousel-placeholder">Lab photo 4</div>
    </div>
  </div>
  <div class="carousel-dots" id="carouselDots"></div>
</section>

<script>
(function() {
  var carousel = document.getElementById('labCarousel');
  if (!carousel) return;
  var slides = carousel.querySelectorAll('.carousel-slide');
  var dotsContainer = document.getElementById('carouselDots');
  var current = 0;
  for (var i = 0; i < slides.length; i++) {
    var dot = document.createElement('button');
    dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', 'Slide ' + (i + 1));
    (function(idx) {
      dot.addEventListener('click', function() { goTo(idx); });
    })(i);
    dotsContainer.appendChild(dot);
  }
  function goTo(idx) {
    slides[current].classList.remove('active');
    dotsContainer.children[current].classList.remove('active');
    current = idx;
    slides[current].classList.add('active');
    dotsContainer.children[current].classList.add('active');
  }
  setInterval(function() { goTo((current + 1) % slides.length); }, 5000);
})();
</script>
