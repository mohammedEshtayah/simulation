#chapter 4: 
#competition simulation dor 2 sspecies
from matplotlib import pyplot as plt
# for bts
bts_pop0 = 15
bts_pop = bts_pop0
bts_birth_fraction = 1
bts_death_prop_const = 0.2
bts_list = []
# for wts
wts_pop0 = 20
wts_pop = wts_pop0
wts_birth_fraction = 1
wts_death_prop_const = 0.27
wts_list = []
# general info
t = 0
t_list = []
time_interval = 5
dt = 0.001
n = time_interval/dt
# for loop
for i in range(int(n)):
    bts_births = bts_birth_fraction * bts_pop
    bts_deaths = (bts_death_prop_const * wts_pop) * bts_pop
    bts_pop = bts_pop + (bts_births - bts_deaths)*dt
    wts_births = wts_birth_fraction * wts_pop
    wts_deaths = (wts_death_prop_const * bts_pop) * wts_pop
    wts_pop = wts_pop + (wts_births - wts_deaths)*dt
    bts_list.append(bts_pop)
    wts_list.append(wts_pop)
    t_list.append(t)
    t = dt * i
plt.plot(t_list, bts_list, 'r')
plt.plot(t_list, wts_list, 'g')
plt.show()