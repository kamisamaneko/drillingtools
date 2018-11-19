import math as m
import numpy as np

################AA##############
def AA_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_avg = m.radians((incl+incl_t)/2)
    azim_avg = m.radians((azim+azim_t)/2)
    i_avg = m.sin(incl_avg)
    a_avg = m.cos(azim_avg)
    return  i_avg*a_avg*seglength/dp

def AA_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_avg = m.radians((incl+incl_t)/2)
    azim_avg = m.radians((azim+azim_t)/2)
    i_avg = m.sin(incl_avg)
    a_avg = m.sin(azim_avg)
    return  i_avg*a_avg*seglength/dp

def AA_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_avg = m.radians((incl+incl_t)/2)
    azim_avg = m.radians((azim+azim_t)/2)
    i_avg = m.cos(incl_avg)
    a_avg = m.cos(azim_avg)
    return  i_avg*seglength/dp
################AA##############

###############TAN#####################
def TAN_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = m.radians(incl)
    azim_rad = m.radians(azim)
    c_incl = m.sin(incl_rad)
    c_azim = m.cos(azim_rad)
    return c_incl*c_azim*seglength/dp

def TAN_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = m.radians(incl)
    azim_rad = m.radians(azim)
    c_incl = m.sin(incl_rad)
    c_azim = m.sin(azim_rad)
    return c_incl*c_azim*seglength/dp

def TAN_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = m.radians(incl)
    azim_rad = m.radians(azim)
    c_incl = m.cos(incl_rad)
    c_azim = m.cos(azim_rad)
    return c_incl*seglength/dp
###############TAN####################

##############Model 5##############################
def M5_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl=m.radians(incl)
    incl_t=m.radians(incl_t)
    azim=m.radians(azim)
    azim_t=m.radians(azim_t)
    sinI=0.5*(m.sin(incl)+m.sin(incl_t))
    cosA=0.5*(m.cos(azim)+m.cos(azim_t))
    return sinI*cosA*seglength/dp

def M5_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl=m.radians(incl)
    incl_t=m.radians(incl_t)
    azim=m.radians(azim)
    azim_t=m.radians(azim_t)
    sinI=0.5*(m.sin(incl)+m.sin(incl_t))
    sinA=0.5*(m.sin(azim)+m.sin(azim_t))
    return sinI*sinA*seglength/dp

def M5_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl=m.radians(incl)
    incl_t=m.radians(incl_t)
    azim=m.radians(azim)
    azim_t=m.radians(azim_t)
    cosI=0.5*(m.cos(incl)+m.cos(incl_t))
    return cosI*seglength/dp

#############Model 5#############################

##############MCM#############################

def MCM_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = m.radians(incl)
    incl_t_rad = m.radians(incl_t)
    azim_rad = m.radians(azim)
    azim_t_rad = m.radians(azim_t)
    c_1 = m.sin(incl_rad)*m.cos(azim_rad)
    c_2 = m.sin(incl_t_rad)*m.cos(azim_t_rad)
    beta = m.sqrt(m.radians(br)*m.radians(br)+m.radians(tr)*m.radians(tr)*m.sin(m.radians(incl))*m.sin(m.radians(incl)))
    return (c_1+c_2)*seglength/(dp*m.radians(beta))*m.tan(m.radians(beta/2))

def MCM_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = m.radians(incl)
    incl_t_rad = m.radians(incl_t)
    azim_rad = m.radians(azim)
    azim_t_rad = m.radians(azim_t)
    c_1 = m.sin(incl_rad)*m.sin(azim_rad)
    c_2 = m.sin(incl_t_rad)*m.sin(azim_t_rad)
    beta = m.sqrt(m.radians(br)*m.radians(br)+m.radians(tr)*m.radians(tr)*m.sin(m.radians(incl))*m.sin(m.radians(incl)))
    return (c_1+c_2)*seglength/(dp*m.radians(beta))*m.tan(m.radians(beta/2))


def MCM_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = m.radians(incl)
    incl_t_rad = m.radians(incl_t)
    azim_rad = m.radians(azim)
    azim_t_rad = m.radians(azim_t)
    c_1 = m.cos(incl_rad)
    c_2 = m.cos(incl_t_rad)
    beta = m.sqrt(m.radians(br)*m.radians(br)+m.radians(tr)*m.radians(tr)*m.sin(m.radians(incl))*m.sin(m.radians(incl)))
    return (c_1+c_2)*seglength/(dp*m.radians(beta))*m.tan(m.radians(beta/2))

