import numpy as np
import matplotlib.pyplot as plt

sigma = 6.0
rmin = 5.5
rmax = 10
dr = 0.1


def ulj(r, epsilon=4E-4, sigma=6):
    '''
    Parameters
    ----------
    r : distance between atoms.
    epsilon : constant of 4E-4.
    sigma : constant of 6.

    Returns
    -------
    result : ulj potential.
    '''
    result = 4 * epsilon * ((sigma/r)**12 - (sigma/r)**6) 
    return result 

r_range = np.arange(rmin, rmax, dr) 
ulj =ulj(r_range)


plt.figure(figsize=(8,5)) 
plt.ylim(-0.0005, 0.002)
plt.xlim(rmin, rmax)
plt.xlabel("r [a.u.]")
plt.ylabel("ULJ(r) [a.u.]")

plt.plot(r_range, ulj, 'b-')
