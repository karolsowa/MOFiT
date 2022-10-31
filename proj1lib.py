import numpy as np
import math

m=0.067 #m0
hw=10 #meV

def Zad1(N,L):
    tab=np.zeros((2*N+1,2*N+1))
    nlg=np.zeros((2*N*2*N+1,5))
    
    for i in range(2*N*2*N+1):  
        if i!=0:
            for j in range(5):
                ry=math.floor(i/(2*N)-0.001)
                rx=i%(2*N) 
                if j==1:
                    nlg[i,1]=i+ry
                if j==2:
                    nlg[i,2]=i+ry+1
                if rx==0:
                    rx=4
                if j==3:
                    nlg[i,3]=(2*N+1)*(1+ry)+rx
                if j==4:
                    nlg[i,4]=(2*N+1)*(1+ry)+rx+1
    return tab,nlg


