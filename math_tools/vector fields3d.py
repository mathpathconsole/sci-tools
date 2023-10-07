from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

u = -np.cos(x)*np.sin(y)*x*y**2 
v = np.sin(x)*np.cos(y)+(x**2)*y*np.cos(z)
w = y**2+z-(x**2)*np.sin(z)

ax.quiver(x, y, z, u, v, w, length=0.4, color = 'blue')

plt.show()


#2d kaynakla aynı yapı
