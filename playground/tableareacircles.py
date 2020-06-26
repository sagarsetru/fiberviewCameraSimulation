# Creates a table of areas for circles with integer radii
import math
for x in range(1,11):
	print 'Radius: {0:2}   Area: {1:3}'.format(x, math.pi*x**2)