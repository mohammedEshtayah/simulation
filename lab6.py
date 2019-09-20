import math ;
import matplotlib.pyplot as plt
import numpy as  np;
if __name__ == "__main__":
    dt=0.1
    mass=0.5
    speed=0
    acc=9.81
    v=0 
    weigtht=mass*acc
    postion=400
    r=0.05
    projected_area=3.14159*r**2
    T=[]
    P=[]
    S=[]  
    i=0
    for i in range(postion):
        air_fri=-0.65*projected_area*v*abs(v)
        total_force=weigtht+air_fri
        acc=total_force/mass
        dv=acc
        dp=v
        v=v+dv*dt
        postion=postion+dp*dt
        speed=abs(v)
        T.append(i*dt)
        P.append(postion/10)
        S.append(speed)
    
    plt.plot(T,S)  
    plt.plot(T,P)  
    plt.show()    

    
