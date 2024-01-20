# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:54:30 2023

@author: yashi
"""

#%%
# plugins
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib_inline as il

#%%

#matrx multiplication

# fixed parameters

a = 5 # link offset from base to 1st joint

L1 = 20 # link lingth of 1st joint

b = 10 # link offset from 1st to 2nd joint

L2 = 5 # link length of 2nd joint

L3 = 0 # link length of third joint

c = 0 # link offset from 3rd to 4th joint

L4 = 4 # link length of end effector

e = 2 # link offset from 4th joint to end effector

d3max = 30
interval = int(d3max/5)

#%%
#Varibale Parameters
#Forward Kinematic Matricies

def Tm01 (theta1): # theta1 must be an angle
    T = [[np.cos(theta1*(np.pi/180)), -np.sin(theta1*(np.pi/180)), 0, 0], [np.sin(theta1*(np.pi/180)), np.cos(theta1*(np.pi/180)), 0, 0], [0, 0 , 1, (a+L1)], [0, 0, 0, 1]]
    return T


def Tm12 (theta2): # theta2 must be an agnle 
    T = [[np.cos(theta2*(np.pi/180)), -np.sin(theta2*(np.pi/180)), 0, 0], [0, 0, 1, (b)], [-np.sin(theta2*(np.pi/180)), -np.cos(theta2*(np.pi/180)), 0, 0], [0, 0, 0, 1]]
    return T

def Tm23 (distance3): # distance3 must be a length
    T = [[1, 0, 0, 0], [0, 0, 1, distance3+L2], [0, -1, 0, 0], [0, 0, 0, 1]]
    return T

def Tm34 (theta4): # theta4 must be an angle
    T = [[np.cos(theta4*(np.pi/180)), -np.sin(theta4*(np.pi/180)), 0, L3], [0, 0, -1, -c], [np.sin(theta4*(np.pi/180)), np.cos(theta4*(np.pi/180)), 0, 0], [0, 0, 0, 1]]
    return T

T45 = [[1, 0, 0, L4], [0, 0, -1, -e], [0, 1, 0, 0], [0, 0, 0, 1]]

#Plotting

# create sets for x,y and z coordinates for each joint

x1=[]
x2=[]
x3=[]
x4=[]
x5=[]

y1=[]
y2=[]
y3=[]
y4=[]
y5=[]

z1=[]
z2=[]
z3=[]
z4=[]
z5=[]

# x point will be T0X [0][3], y point will be T0X [1][3], zpoint will be T0X [2][3]

for t1 in range(0, 360, 90): # varies angles of t1

    T01 = Tm01(t1)
    x1=x1+[T01[0][3]]
    y1=y1+[T01[1][3]]
    z1=z1+[T01[2][3]-L1]
    for t2 in range (180, 360, 30): # varies angles of t2
        
        T12 = Tm12(t2)
        T02 = np.matmul(T01, T12)
        x2=x2+[T02[0][3]]
        y2=y2+[T02[1][3]]
        z2=z2+[T02[2][3]]
        if t2 <= 270:
            
            for d3 in range (0, d3max, interval): # varies d3 for t2 less than or equal to 0
                
                T23 = Tm23(d3)
                T03 = np.matmul(T02, T23)
                
                x3=x3+[T03[0][3]]
                y3=y3+[T03[1][3]]
                z3=z3+[T03[2][3]]
                
                for t4 in range(0, 360, 30): #varies t4
                    
                    T34 = Tm34(t4)
                    T04 = np.matmul(T03, T34)
                    x4=x4+[T04[0][3]]
                    y4=y4+[T04[1][3]]
                    z4=z4+[T04[2][3]]
                    # detrmine position of end effector
                    T05 = np.matmul(T04, T45)
                    
                    x5=x5+[T05[0][3]]
                    y5=y5+[T05[1][3]]
                    z5=z5+[T05[2][3]]
                    
                    #For a single 2d plane plot T0X
        else: # when t2 is greater than 270, the end effector will reach the plane.
            limit = int((a+L1)/np.cos((360-t2)*(np.pi/180)) - L2 - L3) # limit defines the maximum length of d3 before reaching plane.
            if limit < d3max:
                
                for d3 in range(0, limit, interval):
                    
                    T23 = Tm23(d3)
                    T03 = np.matmul(T02, T23)
                    
                    x3=x3+[T03[0][3]]
                    y3=y3+[T03[1][3]]
                    z3=z3+[T03[2][3]]
                    
                    # must detrmine maximum rotation angle so that end effector will not cross plane boundary
                    for t4 in range(0, 360, 30):
                        
                        T34 = Tm34(t4)
                        T04 = np.matmul(T03, T34)
                        
                        x4=x4+[T04[0][3]]
                        y4=y4+[T04[1][3]]
                        z4=z4+[T04[2][3]]
                        heighte = int(e*np.cos(t4*(np.pi/180))+L4*np.sin(t4*(np.pi/180)))
                        if heighte<int((a+L1)-(d3+L3+L2)*np.cos(t2*(np.pi/180))): # determines position only when end efector is not beyond the table plane.
                            # determine position of end effector
                            T05 = np.matmul(T04, T45)
                            
                            x5=x5+[T05[0][3]]
                            y5=y5+[T05[1][3]]
                            z5=z5+[T05[2][3]]
                            
                            
            else: # when t2 is is greater than 0, and joint 4 does not reach the table plane.
                
                for d3 in range (0, d3max, interval):
                    
                    T23 = Tm23(d3)
                    T03 = np.matmul(T02, T23)
                    
                    x3=x3+[T03[0][3]]
                    y3=y3+[T03[1][3]]
                    z3=z3+[T03[2][3]]
                    
                    for t4 in range(0, 360, 30):
                            
                        T34 = Tm34(t4)
                        T04 = np.matmul(T03, T34)
                        
                        x4=x4+[T04[0][3]]
                        y4=y4+[T04[1][3]]
                        z4=z4+[T04[2][3]]
                        heighte = int(e*np.cos(t4*(np.pi/180))+L4*np.sin(t4*(np.pi/180)))
                        if heighte<int((a+L1)-(d3+L3+L2)*np.cos(t2*(np.pi/180))): # determines position only when end efector is not beyond the table plane.
                            # determin position of end effector
                            T05 = np.matmul(T04, T45)
                            
                            x5=x5+[T05[0][3]]
                            y5=y5+[T05[1][3]]
                            z5=z5+[T05[2][3]]
                          
print(len(y1)) 
""    
print(len(y2))
""
print(len(y3))
""
print(len(y4))
""
print(len(y5))
#%%
#plot points on same axis

#2d slice
x = np.linspace(-5, 45, 5)
z = np.zeros(len(x))
i = int(len(x1)/len(x1))
j = int(len(x2)/len(x1))
k = int(len(x3)/len(x1))
l = int(len(x4)/len(x1))
m = int(len(x5)/len(x1))

fig = plt.figure()
ax = plt.axes()

ax.scatter(x1[:i], z1[:i], c='r')
ax.scatter(x2[:j], z2[:j], c='b')
ax.scatter(x3[:k], z3[:k], c='g')

ax.scatter(x4[:l], z4[:l], c='g')
ax.scatter(x5[:m],z5[:m], marker ='^', c='b')
ax.plot( x,z ,c='g')
plt.show()

#%%
#3d slice

fig = plt.figure()
ax3 = plt.axes(projection='3d')

ax3.scatter(x1, y1, z1, c='r')
ax3.scatter(x2, y2, z2, c='b')
ax3.scatter(x3, y3, z3, c='g')

ax3.scatter(x4, y4, z4, c='g')
ax3.scatter(x5,y5, z5, marker ='^', c='b')
plt.show()
#%%

#calculating Jacobian
#determine velocities of links

#velocity equations



# angular velocity 

## revolute joint

def Romega (i1Ri, iomegai, thetadoti1):
    
    omega = np.matmul(i1Ri,iomegai) + [0,0,thetadoti1] 
    
    return omega

## prismatic joint

def Pomega (i1Ri, iomegai):
    
    omega = np.matmul(i1Ri,iomegai)
    
    return omega

# linear velocity

## revolute joint

def RV (i1Ri, iVi, iomegai, iPoi1):
    
    iVi1 = iVi + np.cross(iomegai, iPoi1)
    
    V = np.matmul(i1Ri,iVi1)
    
    return V

## prismatic joint

def PV (i1Ri, iVi, iomegai, iPoi1, ddoti1):
    
    iVi1 = iVi + np.cross(iomegai, iPoi1)
    
    V = np.matmul(i1Ri, iVi1) + [0,0,ddoti1]
    
    return V

# velocity of link 1 relative to frame {1}

1V1

# velocity of link 2 realtive to frame {2}


# velocity of link 3 relative to frame {3}


# velocity of link 4 realyive to frame {4}


# velocity of link 5 realtive to frame {5}


# velocity of end effector relative to base


