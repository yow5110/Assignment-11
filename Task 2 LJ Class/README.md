# Week 14 Task 2

Earlier in Part 1 of the course we dealt with Lennard-Jones potential multiple times. Here we'll practice rewriting the LJ potential plotting scripts using objects.

Using quiz #2 script as a starting point (provided here), create a Python class LJ(). The \_\_init\_\_ method of this class should take as input the values of the two parameters of the Lennard-Jones potential and save them as attributes of the class. 

The class should have an internal LJ.\_\_calc\_\_(self,r) method, which compute the values of the potential, given a value of the separation between two atoms r. 

The class should also have a LJ.table(self, L, R, n) method similar to the Line/Parabola/Cubic classes, which then sets up a range of of r values between r=L and r=R and return potential values.

Finally, still shadowing the Cubic class, create a plot of the LJ potential using the table() method.
