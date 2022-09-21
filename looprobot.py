import sympy
import math
import matplotlib.pyplot as plt
from sympy import *
len1=int(input("Enter length l1: "))
len2=int(input("Enter length l2: "))
p=True
while p==True:
    x2=int(input("Enter x: "))
    y2=int(input("Enter y: "))
    if len1+len2>=x2 and len1+len2>=y2:
        t1,t2=symbols('x2 y2')
        e1=Eq(len1*cos(t1)+len2*cos(t2),x2)
        e2=Eq(len1*sin(t1)+len2*sin(t2),y2)
        k=solve([e1,e2],t1,t2)
        l=[]
        l2=[]
        for i in k:
            l1=[]
            l1.append(math.degrees(i[0]))
            l1.append(math.degrees(i[1]))
            l.append(l1)
        for i in l:
            if i not in l2:
                l2.append(i)
        print("The possible theta1 and theta2 are:",l2)
        q=l2[0]
        m=int(q[0])
        n=int(q[1])
        th1=math.radians(m)
        th2=math.radians(n)
        print("Theta1 and Theta2 in radians:",th1,th2)
        x0=0
        y0=0
        x=[]
        x1=len1*math.cos(th1)
        y1=len1*math.sin(th1)
        x.append(x0)
        x.append(x1)
        x.append(x2)
        y=[]
        y.append(y0)
        y.append(y1)
        y.append(y2)
        plt.plot(x, y,marker='D',mfc='royalblue',ms=8,color="cornflowerblue")
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.text(x0+0.03,y0+0.03,'Joint 1')
        plt.text(x1+0.05,y1+0.03,'Joint 2')
        plt.text(x2+0.05,y2,'Final Point',horizontalalignment='right')
        plt.title('Robot Hand Reverse')
        plt.show()
        k=int(input("Press 1 to stop, 2 to continue "))
        if k==1:
            p=False
        else:
            p=True
    else:
        print("Not possible to reach")
