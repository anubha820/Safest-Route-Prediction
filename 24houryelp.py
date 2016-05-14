import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
    consumer_key='Qas4yX9C4dXU-rd6ABmPEA',
    consumer_secret='5Rtb9Gm5KuwRHSevprdb450E37M',
    token='xBq8GLMxtSbffTWPPXx7au7EUd2ed3MO',
    token_secret='Nee0b14NkDO9uSX5cVsS7c4j6GQ'
)

client = Client(auth)

params = {
	'term':'stores open 24 hours',
	'sort':'2',
	'radius_filter':'4828.03' # 3 mi radius
}

#response = client.search_by_coordinates(40.758895,-73.985131, **params)
response = client.search_by_coordinates(lat_input,long_input,**params)

#response = client.search('stores open 24 hours')

response.businesses

f = open('output_yelp.txt','w+')

for i in range(0,len(response.businesses)):
	f.write(response.businesses[i].name)
	f.write(",")
	f.write('%d' % response.businesses[i].location.coordinate.latitude)
	f.write(",")
	f.write('%d' % response.businesses[i].location.coordinate.longitude)
	f.write("\n")
