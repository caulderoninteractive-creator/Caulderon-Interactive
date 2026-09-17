
(function(){
  'use strict';
  var root = document.querySelector('[data-jobs-app]');
  if(root){
    var cards = Array.prototype.slice.call(root.querySelectorAll('[data-job-card]'));
    var input = root.querySelector('[data-jobs-search]');
    var filters = Array.prototype.slice.call(root.querySelectorAll('[data-jobs-filter]'));
    var count = root.querySelector('[data-jobs-count]');
    var empty = root.querySelector('[data-jobs-empty]');
    var more = root.querySelector('[data-jobs-more]');
    var sections = Array.prototype.slice.call(root.querySelectorAll('[data-job-section]'));
    var activeFilter = 'all';
    var expandedUpdates = false;
    var INITIAL_UPDATES = 8;

    function normalized(value){ return String(value || '').toLowerCase().trim(); }
    function filterMatch(card){
      var kind = card.getAttribute('data-kind') || '';
      var status = card.getAttribute('data-status') || '';
      if(activeFilter === 'all') return true;
      if(activeFilter === 'updates') return kind === 'update';
      if(activeFilter === 'open') return kind === 'opening' && ['open','open_unknown','recent_unknown'].indexOf(status) !== -1;
      if(activeFilter === 'closing') return kind === 'opening' && status === 'closing_soon';
      if(activeFilter === 'upcoming') return kind === 'opening' && status === 'upcoming';
      return true;
    }
    function apply(){
      var query = normalized(input && input.value);
      var visible = 0;
      var matchingUpdates = 0;
      cards.forEach(function(card){
        var match = filterMatch(card) && (!query || normalized(card.getAttribute('data-search')).indexOf(query) !== -1);
        var isUpdate = card.getAttribute('data-kind') === 'update';
        if(match && isUpdate){
          matchingUpdates += 1;
          if(!query && activeFilter === 'all' && !expandedUpdates && matchingUpdates > INITIAL_UPDATES) match = false;
        }
        card.hidden = !match;
        if(match) visible += 1;
      });
      sections.forEach(function(section){
        var any = Array.prototype.some.call(section.querySelectorAll('[data-job-card]'), function(card){ return !card.hidden; });
        var notice = section.querySelector('.jobs-notice');
        section.hidden = !any && Boolean(query || activeFilter !== 'all');
      });
      if(count) count.textContent = visible + (visible === 1 ? ' result' : ' results');
      if(empty) empty.hidden = visible !== 0;
      if(more){
        var totalUpdates = cards.filter(function(c){ return c.getAttribute('data-kind') === 'update'; }).length;
        more.hidden = query || activeFilter !== 'all' || expandedUpdates || totalUpdates <= INITIAL_UPDATES;
      }
    }
    if(input) input.addEventListener('input', apply);
    filters.forEach(function(button){
      button.addEventListener('click', function(){
        activeFilter = button.getAttribute('data-filter') || 'all';
        filters.forEach(function(b){ var on = b === button; b.classList.toggle('is-active', on); b.setAttribute('aria-pressed', on ? 'true' : 'false'); });
        apply();
      });
    });
    if(more) more.addEventListener('click', function(){ expandedUpdates = true; apply(); });
    apply();
  }

  function fallbackCopy(value, done){
    var field = document.createElement('textarea');
    field.value = value;
    field.setAttribute('readonly','');
    field.style.position = 'fixed';
    field.style.opacity = '0';
    document.body.appendChild(field);
    field.select();
    try{ if(document.execCommand('copy')) done(); }catch(_e){}
    field.remove();
  }

  document.querySelectorAll('[data-copy-link]').forEach(function(button){
    button.addEventListener('click', function(){
      var value = window.location.href;
      var done = function(){
        var old = button.textContent;
        button.textContent = 'Link copied';
        button.classList.add('is-copied');
        window.setTimeout(function(){ button.textContent = old; button.classList.remove('is-copied'); }, 1600);
      };
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(value).then(done).catch(function(){ fallbackCopy(value, done); });
      }else{
        fallbackCopy(value, done);
      }
    });
  });
})();
