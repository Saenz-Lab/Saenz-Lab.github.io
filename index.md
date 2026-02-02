---
layout: default
title: Home
---

<section class="hero">
  <div class="hero-text">
    <p class="hero-tagline">From <em>lipids</em> to <em>life</em></p>
    <h1>Laboratory of Synthetic Membrane Biology</h1>
  </div>
</section>

<section class="intro-row">
  <div class="intro-text">
    <h2>Research outlook</h2>
    <div class="intro-media">
      <!-- Replace src with your membrane animation file, e.g. assets/img/membrane.mp4 -->
      <video autoplay loop muted playsinline class="membrane-video">
        <source src="{{ '/assets/img/membrane.mp4' | relative_url }}" type="video/mp4">
        <img src="{{ '/assets/img/membrane-placeholder.svg' | relative_url }}" alt="Membrane animation" />
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
    <!-- Replace these with your actual lab photos in assets/img/ -->
    <div class="carousel-slide active">
      <div class="carousel-placeholder">Lab photo 1</div>
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

<section class="pillars-section">
  <h2 class="section-title">What we do</h2>

  <div class="grid">
    <a class="card pillar half" href="{{ '/research/' | relative_url }}#composition">
      <!-- Replace with your research area image: assets/img/pillar-ordering.png -->
      <div class="pillar-img-wrap">
        <div class="pillar-img-placeholder">Image</div>
      </div>
      <h3>Membrane phenotypes</h3>
      <p>
        How lipid composition and organization give rise to measurable physical
        properties — order, permeability, stability — that constrain cellular function.
      </p>
    </a>

    <a class="card pillar half" href="{{ '/research/' | relative_url }}#lipidomes">
      <div class="pillar-img-wrap">
        <div class="pillar-img-placeholder">Image</div>
      </div>
      <h3>Lipidomes as control spaces</h3>
      <p>
        Lipidomes as genetically encoded, adaptable design spaces whose composition
        can be tuned to modulate membrane physical state and functional robustness.
      </p>
    </a>
  </div>

  <div class="grid">
    <a class="card pillar third" href="{{ '/research/' | relative_url }}#minimal">
      <div class="pillar-img-wrap">
        <div class="pillar-img-placeholder">Image</div>
      </div>
      <h3>Minimal and synthetic cells</h3>
      <p>
        Genomically minimal cells as reduced experimental systems for
        systematically rebuilding membrane complexity and revealing design principles.
      </p>
    </a>

    <a class="card pillar third" href="{{ '/research/' | relative_url }}#regulation">
      <div class="pillar-img-wrap">
        <div class="pillar-img-placeholder">Image</div>
      </div>
      <h3>Regulation and homeostasis</h3>
      <p>
        How cells sense and regulate membrane physical state, coupling membrane
        properties to lipid synthesis and gene regulation.
      </p>
    </a>

    <a class="card pillar third" href="{{ '/research/' | relative_url }}#rna-lipid">
      <div class="pillar-img-wrap">
        <div class="pillar-img-placeholder">Image</div>
      </div>
      <h3>RNA–lipid interactions</h3>
      <p>
        How membrane composition and physical state influence RNA structure,
        catalytic activity, and stability at membrane interfaces.
      </p>
    </a>
  </div>
</section>

<script>
// Minimal carousel script
(function() {
  const carousel = document.getElementById('labCarousel');
  if (!carousel) return;
  const slides = carousel.querySelectorAll('.carousel-slide');
  const dotsContainer = document.getElementById('carouselDots');
  let current = 0;

  slides.forEach(function(_, i) {
    const dot = document.createElement('button');
    dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', 'Slide ' + (i + 1));
    dot.addEventListener('click', function() { goTo(i); });
    dotsContainer.appendChild(dot);
  });

  function goTo(idx) {
    slides[current].classList.remove('active');
    dotsContainer.children[current].classList.remove('active');
    current = idx;
    slides[current].classList.add('active');
    dotsContainer.children[current].classList.add('active');
  }

  setInterval(function() {
    goTo((current + 1) % slides.length);
  }, 5000);
})();
</script>
