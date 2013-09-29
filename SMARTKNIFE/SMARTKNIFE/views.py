from django.shortcuts						import render_to_response
from django.http							import HttpResponseRedirect
from django.contrib.auth.models				import User
from django.contrib.auth					import authenticate, login
from django.template.loader					import get_template
from django.template						import Context
from django.template						import RequestContext


import foursquare

#Define Global Parameters
clientID 		= '1RRP5FHPMPWLXO5CHEUABYGERS23HKQSQ4PDIKCO0TEODB44'
clientSecret 	= '14W01MTLD5W1XKDT3P1ZRF2WVPWRNWBIUQYSZMUB0IYK2L1O'


def homepage_view(request):
	sitename = 'OpenEdit'
	
	'''Foursquare Fun'''
	#construct the client object
	client = foursquare.Foursquare(
		client_id=clientID, 
		client_secret=clientSecret)

	#Search for venue
	results = client.venues.search(params={'query': 'grocery store', 'll':'40.7317, -73.9885'})

	venue_name	= []
	venue_lat	= []
	venue_lon	= []
	for items in results['venues']:
		if items['name']=="Grocery Store" or items['name']=='Grocery store' or items['name']=='Grocery store!!':
			continue
		venue_name.append(items['name'])
		venue_lat.append(items['location']['lat'])
		venue_lon.append(items['location']['lng'])



	context = {'sitename':sitename, 'names': venue_name} #render with vars
	return render_to_response('homepage.html', context, context_instance=RequestContext(request))


