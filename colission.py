import json
import math
import numpy as np
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time
import random

def warna():
    x = random.randint(1, 6)
    if x == 1:
        iro="blue"
    elif x ==2:
        iro="green"
    elif x ==3:
        iro="yellow"
    elif x ==4:
        iro="red"
    elif x ==5:
        iro="cyan"
    elif x ==6:
        iro="magenta"
    return iro

# print('Longest X : ')
# xt = int(input())
# print('Longest Y : ')
# yt = int(input())
# print('Longest Z : ')
# zt = int(input())
# print('Origin X : ')
# xo = int(input())
# print('Origin Y : ')
# yo = int(input())
# print('Origin Z : ')
# zo = int(input())
# print('Grid Area : ' )
# grid = int(input())

print('Longest X : ')
xt =8300
print('Longest Y : ')
yt = -2200
print('Longest Z : ')
zt = 5600
print('Origin X : ')
xo = 0
print('Origin Y : ')
yo = 0
print('Origin Z : ')
zo = 0
print('Grid Area : ' )
grid = 50

print('How many wells are we gonna play with? : ')
g=globals()
wells_num = int(input())
i=0
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
start = time.time()


#area mapping
area_length = 2*np.abs(xt-xo)
area_wide = 2*np.abs(yt-yo)
area_deep = np.abs(zt-zo)
grid_row = area_length/grid
grid_coloum = area_wide/grid
grid_deep = area_deep/grid
xs = xo-np.abs(xt-xo)
ys = yo+np.abs(yt-yo)
zs = 1300
#array assignment

trak_x = []
trak_y = []
trak_z = []
A=[0,0,0]
B=[0,0,0]
C=[0,0,0]
D=[0,0,0]
AP=[0,0,0]
BP=[0,0,0]
CP=[0,0,0]
DP=[0,0,0]
xmax=[0]
ymax=[0]
zmax=[0]
xmin=[0]
ymin=[0]
zmin=[0]
counter=0

i=0;j=0;k=0

for k in range(0,int(grid_deep)):
    for j in range(0,int(grid_coloum)):
        for i in range(0,int(grid_row)):
            box = 'box_{}_{}_{}'.format(i,j,k)
            g[box] = [A,B,C,D,AP,BP,CP,DP,xmax,xmin,ymax,ymin,zmax,zmin]
            A[0]=xs+(grid*i)
            A[1]=ys-(grid*j)
            A[2]=zs-(grid*k)
            g[box][0]=[A[0],A[1],A[2]]
            trak_x.append(g[box][0][0])
            trak_y.append(g[box][0][1])
            trak_z.append(g[box][0][2])
            #B
            g[box][1]=[g[box][0][0]+grid,g[box][0][1],g[box][0][2]]
            trak_x.append(g[box][1][0])
            trak_y.append(g[box][1][1])
            trak_z.append(g[box][1][2])
            #C
            g[box][2]=[g[box][0][0]+grid,g[box][0][1]-grid,g[box][0][2]]
            trak_x.append(g[box][2][0])
            trak_y.append(g[box][2][1])
            trak_z.append(g[box][2][2])
            #D
            g[box][3]=[g[box][0][0],g[box][0][1]-grid,g[box][0][2]]
            trak_x.append(g[box][3][0])
            trak_y.append(g[box][3][1])
            trak_z.append(g[box][3][2])
            #AP
            g[box][4]=[g[box][0][0],g[box][0][1],g[box][0][2]-grid]
            trak_x.append(g[box][4][0])
            trak_y.append(g[box][4][1])
            trak_z.append(g[box][4][2])
            #BP
            g[box][5]=[g[box][1][0],g[box][1][1],g[box][0][2]-grid]
            trak_x.append(g[box][5][0])
            trak_y.append(g[box][5][1])
            trak_z.append(g[box][5][2])
            #CP
            g[box][6]=[g[box][2][0],g[box][2][1],g[box][0][2]-grid]
            trak_x.append(g[box][6][0])
            trak_y.append(g[box][6][1])
            trak_z.append(g[box][6][2])
            #DP
            g[box][7]=[g[box][3][0],g[box][3][1],g[box][0][2]-grid]
            trak_x.append(g[box][7][0])
            trak_y.append(g[box][7][1])
            trak_z.append(g[box][7][2])
            #xmax
            max_x=max(g[box][0][0],g[box][6][0])
            #xmin
            min_x=min(g[box][0][0],g[box][6][0])
            #ymax
            max_y=max(g[box][0][1],g[box][6][1])
            #ymin
            min_y=min(g[box][0][1],g[box][6][1])
            #zmax
            max_z=max(g[box][0][2],g[box][6][2])
            #zmin
            min_z=min(g[box][0][2],g[box][6][2])
            g[box][8]=max_x
            g[box][9]=min_x
            g[box][10]=max_y
            g[box][11]=min_y
            g[box][12]=max_z
            g[box][13]=min_z

