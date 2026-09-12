// Caulderon Interactive — shared site script

// Footer year
document.querySelectorAll('#year, #cyear').forEach(function(el){
  el.textContent = new Date().getFullYear();
});

// Mobile nav toggle
document.querySelectorAll('.nav-toggle').forEach(function(btn){
  btn.addEventListener('click', function(){
    var inner = btn.closest('.nav-inner');
    var links = inner && inner.querySelector('.nav-links');
    if(!links) return;
    var open = links.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var inner = btn.closest('.nav-inner');
  var links = inner && inner.querySelector('.nav-links');
  if(links){
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        links.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  }
});