##############MCM#############################

#################Quadratic#####################
# def Quad_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
#     incl=m.radians(incl)
#     incl_t=m.radians(incl_t)
#     azim=m.radians(azim)
#     azim_t=m.radians(azim_t)
#     V_x=m.sin(incl)*m.cos(azim)
#     V_y=m.sin(incl)*m.sin(azim)
#     V_z=m.cos(incl)
#     U_x=m.sin(incl_t)*m.cos(azim_t)
#     U_y=m.sin(incl_t)*m.sin(azim_t)
#     U_z=m.cos(incl_t)
#     DLA=V_x*U_x+V_y*U_y+V_z*U_z
#     M=1-DLA
#     N=1+DLA
#     G_q=(1/(0.5-N/((32**0.5)*(1-M)**0.5)))*np.log(((M-(2*M)**0.5)/(M+(2*M)**0.5))
#     return 0.5*seglength/dp*G_q*(U_x+V_x)
#
# def Quad_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
#     incl=m.radians(incl)
#     incl_t=m.radians(incl_t)
#     azim=m.radians(azim)
#     azim_t=m.radians(azim_t)
#     V_x=m.sin(incl)*m.cos(azim)
#     V_y=m.sin(incl)*m.sin(azim)
#     V_z=m.cos(incl)
#     U_x=m.sin(incl_t)*m.cos(azim_t)
#     U_y=m.sin(incl_t)*m.sin(azim_t)
#     U_z=m.cos(incl_t)
#     DLA=V_x*U_x+V_y*U_y+V_z*U_z
#     M=1-DLA
#     N=1+DLA
#     G_q=(1/(0.5-N/((32**0.5)*(1-M)**0.5)))*np.log(((M-(2*M)**0.5)/(M+(2*M)**0.5))
#     return 0.5*seglength/dp*G_q*(U_y+V_y)
#
# def Quad_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
#     incl=m.radians(incl)
#     incl_t=m.radians(incl_t)
#     azim=m.radians(azim)
#     azim_t=m.radians(azim_t)
#     V_x=m.sin(incl)*m.cos(azim)
#     V_y=m.sin(incl)*m.sin(azim)
#     V_z=m.cos(incl)
#     U_x=m.sin(incl_t)*m.cos(azim_t)
#     U_y=m.sin(incl_t)*m.sin(azim_t)
#     U_z=m.cos(incl_t)
#     DLA=V_x*U_x+V_y*U_y+V_z*U_z
#     M=1-DLA
#     N=1+DLA
#     G_q=(1/(0.5-N/((32**0.5)*(1-M)**0.5)))*np.log(((M-(2*M)**0.5)/(M+(2*M)**0.5))
#     return 0.5*seglength/dp*G_q*(U_z+V_z)

#################Quadratic####################


#def segment_hold(T_Angle_Hold,mdsegment):

def calculation(method, d, xi,yi,zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    #CALL AVG METHOD
    if method == 'avg' and d == 'deltax':
        dx = AA_dx(xi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dx
    elif method == 'avg' and d == 'deltay':
        dy = AA_dy(yi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dy
    elif method == 'avg' and d == 'deltaz':
        dz = AA_dz(zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dz

    #CAL TAN METHOD
    elif method == 'tan' and d == 'deltax':
        dx = TAN_dx(xi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dx
    elif method == 'tan' and d == 'deltay':
        dy = TAN_dy(yi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dy
    elif method == 'tan' and d == 'deltaz':
        dz = TAN_dz(zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dz

    #CAL Model5 METHOD
    elif method == 'm5' and d == 'deltax':
        dx = M5_dx(xi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dx
    elif method == 'm5' and d == 'deltay':
        dy = M5_dy(yi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dy
    elif method == 'm5' and d == 'deltaz':
        dz = M5_dz(zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dz

    #CAL Quadratic METHOD
    elif method == 'quad' and d == 'deltax':
        dx = Quad_dx(xi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dx
    elif method == 'quad' and d == 'deltay':
        dy = Quad_dy(yi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dy
    elif method == 'quad' and d == 'deltaz':
        dz = Quad_dz(zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dz

    #Call MCM METHOD
    elif method == 'mcm' and d == 'deltax':
        dx = MCM_dx(xi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dx
    elif method == 'mcm' and d == 'deltay':
        dy = MCM_dy(yi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dy
    elif method == 'mcm' and d == 'deltaz':
        dz = MCM_dz(zi,incl,incl_t,azim,azim_t,seglength,dp,br,tr)
        return dz
