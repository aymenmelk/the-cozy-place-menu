/* ═══════════════════════════════════════════
   THE COZY PLACE — Premium Café Menu Script
   ═══════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── FLOATING PARTICLES ── */
  initParticles();

  /* ── SCROLL REVEAL ── */
  initReveal();

  /* ── PARALLAX HERO ── */
  initParallax();

  /* ── CARD STAGGER ── */
  initCardStagger();

  /* ── MASCOT WAKE UP ── */
  setTimeout(() => {
    const mascot = document.querySelector('.coffee-mascot-container');
    if (mascot) {
      mascot.classList.add('waking-up');
      setTimeout(() => mascot.classList.remove('waking-up'), 2500);
    }
  }, 2000);

});

/* ══ PARTICLES ══ */
function initParticles() {
  const canvas = document.getElementById('particles-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const particles = [];
  const COLORS = ['#C9921A', '#E8B84B', '#F5D07A', '#8B2020', '#EDD9B4'];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = canvas.height + Math.random() * 100;
      this.size = Math.random() * 6 + 2;
      this.speedY = Math.random() * 0.6 + 0.2;
      this.speedX = (Math.random() - 0.5) * 0.4;
      this.color = COLORS[Math.floor(Math.random() * COLORS.length)];
      this.opacity = 0;
      this.maxOpacity = Math.random() * 0.3 + 0.05;
      this.rotation = Math.random() * Math.PI * 2;
      this.rotSpeed = (Math.random() - 0.5) * 0.02;
      this.shape = Math.random() > 0.6 ? 'circle' : 'diamond';
    }
    update() {
      this.y -= this.speedY;
      this.x += this.speedX;
      this.rotation += this.rotSpeed;
      // Fade in and out
      if (this.y > canvas.height * 0.8) {
        this.opacity = Math.min(this.maxOpacity, this.opacity + 0.004);
      } else if (this.y < canvas.height * 0.2) {
        this.opacity = Math.max(0, this.opacity - 0.008);
      }
      if (this.y < -20) this.reset();
    }
    draw() {
      ctx.save();
      ctx.globalAlpha = this.opacity;
      ctx.translate(this.x, this.y);
      ctx.rotate(this.rotation);
      ctx.fillStyle = this.color;
      if (this.shape === 'diamond') {
        ctx.beginPath();
        ctx.moveTo(0, -this.size);
        ctx.lineTo(this.size, 0);
        ctx.lineTo(0, this.size);
        ctx.lineTo(-this.size, 0);
        ctx.closePath();
        ctx.fill();
      } else {
        ctx.beginPath();
        ctx.arc(0, 0, this.size, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }
  }

  // Create particles
  for (let i = 0; i < 35; i++) {
    const p = new Particle();
    p.y = Math.random() * canvas.height; // Distribute initially
    particles.push(p);
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    requestAnimationFrame(animate);
  }
  animate();
}

/* ══ SCROLL REVEAL ══ */
function initReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('vis');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

/* ══ PARALLAX HERO BG ══ */
function initParallax() {
  const heroBg = document.querySelector('.hero-bg');
  if (!heroBg) return;

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrolled = window.pageYOffset;
        const rate = scrolled * 0.3;
        heroBg.style.transform = `scale(1.05) translateY(${rate}px)`;
        ticking = false;
      });
      ticking = true;
    }
  });
}

