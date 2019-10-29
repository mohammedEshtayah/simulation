#bilogistic model for population
from matplotlib import pyplot as plt
import math
p0 = 10000
m1 = 20000
m2 = 50000
m = m1 + 1
a = 0.2
p = p0
r = 0.1
dt = 0.01
n = int(100/dt)
t = 0
pList = []
tList = []
mList = []
for i in range(n):
    growth = r * p*(1 - p/m)
    mGrowth = a*(m - m1)*(1 - (m - m1)/m2)
    m = m + mGrowth * dt
    p = p + growth * dt
    t = t + dt
    tList.append(t)
    pList.append(p)
    mList.append(m)
print(p)
plt.plot(tList, pList, 'r')
plt.plot(tList, mList, 'g')
plt.show()