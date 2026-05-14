def update_css_polish():
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('''

/* ═══════════════════════════════════════
   FINAL POLISH & MOBILE OPTIMIZATION
═══════════════════════════════════════ */

/* Breakfast Section Polish */
.highlight-overlay {
  background: linear-gradient(110deg, rgba(30, 15, 6, 0.98) 0%, rgba(30, 15, 6, 0.8) 40%, rgba(30, 15, 6, 0.2) 100%);
  transition: all 0.5s ease;
}
.highlight-card:hover .highlight-overlay {
  background: linear-gradient(110deg, rgba(30, 15, 6, 0.95) 0%, rgba(30, 15, 6, 0.7) 40%, rgba(30, 15, 6, 0.1) 100%);
}
.highlight-card .card-title {
  text-shadow: 0 2px 10px rgba(0,0,0,0.5);
  font-family: 'Cormorant Garamond', serif;
  font-size: 32px !important;
  font-weight: 700;
  letter-spacing: 1px;
}
.premium-item {
  transition: transform 0.3s ease, background 0.3s ease;
  padding: 15px 10px;
  border-radius: 8px;
}
.premium-item:hover {
  background: rgba(255, 255, 255, 0.05);
  transform: translateX(5px);
}

/* Mascot Refinement */
.coffee-mascot-container {
  bottom: 40px;
  right: 40px;
  transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}
@media (max-width: 768px) {
  .coffee-mascot-container {
    bottom: 25px;
    right: 25px;
    width: 55px;
    height: 55px;
    z-index: 9999;
  }
  .mascot-tooltip {
    display: none; /* Hide tooltip on mobile to prevent overlap */
  }
}

/* Mobile Spacing & Readability */
@media (max-width: 768px) {
  .sec-title {
    font-size: 36px;
  }
  .cards-grid {
    gap: 20px;
  }
  .cat-card {
    margin-bottom: 5px;
  }
  .card-body {
    padding: 20px;
  }
  .horaires-content {
    padding: 40px 20px;
  }
  .horaires-grid {
    gap: 15px;
  }
  .footer-map-btn {
    padding: 12px 24px; /* More touch-friendly */
    font-size: 14px;
  }
  .cat-nav {
    gap: 10px;
  }
  .cat-nav-btn {
    padding: 10px 20px;
    font-size: 13px;
  }
}

/* Unified Buttons and Shadows */
.cat-card {
  box-shadow: 0 8px 30px rgba(30, 15, 6, 0.08);
}
.cat-card:hover {
  box-shadow: 0 15px 40px rgba(30, 15, 6, 0.15);
}
''')
    print("Final CSS polish added successfully!")

if __name__ == '__main__':
    update_css_polish()
