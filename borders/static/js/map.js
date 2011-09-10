$(function () {
  var map = new OpenLayers.Map("map");
  var lonlat = new OpenLayers.LonLat(-82.998962, 42.365462);
  var layer = new OpenLayers.Layer.OSM("OSM Example");
  map.addLayer(layer);
  map.setCenter(lonlat);
});

