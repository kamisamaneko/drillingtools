import math
################AA##############
def AA_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_avg = math.radians((incl+incl_t)/2)
    azim_avg = math.radians((azim+azim_t)/2)
    i_avg = math.sin(incl_avg)
    a_avg = math.cos(azim_avg)
    return  i_avg*a_avg*seglength

def AA_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_avg = math.radians((incl+incl_t)/2)
    azim_avg = math.radians((azim+azim_t)/2)
    i_avg = math.sin(incl_avg)
    a_avg = math.sin(azim_avg)
    return  i_avg*a_avg*seglength

def AA_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_avg = math.radians((incl+incl_t)/2)
    azim_avg = math.radians((azim+azim_t)/2)
    i_avg = math.cos(incl_avg)
    a_avg = math.cos(azim_avg)
    return  i_avg*seglength
################AA##############

###############TAN#####################
def TAN_dx(xt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = math.radians(incl)
    azim_rad = math.radians(azim)
    c_incl = math.sin(incl_rad)
    c_azim = math.cos(azim_rad)
    return c_incl*c_azim*seglength

def TAN_dy(yt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = math.radians(incl)
    azim_rad = math.radians(azim)
    c_incl = math.sin(incl_rad)
    c_azim = math.sin(azim_rad)
    return c_incl*c_azim*seglength

def TAN_dz(zt,incl,incl_t,azim,azim_t,seglength,dp,br,tr):
    incl_rad = math.radians(incl)
    azim_rad = math.radians(azim)
    c_incl = math.cos(incl_rad)
    c_azim = math.cos(azim_rad)
    return c_incl*seglength
###############TAN####################



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

