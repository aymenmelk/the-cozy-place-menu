def update_mascot():
    # Update script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        script = f.read()
    
    target = '''  /* ── CARD STAGGER ── */
  initCardStagger();

});'''
    replacement = '''  /* ── CARD STAGGER ── */
  initCardStagger();

  /* ── MASCOT WAKE UP ── */
  setTimeout(() => {
    const mascot = document.querySelector('.coffee-mascot-container');
    if (mascot) {
      mascot.classList.add('waking-up');
      setTimeout(() => mascot.classList.remove('waking-up'), 2500);
    }
  }, 2000);

});'''
    script = script.replace(target, replacement)
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)

    # Update style.css
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('''
.coffee-mascot-container.waking-up .mascot-sleepy { opacity: 0; }
.coffee-mascot-container.waking-up .mascot-awake { opacity: 1; }
.coffee-mascot-container.waking-up .mascot-tooltip {
  opacity: 1;
  transform: translateY(0);
}
''')

if __name__ == '__main__':
    update_mascot()
