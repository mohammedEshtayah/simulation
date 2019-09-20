
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t=[]
    pt=[]
    #print("Goodbye, World!")
    p=100 # عدد السكان 
    r=0.1 #نسبة التغير عدد السكان 
    dt=0.01   #انسبة التغير بالسنة 
    #t=0 # الزمن 
    n=5/dt # الفترة الزمنية 
    g=0.0 
    
    for i in range(int(n)):
        g=r*p
        p=p+(g*dt)
        t.append(i*dt)
        pt.append(p)
    #print(p)
    plt.plot(t,pt) 
    plt.show()