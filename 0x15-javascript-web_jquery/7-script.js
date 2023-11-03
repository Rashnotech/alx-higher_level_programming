$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json',
  success: function (response) {
    $.each(response.results, function (index, character) {
      $('DIV#character').append(character);
    });
  }
});
