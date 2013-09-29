import foursquare

#Define Global Parameters
clientID 		= '1RRP5FHPMPWLXO5CHEUABYGERS23HKQSQ4PDIKCO0TEODB44'
clientSecret 	= '14W01MTLD5W1XKDT3P1ZRF2WVPWRNWBIUQYSZMUB0IYK2L1O'


def main():
	#construct the client object
	client = foursquare.Foursquare(
		client_id=clientID, 
		client_secret=clientSecret)

	#Search for venue
	results = client.venues.search(params={'query': 'grocery store', 'll':'40.7317, -73.9885'})

	for key in results:
		print key

	count = 0
	venue_name	= []
	venue_lat	= []
	venue_lon	= []
	for items in results['venues']:
		venue_name.append(items['name'])
		venue_lat.append(items['location']['lat'])
		venue_lon.append(items['location']['lng'])

		count +=1

	for i in range(len(venue_name)):
		print venue_name[i]+"\t"+str(venue_lat[i])+":"+str(venue_lon[i])

if __name__=="__main__":
	main()