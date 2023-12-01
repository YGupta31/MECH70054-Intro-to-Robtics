# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:54:30 2023

@author: yashi
"""

#%%
# plugins
import numpy as np

import matplotlib as mtplt
import matplotlib_inline as mtpltil

#%%

#matrx multiplication

# fixed parameters

a = 0 # link offset from base to 1st joint

L1 = 0 # link lingth of 1st joint

b = 0 # link offset from 1st to 2nd joint

L2 = 0 # link length of 2nd joint

L3 = 0 # link length of third joint

c = 0 # link offset from 3rd to 4th joint

L4 = 0 # link length of end effector

e = 0 # link offset from 4th joint to end effector

#%%
#Varibale Parameters
#Forward Kinematic Matricies

def Tm01 (theta1): # theta1 must be an angle
    T = [[np.cos(theta1), -np.sin(theta1), 0, 0], [np.sin(theta1), np.cos(theta1), 0, 0], [0, 0 , 1, (a+L1)], [0, 0, 0, 1]]
    return T


def Tm12 (theta2): # theta2 must be an agnle 
    T = [[np.cos(theta2), -np.sin(theta2), 0, 0], [0, 0, 1, (b+L2)], [-np.sin(theta2), -np.cos(theta2), 0, 0], [0, 0, 0, 1]]
    return T

def Tm23 (distance3): # distance3 must be a length
    T = [[1, 0, 0, 0], [0, 0, 1, distance3], [0, -1, 0, 0], [0, 0, 0, 1]]
    return T

def Tm34 (theta4): # theta4 must be an angle
    T = [[np.cos(theta4), -np.sin(theta4), 0, L3], [0, 0, -1, -c], [np.sin(theta4), np.cos(theta4), 0, 0], [0, 0, 0, 1]]
    return T

T45 = [[1, 0, 0, L4], [0, 0, -1, -e], [0, 1, 0, 0], [0, 0, 0, 1]]

#Plotting

for t1 in range(0, 360, 90): # varies angles of t1

    T01 = Tm01(t1)
    
    for t2 in range (-90, 90, 10): # varies angles of t2
        
        T12 = Tm12(t2)
        T02 = np.matmul(T01, T12)
        
        if t2 <= 0:
            
            for d3 in range (0, 100, 5): # varies d3 for t2 less than or equal to 0
                
                T23 = Tm23(d3)
                T03 = np.matmul(T02, T23)
                
                for t4 in range(0, 360, 10): #varies t4
                    
                    T34 = Tm34(t4)
                    T04 = np.matmul(T03, T34)
                    # detrmine position of end effector
                    T05 = np.matmul(T04, T45)
                    
                    #plot point
                
        elif t2 > 0: # when t2 is greater than 0, the end effector will reach the plane.
            limit = int (np.cos((90-t2))*(a+L1) - L2 - L3) # limit defines the maximum length of d3 before reaching plane.
            if limit < 100:
                
                for d3 in range(0, limit, 5):
                    
                    T23 = Tm23(d3)
                    T03 = np.matmul(T02, T23)
                            
                    # must detrmine maximum rotation angle so that end effector will not cross plane boundary
                    for t4 in range(0, 360, 10):
                        
                        T34 = Tm34(t4)
                        T04 = np.matmul(T03, T34)
                        
                        if (a+L1)-(d3+L3+L2)*np.cos(t2) > e*np.cos(t4)+L4*np.sin(t4): # determines position only when end efector is not beyond the table plane.
                            # determine position of end effector
                            T05 = np.matmul(T04, T45)
                            # plot point
                            
            else: # when t2 is is greater than 0, and joint 4 does not reach the table plane.
                
                for d3 in range (0, 100, 5):
                    
                    T23 = Tm23(d3)
                    T03 = np.matmul(T02, T23)
                        
                    for t4 in range(0, 360, 10):
                            
                        T34 = Tm34(t4)
                        T04 = np.matmul(T03, T34)
                            
                        if (a+L1)-(d3+L3+L2)*np.cos(t2) > e*np.cos(t4)+L4*np.sin(t4): # determines position only when end efector is not beyond the table plane.
                            # determin position of end effector
                            T05 = np.matmul(T04, T45)
                            #plot point


