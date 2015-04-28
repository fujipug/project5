// initializes the map and its style
function initialize() {
  var mapCanvas = document.getElementById('map-canvas');

  // set the starting lat/long location, zoom level, and map type
  var mapOptions = {
    center: new google.maps.LatLng(35.189907, -111.652755),
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  // create the map
  var map = new google.maps.Map(mapCanvas, mapOptions);

  // see https://gmaps-samples-v3.googlecode.com/svn/trunk/styledmaps/wizard/index.html
  map.set('styles', [
  {
    // hide position of interest styling
    featureType: 'poi',
    elementType: 'geometry',
    stylers: [ { visibility: 'off' } ]
  },
  // set the school position of interests to have a green shade
  {
    featureType: 'poi.school',
    elementType: 'geometry',
    stylers: [
    { visibility: 'on' },
    { hue: '#F6F8EE'/*'#338800'*/ },
    ]
  }
  ]);
//var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';-->
// CC BYSA 3.0 Maps Icons Collection https://mapicons.mapsmarker.com
var icons = {
parking: {
  icon: 'static/parking.png'
}
};
}
// end initialize()

google.maps.event.addDomListener(window, 'load', initialize);
