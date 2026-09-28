(function(){
  var links = document.querySelectorAll('.rail-nav a');
  var sections = Array.prototype.map.call(links, function(a){
    return document.querySelector(a.getAttribute('href'));
  });
  function onScroll(){
    var pos = window.scrollY + 120;
    var activeIdx = 0;
    sections.forEach(function(sec, i){
      if(sec && sec.offsetTop <= pos) activeIdx = i;
    });
    links.forEach(function(a, i){ a.classList.toggle('active', i === activeIdx); });
  }
  document.addEventListener('scroll', onScroll, {passive:true});
  onScroll();
})();

(function(){
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCap = document.getElementById('lightboxCap');
  var closeBtn = document.getElementById('lightboxClose');
  var lastTrigger = null;

  function openLightbox(src, alt, caption){
    lightboxImg.src = src;
    lightboxImg.alt = alt || '';
    lightboxCap.textContent = caption || '';
    lightbox.classList.add('open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }
  function closeLightbox(){
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    lightboxImg.src = '';
    if(lastTrigger){ lastTrigger.focus(); }
  }

  document.querySelectorAll('.shot[data-full]').forEach(function(btn){
    btn.addEventListener('click', function(){
      lastTrigger = btn;
      var img = btn.querySelector('img');
      openLightbox(btn.getAttribute('data-full'), img ? img.alt : '', btn.getAttribute('data-caption'));
    });
  });

  closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', function(e){
    if(e.target === lightbox){ closeLightbox(); }
  });
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && lightbox.classList.contains('open')){ closeLightbox(); }
  });
})();
