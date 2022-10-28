import matplotlib.pyplot as plt
from matplotlib import collections as matcoll
import numpy as np

x = np.arange(-5,5)
y = 0.7**x
lines = []
for i in range(len(x)):
    pair=[(x[i],0), (x[i], y[i])]
    lines.append(pair)
linecoll = matcoll.LineCollection(lines)
fig, ax = plt.subplots()
ax.add_collection(linecoll)
plt.subplot(2,2,1)
plt.scatter(x,y)
# plt.plot(x,np.zeros(x.shape[0]),"r")
plt.title("y=0.7^x")
plt.grid(True)

y = [0,0,0,0,0,1,1,1,1,1]
plt.subplot(2,2,2)
plt.scatter(x,y)
plt.grid(True)

y = np.zeros(10)
y[5] = 1
plt.subplot(2,2,3)
plt.scatter(x,y)
plt.grid(True)

x = np.arange(-10,10)
y = np.array(np.sin(x))
plt.subplot(2,2,4)
plt.scatter(x,y)
plt.grid(True)
plt.show()
