import math
from animation import AnimateShit
import pandas as pd
import numpy as np

## Variables
xpos = [0]   # starting x-position
ypos = [10]  # starting y-position
vx = [3]     # starting x-velocity
vy = [0]     # starting y-velocity
mass = 5     # mass of the pointmass
g = -9.81
t_max = 20
delta_t = 0.01
precision = int(1/delta_t)
bounce_coeff = 1


# core calculations
t_array = range(int(t_max*precision))
v_tot = 10
for i in range(1, len(t_array)):
    if ypos[-1] <= 0 or ypos[-1] >= 10:
        vy[-1] *= -1 * bounce_coeff

    if xpos[-1] <= -10 or xpos[-1] >= 10:
        vx[-1] *= -1 * bounce_coeff
    # defining the matrices (known/A, connection/C and unknowns/X)
    A = np.array([[-mass, 0], [0, -mass]])
    C = np.array([[0], [-g*mass]])
    X = np.matmul(np.linalg.inv(A), C)
    # integrating to get the velocity and position
    vx.append(vx[-1] + X[0][0]*delta_t)
    vy.append(vy[-1] + X[1][0]*delta_t)
    xpos.append(xpos[-1] + vx[-1]*delta_t + X[0][0]*math.pow(delta_t, 2))
    ypos.append(max(0, ypos[-1] + vy[-1]*delta_t + X[1][0]*math.pow(delta_t, 2)))

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

AnimateShit(data).run()