# for k in range(0,int(grid_deep)):
#     for j in range(0,int(grid_coloum)):
#         for i in range(0,int(grid_row)):
#             box = 'box_{}_{}_{}'.format(i,j,k)
#             print("***********")
#             print(box)
#             print(g[box])


################### 3D Plot ####################
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(trak_x,trak_y,trak_z, color='blue')
ax.scatter3D(xs,ys,zs,color='yellow')
ax.scatter3D(xo,yo,zo,color='red')

i=0;j=0;k=0;a=0;
zz=0;yy=0;xx=0;
step=0
counter=0
col = 0
for k in range(0,int(grid_deep)):
    for j in range(0,int(grid_coloum)):
        for i in range(0,int(grid_row)):
            for a in range(0,wells_num):
                box = 'box_{}_{}_{}'.format(i,j,k)
                arx = 'traj_x{}'.format(a)
                ary = 'traj_y{}'.format(a)
                arz = 'traj_z{}'.format(a)
                len_arx = len(g[arx][0])
                len_ary = len(g[ary][0])
                len_arz = len(g[arz][0])
                len_ark= len(traj_x0[0])
                for zz in range(0,int(len_arz)):
                    #print("xx={},yy={},zz={}".format(xx,yy,zz))
                    xmax = g[box][8]
                    xmin = g[box][9]
                    ymax = g[box][10]
                    ymin = g[box][11]
                    zmax = g[box][12]
                    zmin = g[box][13]
                    px = g[arx][0][zz]
                    py =g[ary][0][zz]
                    pz = -1*g[arz][0][zz]
                    step=step+1
                    elaps = time.time()
                    clock = start-elaps
                    print("X={}<{}<{}---Y={}<{}<{}---Z={}<{}<{}---zz={},counter={},col={},box={},I={},J={},K={},STEP={},Well={},Time={}".format(xmin,px,xmax,ymin,py,ymax,zmin,pz,zmax,zz,counter,col,box,i,j,k,step,a,clock))
                    if xmin<=px and px<=xmax and ymin<=py and py<=ymax and zmin<=pz and pz<=zmax:
                        counter = counter + 1
                    if counter > 2:
                        col = col+1
                        counter = 0
                        print("MIN DISTANCE BREACH AT {}, x={},y={},z={}".format(box,g[box][8],g[box][10],g[box][12]))


for j in range (0,wells_num):
    arx = 'traj_x{}'.format(j)
    ary = 'traj_y{}'.format(j)
    arz = 'traj_z{}'.format(j)
    fn = 'file_{}'.format(j)
    ax.scatter3D(g[arx],g[ary],g[arz],color=warna(), label=g[fn])
    legend = ax.legend(loc='upper left')

    # Put a nicer background color on the legend.
    legend.get_frame()

ax.set_xlabel('N(x)')
ax.set_ylabel('E(y)')
ax.set_zlabel('Z')
end = time.time()
time = end-start
print('Execution time {0} seconds'.format(time))
plt.show()
################### 3D Plot ####################
