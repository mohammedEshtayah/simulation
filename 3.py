#page 50 textbook
from matplotlib import pyplot as plt
halfLife = 22
plazmaVol = 3000
dozeInPlazma0 =  (100 * 1000) * 0.12
dozeInPlazma = dozeInPlazma0
t = 0
tList = []
aspList = []
k = - (math.log(0.5) / halfLife)
dt = 0.01
n = (24*14)/dt
for i in range(int(n)):
    elemination = - dozeInPlazma * k
    dozeInPlazma = dozeInPlazma + elemination*dt
    if ((i * dt) % 8) == 0:
        dozeInPlazma = dozeInPlazma + dozeInPlazma0
    tList.append(t)
    aspList.append(dozeInPlazma / plazmaVol)
    t = t + dt
print(dozeInPlazma)
plt.plot(tList, aspList, 'g')