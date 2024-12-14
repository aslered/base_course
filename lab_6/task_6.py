import matplotlib.pyplot as plt
import numpy as np

k = 1 
phi = np.arange(0.01, 8 * 3.14, 0.01) 
r = k / np.sqrt(phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.savefig('fig_6.png')
plt.axis('equal')