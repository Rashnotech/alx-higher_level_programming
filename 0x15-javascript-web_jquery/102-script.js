$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + lang,
      success: function (res) {
        $('DIV#hello').text(res.hello);
      }
    });
  });
});
