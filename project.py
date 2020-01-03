import math ;
import matplotlib.pyplot as plt
import numpy as  np;
 
if __name__ == "__main__":
    dt = 0.01
    t=0
    it = 1
    n=it/dt
    atmosphere_list=[]
    terrestrial_biosphere_list=[]
    ocean_surface_list=[]
    deep_ocean_list=[]
    soil_list=[]
    atmospheric_list=[]
    #---------------
    atmosphere=750
    terrestrial_biosphere=600
    ocean_surface=800
    deep_ocean=38000
    soil=1500
    tList=[]
    for i in range(int(n)):
        tList.append( t)
        t = t +   dt
        atmosphere=atmosphere +   55 * dt + 55 *dt  - 110 * dt - 100 * dt   - 40 * dt  
        terrestrial_biosphere= terrestrial_biosphere + 110 *dt - 55 *dt - 55 *dt
        ocean_surface= ocean_surface -40 * dt - 100* dt -40* dt -23 *dt + 27*dt+ 40 *dt +100 *dt
        deep_ocean=deep_ocean-27*dt +27 *dt 
        soil= soil +55*dt -55 *dt
      
         

        atmosphere_list.append(atmosphere)
        terrestrial_biosphere_list.append(terrestrial_biosphere)
        ocean_surface_list.append(ocean_surface)
        deep_ocean_list.append(deep_ocean)
        soil_list.append(soil)

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.15, left=0.2)
    plt.plot(tList,atmosphere_list)
    plt.plot(tList,terrestrial_biosphere_list)
    plt.plot(tList,ocean_surface_list)
    #plt.plot(tList,deep_ocean_list)
    plt.plot(tList,soil_list)
    ax.set_xlabel('time')
    ax.set_ylabel('Amount of Carbon (Gt)')
    plt.show()
   
     
    