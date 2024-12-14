import matplotlib.pyplot as plt
import numpy as np

#a: большая полуось эллипса
#b: малая полуось эллипса
a = 5
b = 3

t = np.arange(0, 10, 0.01)  
x = a * np.cos(t)
y = b * np.sin(t)



plt.plot(x, y)
plt.savefig('fig_3.png')
plt.axis('equal')

    

