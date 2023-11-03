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
## Rotation of Frame Matrix about x

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

#%%
#Q3

# Rotation of Frame Matrix about y
def Q_yaxis (rad):
    T=np.zeros((3,3))
    theta = rad
    for i in range(0,len(T)):
        if i == 1:
            T[i][1]= 1
        else:
            for j in range(0,len(T[i])):
                if j == 1:
                    T[i][j] = 0
                else:
                    T[i][j] = np.cos(theta - (j-i)*np.pi/2)
    return T

#Form homogeneous matrix

def T_hom (Q, V): #Rotation matrix Q and translation vector V
    T=np.zeros((4,4))
    for i in range(0,len(T)):
        if i==3:
            T[i][3]=1
        else:
            for j in range(0, len(T[i])):
                if j==3:
                    T[i][j]=V[i]
                elif j<3:
                    T[i][j]=Q[i][j]
    return T

def MatMul_hom (T, P): #Matrix Multiplication of a homogenous transformation T and a position vector P
    P_hom = P+[1] #convert P into homogeneous form
    P_out = np.matmul(T,P_hom)
    
    P_A = P[0:3] # remove homogeenous form
    return P_A
