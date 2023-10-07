import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

#Reşat Berk --stars of the sky
#*spherical coordinates referance -https://stackoverflow.com/questions/36816537/spherical-coordinates-plot-in-matplotlib gidiniz
#*spherical harmonics referance: "intro to quantum mechanics 2nd edition, David J. Griffiths, page 139, table of a few spherical harmonics"

#*** for run create lib numpy and matplotlib

#on spherical coordinates theta,phi angles 0->pi, 0->2pi) 
theta, phi = np.linspace(0, np.pi, 40), np.linspace(0, 2*np.pi, 40)
THETA, PHI = np.meshgrid(theta, phi)

#function of spherical harmonics l and m 
def y(l,m):
    if l==3 and m==3:
        r1=(np.sqrt(35/(64*np.pi))*(np.sin(theta)**3)*(np.exp(3*np.imag(1)*phi)))
        r2=(np.sqrt(35/(64*np.pi))*(np.sin(theta)**3)*(np.exp(-3*np.imag(1)*phi)))
        R=r1*r2 #attention these are imaginer number
    elif l==3 and m==2:
        r1=(np.sqrt(105/(32*np.pi))*(np.sin(theta)**2)*(np.cos(theta))*(np.exp(2*np.imag(1)*phi)))
        r2=(np.sqrt(105/(32*np.pi))*(np.sin(theta)**2)*(np.cos(theta))*(np.exp(-2*np.imag(1)*phi)))
        R=r1*r2
    elif l==3 and m==1:
        r1=(np.sqrt(21/(64*np.pi))*(np.sin(theta))*((5*np.cos(theta)**2)-1)*(np.exp(np.imag(1)*phi)))
        r2=(np.sqrt(21/(64*np.pi))*(np.sin(theta))*((5*np.cos(theta)**2)-1)*(np.exp(-np.imag(1)*phi)))
        R=r1*r2
    elif l==3 and m==0:
        R=(np.sqrt(7/(16*np.pi))*((5*np.cos(theta)**3)-(3*np.cos(theta))))**2
    elif l==2 and m==2:
        r1=(np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*(np.exp(2*np.imag(1)*phi)))
        r2=(np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*(np.exp(-2*np.imag(1)*phi)))
        R=r1*r2
    elif l==2 and m==1:
        r1=(np.sqrt(15/(8*np.pi))*(np.sin(theta))*(np.cos(theta))*(np.exp(np.imag(1)*phi)))
        r2=(np.sqrt(15/(8*np.pi))*(np.sin(theta))*(np.cos(theta))*(np.exp(-np.imag(1)*phi)))
        R=r1*r2
    elif l==2 and m==0:
        R=(np.sqrt(5/(16*np.pi))*((3*np.cos(theta)**2)-1))**2
    elif l==1 and m==1:
        r1=(np.sqrt(3/(8*np.pi))*(np.sin(theta))*(np.exp(np.imag(1)*phi)))
        r2=(np.sqrt(3/(8*np.pi))*(np.sin(theta))*(np.exp(-np.imag(1)*phi)))
        R=r1*r2
    elif l==1 and m==0:
        R=(np.sqrt(3/(4*np.pi))*np.cos(theta)**2)**2
    elif l==0 and m==0:
        R=(np.sqrt(1/(np.pi)))**2
    else:
        print("""please entry to such >>>y(1,0) integer values

defineted harmonics:
{'y(0,0)' , 'y(1,0)', 'y(1,1)' , 'y(2,0)' , 'y(2,1)' , 'y(2,2)'
'y(3,0)' , 'y(3,1)' , 'y(3,2)' , 'y(3,3)'}
*intro to quantum physics 2nd edition, David J. Griffiths, page 139, table of a few spherical harmonics

---Reşat Berk // Stars of the sky---""")
    
           
    X = R * np.sin(THETA) * np.cos(PHI) #x,y,z on spherical coordinates
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)
    
    plt.show()
    

