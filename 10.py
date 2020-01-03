 
#competition simulation for predators and preys
#Graph of populations versus time in months
from matplotlib import pyplot as plt
# for bts
pred_pop0 = 15
pred_pop = pred_pop0
pred_birth_fraction = 0.01
pred_death_prop_const = 1.06
pred_list = []
# for wts
prey_pop0 = 100
prey_pop = prey_pop0
prey_birth_fraction = 2
prey_death_prop_const = 0.02
prey_list = []
# general info
t = 0
t_list = []
time_interval = 12
dt = 0.001
n = time_interval/dt
# for loop
for i in range(int(n)):
    pred_births = prey_pop * pred_pop * pred_birth_fraction
    pred_deaths = pred_death_prop_const * pred_pop
    pred_pop = pred_pop + (pred_births - pred_deaths)*dt
    
    prey_births = prey_birth_fraction * prey_pop
    prey_deaths = (prey_death_prop_const * pred_pop) * prey_pop
    prey_pop = prey_pop + (prey_births - prey_deaths)*dt

    pred_list.append(pred_pop)
    prey_list.append(prey_pop)
    t_list.append(t)
    t = dt * i
plt.plot(t_list, pred_list, 'r')
plt.plot(t_list, prey_list, 'g')
plt.show() 
