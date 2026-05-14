import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add Google Maps Button to Hero
    socials_target = '''    <!-- Social buttons -->
    <div class="socials">'''
    socials_replacement = '''    <!-- Social buttons -->
    <div class="socials">
      <a href="https://maps.app.goo.gl/YourMapLinkHere" target="_blank" class="soc-btn soc-map">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="white"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        Voir la localisation
      </a>'''
    html = html.replace(socials_target, socials_replacement)

    # 2. Add Google Maps Button to Footer
    footer_target = '''  <span style="font-size: 12px; opacity: 0.45;">© 2026 The Cozy Place · Tous droits réservés</span>'''
    footer_replacement = '''  <div style="margin: 20px 0;">
    <a href="https://maps.app.goo.gl/YourMapLinkHere" target="_blank" class="footer-map-btn">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
      Voir la localisation
    </a>
  </div>
  <span style="font-size: 12px; opacity: 0.45;">© 2026 The Cozy Place · Tous droits réservés</span>'''
    html = html.replace(footer_target, footer_replacement)

    # 3. Update Category Nav
    nav_target = '''    <nav class="cat-nav reveal">
      <button class="cat-nav-btn active" onclick="filterCategory(this,'all')">Tout voir</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'drinks')">Boissons</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'food')">Restauration</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'coffee')">Café</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'cold')">Frais</button>
    </nav>'''
    nav_replacement = '''    <nav class="cat-nav reveal">
      <button class="cat-nav-btn active" onclick="filterCategory(this,'all')">Tout voir</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'petit-dejeuner')">Petit Déjeuner</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'drinks')">Boissons</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'food')">Restauration</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'coffee')">Café</button>
      <button class="cat-nav-btn" onclick="filterCategory(this,'dessert')">Desserts</button>
    </nav>'''
    html = html.replace(nav_target, nav_replacement)

    # 4. Insert New Cards into cards-grid
    # We will find the beginning of cards-grid and insert Formules Petit Dejeuner
    grid_target = '''    <!-- Cards grid -->
    <div class="cards-grid">'''
    
    petit_dejeuner_html = '''

      <!-- ── FORMULES PETIT DÉJEUNER ── -->
      <div class="cat-card highlight-card reveal" data-category="petit-dejeuner food">
        <div class="highlight-bg">
          <img src="assets/images/petit_dejeuner_atmosphere_1778656533946.png" alt="Petit Déjeuner Atmosphere">
        </div>
        <div class="highlight-overlay"></div>
        <div class="card-header highlight-header">
          <div class="card-title-group">
            <div class="card-title" style="color:var(--gold2); font-size:26px;">Formules Petit Déjeuner</div>
            <div class="highlight-note">Disponible de 07:00 à 11:30</div>
          </div>
        </div>
        <div class="card-body">
          <div class="menu-item premium-item">
            <div class="item-info">
              <span class="item-name">Menu Express</span>
              <span class="item-desc">Café, Viennoiserie au choix</span>
            </div>
            <span class="item-price highlight-price">4.000 dt</span>
          </div>
          <div class="menu-item premium-item">
            <div class="item-info">
              <span class="item-name">Menu Classique</span>
              <span class="item-desc">Café, Jus, Eau 0.5L, Viennoiserie au choix</span>
            </div>
            <span class="item-price highlight-price">6.000 dt</span>
          </div>
          <div class="menu-item premium-item">
            <div class="item-info">
              <span class="item-name">Menu Copio</span>
              <span class="item-desc">Café, Jus, Eau 0.5L, Viennoiserie, Omelette, Beurre, Confiture, Toast</span>
            </div>
            <span class="item-price highlight-price">8.000 dt</span>
          </div>
        </div>
      </div>
'''
    html = html.replace(grid_target, grid_target + petit_dejeuner_html)

    # Insert Soft Drinks before MOJITOS CORE
    mojito_target = '''      <!-- ── MOJITOS CORE ── -->'''
    soft_drinks_html = '''      <!-- ── SOFT DRINKS ── -->
      <div class="cat-card reveal" data-category="drinks cold">
        <div class="card-header">
          <div class="card-icon" style="border-radius:12px; overflow:hidden;">
            <img src="assets/images/soft_drinks_premium_1778656187646.png" alt="Soft Drinks" style="width:100%; height:100%; object-fit:cover;">
          </div>
          <div class="card-title-group">
            <div class="card-title">Soft Drinks</div>
            <div class="card-subtitle">Boissons rafraîchissantes</div>
          </div>
          <span class="card-count">6 items</span>
        </div>
        <div class="card-body">
          <div class="menu-item">
            <span class="item-name">Eau minérale 0.5L</span>
            <span class="item-price">1.000 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Eau minérale 1.5L</span>
            <span class="item-price">2.000 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Schweppes</span>
            <span class="item-price">3.500 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Boga</span>
            <span class="item-price">3.500 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Coca Cola</span>
            <span class="item-price">3.500 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Fanta</span>
            <span class="item-price">3.500 dt</span>
          </div>
        </div>
      </div>

'''
    html = html.replace(mojito_target, soft_drinks_html + mojito_target)

    # Insert Tabouna after MAKLOUB
    baguette_target = '''      <!-- ── BAGUETTE FARCIE ── -->'''
    tabouna_html = '''      <!-- ── TABOUNA ── -->
      <div class="cat-card reveal" data-category="food">
        <div class="card-header">
          <div class="card-icon" style="border-radius:12px; overflow:hidden;">
            <img src="assets/images/tabouna_premium_1778656218253.png" alt="Tabouna" style="width:100%; height:100%; object-fit:cover;">
          </div>
          <div class="card-title-group">
            <div class="card-title">Tabouna</div>
            <div class="card-subtitle">Pain traditionnel garni</div>
          </div>
          <span class="card-count">3 items</span>
        </div>
        <div class="card-body">
          <div class="menu-item">
            <span class="item-name">Tabouna Jambon</span>
            <span class="item-price">4.500 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Tabouna Thon</span>
            <span class="item-price">5.500 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Tabouna Escalope</span>
            <span class="item-price">6.000 dt</span>
          </div>
        </div>
      </div>

'''
    html = html.replace(baguette_target, tabouna_html + baguette_target)

    # Insert Gateaux after BURGER (at the end of cards-grid)
    grid_end_target = '''    </div><!-- /cards-grid -->'''
    gateaux_html = '''      <!-- ── GÂTEAUX ── -->
      <div class="cat-card reveal" data-category="dessert food">
        <div class="card-header">
          <div class="card-icon" style="border-radius:12px; overflow:hidden;">
            <img src="assets/images/gateaux_premium_1778656518833.png" alt="Gâteaux" style="width:100%; height:100%; object-fit:cover;">
          </div>
          <div class="card-title-group">
            <div class="card-title">Gâteaux</div>
            <div class="card-subtitle">Pâtisseries fines</div>
          </div>
          <span class="card-count">6 items</span>
        </div>
        <div class="card-body">
          <div class="menu-item">
            <span class="item-name">Opera</span>
            <span class="item-price">4.000 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Fondant</span>
            <span class="item-price">3.000 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Cheese Cake</span>
            <span class="item-price">4.000 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Chocolat Noisette</span>
            <span class="item-price">3.500 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Pistache</span>
            <span class="item-price">4.200 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name">Chocolate Nuts</span>
            <span class="item-price">4.000 dt</span>
          </div>
        </div>
      </div>

'''
    html = html.replace(grid_end_target, gateaux_html + grid_end_target)

    # Add Pizza Tranche to Pizza
    pizza_target = '''          <div class="menu-item">
            <span class="item-name">4 fromage</span>
            <span class="item-price">11.000 dt</span>
          </div>
        </div>
      </div>'''
    pizza_replacement = '''          <div class="menu-item">
            <span class="item-name">4 fromage</span>
            <span class="item-price">11.000 dt</span>
          </div>
          <div class="menu-item">
            <span class="item-name" style="color:var(--gold2);">Pizza Tranche</span>
            <span class="item-price">1.500 dt</span>
          </div>
        </div>
      </div>'''
    html = html.replace(pizza_target, pizza_replacement)
    
    # Change pizza item count from 4 to 5
    pizza_count_target = '''          <span class="card-count">4 items</span>
        </div>
        <div class="card-body">
          <div class="menu-item">
            <span class="item-name">Escalope</span>'''
    pizza_count_replacement = '''          <span class="card-count">5 items</span>
        </div>
        <div class="card-body">
          <div class="menu-item">
            <span class="item-name">Escalope</span>'''
    html = html.replace(pizza_count_target, pizza_count_replacement)

    # 5. Insert Horaires d'ouverture after menu section
    menu_section_end = '''</section>

<!-- ═══════════════════════════════════════
     INSTAGRAM SECTION'''
    horaires_html = '''</section>

<!-- ═══════════════════════════════════════
     HORAIRES SECTION
═══════════════════════════════════════ -->
<section class="horaires-section" id="horaires">
  <div class="section-inner">
    <div class="horaires-card reveal">
      <div class="horaires-glass"></div>
      <div class="horaires-content">
        <p class="sec-badge">Informations</p>
        <h2 class="sec-title" style="color:var(--white);">Horaires d’<em>ouverture</em></h2>
        <div class="ornament">
          <div class="orn-line" style="background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2))"></div>
          <div class="orn-diamond" style="background:rgba(255,255,255,0.2)"></div>
          <div class="orn-line r" style="background:linear-gradient(90deg,rgba(255,255,255,0.2),transparent)"></div>
        </div>
        
        <div class="horaires-grid">
          <div class="horaires-col">
            <div class="horaires-row"><span class="day">Lundi</span><span class="dots"></span><span class="hours">07:00 – 23:30</span></div>
            <div class="horaires-row"><span class="day">Mardi</span><span class="dots"></span><span class="hours">07:00 – 23:30</span></div>
            <div class="horaires-row"><span class="day">Mercredi</span><span class="dots"></span><span class="hours">07:00 – 23:30</span></div>
            <div class="horaires-row"><span class="day">Jeudi</span><span class="dots"></span><span class="hours">07:00 – 23:30</span></div>
          </div>
          <div class="horaires-col">
            <div class="horaires-row"><span class="day">Vendredi</span><span class="dots"></span><span class="hours">07:00 – 23:30</span></div>
            <div class="horaires-row"><span class="day">Samedi</span><span class="dots"></span><span class="hours">07:00 – 23:30</span></div>
            <div class="horaires-row highlight-day"><span class="day">Dimanche</span><span class="dots"></span><span class="hours">08:30 – 22:00</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     INSTAGRAM SECTION'''
    html = html.replace(menu_section_end, horaires_html)

    # 6. Insert Coffee Mascot
    body_end_target = '''<script src="script.js"></script>
</body>'''
    mascot_html = '''<!-- Coffee Mascot -->
<div class="coffee-mascot-container">
  <div class="coffee-mascot">
    <img src="assets/images/coffee_mascot_sleepy_1778656639766.png" alt="Sleepy Coffee" class="mascot-sleepy">
    <img src="assets/images/coffee_mascot_awake_1778656692880.png" alt="Awake Coffee" class="mascot-awake">
  </div>
  <div class="mascot-tooltip">Besoin d'un café ?</div>
</div>

<script src="script.js"></script>
</body>'''
    html = html.replace(body_end_target, mascot_html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML updated successfully!")

if __name__ == '__main__':
    update_html()
