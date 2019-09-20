
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t=[]
    pt=[]
    p=10 # عدد السكان 
    r=0.1 #نسبة التغير عدد السكان 
    dt=0.01   #انسبة التغير بالسنة 
    #t=0 # الزمن 
    n=450/dt # الفترة الزمنية 
    g=0.0 
    m=20000000
    dr=2
    a=0.5
    m1=20000000
    m2=50000000
    
    for i in range(int(n)):
        m=m+a*(m-m1)*1-(m-m1)/m2*dt
        g=r*p*(1-(p/m) )
         
        p=p+(g*dt)
        
        t.append(i*dt)
        pt.append(p)
    #print(p)
    plt.plot(t,pt) 
    plt.show()