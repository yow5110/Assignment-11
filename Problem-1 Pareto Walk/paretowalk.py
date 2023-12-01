
import numpy as np
import nd_rw as RW
import matplotlib.pyplot as plt

lattice_2d = RW.LatticeWalk(2)
pareto_2d = RW.ParetoWalk(2)

Nstep = 1000
Nparticle = 1000

fig, ax = plt.subplots(3)
ax[1].set_aspect('equal', 'box')
ax[2].set_aspect('equal', 'box')


# Use the _get_steps() method to obtain the step magnitudes of the two types of random walk
# (Nstep numbers for lattice_2d and Nstep numbers for pareto_2d),
# and plot a histogram of step magnitudes of each type.
bins=100
steps1 = 
steps2 = 

ax[0].hist( steps1 , bins=bins, range=(0,10))
ax[0].hist( steps2, bins=bins, range=(0,10))


# Use the get_walk() method to obtain the trajectory of a particle doing
# lattice_2d walk and pareto_2d walk.
ax[1].plot(,'r-')
ax[1].plot(,  'k-')

# Use get_endpoints() method to obtain a scatter plot of 
# the final positions of 1000  particles
ax[2].plot( ,'r.')
ax[2].plot( ,'k.')
