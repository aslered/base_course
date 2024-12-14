import matplotlib.pyplot as plt
import numpy as np

k_values = [1, 2, 3, 2.5, 3.5] 

phi = np.arange(0, 2 * 3.14, 0.01) 

for k in k_values:
    r = np.sin(k * phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)

plt.plot(x, y)
plt.savefig('fig_7.png')
plt.axis('equal')