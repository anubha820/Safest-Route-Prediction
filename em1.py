import imaplib
import numpy
import email
import re
import os
from sys import argv
from mqp import togps
crimes = ["Robbery","Theft","Assault","Other","Arrest","Vandalism","Shooting","Burglary","Arson"]
space=["                 ","   ","  "]
cl4 = open('mess_clean4.txt','r')
#target =open('mess_clean1.txt','a')
#cla = open('numlines.txt','w')
lines= cl4.readlines()
numlines=len(lines)
cl4.close()
cl4 = open('mess_clean4.txt','a')
####
#cl3 = open('mess_clean3.txt','a')
M = imaplib.IMAP4_SSL('imap.gmail.com',993)
M.login('abgtm2122@gmail.com','gtmab2122')
M.select()
cl5= open('mailnum.txt','r')
start = cl5.read()
print start
cl5.close()
typ,data = M.uid('search',None,'ALL')
#cl5= open('mailnum.txt','w')
#print data[0].split()[-1]



for num in (start,data[0].split()[-1]):
	idx_crime=[]
	
	t,d = M.fetch(num,'(RFC822)')
	if(d[0] == None):
		pass
	else:
		mess = email.message_from_string(d[0][1])
		if mess['From'] == '"spotcrime.com" <system@spotcrime.com>' :
			print num
			#print str(mess['Link'])
			p = str(mess)
			cl2.write(p)
			#print len(str(mess))
			idx_copy = p.find("Address: Columbia University,=")
			#print idx_copy
			idx_stop = p.find("unsubscribe")
			print idx_stop
			idx=0	
			p = p[idx_copy+30+25+51+74+73+1:idx_stop-130]
			for j in crimes:
				for i in re.finditer(j,p):
					idx_crime.append(i.start())
			idx_crime=numpy.sort(idx_crime)
			#print idx_crime
			for i in range(len(idx_crime)-1):
				inter_str = (p[idx_crime[i]:idx_crime[i+1]-1])
				#print inter_str
				
			
				inter_str=inter_str.replace('=','')
				inter_str=inter_str.replace('\r','')
				inter_str=inter_str.replace('\n','')
				idx_http = inter_str.find("http") -10
				inter_str=inter_str[0:idx_http]
				#print idx_http
				ptest=list(inter_str)
				#for j in space:
				#	for i in re.finditer(j,inter_str):
				#		count = 0
				#		for t in range(i.start(),i.end()):
							#ptest=list(inter_str)
				#			ptest[t]=''
				#			count+=1
						#ptest[i.end()-count]=','
				#ptest=ptest.replace(',','')
				#print ptest
				ptest=''.join(ptest)
				#ptest=ptest.replace(',','')
				print ptest
				idx_http = inter_str.find("http") -10
				
				
					
				cl4.write(ptest[0:idx_http])
				cl4.write('\r'+'\n')
cl5=open('mailnum.txt','w')	
cl5.write(data[0].split()[-1])
togps(numlines)
cl5.close()
cl4.close()
#cl4=open('mess_clean4.txt','r')




'''
for line in cl4:
	k,v=line.strip().split('=')
	ans[k.strip()]=v.strip()
cl5 = open('mess_clean5.txt','a')
cl5.write(ans)
cl5.close()
'''	
'''										
cl4.close()	
os.remove("mess_clean2.txt")							
			

t,d = M.fetch(5,'(RFC822)')
print t
mess=email.message_from_string(d[0][1])
print mess
print mess['From']
#print email.utils.parseaddr(mess['To'])
#print mess.items()
'''
M.close()
M.logout()



