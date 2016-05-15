import numpy as np
import json
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import mapq
def con_gps(address):

	Con_key='YvRfEjkHuVoPigHYHQNlxBRvL1Kn2UKb'
#Con_sec = 'dI6pXbJaFu6pmrie'
	mapq.key(Con_key)#,Con_sec)
	gps=mapq.geocode(address)['displayLatLng']
	return float( gps['lat']),float(gps['lng'])

#Origin
address1="Columbus Ave,New York,New York"
address2="503W Seminary Row,New York,New York"

latitude1,longitude1 = con_gps(address1)


#Destination
latitude2,longitude2 = con_gps(address2)

# Calculate Midpoint and Radius
def calc_midpt_radius(latitude1, longitude1, latitude2, longitude2):
    earth_radius = 3959*5280.0
    
    Lat1 = (latitude1)*(np.math.pi/180.0)
    Long1 = (longitude1)*(np.math.pi/180.0)
    Lat2 = (latitude2)*(np.math.pi/180.0)
    Long2 = (longitude2)*(np.math.pi/180.0)
    
    dist = 2.0*earth_radius*np.arcsin(np.sqrt(np.power(np.math.sin((Lat2 - Lat1)/2.0),2.0)+np.math.cos(Lat1)*np.math.cos(Lat2)*np.power(np.math.sin((Long2 - Long1)/2.0),2.0)))
    #dis = np.sqrt((Lat1-Lat2)**2 +(Long1-Long2)**2)
    radius = dist/2.0
    #radius = radius+100.0
    
    mid_lat = (latitude1+latitude2)/2.0
    mid_long = (longitude1+longitude2)/2.0
            
    return mid_lat, mid_long, radius
   # returns center coordinate and radius in ft (plus 100 ft)


# Call Yelp for 24 hour shops
def call_yelp(midlat,midlong,radius):
	auth = Oauth1Authenticator(
    		consumer_key='Qas4yX9C4dXU-rd6ABmPEA',
    		consumer_secret='5Rtb9Gm5KuwRHSevprdb450E37M',
    		token='xBq8GLMxtSbffTWPPXx7au7EUd2ed3MO',
    		token_secret='Nee0b14NkDO9uSX5cVsS7c4j6GQ'
	)
	print radius
	client = Client(auth)

	params = {
        	'term':'24 hour',
        	'sort':'0',
       		'radius_filter': str(radius) # 3 mi radius
	}

	#ex: response = client.search_by_coordinates(40.758895,-73.985131, **params)
	response = client.search_by_coordinates(float(midlat),float(midlong), **params)

	f = open('output_yelp.txt','w+')

	for i in range(0,len(response.businesses)):
        	#f.write(response.businesses[i].name)
        	#f.write(",")
       	 	f.write('%f' % response.businesses[i].location.coordinate.latitude)
        	f.write(",")
        	f.write('%f' % response.businesses[i].location.coordinate.longitude)
        	f.write("\n")
	f.close()
midlat,midlong,r = calc_midpt_radius(latitude1, longitude1, latitude2, longitude2)
call_yelp(midlat,midlong,r)

