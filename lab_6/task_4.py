import matplotlib.pyplot as plt
import numpy as np

b = 1  
phi = np.arange(0, 8 * 3.14, 0.01)  
r = np.exp(b * phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.savefig('fig_4.png')
plt.axis('equal')

