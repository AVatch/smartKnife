from django.shortcuts						import render_to_response
from django.http							import HttpResponseRedirect
from django.contrib.auth.models				import User
from django.contrib.auth					import authenticate, login
from django.template.loader					import get_template
from django.template						import Context
from django.template						import RequestContext
from django.utils 							import simplejson


import foursquare

import urllib2 as recipeUrl
import urllib
import sys
import webbrowser
import random as rand

#Define Global Parameters - Foursquare
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

	venues = []
	for items in results['venues']:
		if items['name']=="Grocery Store" or items['name']=='Grocery store' or items['name']=='Grocery store!!':
			continue
		new_venue = {}
		new_venue['name'] = items['name']
		new_venue['lat']  = items['location']['lat']
		new_venue['lon']  = items['location']['lng']
		venues.append(new_venue)

	#js_data = simplejson.dumps(my_dict)

	'''Pull recipes from Allrecipes.com'''
	urlAddr = 'http://allrecipes.com/'
	#REQUEST RECIPES FOR
	veggie = 'apples'

	req = recipeUrl.Request('http://allrecipes.com/search/default.aspx?qt=k&wt=' + veggie + '&rt=r&origin=Home%20Page')
	f = recipeUrl.urlopen(req)
	    
	search =  f.read()
	href = []

	for word in search.split(" "):
	    if word.startswith('href="/Recipe/'):
	        href.append(word)

	for i in range(len(href)):
	    href[i] = 'http://allrecipes.com'+href[i][6:]

	randNumber = rand.randint(1, len(href))
	recipeToDisplay = href[randNumber]

	'''Nokia Maps Fun'''
	#See embedded js in homepage.html

	print venues

	context = {'sitename':sitename, 'recipeToDisplay':recipeToDisplay, 'venues': venues} #render with vars
	return render_to_response('homepage.html', context, context_instance=RequestContext(request))


