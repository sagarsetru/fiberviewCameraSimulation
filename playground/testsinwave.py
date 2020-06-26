import numpy as np
import matplotlib.pyplot as plt
from numpy import *

def f(x):
    return sin(x)

def g(x):
    return cos(x)
    
x = np.linspace( 0,2*pi,100 )
print x
plt.plot(x,f(x),'bo',x, g(x), 'r--')
plt.show()



# plt.plot(x, g(x), 'r--')
# plt.show()