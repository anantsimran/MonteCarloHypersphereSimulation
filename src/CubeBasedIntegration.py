from collections import deque
import timeit
from helper import *

def generateNewPoints(point, k, delta):
	points = []
	for i in range(len(point)):
		newPoint = list(point)
		if newPoint[i] < (1 - (delta / 2)):
			newPoint[i] = newPoint[i] + delta
			points.append(newPoint)
	return points


def getAllPoints(point, startDim, delta, npPoints):
	dim = len(point)
	newPoint1 = point[:]
	newPoint1[startDim] = newPoint1[startDim] + (delta / 2)
	newPoint2 = point[:]
	newPoint2[startDim] = newPoint2[startDim] - (delta / 2)
	if (startDim == dim - 1):
		npPoints.append(newPoint1)
		npPoints.append(newPoint2)
		return
	getAllPoints(newPoint1, startDim + 1, delta, npPoints)
	getAllPoints(newPoint2, startDim + 1, delta, npPoints)


def checkStatusOfPoint(point, delta):
	npPoints = []
	getAllPoints(point, 0, delta, npPoints)
	npPoints = np.asarray(npPoints)
	npSum = np.count_nonzero(np.sum(np.multiply(npPoints, npPoints), axis=1) <= 1)
	if (npSum == 0):
		return 0
	if (npSum < len(npPoints)):
		return 1
	return 2


def checkAndInsert(point, pointSet):
	pointStr = ",".join([str(x) for x in point])
	if pointStr in pointSet:
		return False
	pointSet.add(pointStr)
	return True


def dfs(point, pointSet, trackList, k, delta, endTime):
	stack = deque()
	stack.append(point)
	while len(stack) > 0:
		point = stack[-1]
		stack.pop()
		if (timeit.default_timer() > endTime):
			raise SystemError("Time got over")
		status = checkStatusOfPoint(point, delta)
		trackList[status] = trackList[status] + 1
		for neighour in generateNewPoints(point, k, delta):
			if (checkAndInsert(neighour, pointSet) == False):
				continue
			stack.append(neighour)

"""
Input : 
k : the number of segments to break the cube
dim: Number of dimensions to run the code
endTime: System periodically checks if current time is greater than endTime. If yes, raises an exception.

returns mean, precision for a particular k
"""
def getPi(k, dim, endTime):
    pointSet = set()
    trackList = [0]*3
    delta = 2/float(k)
    point = [-1+delta/2]*dim
    checkAndInsert(point,pointSet)
    dfs(point,pointSet,trackList,k,delta,endTime)
    cubeVolume = (2/k)**dim
    vInside = trackList[2]*cubeVolume
    vPartial = vInside+ trackList[1]*cubeVolume
    mean = (vPartial+vInside)/2
    precision = (vPartial-vInside)/mean
    return mean, precision


"""
Input :
dim: the number of dimensions to run on
acc: required accuracy.
maxSeconds: Maximum time to run the simulation ( in seconds)

Starts from k=2 and doubles k at each iteration until we reach desired accuracy or simulation is not able to run in specified time. 

"""
def getPi(dim, precision, maxSeconds):
    k =2
    currentPrecision =1000
    while(currentPrecision>precision):
        try:
            endTime = timeit.default_timer()+maxSeconds
            mean, currentAcc = getPi(k, dim, endTime)
            print(k, dim, mean, currentPrecision)
            k=k*2
        except Exception:
            return k,mean,currentPrecision
    return k, mean, currentPrecision
