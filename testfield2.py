"""
Generate four example plots with 2d gaussians at the currently accepted
positions of the 'residual' fibers.

For testing the simCCD code.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#import simCCD

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

def gaussian_profile(sigma,center_x,center_y,dark=0,readnoise=0,height=40000.,xygrid=None):
    """
    Returns a symmetric 2d Gaussian profile, with a sigma in pixels.
    Centered in the middle of a gridsize x gridsize array.
    The height is the value at the peak of the Gaussian.
    """
    if xygrid is None:
        x,y = np.mgrid[0:20,0:20]
    else:
        x,y = xygrid
    gauss = lambda x,y: height*np.exp(-(((center_x-x)/sigma)**2+((center_y-y)/sigma)**2)/2)
    return gauss(x,y)
#...

Nx = 1000
Ny = 1000
image = np.empty([Nx,Ny],dtype=np.float64)
x,y = np.mgrid[0:Nx,0:Ny]
x -= Nx/2
y -= Ny/2
xygrid = x,y

for c in coords:
    image += gaussian_profile(2, c[0], c[1],xygrid=xygrid)

# The CCD output will be 16 bit unsigned integers.
int_image = np.empty(image.shape,dtype=np.uint16)
np.round(image,out=int_image)

plt.matshow(image,cmap=cm.gist_ncar)
plt.title('float image, linear scaling')
plt.matshow(np.log10(image),cmap=cm.gist_ncar)
plt.title('float image, log10 scaling')
plt.matshow(int_image,cmap=cm.gist_ncar)
plt.title('int image, linear scaling')
plt.matshow(np.log10(int_image),cmap=cm.gist_ncar)
plt.title('int image, log10 scaling')
plt.show()
