import math
from animation import animate_shit
import pandas as pd
import numpy as np

## Variables
xpos =[0]       #starting x-position
ypos = [10]     #starting y-position
vx = [0]        #starting x-velocity
vy = [0]        #starting y-velocity
mass = 5        #mass of the pointmass
g = -9.81
t_max = 13
delta_t = 0.01
precision = int(1/delta_t)
bounce_coeff = 0.8

# core calculations
t_array = range(int(t_max*precision))

# test matrix
for i in range(1, len(t_array)):
    if ypos[-1] <= 0:
        vy[-1] *= -1 * bounce_coeff
    # defining the matrices (known/A, connection/C and unknowns/X)
    A = np.array([[-mass,0],[0,-mass]])
    C = np.array([[0], [-g*mass]])
    X = np.matmul(np.linalg.inv(A),C)
    # integrating to get the velocity and position
    vx.append(vx[i-1] + X[0]*delta_t)
    vy.append(vy[i-1] + X[1]*delta_t)
    xpos.append(xpos[i-1] + vx[i-1]*delta_t + X[0]*math.pow(delta_t, 2))
    ypos.append(max(0, ypos[i-1] + vy[i-1]*delta_t + X[1]*math.pow(delta_t, 2)))

# save the data
data = {
    "ypos": ypos,
    "xpos": xpos,
    "vy": vy,
    "vx": vx,
    "time(s)": list(x/precision for x in range(0, t_max*precision))
}
data = pd.DataFrame(data)
data = data.set_index(data["time(s)"])
data = data.drop("time(s)", axis=1)

animate_shit(list(data["y"]))

