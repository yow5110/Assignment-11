import numpy as np
class Line():
    def __init__(self,c0, c1):
        self.c0 = c0
        self.c1 = c1
        self.D = 2
    def __calc__(self, x):
        return self.c0 + self.c1*x
    def table(self, L=0, R=20, n=100):
        x = np.linspace(L, R, n)
        y = self.__calc__(x)
        return x, y
    
class Parabola(Line):
    def __init__(self,c0, c1, c2):
        super().__init__(c0, c1)  # call the __init__ of Line
        self.c2 = c2
        
    def __calc__(self, x):
        return super().__calc__(x) + self.c2*x**2

L1 = Line(c0=1, c1=2)
L2 = Line(c0=0.5, c1=2.5)
P1 = Parabola(1,2,3) 

import matplotlib.pyplot as plt
plt.figure()

# plt.plot() expects two arguments for x and y.
# The * sign unpacks the results of the table() method 
# to the two arguments needed here
plt.plot( *L1.table(0,10, 20), 'ko')
plt.plot( *L2.table(0,10, 20), 'bo') 
plt.plot( *P1.table(0,10, 20), 'ro')  
plt.show()


