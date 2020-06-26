from numpy import *
from pylab import *

coords = [[0.000,0.000],
[0.000,-120.000],
[103.923,-60.000],
[103.923,60.000],
[0.000,120.000],
[207.846,-120.000],
[240.000,0.000],
[207.846,120.000],
[120.000,207.846],
[0.000,240.000],
[354.531,-62.513],
[354.531,62.514],
[311.769,180.000],
[231.403,275.776],
[463.644,-124.233],
[480.000,0.000],
[463.644,124.233],
[415.692,240.000]]

def gaussian_profile(sigma,center_x,center_y,dark=0,readnoise=0,height=40000.):
    """
    Returns a symmetric 2d Gaussian profile, with a sigma in pixels.
    Centered in the middle of a gridsize x gridsize array.
    The height is the value at the peak of the Gaussian.
    """
    x,y = mgrid[0:10,0:10]
    # center_x = (gridsize-1)/2.
    # center_y = (gridsize-1)/2.
    gauss = lambda x,y: height*exp(-(((center_x-x)/sigma)**2+((center_y-y)/sigma)**2)/2)
    return gauss(x,y)

image = np.empty([500,500],dtype='f8')
    
for c in coords:
    new_gaussian = gaussian_profile(2, c[0], c[1])
    # image = np.zeros((500,500),dtype='f8')
    image[c[0]-1:c[0]+1,c[1]-1:c[1]+1] += new_gaussian
    return image
    matplotlib.pyplot.matshow(image)
    show()
    # matplotlib.pyplot.matshow(gaussian_profile(2,c[0],c[1]))
    # show()