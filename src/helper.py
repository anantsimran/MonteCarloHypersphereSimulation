import numpy as np;

# For 95% of confidence interval
def clt(dist):
    x= np.mean(dist)
    return x, (2 * np.sqrt(np.var(dist) / dist.shape[0]))/x


def getPoints(shape, low=-1.0, high=1.0):
    return np.random.uniform(low=low,high = high,size=shape)

