import math ;
import matplotlib.pyplot as plt
import numpy as  np;
if __name__ == "__main__":
    t=[]
    pt=[]
 
    elem=2*325*1000 # نسبة الاسبرين
    h=22
    k=-math.log(0.5)/h
    pv=3000 # البلازمه
    dt=0.01 #تغير بالزمن
    tt=24 #ساعة
    q=1
  
    d=0.12*q
    for i in range(int(tt/dt)):
        elem= k*elem*dt # نسبة التناقص بالسنة
        q=q-elem
         
        if(tt%8==0):
            q=q+d
        t.append(i*dt)
        pt.append(q)
    
    plt.plot(t,pt)  
    plt.show()    

    
