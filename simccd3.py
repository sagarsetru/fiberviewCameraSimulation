#/usr/bin/env python
"""
this is the framework for generating simulated CCD output.

Generates images with points distributed in Gaussian profiles, with errors
like those expected from the FLI PL50100 dark current and read noise.

Example:
    simCCD = SimCCD(Ndim=(1000,1000))
    simCCD(100,layout='xygrid')
    pylab.matshow(simCCD.image) # plot the array
    simCCD.save('xy_simulation.fits')
    simCCD(50,layout='random')
    simCCD.save('random_simulation.fits')
"""

import numpy as np
from numpy import *
from pylab import *

# NOTE: scipy.ndimage and scipy.signal may have some useful tools.
# NOTE: for testing purposes, pylab.matshow could be useful.

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
#...

class SimCCD:
    """Generate a simulated CCD image."""
    def __init__(self,Ndim=(512,512),dark=0,readnoise=0):
        """
        Ndim a tuple of the dimensions of the resulting image.
        """
        self.Ndim = Ndim
        self.dark = dark
        self.readnoise = readnoise
    #...

    def __call__(self,Npoints,layout='xygrid'):
        """
        Generates an image with Npoints distributed by layout.
        Valid options for layout are:
            xygrid
            random
            ???
        """
        # determine spacing between points
        # 1. how many points along each dimension (Ndim[0],Ndim[1])
        # 2. compute coordinates of each point
        image = np.empty([500,500],dtype='f8')
        # image = np.zeros((500,500),dtype='f8')
        self.image = image
        # layout == 'xygrid'
        if layout == 'xygrid':
            coords = 
                [[0.000,125.000],
                [0.000,5.000],
                [103.923,65.000],
                [103.923,185.000],
                [0.000,245.000],
                [207.846,5.000],
                [240.000,125.000],
                [207.846,245.000],
                [120.000,332.846],
                [0.000,365.000],
                [354.531,62.487],
                [354.531,187.514],
                [311.769,305.000],
                [231.403,400.776],
                [463.644,0.767],
                [480.000,125.000],
                [463.644,249.233],
                [415.692,365.000]]

            for c in coords:
                new_gaussian = gaussian_profile(2, c[0], c[1])
                
                # center_x=c[1]
                # center_y=c[2]
                
                # c is the center of this Gaussian
                # generate Gaussian centered at this location
                # Add values of resulting Gaussian to the image
                # look up numpy slicing
                image[[c[0]-1:c[0]+1,c[1]-1:c[1]+1] += new_gaussian
                #c[0]-1:c[0]+1 is to reflect dimensions of gaussian
                matplotlib.pyplot.matshow(image)
                show()
        else:
            raise ValueError("I don't understand this layout: "+layout)
        # self.image = image
    def show_output

        
    #...
    
    def save(self,filename):
        """Save the current image to a .fits file named filename."""
    #...
#...
