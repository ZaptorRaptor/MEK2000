import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt("Regresjon/Tidevann.dat", unpack=True, skiprows=1, delimiter=",")
#a)
plt.plot(x,y, color="red")
#b)
plt.plot(x,(np.cos((np.pi/6)*x)), color="blue")
#c)
N = len(x)
x_snitt = sum(x)/N
y_snitt = sum(y)/N
A = (sum((x-x_snitt)*(y-y_snitt))/sum(x-x_snitt)**2)
V_0 = y_snitt - A*x_snitt
Vx = V_0 + A*np.cos((np.pi/6)*x)
plt.plot(x,Vx, color="black")

plt.show()
plt.xlabel("hours")
plt.ylabel("depth")