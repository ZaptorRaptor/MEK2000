import matplotlib.pyplot as plt
import numpy as np
plt.close('all')
#X is years, Y is CO2-levels in ppm
X, Y = np.loadtxt("Regresjon/Datasett2.dat", unpack=True)
plt.title("CO2 levels in Muana lua")
plt.xlabel("Years")
plt.ylabel("CO2, ppm")
plt.grid()
#plots the datapoints from the Datasett2.dat file
plt.scatter(X,Y, color="#014D4E")
plt.show()