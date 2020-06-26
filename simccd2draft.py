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

# import numpy as np
# from numpy import *
# from pylab import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# NOTE: scipy.ndimage and scipy.signal may have some useful tools.
# NOTE: for testing purposes, pylab.matshow could be useful.

class Gaussian:

    """Class to make single Gaussian Profile"""
    
    # def __init__(self,sigma,center_x,center_y,dark=0,readnoise=0,height=40000):
    def __init__(self,sigma,height=40000):
        self.sigma = sigma
        # self.center_x = center_x
        # self.center_y = center_y
        # self.dark = dark
        # self.readnoise = readnoise
        # self.height = height
        
    def __call__(self,center_x,center_y):
        # coords = [[0.000,0.000],
                 # [0.000,-120.000],
                 # [103.923,-60.000],
                 # [103.923,60.000],
                 # [0.000,120.000],
                 # [207.846,-120.000],
                 # [240.000,0.000],
                 # [207.846,120.000],
                 # [120.000,207.846],
                 # [0.000,240.000],
                 # [354.531,-62.513],
                 # [354.531,62.514],
                 # [311.769,180.000],
                 # [231.403,275.776],
                 # [463.644,-124.233],
                 # [480.000,0.000],
                 # [463.644,124.233],
                 # [415.692,240.000]]
        # for c in coords,
            # self.center_x = c[0]
            # self.center_y = c[1]
        # return self.center_x
        # return self.center_y
        
        def gaussian_profile(self,sigma,center_x,center_y,dark=0,readnoise=0,height=40000.,xygrid=None):
            """
            Returns a symmetric 2d Gaussian profile, with a sigma in pixels.
            Centered in the middle of a gridsize x gridsize array.
            The height is the value at the peak of the Gaussian.
            """
            if xygrid is None:
                x,y = np.mgrid[0:20,0:20]
            else:
                x,y = xygrid
            gauss = lambda x,y: height*np.exp(-(((self.center_x-x)/self.sigma)**2+((self.center_y-y)/self.sigma)**2)/2)
            return gauss(x,y)
#...
        
    # def gaussian_profile(self):
        # """
        # Returns a symmetric 2d Gaussian profile, with a sigma in pixels.
        # The height is the value at the peak of the Gaussian.
        # """
        # x,y = mgrid[0:10,0:10]
        # center_x = (gridsize-1)/2.
        # center_y = (gridsize-1)/2.
        # gauss = lambda x,y: height*exp(-(((center_x-x)/sigma)**2+((center_y-y)/sigma)**2)/2)
        # return gauss(x,y)

#...

class SimCCD:
    """Generate a simulated CCD image."""
    # def __init__(self,Ndim=(512,512),dark=0,readnoise=0):
    # def __init__(self,Nx,Ny,dark=0,readnoise=0):
    def __init__(self,dark=0,readnoise=0):
        """
        Ndim a tuple of the dimensions of the resulting image.
        """
        # self.Nx = Nx
        # self.Ny = Ny
        self.dark = dark
        self.readnoise = readnoise
    #...
    

    def __call__(self,Nx,Ny,layout='Baltay_default'):
        """
        Generates an image with Npoints distributed by layout.
        Valid options for layout are:
            xygrid
            random
            ???
        """
        # coords = [[0.000,0.000],
         # [0.000,-120.000],
         # [103.923,-60.000],
         # [103.923,60.000],
         # [0.000,120.000],
         # [207.846,-120.000],
         # [240.000,0.000],
         # [207.846,120.000],
         # [120.000,207.846],
         # [0.000,240.000],
         # [354.531,-62.513],
         # [354.531,62.514],
         # [311.769,180.000],
         # [231.403,275.776],
         # [463.644,-124.233],
         # [480.000,0.000],
         # [463.644,124.233],
         # [415.692,240.000]]
         
        def make_gaussian(t):
            # for c in coords:
            t = Gaussian(2)
            return t
            
        def add_gaussian(a, b):
            a += b
            return a
            
            
        if layout == 'Baltay_default':
            # self.Nx = 1000
            # self.Ny = 1000
            # image = np.empty([Nx,Ny],dtype=np.float64)
            image = np.empty([Nx,Ny])
            x,y = np.mgrid[0:Nx,0:Ny]
            x -= Nx/2
            y -= Ny/2
            xygrid = x,y
            
            # add_gaussian(image, make_gaussian(t))
            
            # image += gaussian_profile(sigma,center_x,center_y,xygrid=xygrid)

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
            
        else:
            raise ValueError("I don't understand this layout: "+layout)
# self.image = image
        # image = np.empty([500,500],dtype='f8')
        # if layout == 'xygrid':
            # coords = [(0.000,0.000),
            # (0.000,-120.000),
            # (103.923,-60.000),
            # (103.923,60.000),
            # (0.000,120.000),
            # (207.846,-120.000),
            # (240.000,0.000)
            # (207.846,120.000),
            # (120.000,207.846),
            # (0.000,240.000),
            # (354.531,-62.513),
            # (354.531,62.514),
            # (311.769,180.000),
            # (231.403,275.776),
            # (463.644,-124.233),
            # (480.000,0.000),
            # (463.644,124.233),
            # (415.692,240.000)]

            # for c in coords:
                # new_gaussian = Gaussian(2,c[0],c[1])
                # image[c[0]-1:c[0]=1,c[1]-1:c[1]+1] += new_gaussian
                # matplotlib.pyplot.matshow(image)
                # show()
                
                # c is the center of this Gaussian
                # generate Gaussian centered at this location
                # Add values of resulting Gaussian to the image
                # look up numpy slicing
                

    #...
    
    # def save(self,filename):
        # """Save the current image to a .fits file named filename."""
    #...
#...

# coords = [[0.000,0.000],
 # [0.000,-120.000],
 # [103.923,-60.000],
 # [103.923,60.000],
 # [0.000,120.000],
 # [207.846,-120.000],
 # [240.000,0.000],
 # [207.846,120.000],
 # [120.000,207.846],
 # [0.000,240.000],
 # [354.531,-62.513],
 # [354.531,62.514],
 # [311.769,180.000],
 # [231.403,275.776],
 # [463.644,-124.233],
 # [480.000,0.000],
 # [463.644,124.233],
 # [415.692,240.000]]
 
# for c in coords:
    # newgaussian = Gaussian(2)
    # newgaussian(c[0],c[1])
    
plot = SimCCD()
plot(1000.,1000.,layout='Baltay_default')