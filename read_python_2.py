import json
import math
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from T_function import AA_dx, AA_dy, AA_dz, TAN_dx, TAN_dy,TAN_dz,calculation
from mpl_toolkits import mplot3d

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
tol= float(tdata['T_Tolerance'])
kop = float(tdata['T_KOP'])
lead= float(tdata['T_Lead Angle'])

#############################segnment part######################################################

segment = tdata['T_segment']
list_segment = list(segment)
list2_segment = list(list_segment)
#closing json
#############################segnment part######################################################
open_json.close()

#############################open data & variable asignment#####################################

###############################preliminary information#########################################
print("Dude, you are working for well cluster {0}, with API number {1}".format(cluster,api))
print("Your starting point is {0}, {1}, {2} and your target is at {3}, {4}, {5}.".format(xo,yo,zo,xtarget,ytarget,ztarget))
print("You are using {0} method to built the trajectory with tolerance of {1} ".format(method, tol))

#counting total segment
i=50
for segnum in segment:
    i=i+1
print("You have {0} segments including 50 sections before KOP at {1}\n following are your segments after KOP".format(i,kop))

###############################preliminary information#########################################

########################################segment before KOP#########################################
#iniziation
j=0
bsegment=[]
xi=xo
yi=yo
zi=zo
for j in range(0,50):
    #calculation
    dx = 0
    dy = 0
    dz = kop/50
    xt = xi+dx
    yt = yi+dy
    zt = zi+dz
    #atribut
    segnum = j+1
    incl = 0
    #azim = (float(tdata['T_Lead Angle'])+float(tdata['T_Lead Target'])-(float(segment[0]['T_TR'])/float(segment[0]['T_rate_length'])*float(segment[0]['T_length'])))/2
    azim=(float(tdata['T_Lead Angle'])+float(tdata['T_Lead Target']))/2
    br = 0
    tr = 0
    #add data to list
    bsegment.append(('Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl),'A = {0}'.format(azim),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt)))
    #dfoutputs = pd.DataFrame(columns= ['Section Number', 'Cluster', 'API', 'B', 'T', 'I', 'A', 'x', 'y', 'z', 'dx','dy','dz'])
    #dfoutputs.iat[j,0] = segnum
    #dfoutputs.iat[j,1] = cluster
    #dfoutputs.iat[j,2] = api
    #dfoutputs.iat[j,3] = br
    #dfoutputs.iat[j,4] = tr
  #  dfoutputs.iat[j,5] =




    #iteration properties
    xi=xt
    yi=yt
    zi=zt

for beforeKOP_segment in bsegment:
    print(beforeKOP_segment)
#    dfoutputs = pd.dataframe[columns = ['Section Number', 'Cluster', 'API', 'B', 'T', 'I', 'A', 'x', 'y', 'z', 'dx','dy','dz']
########################################segment before KOP#########################################


#################after KOP##################################################################
#to hold lead angle
mdsegment=0
w=0
ww=0
for w in range(50,i):
    mdsegment = float(segment[ww]['T_length'])+mdsegment
    if mdsegment <= float(tdata['T_Angle Hold']):
        ww=ww+1
    else:
        ww=ww

k=0
ii=0
asegment=[]
xi=xt
yi=yt
zi=zt
ddx = 'deltax'
ddy = 'deltay'
ddz = 'deltaz'
for k in range(50,50+ww):
    #atribut
    segnum = segnum+1
    incl_t=float(segment[ii]['T_BR'])/float(segment[ii]['T_rate_length'])*float(segment[ii]['T_length'])+incl
    azim_t= azim
    br=float(segment[ii]['T_BR'])
    tr=float(segment[ii]['T_TR'])
    seglength = float(segment[0]['T_length'])
    #calculation
    dx = calculation(method, ddx, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
    dy = calculation(method, ddy, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
    dz = calculation(method, ddz, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
    xt = xi+dx
    yt = yi+dy
    zt = zi+dz
    #add data to list
    asegment.append(('Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl_t),'A = {0}'.format(azim_t),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt)))
    #iteration properties
    xi=xt
    yi=yt
    zi=zt
    ii=ii+1
    incl=incl_t
    azim=azim_t

for k in range(50+ww,i):
    #atribut
    segnum = segnum+1
    incl_t=float(segment[ii]['T_BR'])/float(segment[ii]['T_rate_length'])*float(segment[ii]['T_length'])+incl
    xxxx = math.radians(incl_t)
    azim_t=float(segment[ii]['T_TR'])/float(segment[ii]['T_rate_length'])*float(segment[ii]['T_length'])+azim
    br=float(segment[ii]['T_BR'])
    tr=float(segment[ii]['T_TR'])
    seglength = float(segment[0]['T_length'])

    #calculation
    dx = calculation(method, ddx, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
    dy = calculation(method, ddy, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
    dz = calculation(method, ddz, xi,yi,zi,incl,incl_t,azim,azim_t,seglength)
    xt = xi+dx
    yt = yi+dy
    zt = zi+dz
    #add data to list
    asegment.append(('Segment Number = {0}'.format(segnum),'Cluster = {0}'.format(cluster),'API = {0}'.format(api),'B = {0}'.format(br),'T = {0}'.format(tr),'I = {0}'.format(incl_t),'A = {0}'.format(azim_t),'xi= {0}'.format(xi),'yi={0}'.format(yi), 'zi = {0}'.format(zi),'dx= {0}'.format(dx),'dy={0}'.format(dy), 'dz = {0}'.format(dz),'xt= {0}'.format(xt),'yt={0}'.format(yt), 'zt = {0}'.format(zt)))
    #iteration properties
    xi=xt
    yi=yt
    zi=zt
    ii=ii+1
    incl=incl_t
    azim=azim_t


for afterKOP_segment in asegment:
    print(afterKOP_segment)

################after KOP##################################################################

#############################################write output########################################
with open('OUT_{0}'.format(fn),'w')as outfile:
    json.dump(bsegment, outfile)
#################################################################################################

#####################HIT TARGET###########################################
distance = (((xtarget-xt)*(xtarget-xt))+((ytarget-yt)*(ytarget-yt))+((ztarget-zt)*(ztarget-zt))**0.5)
dis = float(distance)
if dis <= tol:
    print('your trajectory hit the target with distance of {0} from target'.format(dis))
else:
    print('miss target, {0} from target'.format(dis))
#####################HIT TARGET###########################################