// ========== Language toggle (TC default, EN secondary) ==========
const STORAGE_KEY = 'erv_lang';
const html = document.documentElement;

function applyLang(lang) {
  html.setAttribute('data-lang', lang);
  html.setAttribute('lang', lang === 'en' ? 'en' : 'zh-Hant');
  document.querySelectorAll('.lang-switch button').forEach((b) => {
    b.classList.toggle('active', b.dataset.lang === lang);
  });
  localStorage.setItem(STORAGE_KEY, lang);
}

const saved = localStorage.getItem(STORAGE_KEY);
applyLang(saved === 'en' ? 'en' : 'zh');

document.querySelectorAll('.lang-switch button').forEach((btn) => {
  btn.addEventListener('click', () => applyLang(btn.dataset.lang));
});

// ========== Mobile nav ==========
function toggleNav() {
  document.getElementById('mobileNav').classList.toggle('open');
}
window.toggleNav = toggleNav;

// ========== Reveal on scroll ==========
const revealEls = document.querySelectorAll('.reveal, .reveal-img');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
revealEls.forEach((el) => revealObs.observe(el));

// ========== Sticky tech-stage image switching ==========
const techSteps = document.querySelectorAll('.tech-step');
const techImgs = document.querySelectorAll('.tech-img');
if (techSteps.length && techImgs.length) {
  const techObs = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        const idx = e.target.getAttribute('data-step');
        techImgs.forEach((img) => img.classList.toggle('active', img.getAttribute('data-tech') === idx));
      }
    });
  }, { rootMargin: '-40% 0px -40% 0px', threshold: 0 });
  techSteps.forEach((s) => techObs.observe(s));
}

// ========== Quote form ==========
const quoteForm = document.getElementById('quoteForm');
if (quoteForm) {
  quoteForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = quoteForm.querySelector('button[type="submit"]');
    const fineprint = quoteForm.querySelector('.form-fineprint');
    const originalBtnText = btn.textContent;
    btn.textContent = html.getAttribute('data-lang') === 'en' ? 'Sending…' : '傳送中…';
    btn.disabled = true;
    try {
      const res = await fetch(quoteForm.action, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(quoteForm),
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok && data.success) {
        btn.textContent = html.getAttribute('data-lang') === 'en' ? 'Sent — we will be in touch' : '已收到 — 我們將盡快回覆';
        btn.style.background = 'var(--accent)';
        if (fineprint) fineprint.textContent = html.getAttribute('data-lang') === 'en' ? 'Thanks — your enquiry has been received.' : '感謝您的查詢，已成功送達。';
      } else {
        throw new Error(data.message || 'Submission failed');
      }
    } catch (err) {
      btn.textContent = originalBtnText;
      btn.disabled = false;
      if (fineprint) {
        fineprint.textContent = html.getAttribute('data-lang') === 'en'
          ? 'Sorry — could not send. Please WhatsApp +852 8404 3880 or email erv@erv.hk.'
          : '抱歉，未能傳送。請 WhatsApp +852 8404 3880 或電郵 erv@erv.hk。';
        fineprint.style.color = '#e8a13a';
      }
    }
  });
}
