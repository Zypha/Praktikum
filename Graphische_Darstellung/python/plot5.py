import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import importlib
import math


x, y, F = np.genfromtxt('python/abs.txt',unpack = True)



plt.plot(x, y , "b.", markersize = 2 )


plt.errorbar(x, y, yerr = F, elinewidth = 1, ls = 'none') 

plt.xlabel("d [cm]")
plt.ylabel("N [1/60s]")

plt.yscale("log")

#plt.show()
plt.tight_layout()
plt.savefig('build/plot5.pdf')