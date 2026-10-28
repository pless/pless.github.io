/* Publications page: location.hash picks one view of the list.
   (none), #all    every paper, newest year first
   #type           the papers grouped by publication type
   #selected #geometry #ML #social #ugrad
                   only the papers with that tag (case does not matter)
   #BIBKEY         every paper; that paper is highlighted, in view, [bib] open
   Without JavaScript the page shows the full by-year list. */
(function () {
  'use strict';

  const TOPICS = ['selected', 'geometry', 'ml', 'social', 'ugrad'];
  const byYear = document.getElementById('pubs-by-year');
  const byType = document.getElementById('pubs-by-type');
  const status = document.querySelector('.pub-count');
  const links = document.querySelectorAll('.pub-views a');
  if (!byYear || !byType || !status) return;

  const papers = byYear.querySelectorAll('li.pub');
  const groups = byYear.querySelectorAll('.pub-group');
  let target = null;
  let started = false;

  function show(element, on) {
    element.hidden = !on;
  }

  function hashName() {
    const name = location.hash.slice(1);
    try {
      return decodeURIComponent(name);
    } catch (error) {
      return name;
    }
  }

  // The view a hash asks for, or null if the hash is not for this page's views.
  function viewFor(name) {
    const lower = name.toLowerCase();
    if (name === '' || lower === 'all') return { type: false, link: '#all' };
    if (lower === 'type') return { type: true, link: '#type' };
    if (TOPICS.includes(lower)) return { type: false, topic: lower, link: '#' + lower };
    const paper = document.getElementById(name);
    if (paper && paper.classList.contains('pub')) return { type: false, link: '#all', paper: paper };
    return null;
  }

  function showPapers(topic) {
    let shown = 0;
    groups.forEach(function (group) {
      let inGroup = 0;
      group.querySelectorAll('li.pub').forEach(function (paper) {
        const on = !topic || paper.dataset.tags.split(' ').includes(topic);
        show(paper, on);
        if (on) inGroup += 1;
      });
      show(group, inGroup > 0);
      shown += inGroup;
    });
    return shown;
  }

  function markCurrent(hash) {
    links.forEach(function (link) {
      if (link.getAttribute('href').toLowerCase() === hash) {
        link.setAttribute('aria-current', 'true');
      } else {
        link.removeAttribute('aria-current');
      }
    });
  }

  function update() {
    let view = viewFor(hashName());
    if (!view) {
      if (started) return;   // another link on the page, such as "Skip to content"
      view = viewFor('');
    }
    started = true;

    if (target) target.classList.remove('is-target');
    target = view.paper || null;

    show(byYear, !view.type);
    show(byType, view.type);
    const shown = showPapers(view.topic);
    if (view.topic) {
      status.textContent = 'Showing ' + shown + ' of ' + papers.length + ' papers.';
    } else if (view.type) {
      status.textContent = papers.length + ' papers, grouped by publication type.';
    } else {
      status.textContent = '';
    }
    markCurrent(view.link);

    if (target) {
      const bib = target.querySelector('details');
      if (bib) bib.open = true;
      target.classList.add('is-target');
      target.scrollIntoView();
    }
  }

  window.addEventListener('hashchange', update);
  update();
})();
