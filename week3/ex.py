import matplotlib.pyplot as plt
import numpy as np

def draw_plot(x,y):
    plt.grid(True)
    plt.plot(x,np.zeros(x.shape[0]),'r')
    plt.xticks(x)
    plt.tight_layout(pad=1.0)
    for i in range(y.shape[0]):
        if y[i] !=0:
            plt.plot(np.array([x[i],x[i]]), np.array([0,y[i]]), 'b')
    plt.stem(x,y)
    

# graph 1
n = np.arange(-4,9,1)
u = np.array(1.0*(n>=0))
x = np.array((0.8**n)*u)
plt.subplot(3,1,1)
plt.title("x(n)")
draw_plot(n,x)

# graph 2
y = np.array([0,0,0,0,1,1,1,1,1,1,1,1,1])
plt.subplot(3,1,2)
plt.title("h(n)")
draw_plot(n,y)

# graph 3
y = np.convolve(x,u, 'same')
plt.subplot(3,1,3)
plt.title("y(n)")
draw_plot(n,y)
plt.show()