import matplotlib.pyplot as plt
import numpy as np
plt.close('all')
#X is years, Y is CO2-levels in ppm
X, Y = np.loadtxt("Regresjon/Datasett2.dat", unpack=True)
plt.title("CO2 levels in Muana lua")
plt.xlabel("Years")
plt.ylabel("CO2, ppm")
plt.grid()
plt.scatter(X,Y, color="#014D4E")

N=len(X)


X_bar = sum(X)/N
Y_bar = sum(Y)/N
#formula for calculating linear regresion (taken from lecture notes)
b = sum((X-X_bar)*(Y-Y_bar)) / sum((X-X_bar)**2)
a = Y_bar - b * X_bar
X_Y_reg = a + b*X
print(f"a = {a:.2f}, b = {b:.2f}")

plt.plot(X, X_Y_reg, color="#8B0000")
plt.show()