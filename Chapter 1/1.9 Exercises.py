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
    
    P_final = P_out[0:3] # remove homogeenous form
    return P_final

#Answer

theta = np.pi/6 # theta == 30deg
B_0 = [2,4,3]
P_B = [2,4,1]
BA_T = T_hom(Q_yaxis(theta), B_0)
print(BA_T)#check homogenous tarnsformation
P_A = MatMul_hom(BA_T, P_B)
print(P_A) #check position vector

#%%

##Q4
# 4a check written answers
R=[[(np.sqrt(2))/2, -0.5, -0.5], [0.5, ((np.sqrt(2))/4)+0.5, ((np.sqrt(2))/4)-0.5], [0.5,((np.sqrt(2))/4)-0.5, ((np.sqrt(2))/4)+0.5]]    
#4b Angle and unit vector of rotation matrix

def decomp_Rot (Q): #Function to decompose a rotation matrix Q into its angle and unit vector
    alpha = np.arccos((np.trace(Q)-1)/2) # gives the angle in radians
    # determine axis of rotatin vector
    u = np.zeros((3,1)) # form size of rotation axis
    u[0] = (1/(2*np.sin(alpha)))*(Q[2][1]-Q[1][2])
    u[1] = (1/(2*np.sin(alpha)))*(Q[0][2]-Q[2][0])
    u[2] = (1/(2*np.sin(alpha)))*(Q[2][0]-Q[0][2])
    

    return (u,alpha)

#Answer

print(decomp_Rot(R))    
    
#4c   
    