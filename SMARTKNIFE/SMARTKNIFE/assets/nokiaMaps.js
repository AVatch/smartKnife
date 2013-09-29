
$(document).ready(function(){
	console.log("hello")
	nokia.Settings.set("app_id", "0aTWVUnvsgTleHtfY2u5"); 
	nokia.Settings.set("app_code", "WnXVwKkX52k6OLlCPWDiMQ");
	// Use staging environment (remove the line for production environment)
	nokia.Settings.set("serviceMode", "cit");

	// Get the DOM node to which we will append the map
	var mapContainer = document.getElementById("mapContainer");
	// Create a map inside the map container DOM node
	var map = new nokia.maps.map.Display(mapContainer, {
		// Initial center and zoom level of the map
		center: [40.72, -74],
		zoomLevel: 15,
		// We add the behavior component to allow panning / zooming of the map
		components:[new nokia.maps.map.component.Behavior()]
	});

	var marker = new nokia.maps.map.StandardMarker(new nokia.maps.geo.Coordinate(40.72, -74));
	map.objects.add(marker);

});


