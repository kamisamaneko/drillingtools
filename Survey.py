import json
import math
import numpy as np
from S_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time

def translate(azimuth):
    if azimuth[0]=='N' and azimuth[-1]=='E':
        degree = 0
        azim = degree + float(azimuth[1:-1])
    elif azimuth[0]=='N' and azimuth[-1]=='W':
        degree = 360
        azim = degree - float(azimuth[1:-1])
    elif azimuth[0]=='S' and azimuth[-1]=='E':
        degree = 180
        azim = degree - float(azimuth[1:-1])
    elif azimuth[0]=='S' and azimuth[-1]=='W':
        degree= 180
        azim = 180+float(azimuth[1:-1])
    return azim

#############################start-open data & variable asignment#####################################
fn ='S_input_666_230.json'
open_json = open('{0}'.format(fn), 'r')
tdata = json.load(open_json)

method = tdata['S_Method']
cluster= int(tdata['S_Cluster'])
api = int(tdata['S_API'])

xo = float(tdata['S_Surface']['S_xo'])
yo = float(tdata['S_Surface']['S_yo'])
zo = float(tdata['S_Surface']['S_zo'])

section = tdata['S_section']

#############################section part######################################################
#closing json
open_json.close()
#closing json

#############################end-open data & variable asignment#####################################

###############################preliminary information#########################################
print("Dude, you are working for well cluster {0}, with API number {1}".format(cluster,api))
print("Your starting point is {0}, {1}, {2}".format(xo,yo,zo))
print("You are using {0} method to built the survey  ".format(method))

#counting total section
i=1
for secnum in section:
    i=i+1
print("You have {0} recorded datas".format(i))
#iniziation
k=0
kk=0
ii=0
xi=xo
yi=yo
zi=zo
mdsection = 0

#array
bsection=[]
psection=[]

#x,y,z array
traj_x=[xi]
traj_y=[yi]
traj_z=[zi]
secnum = 0

for k in range(k,i-2):
    secnum = secnum+1
    incl = float(section[k]['S_I'])
    azim_r= section[k]['S_A']
    azim = float(translate(azim_r))
    incl_t=float(section[k+1]['S_I'])
    azim_tr=section[k+1]['S_A']
    azim_t=float(translate(azim_tr))
    seglength = (float(section[k]['S_MD']))
    br = (azim_t-azim)/seglength
    tr = (incl_t-incl)/seglength
    dp = secnum
    segnum = secnum
    fortype = section[k]['S_ForType']
    mudtype = section[k]['S_MudType']
    pumprate = section[k]['S_PumpRate']
    mudweight =section[k]['S_MudWeight']

    dx = calculation(method, 'deltax', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
    dy = calculation(method, 'deltay', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
    dz = calculation(method, 'deltaz', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
    xt = xi+dx
    yt = yi+dy
    zt = zi+dz
    mdsection = mdsection + seglength
    #add data to list
    bsection.append(('Section Number = {0}'.format(secnum),'Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl),'A = {0}'.format(azim),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt),'MD = {}'.format(mdsection),'Formation = {}'.format(fortype),'Mud Type = {}'.format(mudtype),'Mud Weight = {}'.format(mudweight),'Pump Rate = {}'.format(pumprate)))
    psection.append((secnum,segnum,cluster,api,br,tr,incl,azim,xi,yi,zi,dx,dy,dz,xt,yt,zt,mdsection,fortype,mudtype,pumprate,mudweight))
    traj_x.append(xt)
    traj_y.append(yt)
    traj_z.append(zt*-1)
    #iteration properties
    xi=xt
    yi=yt
    zi=zt
    incl=incl_t
    azim=azim_t

#########last data##########
secnum = secnum+1
incl = float(section[k+1]['S_I'])
azim_r= section[k+1]['S_A']
azim = float(translate(azim_r))
incl_t=float(section[k+1]['S_I'])
azim_tr=section[k+1]['S_A']
azim_t=float(translate(azim_tr))
seglength = (float(section[k+1]['S_MD']))
br = (azim_t-azim_t)/seglength
tr = (incl_t-incl_t)/seglength
dp = secnum
segnum = secnum
fortype = section[k+1]['S_ForType']
mudtype = section[k+1]['S_MudType']
pumprate = section[k+1]['S_PumpRate']
mudweight =section[k+1]['S_MudWeight']

dx = calculation(method, 'deltax', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
dy = calculation(method, 'deltay', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
dz = calculation(method, 'deltaz', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
xt = xi+dx
yt = yi+dy
zt = zi+dz
mdsection = mdsection + seglength
#add data to list
bsection.append(('Section Number = {0}'.format(secnum),'Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl),'A = {0}'.format(azim),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt),'MD = {}'.format(mdsection),'Formation = {}'.format(fortype),'Mud Type = {}'.format(mudtype),'Mud Weight = {}'.format(mudweight),'Pump Rate = {}'.format(pumprate)))
psection.append((secnum,segnum,cluster,api,br,tr,incl,azim,xi,yi,zi,dx,dy,dz,xt,yt,zt,mdsection,fortype,mudtype,pumprate,mudweight))
traj_x.append(xt)
traj_y.append(yt)
traj_z.append(zt*-1)
#########last data##########


for afterKOP_section in bsection:
    print(afterKOP_section)

#########wrintin files########
with open('OUT_S_{0}'.format(fn),'w')as outfile:
    json.dump(bsection, outfile)
with open('RESULT_S_{0}'.format(fn),'w')as outfile:
    json.dump(psection, outfile)


##########Graph#############
################### 3D Plot ####################
fig = plt.figure()
ax = plt.axes(projection='3d')
#x = np.cos(u)*np.sin(v)
#y = np.sin(u)*np.sin(v)
#z = np.cos(v)
#ax.plot_wireframe(x, y, z, color="r")
ax.plot3D(traj_x,traj_y,traj_z, color='blue')
plt.show()
################### 3D Plot ####################
