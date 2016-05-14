import numpy as np
import time
'''
file = open('./NYPD_7_Major_Felony_Incidents.csv','r')
#file = open('./crime_gps.txt','r')
#t = time.time()
cl = open("./coord.txt",'a')
for idx,line in enumerate(file):
	
	#print line
	if idx >= 100000:
	#if idx >=1:
	#print idx
		idx = line.find('"(')
		idx2=line.find(')"')
	#print line
		#print idx
		#print idx2
		#print line
		cl.write(line[idx+2:idx2]+"\n") ##Initial loading of fixed data from NYC crime dataset
		
		#break
	
	#idx1 = line.find("               ")
	#idx2=line.find("\n")
	#print line[idx+15:idx2]
	#cl.write(line[idx+15:idx2])
	#break

cl.close()
file.close()
'''
'''
file = open('./crime_gps.txt','r')
#t = time.time()
cl = open("./coord.txt",'a')
#print "A"
for idx,line in enumerate(file):
	#print line
	s=line.find("               ")
	print line[s+15:line.find("\n")]	
	cl.write(line[s+15:line.find("\n")-1]+"\n")
	
print idx
file.close()
cl.close()
file = open('./nlines.txt','w')
file.write(str(idx))
file.close()
'''
'''
file2 = open('./nlines.txt','w')
file = open('./crime_gps.txt','r')
file2.write(str(len(file.readlines())))
file2.close()
file.close()
#file.close()
#cl.close()
'''


file1=open("./nlines.txt",'r')
file2=open("./crime_gps.txt",'r')
cl=open("./coord.txt",'a')
t= int(file1.readlines()[0])
print t
v = len(file2.readlines())
print v
#file1.close()
#file2.close()

#file1.close()
file1.close()
file1=open("./nlines.txt",'w')
#cl1=open("./coord.txt",'a')
for ind,line in enumerate(file2):
	if ind<v and ind>=t :
		
		#file1.write(line)		
		a = line.find("               ")
	        b=line.find("\n")
		cl.write(line[a+15:b-1]+"\n")

#file.close()
file2.close()
cl.close()
#file1=open("./nlines.txt",'w')
file1.write(str(v))
file1.close()

#print time.time()-t



#print L.shape()
