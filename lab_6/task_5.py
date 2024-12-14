import matplotlib.pyplot as plt
import numpy as np

k = 0.5 
phi = np.arange(0, 8 * 3.14, 0.01)
r = k * phi

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.savefig('fig_5.png')
plt.axis('equal')