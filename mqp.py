import mapq
import csv
import json
import numpy as np
import re
#mapq.key
Con_key='YvRfEjkHuVoPigHYHQNlxBRvL1Kn2UKb'
#Con_sec = 'dI6pXbJaFu6pmrie'
mapq.key(Con_key)#,Con_sec)
#mapq.secret(Con_sec)
def togps(numlines):
	cl = open('mess_clean4.txt','r')
	fl = open('crime_gps.txt','a')
	lines = cl.readlines()
	count=-1

#print lines
	for line in lines[numlines:len(lines)]:
		count+=1
		dummy=[]
		#print line
		if ('N/A' in line):
			pass
		else:
			for m in re.finditer("              ",line):
				t=m.end()+1
		#print t
		
			address= line[t:-2]
#			print address

				
			
			gps=mapq.geocode(address+",New York")['displayLatLng']
			gpx=str(gps['lat'])#.split()
			gpy=str(gps['lng'])#.split()
#			print gpx
#			print gpy
			#for o in range(t,len(lines)):
			dummy.append( line[0:t])
#		print dummy
			#for j in range(len(gpx)):
			dummy.append(gpx)
			#print line[t+j],"  ",gpx[j]
			#print dummy
			dummy.append(',')
			#for k in range(len(gpy)):
			dummy.append(gpy)
#			print dummy
			dummy.append('\r')
			dummy.append('\n')
#			print dummy
			#lines[count]=(dummy)
			#print len(''.join(dummy))
			
			if (len(''.join(dummy))>70):
				pass
			else:
			#lines[count]=line
#			print lines[count]
				fl.write(''.join(dummy))
		
		
		
		
	fl.close()

#togps(numlines)	

''' 
address= "LEFFERTS BOULEVARD, NEW YORK"

#a=mapq.batch('40.811015, -73.958767','40.799813,  -73.962447')#, 'Yerba Buena Park')
#[{'multiple': 'locations'}, ...]011
gps=mapq.geocode(address)['displayLatLng']
print( gps['lat'],gps['lng'])

'''
#json_obj = json.load(a)
#import json
#with open('result.json','w') as fp:
#	json.dump(a,fp)

#for i in a:
#	for j in i['providedLocation']:
#   		print j[0:2000]

#print mapq.latlng('503W 122nd street, New York City, NY,10027')
