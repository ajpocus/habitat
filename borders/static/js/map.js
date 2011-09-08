function init () {
  var latlng = new google.maps.LatLng(42.365462, -82.998962);
  var opts = {
    zoom: 8,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map_canvas"), opts);
}

