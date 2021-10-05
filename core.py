import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Variables
y0 = 10
v0 = 0
mass = 5
g = -9.81
t_max = 20
delta_t = 0.001
precision = int(1/delta_t)
bounce_coeff = 0.8

# core calculations
y = [y0]
v = [v0]
t_array = range(int(t_max*precision))

for i in range(1, len(t_array)):
    if y[-1] <= 0:
        v[-1] *= -1 * bounce_coeff
    v.append(v[i-1] + g*delta_t)
    y.append(max(0, y[i-1] + v[i-1]*delta_t + g*math.pow(delta_t, 2)))


# test matrix
A = np.array([[-mass,0],[0,-mass]])
C = np.array([[0], [-g*mass]])
X = np.matmul(np.linalg.inv(A),C)

import pdb; pdb.set_trace()

# save the data
data = {
    "y": y,
    "v": v,
    "time(s)": list(x/precision for x in range(0, t_max*precision))
}
data = pd.DataFrame(data)
data = data.set_index(data["time(s)"])
data = data.drop("time(s)", axis=1)

data.plot()
plt.show()


import pdb; pdb.set_trace()