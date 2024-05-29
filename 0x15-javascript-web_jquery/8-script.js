$(document).ready(function() {
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {

    $.each(data.results, function(index, film) {
      let title = film.title;
      $("#list_movies").append("<li>" + title + "</li>");
    });
  }).fail(function(jqXHR, textStatus, errorThrown) {
    console.error("Request Failed:", textStatus, errorThrown);
  });
});

