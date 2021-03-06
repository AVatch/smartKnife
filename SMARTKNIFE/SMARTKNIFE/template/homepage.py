{% extends "base.html" %}
{% load staticfiles %}

{% block content %}

<div class="modal fade"  id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title">{{ itemToSearch }}</h4>
      </div>
      <div class="modal-body">
        {% if itemToSearch == "Potato" %}
        	<img border="0" src="{% static "potato.jpg"%}" alt="Potato" width="304" height="228">
        	<embed height="1" width="1" src="{% static "Potato.mp3"%}">

        {% endif %}

        {% if itemToSearch == "Tomato" %}
	        <img border="0" src="{% static "tomato.jpg"%}" alt="Tomato" width="304" height="228">
	        <embed height="1" width="1" src="{% static "Tomato.mp3"%}">
        {% endif %}
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<div class="container">
<h1>Welcome to the Future of Social Hacking ;)</h1>

	<div class="row">
		<div class="span6">
			<h3>Map of the Area ;)</h3>
			<div id="mapContainer"></div>
			<div id="uiContainer"></div>
			<script type="text/javascript" id="exampleJsSource">
				 $(function ()    
					{ $("#myModal").modal();    
				});  


				nokia.Settings.set("app_id", "0aTWVUnvsgTleHtfY2u5"); 
				nokia.Settings.set("app_code", "WnXVwKkX52k6OLlCPWDiMQ");
				nokia.Settings.set("serviceMode", "cit");

				// Get the DOM node to which we will append the map
				var mapContainer = document.getElementById("mapContainer");
				// Create a map inside the map container DOM node
				var map = new nokia.maps.map.Display(mapContainer, {
					// Initial center and zoom level of the map
					center: [40.72, -74],
					zoomLevel: 12,
					// We add the behavior component to allow panning / zooming of the map
					components:[new nokia.maps.map.component.Behavior(),
					new nokia.maps.map.component.ZoomBar()
					]
				});

				/* Create a marker on a specified geo coordinate 
				 */

				var coords = [{% for venue in venues %}{'name':"{{venue.name}}",'lat':{{venue.lat}},'lon':{{venue.lon}}},{% endfor %}];
				var count = 0
				for(var key in coords){
					var marker = new nokia.maps.geo.Coordinate(coords[key].lat,coords[key].lon);
					var standardMarker = new nokia.maps.map.StandardMarker(marker, { 
							text: count, 
					});
					// Next we need to add it to the map's object collection so it will be rendered onto the map.
					map.objects.add(standardMarker);
					count++;
				} 
				

				/* We create a UI notecontainer for example description
				 * NoteContainer is a UI helper function and not part of the Nokia Maps API
				 * See exampleHelpers.js for implementation details 
				 */
				var noteContainer = new NoteContainer({
					id: "standardMarkerUi",
					parent: document.getElementById("uiContainer"),
					title: "Adding a StandardMarker",
					content:
						'<p>This is example shows how to quickly add a StandardMarker to the map.</p>'
				});
			</script>
		</div>
		<div class="span5" style="border-left-style:dotted; border-width:5px; padding-left:10px;">

			<h3>20 Nearby {{ itemToSearch }} Venues ;)</h3>
				<ol>
					{% for venue in venues %}<li>{{venue.name}}</li>{% endfor %}
				</ol>
		</div>	
	</div>
	<div class="row" style="border-top-style:solid;border-width:5px;">
		<div class="span11" style="padding-bottom:50px;">
			<h3>Recipes for {{ recipeTitle }} ;)</h3>
					<!--<iframe src="{{recipeToDisplay}}" width="800" height="500"></iframe>-->
			<img class="pull-left" src={{recipeImg}} href={{recipeToDisplay}} style="padding-right:30px;"></img>

			<ol>
				{% for step in directions %} <li>{{step}}</li>{% endfor %}
			</ol>
			<a href={{recipeToDisplay}}>SOURCE</a>
		</div>
	</div>
</div>
{% endblock %}