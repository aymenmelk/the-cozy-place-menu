def update_css():
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('''

/* ═══════════════════════════════════════
   NEW PREMIUM STYLES (ADDED)
═══════════════════════════════════════ */

/* Map Buttons */
.soc-map {
  background: linear-gradient(135deg, var(--dark), #2a160a);
  border: 1px solid rgba(201, 146, 26, 0.5) !important;
  color: var(--gold2);
  box-shadow: 0 4px 15px rgba(201, 146, 26, 0.15);
}
.soc-map:hover {
  background: var(--gold);
  color: var(--dark);
  box-shadow: 0 8px 25px rgba(201, 146, 26, 0.4);
}
.footer-map-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 30px;
  background: rgba(201, 146, 26, 0.1);
  border: 1px solid rgba(201, 146, 26, 0.3);
  color: var(--gold2);
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  transition: var(--transition);
}
.footer-map-btn:hover {
  background: var(--gold);
  color: var(--dark);
  transform: translateY(-2px);
}

/* Petit Dejeuner Highlight Card */
.highlight-card {
  grid-column: 1 / -1; /* Make it span all columns */
  display: flex;
  flex-direction: column;
  min-height: 400px;
  border: 2px solid var(--gold) !important;
  box-shadow: 0 15px 40px rgba(201, 146, 26, 0.2) !important;
  color: var(--white);
}
@media (min-width: 768px) {
  .highlight-card {
    flex-direction: row;
    align-items: center;
  }
  .highlight-card .card-header {
    flex: 1;
    padding: 40px;
  }
  .highlight-card .card-body {
    flex: 1.5;
    padding: 40px;
    background: rgba(30, 15, 6, 0.85);
    backdrop-filter: blur(10px);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
}
.highlight-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}
.highlight-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.highlight-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(30, 15, 6, 0.95) 0%, rgba(30, 15, 6, 0.6) 50%, rgba(30, 15, 6, 0.9) 100%);
  z-index: 1;
}
.highlight-card .card-header,
.highlight-card .card-body {
  position: relative;
  z-index: 2;
}
.highlight-note {
  display: inline-block;
  margin-top: 10px;
  padding: 6px 14px;
  background: rgba(201, 146, 26, 0.2);
  border: 1px solid rgba(201, 146, 26, 0.5);
  border-radius: 20px;
  font-size: 12px;
  color: var(--gold3);
  font-weight: 600;
  letter-spacing: 1px;
}
.premium-item {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  padding: 15px 0;
}
.premium-item .item-name {
  color: var(--white);
  font-size: 18px;
  font-weight: 600;
}
.premium-item .item-desc {
  display: block;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.6);
  margin-top: 4px;
}
.highlight-price {
  color: var(--gold2) !important;
  font-size: 18px !important;
  font-weight: 700 !important;
  background: rgba(201, 146, 26, 0.15);
  padding: 4px 10px;
  border-radius: 8px;
}

/* Horaires d'ouverture Section */
.horaires-section {
  padding: 80px 20px;
  position: relative;
  display: flex;
  justify-content: center;
}
.horaires-card {
  position: relative;
  max-width: 800px;
  width: 100%;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-hover);
  background: url('assets/images/background.png') center/cover no-repeat;
}
.horaires-glass {
  position: absolute;
  inset: 0;
  background: rgba(30, 15, 6, 0.85);
  backdrop-filter: blur(15px);
}
.horaires-content {
  position: relative;
  z-index: 2;
  padding: 60px 40px;
  text-align: center;
}
.horaires-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  margin-top: 40px;
  text-align: left;
}
@media (min-width: 768px) {
  .horaires-grid {
    grid-template-columns: 1fr 1fr;
    gap: 60px;
  }
}
.horaires-col {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.horaires-row {
  display: flex;
  align-items: center;
  color: var(--cream);
  font-size: 16px;
  font-weight: 500;
}
.horaires-row .day {
  flex-shrink: 0;
  width: 90px;
}
.horaires-row .dots {
  flex-grow: 1;
  height: 2px;
  margin: 0 15px;
  border-bottom: 2px dotted rgba(201, 146, 26, 0.3);
}
.horaires-row .hours {
  flex-shrink: 0;
  color: var(--gold3);
}
.highlight-day {
  color: var(--gold2) !important;
  font-weight: 700;
}
.highlight-day .day {
  color: var(--gold);
}
.highlight-day .hours {
  color: var(--gold);
  background: rgba(201, 146, 26, 0.1);
  padding: 2px 8px;
  border-radius: 6px;
}

/* Coffee Mascot */
.coffee-mascot-container {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 80px;
  height: 80px;
  z-index: 100;
  cursor: pointer;
  animation: floatMascot 4s ease-in-out infinite;
}
.coffee-mascot {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(30, 15, 6, 0.9);
  border: 2px solid rgba(201, 146, 26, 0.5);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(201, 146, 26, 0.2);
  overflow: hidden;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.coffee-mascot:hover {
  transform: scale(1.1);
  border-color: var(--gold);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 25px rgba(201, 146, 26, 0.4);
}
.coffee-mascot img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 120%;
  height: 120%;
  object-fit: contain;
  transition: opacity 0.4s ease;
}
.mascot-awake {
  opacity: 0;
}
.coffee-mascot-container:hover .mascot-sleepy {
  opacity: 0;
}
.coffee-mascot-container:hover .mascot-awake {
  opacity: 1;
}

.mascot-tooltip {
  position: absolute;
  top: -45px;
  right: 10px;
  background: var(--card-bg);
  color: var(--dark);
  padding: 8px 14px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  opacity: 0;
  transform: translateY(10px);
  pointer-events: none;
  transition: all 0.3s ease;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  border: 1px solid rgba(201, 146, 26, 0.2);
}
.mascot-tooltip::after {
  content: '';
  position: absolute;
  bottom: -5px;
  right: 25px;
  width: 10px;
  height: 10px;
  background: var(--card-bg);
  transform: rotate(45deg);
  border-right: 1px solid rgba(201, 146, 26, 0.2);
  border-bottom: 1px solid rgba(201, 146, 26, 0.2);
}
.coffee-mascot-container:hover .mascot-tooltip {
  opacity: 1;
  transform: translateY(0);
}

@keyframes floatMascot {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

@media (max-width: 768px) {
  .coffee-mascot-container {
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
  }
}

''')
    print("CSS updated successfully!")

if __name__ == '__main__':
    update_css()
