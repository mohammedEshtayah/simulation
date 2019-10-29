#chapter 3: simulation in page 106
from matplotlib import pyplot as plt
m = 0.5 # mass in kg
a = -9.81 # accelaration due to gravity in m/s^2
r = 0.05 # radius in m
dt = 0.01 
timeInterval = 15 # in seconds
n = timeInterval / dt
weight = m * a 
projectedArea = 3.14159 * r * r
v0 = 0 #initial velocity in m/s
v = v0
p0 = 400 #initial poosition in m
p = p0
t = 0
tList = []
speedList = []
positionList = []
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
    
plt.plot(tList, speedList, 'r')
plt.plot(tList, positionList, 'g')
plt.show()