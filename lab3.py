import math ;
import matplotlib.pyplot as plt
import numpy as  np;
if __name__ == "__main__":
    
    A=2*325*1000 # نسبة الاسبرين
    h=3.2
    k=-math.log(0.5)/h
    pv=3000 # البلازمه
    dt=0.01 #تغير بالزمن
    t=[]
    pt=[]
    tt=21 #ساعة
    e=0
    c=0
    for i in range(int(tt/dt)):
        e= k*A*dt # نسبة التناقص بالسنة
        A=A-e
        c=pv*A
        t.append(i*dt)
        pt.append(c)
    
    plt.plot(t,pt)  
    plt.show()    

    
