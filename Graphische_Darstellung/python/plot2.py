import numpy as np
import matplotlib.pyplot as plt
import math

g, b = np.genfromtxt("python/tabel2.txt", unpack=True)
plt.plot(1/g,1/b, "k." , label="G-B")
plt.xlim(0, 0.02)
plt.ylim(0,0.025)
plt.xlabel(r'$  \symup{1/G}$')
plt.ylabel(r'$  \symup{1/B}$')

plt.tight_layout()


plt.savefig('build/plot2.pdf')

#plt.savefig('build/plot2.pdf')

