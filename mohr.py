import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
from numpy import linalg as la 
l1 = []
l2 = []
l3 = []
print("Enter the first row of the stress tensor:")
for i in range(0,3):
	x = float(input())
	l1.append(x)
print("Enter the second row of the stress tensor:")
for i in range(0,3):
    x = float(input())
    l2.append(x)
print("Enter the third row of the stress tensor:")
for i in range(0,3):
   	x = float(input())
   	l3.append(x)
stress = np.array([l1,l2,l3])	
w, v = la.eig(stress)
a1 = w[2]
a2 = w[1]
a3 = w[0]
R1 = (a1-a3)/2
R2 = (a2-a3)/2
R3 = (a1-a2)/2
c1 = (a1+a3)/2
c2 = (a2+a3)/2
c3 = (a1+a2)/2
t = np.linspace(0,2*np.pi)
x1 = R1 * np.cos(t) + c1
y1 = R1 * np.sin(t)
x2 = R2 * np.cos(t) + c2
y2 = R2 * np.sin(t)
x3 = R3 * np.cos(t) + c3
y3 = R3 * np.sin(t) 
plt.plot(x1,y1,color = 'k')
plt.plot(x2,y2,color = 'b')
plt.plot(x3,y3,color = 'r')
plt.xlabel(r'Normal stress($\sigma$)')
plt.ylabel(r'Shear stress($\tau$)')
plt.show()



