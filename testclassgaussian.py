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
            gauss = lambda x,y: height*np.exp(-(((self.center_x-x)/self.sigma)**2+((self.center_y-y)/self.sigma)**2)/2)
            return gauss(x,y)