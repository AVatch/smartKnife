from django.shortcuts						import render_to_response
from django.http							import HttpResponseRedirect
from django.contrib.auth.models				import User
from django.contrib.auth					import authenticate, login
from django.template.loader					import get_template
from django.template						import Context
from django.template						import RequestContext
from django.utils 							import simplejson
from django.core.urlresolvers import reverse
from settings import KEYS


import foursquare

from twilio.rest import TwilioRestClient


import urllib2 as recipeUrl
import urllib
import sys
import webbrowser
import random as rand
import re as patt



#Define Global Parameters - Foursquare
try:
	clientID = KEYS['foursquare_clientSecret'] 
except:
	clientID = ""
try:
	clientSecret = KEYS['foursquare_clientID'] 
except:
	clientSecret = ""

#itemToSearch = 'Potato'


def choose_page(request):
	#potato_url = reverse('result', args=('potato',))
	#potato_url = reverse('result', args=('tomato',))
	return render_to_response('chose.html', 
#{'potato_url':potato_url,'tomato':tomato_url},
	context_instance=RequestContext(request))

def homepage_view(request,itemToSearch=''):
	if len(itemToSearch) <= 0:
		return render_to_response('error.html', context_instance=RequestContext(request))
	'''Foursquare Fun'''
	#construct the client object
	client = foursquare.Foursquare(
		client_id=clientID, 
		client_secret=clientSecret)

	#Search for venue
	results = client.venues.search(params={'query': itemToSearch, 'll':'40.7317, -73.9885'})

	venues = []
	count = 0
	for items in results['venues']:
		if items['name']=="Grocery Store" or items['name']=='Grocery store' or items['name']=='Grocery store!!':
			continue
		if count > 19:
			continue
		new_venue = {}
		new_venue['name'] = items['name']
		new_venue['lat']  = items['location']['lat']
		new_venue['lon']  = items['location']['lng']
		venues.append(new_venue)
		count+=1

	#js_data = simplejson.dumps(my_dict)

	'''Pull recipes from Allrecipes.com'''
	urlAddr = 'http://allrecipes.com/'
	#REQUEST RECIPES FOR
	veggie = itemToSearch

	req = recipeUrl.Request('http://allrecipes.com/search/default.aspx?qt=k&wt=' + veggie + '&rt=r&origin=Home%20Page')
	f = recipeUrl.urlopen(req)
	    
	search =  f.read()
	href = []
	imageUrl = ''
	recipeTitle = ''

	for word in search.split(" "):
	    if word.startswith('href="/Recipe/'):
	        href.append(word)

	for i in range(len(href)):
	    href[i] = 'http://allrecipes.com'+href[i][6:]

	randNumber = rand.randint(1, len(href)-1)
	recipeToDisplay = href[randNumber]

	randRecipeReq = recipeUrl.Request(href[randNumber])
	randRecipe = recipeUrl.urlopen(randRecipeReq)
	content = randRecipe.read()

	recipe = []

	m = patt.findall('plaincharacterwrap break">(.*?)</span>', content)
	imageUrl = patt.search('http://images(.*?).jpg', content)
	recipeTitle = patt.findall('itemprop="name">(.*?)</h1>', content)[0]

	directions = m
	recipeImg = imageUrl.group(0)

	'''Twilio'''
	try:
		account_sid = KEYS['twilio_account_sid'] 
	except:
		account_sid = ""
	try:
		auth_token = KEYS['twilio_auth_token']
	except:
		auth_token = ""

	try:
		nokia_app_id = KEYS['nokia_app_id']
	except:
		nokia_app_id = ""
	try:
		nokia_app_code = KEYS['nokia_app_code']
	except:
		nokia_app_code = ""
	
	print nokia_app_id,nokia_app_code,auth_token,account_sid,clientID,clientSecret
	# UNCOMMENT THE FOLLOWING LINES TO ENABLING TEXTING
	#client = TwilioRestClient(account_sid, auth_token)

	#message = client.messages.create(to="+12673349121", from_="+16314065044",
       #                              body="Hello there! I am chopping "+itemToSearch+"!")
	#message = client.messages.create(to="+13479071371", from_="+16314065044",
      #                               body="Hello there! I am chopping "+itemToSearch+"!")
	#message = client.messages.create(to="+1 917-272-7758", from_="+16314065044",
     #                                body="Hello there! I am chopping "+itemToSearch+"!")

	'''Nokia Maps Fun'''
	#See embedded js in homepage.html
	sitename='derp'
	context = {'sitename':sitename, 'itemToSearch':itemToSearch, 'recipeTitle':recipeTitle, 'recipeToDisplay':recipeToDisplay, 'directions':directions, 'recipeImg':recipeImg, 'venues': venues, 'nokia_app_id':nokia_app_id,'nokia_app_code':nokia_app_code} #render with vars
	return render_to_response('homepage.html', context, context_instance=RequestContext(request))
