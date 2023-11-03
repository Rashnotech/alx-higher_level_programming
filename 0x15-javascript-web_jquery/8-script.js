$.ajax({
  type: 'GET',
  dataType: 'json',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function(res) {
    $.each(res.result, function(index, movie) {
      $('UL#list_movies').append('<li>'+ movie.title +'</li>');
    });
  }
});
