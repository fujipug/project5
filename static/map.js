// initializes the map and its style
var map;
var icons;

function initialize() {
  var mapCanvas = document.getElementById('map-canvas');

  // set the starting lat/long location, zoom level, and map type
  var mapOptions = {
    center: new google.maps.LatLng(35.181794, -111.654232),
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  // create the map
  map = new google.maps.Map(mapCanvas, mapOptions);

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
  icons = {
    parking: {
      icon: 'static/parking.png'
    }
  };

  // request used for querying google map places 5000m from NAU center
  // i.e. look for parking lots
  var request = {
    location: map.getCenter(),
    radius: '5000',
    types: ['parking'],
    query: 'P62A'
  };
  var service = new google.maps.places.PlacesService(map);
  service.textSearch(request, callback);
}
// end initialize()


// Checks that the PlacesServiceStatus is OK, and adds a marker
// using the place ID and location from the PlacesService.
function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    var marker = new google.maps.Marker({
      map: map,
      icon: icons['parking'].icon,
      place: {
        // get the most relevant results
        placeId: results[0].place_id,
        location: results[0].geometry.location
      }
    });
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
