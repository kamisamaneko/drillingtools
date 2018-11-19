import json
import math
import numpy as np
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time

#

# def random_color():
#     rgbl=[255,0,0]
#     np.random.shuffle(rgbl)
#     return tuple(rgbl)

print('How many wells are we gonna play with? : ')

wells_num = int(input())
start = time.time()
i=0
g = globals()
j=0
for i in range(0,wells_num):
    filename = input(print('Input file of well {} =  '.format(i+1)))
    open_json = open('{0}'.format(filename), 'r')
    data = json.load(open_json)
    open_json.close()
    wellname= 'wells{}'.format(i)
    arx = 'traj_x{}'.format(i)
    ary = 'traj_y{}'.format(i)
    arz = 'traj_z{}'.format(i)
    fn = 'file_{}'.format(i)
    #checker


    g[fn]=[]
    g[wellname]=[]
    g[arx]=[]
    g[ary]=[]
    g[arz]=[]
    x = data['x']
    y = data['y']
    z = data['z']
    g[arx].append(x)
    g[ary].append(y)
    g[arz].append(z)
    g[fn].append(filename)
N=945
colors = np.random.rand(N)
fig=plt.figure()
ax = plt.axes(projection='3d')
for j in range (0,wells_num):
    arx = 'traj_x{}'.format(j)
    ary = 'traj_y{}'.format(j)
    arz = 'traj_z{}'.format(j)
    fn = 'file_{}'.format(j)
    ax.scatter3D(g[arx],g[ary],g[arz],color='blue', label=g[fn])
    legend = ax.legend(loc='upper left')

# Put a nicer background color on the legend.
    legend.get_frame()


plt.show()




