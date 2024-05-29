$(document).ready(function() {
  $('#btn_translate').click(function() {
    let languageCode = $('#language_code').val();
    let apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode + '/';
    
    $.getJSON(apiUrl, function(data) {
      $('#hello').text(data.hello);
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.error("Request Failed:", textStatus, errorThrown);
      $('#hello').text('Translation failed.');
    });
  });
});
