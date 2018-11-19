import json
import math
import numpy as np
#from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d
#from mpl_toolkits import Axes3d
import matplotlib.pyplot as plt
import time

start = time.time()

#############################start-open data & variable asignment#####################################
fn ='T_input_666_235.json'
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
#############################section part######################################################
#closing json
open_json.close()
#closing json

#############################end-open data & variable asignment#####################################

###############################preliminary information#########################################
print("Dude, you are working for well cluster {0}, with API number {1}".format(cluster,api))
print("Your starting point is {0}, {1}, {2} and your target is at {3}, {4}, {5}.".format(xo,yo,zo,xtarget,ytarget,ztarget))
print("You are using {0} method to built the trajectory with tolerance of {1} ".format(method, tol))

#counting total section
i=50
for secnum in section:
    i=i+1
print("You have {0} sections including 50 sections before KOP at {1}\n following are your sections after KOP".format(i,kop))
datapoint = float(tdata['T_datapoint'])
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
mdsection = 0
azim_init = 0


for azim_init in range(0,360):
    for j in range(0,50):
        secnum = secnum+1
        fortype = tdata['T_Formation']
        mudtype = tdata['T_MudType']
        pumprate = tdata['T_PumpRate']
        mudweight =tdata['T_MudWeight']
        for jj in range(0,dp):
            #calculation
            dx = 0
            dy = 0
            dz = (kop/50)/dp
            xt = xi+dx
            yt = yi+dy
            zt = zi+dz
            #data
            #atribut
            segnum = segnum+1
            incl = 0
            #azim = (float(tdata['T_Lead Angle'])+float(tdata['T_Lead Target'])-(float(section[0]['T_TR'])/float(section[0]['T_rate_length'])*float(section[0]['T_length'])))/2
            azim=azim_init
            br = 0
            tr = 0
            mdsection = zt
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

    #for beforeKOP_section in bsection:
        #print(beforeKOP_section)
    ########################################section before KOP#########################################

    #################after KOP##################################################################
    #inizaiation
    k=0
    kk=0
    ii=0
    #asection=[]
    xi=xt
    yi=yt
    zi=zt

    for k in range(50,i):
        secnum = secnum+1
        incl_t=float(section[k-50]['T_BR'])/float(section[k-50]['T_rate_length'])*float(section[k-50]['T_length'])+incl
        azim_t=float(section[k-50]['T_TR'])/float(section[k-50]['T_rate_length'])*float(section[k-50]['T_length'])+azim
        br=float(section[k-50]['T_BR'])
        tr=float(section[k-50]['T_TR'])
        seglength = (float(section[k-50]['T_length']))
        fortype = section[k-50]['T_Formation']
        mudtype = section[k-50]['T_MudType']
        pumprate = section[k-50]['T_PumpRate']
        mudweight =section[k-50]['T_MudWeight']
        for kk in range(0,dp):
            #atribut
            segnum = segnum+1
            #calculation
            dx = calculation(method, 'deltax', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
            dy = calculation(method, 'deltay', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
            dz = calculation(method, 'deltaz', xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
            xt = xi+dx
            yt = yi+dy
            zt = zi+dz
            mdsection = mdsection + (seglength/dp)
            #add data to list
            #bsection.append(('Section Number = {0}'.format(secnum),'Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl),'A = {0}'.format(azim),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt),'MD = {}'.format(mdsection)))
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


    #for afterKOP_section in bsection:
        #print(afterKOP_section)
    #clearing
    distance = math.sqrt(((xtarget-xt)*(xtarget-xt))+((ytarget-yt)*(ytarget-yt))+((ztarget-zt)*(ztarget-zt)))
    dis = float(distance)
    if dis <= tol:
        print('your trajectory hit the target with distance of {0} from target'.format(dis))
        print('lead angle = {}'.format(azim_init))
        break
    elif dis > tol and azim_init<359:
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
        mdsection = 0
    elif azim_init==359:
        print("not hit target")
        print('miss {0} from target'.format(dis))
        print('lead angle = {}'.format(azim_init))
    ################after KOP##################################################################

#print('your trajectory hit the target with distance of {0} from target'.format(dis))
#print('lead angle = {}'.format(azim_init))
#print(tol)
#############################################write output########################################
#with open('OUT_T_{0}_{1}'.format(method,fn),'w')as outfile:
# json.dump(bsection, outfile)
with open('RESULT_T_{0}_{1}'.format(method,fn),'w')as outfile:
    json.dump(psection, outfile)
#################################################################################################

#####################HIT TARGET###########################################
# distance = math.sqrt(((xtarget-xt)*(xtarget-xt))+((ytarget-yt)*(ytarget-yt))+((ztarget-zt)*(ztarget-zt)))
# #distance = math.sqrt(((xtarget-psection[-1][14])*(xtarget-psection[-1][14]))+((ytarget-psection[-1][15])*(ytarget-psection[-1][15]))+((ztarget-psection[-1][16])*(ztarget-psection[-1][16])))
# dis = float(distance)
# if dis <= tol:
#     print('your trajectory hit the target with distance of {0} from target'.format(dis))
# else:
#     print('miss target, {0} from target'.format(dis))
#####################HIT TARGET###########################################



################### 3D Plot ####################
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(traj_x,traj_y,traj_z, color='blue')
ax.scatter3D(xtarget,ytarget,ztarget*-1,color='Red',s=100)
plt.show()
################### 3D Plot ####################

trajectory = {"x":traj_x,"y":traj_y,"z":traj_z}
with open('DP_T_{0}_{1}'.format(method,fn),'w')as outfile:
    json.dump(trajectory, outfile)
end = time.time()
time = end-start
print('Execution time {0} seconds'.format(time))