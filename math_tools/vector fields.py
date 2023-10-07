#vector fields --sky of the stars,RBerk
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *

x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

u= x**2
v=0

plt.quiver(x,y,u,v)
plt.title("Vector fields")
plt.show()

#libraries:
#pip install numpy
#pip install matplotlib

