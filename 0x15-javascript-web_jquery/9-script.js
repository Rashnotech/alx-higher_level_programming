$.ajax({
  type: 'GET',
  dataType: 'json',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: function(res) {
    $('DIV#hello').text(res.hello)
  })
});
