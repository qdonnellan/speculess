import math

def leftRiemann(f, partitions, a, b):
	delta_x = (1.*b-a)/partitions
	sumArea = 0
	for i in range(partitions):
		xVal = a+i*delta_x
		sumArea += f(xVal)*delta_x
	return sumArea
		

def rightRiemann(f, partitions, a, b):
	delta_x = (1.*b-a)/partitions
	sumArea = 0
	for i in range(partitions):
		xVal = a+(i+1)*delta_x
		sumArea += f(xVal)*delta_x
	return sumArea

def midpointRiemann(f, partitions, a, b):
	delta_x = (1.*b-a)/partitions
	sumArea = 0
	for i in range(partitions):
		xVal = a+(delta_x+i)/2
		sumArea += f(xVal)*delta_x
	return sumArea

def trapezoid(f, partitions, a,b):
	leftR = leftRiemann(f, partitions, a, b)
	rightR = rightRiemann(f, partitions, a, b)
	return (leftR+rightR)/2.

		
print midpointRiemann(math.exp, 2, 1, 2)

# testing commit in ubuntu (hg)