
import matplotlib.pyplot as plt
if __name__ == "__main__":
    p=10000
    r=0.000120008
    dt=21 #تغير بالزمن
    pt=[]
    t=[]
    for i in range(int(10000/dt)):
       g= p*r # نسبة التناقص بالسنة
       p=p-(g*dt)
       t.append(i*dt)
       pt.append(p)
       
    print(p) 
    plt.plot(t,pt)  
    plt.show()
