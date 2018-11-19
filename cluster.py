import json
import math
import numpy as np
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time

#DP_T_avg_T_input_666_230.json

print('How many wells are we gonna play with? : ')
wells_num = int(input())
i=0
wells=[]
traj_x=[]
traj_y=[]
traj_z=[]
all_x=[]
all_y=[]
for i in range(0,wells_num):
    filename = input(print('Input file of well {} =  '.format(i+1)))
    open_json = open('{0}'.format(filename), 'r')
    data = json.load(open_json)
    open_json.close()
    x = data['x']
    y = data['y']
    z = data['z']
    traj_x.append(x)
    traj_y.append(y)
    traj_z.append(z)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(traj_x,traj_y,traj_z, color='blue')
    wells.append(filename)
    plt.gca().legend((wells))
    plt.show()
    #arr = {}
    #for x in xs:
    #arr[x.index] = x1

    #DP_T_mcm_T_input_666_230.json


################### 3D Plot ####################
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#x.plot_wireframe(x, y, z, color="r")
#ax.scatter3D(traj_x,traj_y,traj_z, color='blue')
#ax.scatter3D(xtarget,ytarget,ztarget*-1,color='Red',s=100)
#plt.gca().legend((wells))
#plt.show()
################### 3D Plot ####################