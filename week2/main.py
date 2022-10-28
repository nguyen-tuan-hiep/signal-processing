import matplotlib.pyplot as plt
import numpy as np


def myplot(x,y):
    plt.grid(True)
    plt.plot(x,np.zeros(x.shape[0]),'r')
    plt.xticks(x)
    plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
    for i in range(y.shape[0]):
        if y[i] !=0:
            plt.plot(np.array([x[i],x[i]]), np.array([0,y[i]]), 'b')
    plt.scatter(x,y)
    

x1  = np.arange(-5,5)
y1 = np.zeros(10)
y1[5] = 1
plt.subplot(2,2,1)
plt.title("Unit Sequence")
myplot(x1,y1)

x2  = np.arange(-5,5)
y2 = np.array([0,0,0,0,0,1,1,1,1,1])
plt.subplot(2,2,2)
plt.title('Unit step Sequence')
myplot(x2,y2)

x3 = np.arange(-5,5)
y3 = np.array(0.7**x3)
plt.subplot(2,2,3)
plt.title('Exponential Sequence')
myplot(x3,y3)

x4 = np.arange(-10,10)
y4 = np.array(np.sin(x4))
plt.subplot(2,2,4)
plt.title('Sinusoidal Sequence')
myplot(x4,y4)
plt.show()