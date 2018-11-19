import json
import math
import numpy as np
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time

start = time.time()

#############################open data & variable asignment#####################################
fn ='T_input_001_001.json'
open_json = open('{0}'.format(fn), 'r')
tdata = json.load(open_json)

#variable asignment
method = tdata['T_Method']
cluster= int(tdata['T_Cluster'])
api = int(tdata['T_API'])

#variable asigment for start position
xo = float(tdata['T_Surface']['T_xo'])
yo = float(tdata['T_Surface']['T_yo'])
zo = float(tdata['T_Surface']['T_zo'])

#variable asigment for target position
xtarget = float(tdata['T_Target']['T_xt'])
ytarget = float(tdata['T_Target']['T_yt'])
ztarget = float(tdata['T_Target']['T_zt'])

#other variable asignment
tol= float(tdata['T_Tolerance'])*1.5
kop = float(tdata['T_KOP'])
lead= float(tdata['T_Lead Angle'])

#############################section part######################################################

section = tdata['T_section']

#closing json
#############################section part######################################################
open_json.close()

#############################open data & variable asignment#####################################

###############################preliminary information#########################################
print("Dude, you are working for well cluster {0}, with API number {1}".format(cluster,api))
print("Your starting point is {0}, {1}, {2} and your target is at {3}, {4}, {5}.".format(xo,yo,zo,xtarget,ytarget,ztarget))
print("You are using {0} method to built the trajectory with tolerance of {1} ".format(method, tol))

#counting total section
i=50
for secnum in section:
    i=i+1
print("You have {0} sections including 50 sections before KOP at {1}\n following are your sections after KOP".format(i,kop))
datapoint = int(tdata['T_datapoint'])
dp = int(datapoint/i)
print("you will have {0} data points per section".format(dp))

###############################preliminary information#########################################

########################################section before KOP#########################################
#iniziation
j=0
jj=0
xi=xo
yi=yo
zi=zo
#array
bsection=[]
psection=[]
traj_x=[xi]
traj_y=[yi]
traj_z=[zi]
segnum = 0
secnum = 0

for j in range(0,50):
    secnum = secnum+1
    for jj in range(0,dp):
        #calculation
        dx = 0
        dy = 0
        dz = (kop/50)/dp
        xt = xi+dx
        yt = yi+dy
        zt = zi+dz
        #atribut
        segnum = segnum+1
        incl = 0
        #azim = (float(tdata['T_Lead Angle'])+float(tdata['T_Lead Target'])-(float(section[0]['T_TR'])/float(section[0]['T_rate_length'])*float(section[0]['T_length'])))/2
        azim=(float(tdata['T_Lead Angle'])+float(tdata['T_Lead Target']))/2
        br = 0
        tr = 0
        #add data to list
        bsection.append(('Section Number = {0}'.format(secnum),'Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl),'A = {0}'.format(azim),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt)))
        psection.append((secnum,segnum,cluster,api,br,tr,incl,azim,xi,yi,zi,dx,dy,dz,xt,yt,zt))
        traj_x.append(xt)
        traj_y.append(yt)
        traj_z.append(zt*-1)
        #iteration properties
        xi=xt
        yi=yt
        zi=zt

for beforeKOP_section in bsection:
    print(beforeKOP_section)
########################################section before KOP#########################################


#################after KOP##################################################################
#inizaiation
mdsection=0
#w=0
#ww=0
#for w in range(50,i):
 #   mdsection = float(section[ww]['T_length'])+mdsection
  #  if mdsection <= float(tdata['T_Angle Hold']):
   #     ww=ww+1
    #else:
     #   ww=ww
k=0
kk=0
ii=0
#asection=[]
xi=xt
yi=yt
zi=zt
ddx = 'deltax'
ddy = 'deltay'
ddz = 'deltaz'
# for k in range(50,50+ww):
#     #atribut
#     secnum = secnum+1
#     incl_t=float(section[ii]['T_BR'])/float(section[ii]['T_rate_length'])*float(section[ii]['T_length'])+incl
#     azim_t= azim
#     br=float(section[ii]['T_BR'])
#     tr=float(section[ii]['T_TR'])
#     seglength = float(section[0]['T_length'])
#     #calculation
#     dx = calculation(method, ddx, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
#     dy = calculation(method, ddy, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
#     dz = calculation(method, ddz, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
#     xt = xi+dx
#     yt = yi+dy
#     zt = zi+dz
#     #add data to list
#     asection.append(('Section Number = {0}'.format(secnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl_t),'A = {0}'.format(azim_t),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt)))
#     #iteration properties
#     xi=xt
#     yi=yt
#     zi=zt
#     ii=ii+1
#     incl=incl_t
#     azim=azim_t

for k in range(50,i):
    secnum = secnum+1
    incl_t=float(section[0]['T_BR'])/float(section[0]['T_rate_length'])*float(section[0]['T_length'])+incl
    azim_t=float(section[0]['T_TR'])/float(section[0]['T_rate_length'])*float(section[0]['T_length'])+azim
    br=float(section[0]['T_BR'])
    tr=float(section[0]['T_TR'])
    seglength = (float(section[0]['T_length']))
    for kk in range(0,dp):
        #atribut
        segnum = segnum+1
        #calculation
        dx = calculation(method, ddx, xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp)
        dy = calculation(method, ddy, xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp)
        dz = calculation(method, ddz, xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp)
        xt = xi+dx
        yt = yi+dy
        zt = zi+dz
        #add data to list
        bsection.append(('Section Number = {0}'.format(secnum),'Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl),'A = {0}'.format(azim),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt)))
        psection.append((secnum,segnum,cluster,api,br,tr,incl,azim,xi,yi,zi,dx,dy,dz,xt,yt,zt))
        traj_x.append(xt)
        traj_y.append(yt)
        traj_z.append(zt*-1)
        #iteration properties
        xi=xt
        yi=yt
        zi=zt
    incl=incl_t
    azim=azim_t


for afterKOP_section in bsection:
    print(afterKOP_section)

################after KOP##################################################################

#############################################write output########################################
with open('OUT_{0}'.format(fn),'w')as outfile:
    json.dump(bsection, outfile)
with open('value_{0}'.format(fn),'w')as outfile:
    json.dump(psection, outfile)
#################################################################################################

#####################HIT TARGET###########################################
distance = (((xtarget-xt)*(xtarget-xt))+((ytarget-yt)*(ytarget-yt))+((ztarget-zt)*(ztarget-zt))**0.5)
dis = float(distance)
if dis <= tol:
    print('your trajectory hit the target with distance of {0} from target'.format(dis))
else:
    print('miss target, {0} from target'.format(dis))
#####################HIT TARGET###########################################

end = time.time()
time = end-start
print('Execution time {0} seconds'.format(time))

################### 3D Plot ####################
fig = plt.figure()
ax = plt.axes(projection='3d')
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
#ax.plot3D(traj_x, traj_y, traj_z, 'blue')
ax.scatter3D(traj_x,traj_y,traj_z, color='Blue')
ax.scatter3D(xtarget,ytarget,ztarget*-1,color='Red',s=20)
plt.show()
################### 3D Plot ####################

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')
# plt.show()

# for ttt in range(0,segnum):
#     xdata = [bsection[ttt][14]]
#     ydata = [bsection[ttt][15]]
#     zdata = [bsection[ttt][16]]
#
# print(traj_x)