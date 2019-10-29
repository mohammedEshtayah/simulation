from matplotlib import pyplot as plot
q0 = 100
q = q0
r = -0.00012098968
dt = 10
n = (60000/dt)
t = 0
tList = []
qList = []
for i in range(int(n)):
    decay = r * q
    q = q + decay * dt
    tList.append(t)
    qList.append(q)
    t = t + dt
print(q)
plt.plot(tList, qList, 'r')
plt.show()