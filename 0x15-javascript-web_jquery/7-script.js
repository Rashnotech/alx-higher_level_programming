$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
}).done(function() {
  $('DIV#character').addClass('done');
});
