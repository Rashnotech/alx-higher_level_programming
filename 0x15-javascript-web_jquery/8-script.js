$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json'
}).done(function(data) {
  $('UL#list_movies').add('<li>'+ data.title +'</li>');
});
