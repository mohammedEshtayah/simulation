#asperin 
from matplotlib import pyplot as plt
halfLife = 3.2
plazmaVol = 3000
asperinInPlazma0 =  650 * 1000 #2 pills
asperinInPlazma = asperinInPlazma0

t = 0
tList = []
aspList = []
k = - (math.log(0.5) / halfLife)
dt = 0.1
n = 24/dt
for i in range(int(n)):
    elemination = elemination- asperinInPlazma * k
    asperinInPlazma = asperinInPlazma + elemination*dt
    tList.append(t)
    aspList.append(asperinInPlazma / plazmaVol)
    t = t + dt
print(asperinInPlazma)
plt.plot(tList, aspList, 'g')

....................