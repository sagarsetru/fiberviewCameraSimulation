#/usr/bin/env python
"""
this is the framework for generating simulated CCD output.

Generates images with points distributed in Gaussian profiles, with errors
like those expected from the FLI PL50100 dark current and read noise.

Example:
    simCCD = SimCCD(Ndim=(1000,1000))
    simCCD(100,layout='xygrid')
    pylab.mashow(simCCD.image) # plot the array
    simCCD.save('xy_simulation.fits')
    simCCD(50,layout='random')
    simCCD.save('random_simulation.fits')
"""

import numpy as np
from numpy import *
from pylab import *

# NOTE: scipy.ndimage and scipy.signal may have some useful tools.
# NOTE: for testing purposes, pylab.matshow could be useful.

def gaussian_profile(sigma,gridsize=20,dark=0,readnoise=0,height=40000.):
    """
    Returns a symmetric 2d Gaussian profile, with a sigma in pixels.
    Centered in the middle of a gridsize x gridsize array.
    The height is the value at the peak of the Gaussian.
    """
    x,y = mgrid[0:gridsize,0:gridsize]
    center_x = (gridsize-1)/2.
    center_y = (gridsize-1)/2.
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
        image = np.empty(Ndim,dtype='f8')
        if layout == 'xygrid':
            # determine spacing between points
            # 1. how many points along each dimension (Ndim[0],Ndim[1])
            # 2. compute coordinates of each point
            coords = ???
            for c in coords:
                # c is the center of this Gaussian
                # generate Gaussian centered at this location
                # Add values of resulting Gaussian to the image
                # look up numpy slicing
                image[xrange,yrange] += new_gaussian
        else:
            raise ValueError("I don't understand this layout: "+layout)
        self.image = image
    #...
    
    def save(self,filename):
        """Save the current image to a .fits file named filename."""
    #...
#...
