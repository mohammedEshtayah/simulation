#bungee jump simulation :), page 84
from matplotlib import pyplot as plt
m = 80 # mass in kg
a = -9.81 # accelaration due to gravity in m/s^2
unWeightedLength = 30 # original length of the cord 
sk = 6 # N/m
#r = 0.4 # radius in m
dt = 0.01 
timeInterval = 70 # in seconds
n = timeInterval / dt
weight = m * a 
projectedArea = 0.1
v0 = 5 #initial velocity in m/s
v = v0
p0 = 0 #initial poosition in m
p = p0
t = 0
tList = []
vList = []
positionList = []
restoringSpringForce = 0
for i in range(int(n)):
    airFriction = -0.65 * projectedArea * v * abs(v)
    if p > unWeightedLength:
        restoringSpringForce = -1*sk * (p - unWeightedLength)
    else:
        restoringSpringForce = 0
    totalForce = airFriction - weight + restoringSpringForce 
    accelaration = totalForce / m
    diffV = accelaration #change in velocity
    diffP = v #change in position
    tList.append(t)
    vList.append(v)
    positionList.append(p)
    t = t + dt
    v = v + diffV * dt
    p = p + diffP * dt
plt.plot(tList, vList, 'r')
plt.plot(tList, positionList, 'g')
plt.show()