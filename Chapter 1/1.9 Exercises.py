# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:18:18 2023

@author: yashi
"""
import numpy as np

##%
#Q1 See written Solutins

#%%
#Q2
## Rotation of Frame Matrix

def Q_xaxis (rad):
    T=np.zeros((3,3))
    theta = rad
    for i in range(0,len(T)):
        if i == 0:
            T[i][0]= 1
        else:
            for j in range(0,len(T[i])):
                if j == 0:
                    T[i][j] = 0
                else:
                    T[i][j] = np.cos(theta - (j-i)*np.pi/2)
    return T
            
BA_T = Q_xaxis((np.pi/3))
print(BA_T)