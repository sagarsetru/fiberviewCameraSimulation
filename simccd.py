#/usr/bin/env python
"""
Framework for generating simulated CCD output.

Generates images with points distributed in Gaussian profiles, with errors
like those expected from the FLI PL50100 dark current and read noise.

Example:
    simCCD = SimCCD(Ndim=(1000,1000))
    simCCD(100,layout='xygrid')
    simCCD.save('xy_simulation.fits')
    simCCD(50,layout='random')
    simCCD.save('random_simulation.fits')
"""

import numpy as np

# NOTE: scipy.ndimage and scipy.signal may have some useful tools.
# NOTE: for testing purposes, pylab.imshow could be useful.

def gaussian_profile(sigma,gridsize=11,dark=0,readnoise=0):
    """
    Returns a symmetric 2d Gaussian profile, with a sigma in pixels.
    Centered in the middle of a gridsize x gridsize.
    """
    grid = np.zeros((gridsize,gridsize),dtype='f8')
    return grid
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
        self.image = np.empty(Ndim,dtype='f8')
    #...
    
    def save(self,filename):
        """Save the current image to a .fits file named filename."""
    #...
#...
