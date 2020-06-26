# Creates two tables of squares and cubes of numbers 1-10
for x in range(1,11):
	print str(x).rjust(2), str(x*x).rjust(3), str(x*x*x).rjust(4)

for x in range(1,11):
	print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)