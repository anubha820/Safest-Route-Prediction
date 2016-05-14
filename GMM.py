'''
Copyright 2016 
Owner- Gabriel Maliakal and Anubha Bhargava

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

from pyspark.mllib.clustering import GaussianMixture
from numpy import array
from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np
#plt.figure()


sc=SparkContext()

data=sc.textFile("./coord.txt")
#test_plot=np.genfromtxt("./coord.txt",delimiter=',',dtype=float)
#plt.plot(test_plot[:,1],test_plot[:,0],'ro')
#plt.show()
parsedData=data.map(lambda line: array([float(x) for x in line.strip().split(',')]))
l=3
gmm = GaussianMixture.train(parsedData,l)
#x=np.zeros(90000)
#y=np.zeros(90000)

#for i in range(0,l):
	#print "w= ",gmm.weights[i]
	#print "sigma= ",gmm.gaussians[i].sigma.toArray()
	#print "mu= ",gmm.gaussians[i].mu
	
#x1=gmm.weights[0]*np.random.multivariate_normal(gmm.gaussians[0].mu,gmm.gaussians[0].sigma.toArray(),90000)
#x2=gmm.weights[1]*np.random.multivariate_normal(gmm.gaussians[1].mu,gmm.gaussians[1].sigma.toArray(),90000)		


file  = open("./GMM.txt",'w')
for j in range(0,l):
	file.write(str(gmm.weights[j])+'\n')
#file.write(str(gmm.weights[1])+'\n')
#file.write(str(gmm.weights[2])+'\n')
	file.write(str(gmm.gaussians[j].mu)+'\n')
#file.write(str(gmm.gaussians[1].mu)+'\n')
#file.write(str(gmm.gaussians[2].mu)+'\n')
	file.write(str(gmm.gaussians[j].sigma.toArray())+'\n')
#file.write(str(gmm.gaussians[1].sigma.toArray())+'\n')
#file.write(str(gmm.gaussians[2].sigma.toArray())+'\n')
file.close()
#file = open("./GMM.txt",'r')

#file.close()
#x1=0.999759846136*np.random.multivariate_normal([40.732356207,-73.9230488499],[[ 0.00637296, 0.00164258],
# [ 0.00164258,  0.00591468]],90000)
#x2=0.00024015386415*np.random.multivariate_normal([41.7766202465,-75.5844575718],[[ 7.9309655,2.49651266],
# [ 2.49651266,  6.97280617]],90000)

#X=x1+x2

#plt.figure()
#plt.plot(X[:,1],X[:,0],'ro')
#plt.show()	
