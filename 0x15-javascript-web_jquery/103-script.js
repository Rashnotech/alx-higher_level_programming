$(function() {
  $('INPUT#btn_translate').on('click', function() {
    translate();
  });

  $('INPUT#language_code').on('keypress', function(event) {
    if (event.key === 'Enter') translate();
  });
  function translate() {
    let lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/'+lang,
      success: function(res) {
        $('DIV#hello').text(res.hello);
      }
    });
  }
});
