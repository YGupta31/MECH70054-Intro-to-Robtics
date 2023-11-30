# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:54:30 2023

@author: yashi
"""

#%%
# plugins
import numpy as np



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

def T01 (t1): # t1 must be an angle
    T = [[np.cos(t1), -np.sin(t1), 0, 0], [np.sin(t1), np.cos(t1), 0, ,0], [0, 0 , 1, (a+L1)], [0, 0, 0, 1]]
    return T


def T12 (t2): # t2 must be an agnle 
    T = [[np.cos(t2), -np.sin(t2), 0, 0], [0, 0, 1, (b+L2)], [-np.sin(t2), -np.cos(t2), 0, 0], [0, 0, 0, 1]]
    return T

def T23 (d3): # d3 must be a length
    T = [[1, 0, 0, 0], [0, 0, 1, d3], [0, -1, 0, 0], [0, 0, 0, 1]]
    return T

def T34 (t4): # t4 must be an angle
    T = [[np.cos(t4), -np.sin(t4), 0, L3], [0, 0, -1, -c], [np.sin(t4), np.cos(t4), 0, 0], [0, 0, 0, 1]]
    return T

T45 = [[1, 0, 0, L4], [0, 0, -1, -e], [0, 1, 0, 0], [0, 0, 0, 1]]

#Plotting




