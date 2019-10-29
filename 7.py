# a human jumping out of the sky and using a parachute :: repeated
from matplotlib import pyplot as plt
m = 90 # mass in kg
a = -9.81 # accelaration due to gravity in m/s^2
#r = 0.4 # radius in m
dt = 0.01 
timeInterval = 40 # in seconds
n = timeInterval / dt
weight = m * a 
projectedArea = 0.4
v0 = 0 #initial velocity in m/s
v = v0
p0 = 2000 #initial poosition in m
p = p0
t = 0
tList = []
speedList = []
positionList = []
flag = 1
for i in range(int(n)):
    airFriction = -0.65 * projectedArea * v * abs(v)
    totalForce = airFriction + weight
    accelaration = totalForce / m
    diffV = accelaration #change in velocity
    diffP = v #change in position
    speed = abs(v)
    tList.append(t)
    speedList.append(speed * 10) # i changed the scale
    positionList.append(p)
    t = t + dt
    v = v + diffV * dt
    p = p + diffP * dt
    if p <= 1000 and flag == 1:
        projectedArea = 28
        flag = 0 
plt.plot(tList, speedList, 'r')
plt.plot(tList, positionList, 'g')
plt.show()