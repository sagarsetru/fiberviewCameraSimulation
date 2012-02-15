#!/usr/bin/env python
"""
Unittests for simccd.
"""
import os
import unittest

import numpy as np

import simccd

class Test_simccd(unittest.TestCase):
    def setUp(self):
        """Setup test classes."""
        self.simCCD = simccd.SimCCD((100,100))
        self.outputfile = 'testoutput.fits'
    #...
    
    def tearDown(self):
        """Remove unneeded temp files."""
        if os.path.exists(self.outputfile):
            os.remove(self.outputfile)
    #...

    def test_gaussian(self):
        """Test the generation of a 2d gaussian profile."""
        simulated_gaussian = simccd.gaussian_profile(1)
        correct_gaussian = np.zeros((5,5))
        self.assertTrue(np.all(simulated_gaussian == correct_gaussian))
        # NOTE: to plot a grid of values, use this:
        # pylab.imshow(simulated_gaussian)
    #...
    
    def test_make_image(self):
        """Generate an image and test if it came out correctly."""
        #self.simCCD(10)
        self.assertTrue(True)
        # TBD: some comparison to make sure the result is sane.
    #...
    
    def test_save_image(self):
        """Save an image, and test if it got put in a file correctly."""
        #self.save(self.outputfile)
        self.assertTrue(True)
    #...
#...

if __name__ == '__main__':
    unittest.main()
