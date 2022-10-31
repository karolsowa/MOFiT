import numpy as np
import proj1lib as lib

N=2
L=100
psi=1

tab,nlg=lib.Zad1(N,L)

print(tab,nlg)

for x in range(2*N*2*N):
    for y in range(4):
        xx=x+1
        yy=y+1
        if yy==1 or yy==2:
            wy=-1
        else:
            wy=1
        if yy==1 or yy==3:
            wx=-1
        else:
            wx=1
        print('nr elementu:',xx,'nr wezla lok:',yy,'nr wezla glob:',nlg[xx,yy], 'wspolrzedne',wx,wy)

