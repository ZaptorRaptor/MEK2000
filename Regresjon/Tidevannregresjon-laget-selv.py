import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt("Regresjon/Tidevann.dat", unpack=True, skiprows=1, delimiter=",")
#a)

plt.plot(x,y, color="red")
#b)
x_smooth = np.linspace(0,16,1000)
X = np.cos((np.pi/6)*x)
X_smooth = np.cos((np.pi/6)*x_smooth)
plt.plot(x_smooth, X_smooth, color="blue")
#c)
N = len(X)
x_snitt = sum(X)/N

y_snitt = sum(y)/N

A = sum((X-x_snitt)*(y-y_snitt))/sum((X-x_snitt)**2)

V_0 = y_snitt - A*x_snitt
Vx = V_0 + A*X

Vx_smooth = V_0 + A * np.cos((np.pi / 6) * x_smooth)
plt.plot(x_smooth, Vx_smooth, color="black")
#linearisation of Vx by making x into X
#plt.plot(X,Vx, color="yellow)

plt.xlabel("hours")
plt.ylabel("depth")
plt.show()
