
function place_pin(map,coordenada,titulo,parrafo){

  var recepcion_marker = new google.maps.Marker({
    position: coordenada,
    map: map
  });

  var mensaje = '<div class="info-window">' +
            '<div class="info-content">' +
            '<h6>'+titulo+'</h6>' +
            '<p>'+parrafo+'</p>'+
            '</div>' +
            '</div>';

  var recepcion_window = new google.maps.InfoWindow({
        content: mensaje,
        maxWidth: 160
  });

  recepcion_window.open(map, recepcion_marker);

  recepcion_marker.addListener('click', function () {
        recepcion_window.open(map, recepcion_marker);
  });

}


  function initMap() {
      var recepcion_coord = {lat: lat_recepcion, lng: lng_recepcion};
      var ceremonia_coord = {lat: lat_ceremonia, lng: lng_ceremonia};
      var entrada_coord = {lat: lat_entrada, lng: lng_entrada};

      var mapOtions = {
        zoom: 15,
        minZoom: 13,
        maxZoom: 17,
        center: recepcion_coord,

      }

      var mapCanvas = document.getElementById('map');

      var map = new google.maps.Map(mapCanvas, mapOtions);

      var coordenada = recepcion_coord;
      var titulo = "Villa Vieja"
      var parrafo = "José Miguel Carrión <br> y Juan Procel"
      place_pin(map,coordenada,titulo,parrafo);

      coordenada = ceremonia_coord;
      titulo = "Sagrada Familia"
      parrafo = "José Gonzalo Coordero <br> y Descalzi"
      place_pin(map,coordenada,titulo,parrafo);

      coordenada = entrada_coord;
      titulo = "Nueva Entrada"
      parrafo = "Entrada para visitantes a la<br>urbanización El Condado, calle Río Peripa"
      place_pin(map,coordenada,titulo,parrafo);


    }

    google.maps.event.addDomListener(window, 'load', initMap);
