import math
import matplotlib.pyplot as plt
import pandas as pd

## Variables
x0 = 10
v0 = 0
mass = 5
g = -9.81
t_max = 20
delta_t = 0.001
precision = 1000
bounce_coeff = 0.8

# core calculations
x = [x0]
v = [v0]
t_array = range(0, int(t_max*precision), int(delta_t*precision))

for i in range(1, len(t_array)):
    if x[-1] <= 0:
        v[-1] *=-1 * bounce_coeff
    v.append(v[i-1] + g*delta_t)
    x.append(max(0, x[i-1] + v[i-1]*delta_t + g*math.pow(delta_t, 2)))

# save the data
data = {
    "x": x,
    "v": v,
    "time(s)": list(x/precision for x in range(0, t_max*precision))
}
data = pd.DataFrame(data)
data = data.set_index(data["time(s)"])
data = data.drop("time(s)", axis=1)

data.plot()
plt.show()


import pdb; pdb.set_trace()