#population in a bounded resource area that has m as a maximum capacity for the growth
from matplotlib import pyplot as plt
import math
p0 = 100
m = 10000
p = p0
r = 0.1
dt = 0.01
n = int(100/dt)
t = 0
pList = []
tList = []
for i in range(n):
    growth = r * p*(1 - p/m)
    p = p + growth * dt
    t = t + dt
    tList.append(t)
    pList.append(p)
print(p)
plt.plot(tList, pList, 'r')
plt.show()