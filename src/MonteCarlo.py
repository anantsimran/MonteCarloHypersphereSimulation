import timeit
from helper import *


def getPiPrecisionNaive(dim, precision, batchSize=15, maxBatches=10000):
	print("Dimension:" + str(dim))
	n = 5000000
	currentPrecision = 100
	dist = np.zeros((0))
	batchNumber = 1
	v = 2 ** dim
	meanArr = []
	precisionArr = []
	timeElapse = []
	start_time = timeit.default_timer()
	while currentPrecision > precision and batchNumber < maxBatches:
		points = getPoints((batchSize, n, dim))
		points = (np.count_nonzero(np.sum(np.multiply(points, points), axis=2) <= 1.0, axis=1)) * (v / n)
		dist = np.hstack((dist, points))
		currentMean, currentAcc = clt(dist)
		elapsed = timeit.default_timer() - start_time
		batchNumber = batchNumber + 1
		meanArr.append(currentMean)
		precisionArr.append(currentAcc)
		timeElapse.append(elapsed)
	return meanArr, precisionArr, timeElapse

def getPiSingleIteration(n, dim, m=50):
    k  = n/m
    dist = np.zeros(m)
    cubeVolume = 2**dim
    for i in range(m):
        points = getPoints((int(k),dim))
        s = np.count_nonzero(np.sum( np.multiply(points,points), axis =1)<=1.0)
        dist[i]= s*cubeVolume/k
    return clt(dist)


def getPiAntitheticVar(n, dim, m=50):
    k  = n/m
    dist = np.zeros(m)
    cubeVolume = 1.0
    for i in range(m):
        points = getPoints(low=0.0,high=1.0,shape= (int(k),dim))
        s = np.count_nonzero(np.sum( np.multiply(points,points), axis =1)<=1.0)
        dist[i]= s*cubeVolume/k
    dist = np.hstack((dist, dist))
    dist = np.hstack((dist, dist))
    return clt(dist)