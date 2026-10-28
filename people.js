// Students page: point at a name (or tab to it, or click it) to show that
// person's photo and description in the box at the top. The last person
// shown stays there, as on the old page.
(function () {
  var img = document.getElementById('feature-img');
  var text = document.getElementById('feature-text');
  var active = null;

  function show(person) {
    img.src = person.dataset.img;
    text.textContent = person.dataset.desc;
    if (active) active.classList.remove('is-active');
    person.classList.add('is-active');
    active = person;
  }

  document.querySelectorAll('.person').forEach(function (person) {
    ['mouseenter', 'focus', 'click'].forEach(function (type) {
      person.addEventListener(type, function () { show(person); });
    });
  });
})();
