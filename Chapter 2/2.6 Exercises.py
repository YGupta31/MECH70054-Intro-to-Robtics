# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:01:46 2023

@author: yashi
"""
import numpy as np

#%%

def mm_1_T(a_m0,alpha_m0,d_m1, theta_m1):#base to end effecetor matrix homogenous transfromation from a row of Denavit-Hartenberg parameters
    T = np.zeros((4,4))
    T[4][4]=1
    T[0] = [np.cos(theta_m1), -np.sin(theta_m1), 0, a_m0]
    T[1] = [np.sin(theta_m1)*np.cos(alpha_m0), np.cos(theta_m1)*np.cos(alpha_m0), -np.sin(alpha_m0), -np.sin(alpha_m0)*d_m1]
    T[2] = [np.sin(theta_m1)*np.sin(alpha_m0), np.cos(theta_m1)*np.sin(alpha_m0), np.cos(alpha_m0), np.cos(alpha_m0)*d_m1]
    return T










