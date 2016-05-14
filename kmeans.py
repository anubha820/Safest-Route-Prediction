from pyspark.mllib.clustering import KMeans, KMeansModel
from numpy import array
from math import sqrt
from pyspark import SparkContext
import numpy as np
#conf = SparkConf()
sc = SparkContext()

# Load and parse the data
data = sc.textFile("./coord.txt")
parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))
#print type(parsedData.take(2)[0])


#print np.shape(parsedData)
# Build the model (cluster the data)

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
	center = clusters.centers[clusters.predict(point)]
	#print center
	return sqrt(sum([x**2 for x in (point - center)]))
#WSSE = parsedData.map(lambda point:error(point)).reduce(lambda x,y:x+y)
WSSE=np.zeros(5)
import time
for i in range(2,7):
	t = time.time()
	clusters = KMeans.train(parsedData, i, maxIterations=100,
        	runs=100, initializationMode="random")
	WSSE[i] = (parsedData.map(lambda point:error(point)).reduce(lambda x,y :x+y))
	print str(WSSE[i])+"   "+str(i)+"   WITH TIME ="+str(time.time()-t)

#WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
#print("Within Set Sum of Squared Error = " + str(WSSSE))



# Save and load model
clusters.save(sc, "./mymodel1")
sameModel = KMeansModel.load(sc, "./mymodel1")

#print clusters

