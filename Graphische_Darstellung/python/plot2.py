import numpy as np
import matplotlib.pyplot as plt

x_messung, y_messung = np.genfromtxt("python/tabel.txt", unpack=True)
plt.plot(1/x_messung, 1/y_messung, "k." , label="G-B")
plt.xlim(0, 10)
plt.ylim(0, 10)

plt.tight_layout()


plt.savefig('build/plot2.pdf')

#plt.savefig('build/plot2.pdf')

