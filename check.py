'''
Copyright 2016
Gabriel Maliakal and Anubha Bhargava

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import numpy as np
from midpt_yelp import con_gps,calc_midpt_radius,call_yelp

orig = raw_input("Enter origin")

dest=raw_input("Where do you want to go?")
#orig = "Columbia University,New York,New York"
#dest= "503W Seminary Row,New York,New York"
lat1,long1=con_gps(orig)
#print con_gps(orig)
#print type(lat1),lat1
lat2,long2=con_gps(dest)
#print con_gps(dest)

mid1,mid2,r=calc_midpt_radius(lat1,long1,lat2,long2)
call_yelp(mid1,mid2,r)

s_loc_t=np.genfromtxt("./output_yelp.txt",delimiter=',',dtype=float)
#print np.shape(s_loc_t)

s_loc=np.zeros((np.shape(s_loc_t)[0]+2,np.shape(s_loc_t)[1]))
s_loc[0,0]=lat1
s_loc[0,1]=long1
s_loc[1:-1,:]=s_loc_t[:,:]
s_loc[-1,0]=lat2
s_loc[-1,1]=long2
#print s_loc

w1=0.514089518096
m1=[40.6821198178,-73.9067822519]
s1=[[ 0.00240385,  0.00165191],
  [0.00165191,  0.00682461]]
w2=0.441874893277
m2=[40.8006823558,-73.9344809051]
s2=[[ 0.00273841,  0.00228556],
  [0.00228556,  0.00293018]]
w3=0.0438074704421
m3=[40.6325022119,-73.9990024268]
s3=[[ 0.00418173,  0.00784755],
  [0.00784755,  0.02397979]]
w4=0.000228118184078
m4=[41.8700400046,-75.6002890133]
s4=[[ 7.96344447,  2.14988616],
  [2.14988616,  5.73711207]]

def mvg(w,m,s,x):
	a=1.0/(np.sqrt(((2*np.pi)**2)*np.linalg.det(s)))
	b=x-m
	c = np.dot(np.dot(b.T,np.linalg.inv(s)),b)
	#print np.linalg.det(s)
	#print m
	#print x
	return w*a*np.exp(-0.5*c)

num = np.shape(s_loc)[0]
g=np.zeros(num)
d=np.zeros((num,num))
def dist(Lat1,Long1,Lat2,Long2):
	earth_radius = 3959*5280.0

   	Lat1 = (Lat1)*(np.math.pi/180.0)
    	Long1 = (Long1)*(np.math.pi/180.0)
    	Lat2 = (Lat2)*(np.math.pi/180.0)
    	Long2 = (Long2)*(np.math.pi/180.0)

	return 2.0*earth_radius*np.arcsin(np.sqrt(np.power(np.math.sin((Lat2 - Lat1)/2.0),2.0)+np.math.cos(Lat1)*np.math.cos(Lat2)*np.power(np.math.sin((Long2 - Long1)/2.0),2.0)))		
i=0
idx=[]

for locs in s_loc:
	
	g1 = mvg(w1,m1,s1,locs)
	#print g1
	#break
	g2 = mvg(w2,m2,s2,locs)
	#print g2
	g3 = mvg(w3,m3,s3,locs)
	#print g3
	g4 = mvg(w4,m4,s4,locs)
	#print g4

	g[i]=g1+g2+g3+g4
	for j in range(0,np.shape(s_loc)[0]):
		d[i,j]=dist(locs[0],locs[1],s_loc[j,0],s_loc[j,1])
		if d[i,j]==0:
			d[i,j]=np.nan
	i+=1
	
#print d
i=0
done=[]
count=0
#print g
d_sort = np.argsort(d,axis=1)
#print d_sort

g3=np.zeros((num,3))
for j in range(0,num):
	g3[j,:]=g[d_sort[j,0:3]]



#print d3
#print g3

def checkPath(path_list, dist_list):
	l = np.argsort(dist_list)[0]
	if len(dist_list)==1 and dist_list[0] in path_list:
		return path_list
	else:
		if l in path_list:
			return checkPath(path_list, np.argsort(dist_list)[1:])
		else:
			path_list.append(l)
			return path_list


path=[]

for M in g3:
	path=checkPath(path,M)	
#print path

idx=[]
for m in path:
	for n in range(0,num):
		if g3[m][m] == g[n]:
			idx.append(n)
			break
	


#print s_loc[idx]

res = open("./results.txt",'w')
#res.write(str(lat1)+","+str(long1))

for i in idx:
	res.write(str(s_loc[i,0])+","+str(s_loc[i,1])+"\n")
res.write(str(lat2)+","+str(long2)+"\n")
res.close()
'''




'''
