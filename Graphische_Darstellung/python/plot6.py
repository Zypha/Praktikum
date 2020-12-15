import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d, N, F = np.genfromtxt("python/abs2.txt", unpack=True)

def absorptionsgesetz(d, A, μ): 
    return A * np.exp(-μ*d)

params, covariance_matrix = curve_fit(absorptionsgesetz, d, N)
uncertainties = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(0, 5, 50)

plt.plot(d, N, '.', label="Messwerte")
plt.plot(x_plot, absorptionsgesetz(x_plot, *params), "r-", label="Curvefit")
plt.yticks(np.arange(0,9100, step=1000))

plt.xlabel("d [cm]")
plt.ylabel("N [1/60s]")



plt.tight_layout()
#plt.show()
plt.savefig("build/plot6.pdf")