/* ══ STAGGERED CARD ENTRANCE ══ */
function initCardStagger() {
  const cards = document.querySelectorAll('.cat-card');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        const idx = Array.from(cards).indexOf(entry.target);
        setTimeout(() => {
          entry.target.classList.add('vis');
        }, (idx % 4) * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  cards.forEach(card => observer.observe(card));
}

/* ══ CATEGORY FILTER ══ */
function filterCategory(btn, category) {
  // Update active button
  document.querySelectorAll('.cat-nav-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  const cards = document.querySelectorAll('.cat-card');
  cards.forEach(card => {
    const categories = card.dataset.category ? card.dataset.category.split(' ') : [];
    if (category === 'all' || categories.includes(category)) {
      card.style.display = '';
      setTimeout(() => card.classList.add('vis'), 10);
    } else {
      card.style.display = 'none';
    }
  });
}

/* ══ SMOOTH HOVER TILT ══ */
document.addEventListener('mousemove', (e) => {
  const cards = document.querySelectorAll('.cat-card:hover');
  cards.forEach(card => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    card.style.transform = `translateY(-10px) rotateX(${-y * 3}deg) rotateY(${x * 3}deg)`;
  });
});

document.querySelectorAll('.cat-card').forEach(card => {
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});

/* ══ MOOD FEATURE: BREW YOUR MOOD ══ */
const moodData = {
  sleepy: {
    icon: '☕',
    title: 'Doux Réveil',
    quote: '"Un réveil en douceur avec la chaleur d\'un bon café."',
    drink: 'Cappuccino Mousseux',
    food: 'Viennoiserie Chaude'
  },
  focused: {
    icon: '🎯',
    title: 'Énergie Pure',
    quote: '"De grandes idées commencent par une petite pause café."',
    drink: 'Double Espresso',
    food: 'Fondant Chocolat'
  },
  relaxed: {
    icon: '🍃',
    title: 'Instant Zen',
    quote: '"Prenez une gorgée de calme et relâchez la pression."',
    drink: 'Vanilla Latte',
    food: 'Cheese Cake'
  },
  hungry: {
    icon: '🍕',
    title: 'Gourmandise',
    quote: '"Le bonheur se trouve dans une bonne part de pizza."',
    drink: 'Coca Cola Frais',
    food: 'Pizza 4 Fromage'
  },
  romantic: {
    icon: '✨',
    title: 'Ambiance Cosy',
    quote: '"La magie opère toujours autour d\'une bonne table."',
    drink: 'Mojito Crimson',
    food: 'Gâteau Opéra'
  },
  chill: {
    icon: '🍹',
    title: 'Moment Détente',
    quote: '"De bonnes boissons. De la meilleure compagnie."',
    drink: 'Mojito Blue',
    food: 'Pizza Escalope'
  },
  energy: {
    icon: '🚀',
    title: 'Coup de Boost',
    quote: '"L\'énergie de ce café vous mènera loin aujourd\'hui."',
    drink: 'Ice Americano',
    food: 'Burger Poulet'
  },
  study: {
    icon: '📖',
    title: 'Concentration Max',
    quote: '"Un esprit clair et un café chaud pour exceller."',
    drink: 'Americano',
    food: 'Baguette Thon'
  },
  rain: {
    icon: '🌧️',
    title: 'Pluie & Chaleur',
    quote: '"Rien de mieux que la pluie dehors et un café chaud dedans."',
    drink: 'Chocolat Chaud',
    food: 'Gâteau Chocolat Noisette'
  }
};

const moodBtns = document.querySelectorAll('.mood-btn');
const moodGrid = document.getElementById('mood-grid');
const moodResult = document.getElementById('mood-result');
const moodClose = document.getElementById('mood-close');

if (moodBtns.length > 0 && moodResult) {
  moodBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const mood = btn.dataset.mood;
      const data = moodData[mood];
      
      if (data) {
        // Hide grid, show result
        moodGrid.style.display = 'none';
        
        document.getElementById('mr-icon').textContent = data.icon;
        document.getElementById('mr-title').textContent = data.title;
        document.getElementById('mr-quote').textContent = data.quote;
        document.getElementById('mr-drink').textContent = data.drink;
        document.getElementById('mr-food').textContent = data.food;
        
        moodResult.style.display = 'block';
      }
    });
  });

  moodClose.addEventListener('click', () => {
    moodResult.style.display = 'none';
    moodGrid.style.display = 'grid';
  });
}

/* ══ DYNAMIC MASCOT TOOLTIPS ══ */
const mascotTooltips = [
  "Besoin d'un café ?",
  "Aujourd'hui, c'est cappuccino !",
  "Une petite pause ?",
  "Passez une belle journée ✨",
  "Il fait soif, non ?",
  "Un fondant au chocolat ?"
];

setInterval(() => {
  const tooltip = document.getElementById('mascot-msg');
  if (tooltip) {
    const randomMsg = mascotTooltips[Math.floor(Math.random() * mascotTooltips.length)];
    // Add brief fade out/in effect
    tooltip.style.opacity = '0';
    setTimeout(() => {
      tooltip.textContent = randomMsg;
      tooltip.style.opacity = '';
    }, 300);
  }
}, 8000);
