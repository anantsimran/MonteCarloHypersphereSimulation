"""

Configuration for running the below written program.

maxNConteCarlo: Set this to the maximum dimension you want to run monteCarlo Simulations in.
For higher dim, the program will take a lot of time to complete for a specified accuracy even though it will eventually terminate.

cubeIntegrationMaxSeconds: Maximum time that the cube based iteration can take .

maxDimFixedPoints:If you fix your points at 10^6, what is the maximum dim you want to work on in Cube Based Integration.
"""
class config():
    maxNConteCarlo= 8
    cubeIntegrationMaxSeconds = 200
    maxDimFixedPoints=8