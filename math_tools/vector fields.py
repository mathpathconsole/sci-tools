#vector fields --sky of the stars,RBerk
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *

x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

def f(x='your func'):
    #x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
    u=np.array(i)
    v=0
    plt.quiver(x,y,u,v)
    plt.title("Vector fields")
    plt.show()

f(x=x**2) #function of x^2
    
#x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
#u= x**2
#v=0
#print(type(u))

#plt.quiver(x,y,u,v)
#plt.title("Vector fields")
#plt.show()

#indirilmesi gereken kütüphaneler:
#pip install numpy
#pip install matplotlib

#https://krajit.github.io/sympy/vectorFields/vectorFields.html --*kaynak*
