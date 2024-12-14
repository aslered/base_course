import matplotlib.pyplot as plt
import numpy as np

def giperbola():

    x = np.arange(0.01, 100, 0.01)
    y = 1/x



    plt.plot(x, y)
    plt.savefig('fig_2.png')
    plt.axis('equal')

    x = np.arange(-100, -0.01, 0.01)
    y = 1/x

    plt.plot(x, y)
    plt.savefig('fig_2.png')
    plt.axis('equal')

if __name__ == '__main__':
    giperbola()