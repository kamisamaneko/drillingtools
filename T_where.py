import json
import math as m
import numpy as np
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time


#print('Please type your input file: ')
#fn = input()
fn ='RESULT_T_input_666_230.json'
open_json = open('{0}'.format(fn), 'r')
tdata = json.load(open_json)
open_json.close()

print('Input your TVD: ')
pz = float(input())
#print('{},{},{},{}'.format(px,py,pz,z))

start = time.time()
############second derivative####################
def deltax2(incl,azim,B,T):
    return m.radians(B)*m.cos(m.radians(incl))*m.cos(m.radians(azim))-m.radians(T)*m.sin(m.radians(incl))*m.sin(m.radians(azim))

def deltay2(incl,azim,B,T):
    return m.radians(B)*m.cos(m.radians(incl))*m.sin(m.radians(azim))+m.radians(T)*m.sin(m.radians(incl))*m.sin(m.radians(azim))

def deltaz2(incl,azim,B,T):
    return m.radians(B)*m.sin(m.radians(incl))*-1
############second derivative####################

#############curvature################
def k1(dx2,dy2,dz2):
    return m.sqrt(dx2*dx2+dy2*dy2+dz2*dz2)
def k2(br,tr,incl):
    return m.sqrt(m.radians(br)*m.radians(br)+(m.radians(tr)*m.radians(tr)*m.sin(m.radians(incl))*m.sin(m.radians(incl))))
#############curvature################

####################HD###############
def HD(xo,yo,zo,xt,yt,zt):
    vertical = zt-zo
    horizontal = m.sqrt((xt-xo)*(xt-xo)+(yt-yo)*(yt-yo))
    #return m.sqrt(vertical*vertical+horizontal*horizontal)
    return horizontal

####################HD###############

#############Radius of Curvature##########
def rok(k1):
    return 1/k1

#############Radius of Curvature##########
i=0
xo =float(tdata[0][8])
yo =float(tdata[0][9])
zo =float(tdata[0][10])
xt = float(tdata[-1][14])
yt = float(tdata[-1][15])
zt = float(tdata[-1][16])
for checkz in tdata:
    z = float(tdata[i][16])
    if z<pz :
        i=i+1
    else:
        secnum = float(tdata[i][0])
        segnum = float(tdata[i][1])
        b = float(tdata[i][4])
        t = float(tdata[i][5])
        incl = float(tdata[i][6])
        azim = float(tdata[i][7])
        x = float(tdata[i][14])
        y = float(tdata[i][15])
        z = float(tdata[i][16])
        fortype = tdata[i][18]
        mudtype = tdata[i][19]
        pumprate = tdata[i][20]
        mudweight =tdata[i][21]

################ second order derivative calculation###########
dx2=deltax2(incl,azim,b,t)
dy2=deltay2(incl,azim,b,t)
dz2=deltaz2(incl,azim,b,t)
################ second order derivative calculation###########

################ MD/TVD###########
md = tdata[i][17]
mdotvd = md/z
################ MD/TVD###########

################ curvature calculation###########
if secnum > 50:
    curv1 = k1(dx2,dy2,dz2)
    curv2 = k2(b,t,incl)
else:
    curv1 = 0
    curv2 = 0
################ curvature calculation###########

################ radius curvature calculation###########
if secnum > 50:
    rcurv = rok(curv1)
    rcurv2 = rok(curv2)
else:
    rcurv = 0
    rcurv2 = 0
################ radius curvature calculation###########

################ horizontal departure calculation###########
hrz_dep = HD(xo,yo,zo,xt,yt,zt)
################ horizontal departure calculation###########

print('At {}, your point is in section={}, segment={}, an x={}, y={}, z={}'.format(pz,secnum,segnum,x,y,z))
print('dx = {}, dy = {}, dz= {}'.format(dx2,dy2,dz2))
print('k1 = {}, k2 = {}, radius of curvature k1 = {},radius of curvature k2 = {}'.format(curv1,curv2,rcurv,rcurv2))
print('xo = {}, yo = {}, zo = {}, xt = {}, yt = {}, zt = {},I = {}, A = {}, HD = {}, MD = {}, TVD = {}, MD/TVD = {}, Formation Type = {}, Mud Type = {}, Pump Rate = {}, Mud Weight = {}'.format(xo,yo,zo,xt,yt,zt,incl,azim,hrz_dep,md,z,mdotvd,fortype,mudtype,pumprate,mudweight))

end = time.time()
time = end-start
print('Execution time {0} seconds'.format(time))