import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt("Datasett.dat", unpack=True)
plt.scatter(X,Y)
plt.show()