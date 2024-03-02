# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 02:01:58 2023

@author: User
"""
import numpy as np

#**46,96
#parametrization
h= 0.1
xmin = -5
xmax = 5
ymin=-7.5
ymax = 7.5
zmin = -15
zmax = 15
V1= 10
V2 = -5
rtol=0.1
Nmax=500
#creation of the mesh#
x = np.arange(xmin,xmax+h,h)
y = np.arange(ymin,ymax+h,h)
z = np.arange(zmin,zmax+h,h)
 


 
#creating array of V & boundary conditions
n=len(x)  #100
m=len(y)  #150
k=len(z)  #300
V=np.zeros((n,m,k))
V[45,50:101,100:201]=V1
V[55,50:101,100:201]=V2
V[1-1,:,:]=0
V[101-1,:,:]=0
V[:,151-1,:]=0
V[:,1-1,:]=0
V[:,:,1-1]=0
V[:,:,301-1]=0

boundarynodesV1= []
for e in range(50,101):
    for f in range(100,201):
        boundarynodesV1.append([45,e,f])
        
boundarynodesV2=[]
for o in range(50,101):
    for p in range(100,201):
        boundarynodesV2.append([55,o,p])
        


#%%        
allnodes=[]
for t in range(1,100):
    for y in range(1,150):
        for u in range(1,300):
            allnodes.append([t,y,u])
calculatednodes1=[x for x in allnodes if x not in boundarynodesV1]
calculatednodes=[x for x in calculatednodes1 if x not in boundarynodesV2]
#%%
np.save("calculated nodes",calculatednodes)



#%%
calculatednodes= np.load("calculated nodes.npy")
for a in range(Nmax):
    for [i,j,l] in calculatednodes:
        V[i,j,l]=(V[i+1,j,l]+V[i-1,j,l]+V[i,j-1,l]+V[i,j+1,l]+V[i,j,l-1]+V[i,j,l+1])/6
    
np.save("V array 2",V)
quit()

#%%

import plotly.graph_objects as go

X, Y, Z = np.mgrid[x, y, z]
values = V

fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=0.1,
    isomax=0.8,
    opacity=0.1, # needs to be small to see through all surfaces
    surface_count=17, # needs to be a large number for good volume rendering
    ))
fig.show()                    